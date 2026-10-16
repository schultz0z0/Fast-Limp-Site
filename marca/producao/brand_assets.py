"""Faithful silhouette tracing, composition and exports. Source PNGs stay intact."""
from pathlib import Path
import json, hashlib, urllib.request
import numpy as np
import cv2
import potrace
import fitz
from PIL import Image
from fontTools.ttLib import TTFont as FontToolsFont
from fontTools.varLib.instancer import instantiateVariableFont
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'marca' / 'brandbook-v1'
FONT_DIR = OUT / 'fontes'
COLORS = dict(blue='#1C94F0', navy='#092131', white='#FFFFFF', mid='#1274C2',
              light='#5AB7F5', glass='#2D546F', ice='#EFF0F0', silver='#D1D3D4', black='#010202')
for folder in ['svg','png','pdf','digital','aplicacoes','matriz','fontes','diretrizes']:
    (OUT/folder).mkdir(parents=True, exist_ok=True)

def setup_fonts():
    url = 'https://raw.githubusercontent.com/google/fonts/main/ofl/manrope/'
    vf = FONT_DIR/'Manrope-Variable.ttf'
    if not vf.exists(): urllib.request.urlretrieve(url+'Manrope%5Bwght%5D.ttf', vf)
    if not (FONT_DIR/'OFL.txt').exists(): urllib.request.urlretrieve(url+'OFL.txt', FONT_DIR/'OFL.txt')
    for name, weight in [('Manrope',400),('Manrope-SemiBold',600),('Manrope-Bold',700)]:
        file = FONT_DIR/(name+'-static.ttf')
        if not file.exists():
            f = FontToolsFont(vf)
            instantiateVariableFont(f, {'wght':weight}, inplace=True)
            style={400:'Regular',600:'SemiBold',700:'Bold'}[weight]
            for record in f['name'].names:
                if record.nameID in (1,2,4,6,16,17):
                    val={1:'Manrope',2:style,4:'Manrope '+style,6:'Manrope-'+style,16:'Manrope',17:style}[record.nameID]
                    record.string=val.encode(record.getEncoding())
            f.save(file)
        if name not in pdfmetrics.getRegisteredFontNames(): pdfmetrics.registerFont(TTFont(name, str(file)))

setup_fonts()

def masks(path):
    a = np.array(Image.open(path).convert('RGB'))
    color = (a.max(2).astype(int)-a.min(2).astype(int)>22) & (a.min(2)<150)
    blue = color & (a[:,:,1]>83) & (a[:,:,2]>145)
    return a, (color & ~blue).astype('uint8')*255, blue.astype('uint8')*255

def trace(mask, offset=(0,0), micro=False):
    if not np.any(mask): return []
    work=mask.copy()
    if micro:
        cs,hs=cv2.findContours(work,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        if hs is not None:
            for i,cnt in enumerate(cs):
                if hs[0][i][3]>=0 and abs(cv2.contourArea(cnt))<6000:cv2.drawContours(work,[cnt],0,255,-1)
    work=cv2.GaussianBlur(work,(0,0),.65)
    bitmap=potrace.Bitmap(work<127)
    curves=bitmap.trace(turdsize=8,alphamax=1.0,opticurve=True,opttolerance=.35)
    paths=[]
    def pt(p):return [float(p.x)-offset[0],float(p.y)-offset[1]]
    for curve in curves:
        commands=[['M',*pt(curve.start_point)]]
        for seg in curve:
            if seg.is_corner:
                commands.extend([['L',*pt(seg.c)],['L',*pt(seg.end_point)]])
            else:commands.append(['C',*pt(seg.c1),*pt(seg.c2),*pt(seg.end_point)])
        commands.append(['Z']);paths.append(commands)
    return paths

def bbox(mask):
    yy,xx=np.nonzero(mask)
    return int(xx.min()),int(yy.min()),int(xx.max()+1),int(yy.max()+1)

def load_component(path, selection, micro=False):
    _,n,b=masks(path); selected=np.zeros_like(n)
    y0,y1,x0,x1=selection; selected[y0:y1,x0:x1]=255
    n=cv2.bitwise_and(n,selected); b=cv2.bitwise_and(b,selected)
    x,y,r,d=bbox(n|b)
    return {'w':r-x,'h':d-y,'paths':{'navy':trace(n,(x,y)), 'blue':trace(b,(x,y),micro)}}

source_type=ROOT/'marca/conceitos/01-monograma-fl.png'
source_symbol=ROOT/'marca/conceitos/03-gesto-de-precisao.png'
SYMBOL=load_component(source_symbol,(0,793,0,580))
MICRO=load_component(source_symbol,(0,793,0,580),True)
TYPE=load_component(source_type,(0,809,600,1942))
NAME=load_component(source_type,(0,490,600,1942))

def moved(component, x=0, y=0, scale=1):
    groups=[]
    for role,paths in component['paths'].items():
        commands=[]
        for curve in paths:
            for cmd in curve:
                values=[]
                for i,v in enumerate(cmd[1:]):values.append(v*scale+(x if i%2==0 else y))
                commands.append([cmd[0],*values])
        if commands:groups.append({'role':role,'commands':commands})
    return groups

def compose(kind):
    sw,sh=SYMBOL['w'],SYMBOL['h']; tw,th=TYPE['w'],TYPE['h']; nw,nh=NAME['w'],NAME['h']; gap=sh*.16
    if kind=='horizontal': return sw+gap+tw,sh,moved(SYMBOL)+moved(TYPE,sw+gap,(sh-th)/2)
    if kind=='compacta': return sw+gap+nw,sh,moved(SYMBOL)+moved(NAME,sw+gap,(sh-nh)/2)
    if kind=='vertical':
        scale=.51; sym_h=sh*1.13; sym_scale=sym_h/sh; w=max(tw*scale,sw*sym_scale); y=sym_h+sh*.15
        return w,y+th*scale,moved(SYMBOL,(w-sw*sym_scale)/2,0,sym_scale)+moved(TYPE,(w-tw*scale)/2,y,scale)
    if kind in ('simbolo','simbolo-micro'): return sw,sh,moved(MICRO if kind=='simbolo-micro' else SYMBOL)
    if kind=='assinatura': return tw,th,moved(TYPE)
    raise KeyError(kind)

def get_size(kind): return compose(kind)[:2]

def role_color(role,colorway):
    if colorway=='negativa': return COLORS['white'] if role=='navy' else COLORS['blue']
    if colorway=='branca': return COLORS['white']
    if colorway=='escura': return COLORS['navy']
    if colorway=='preta': return COLORS['black']
    return COLORS[role if role=='navy' else 'blue']

def draw_logo(c, kind, x, y, width, colorway='principal'):
    w,h,groups=compose(kind); s=width/w
    c.saveState(); c.translate(x,y+h*s); c.scale(s,-s)
    for group in groups:
        c.setFillColor(HexColor(role_color(group['role'],colorway))); path=c.beginPath()
        for cmd in group['commands']:
            if cmd[0]=='M':path.moveTo(*cmd[1:])
            elif cmd[0]=='L':path.lineTo(*cmd[1:])
            elif cmd[0]=='C':path.curveTo(*cmd[1:])
            elif cmd[0]=='Z':path.close()
        c.drawPath(path,stroke=0,fill=1,fillMode=0)
    c.restoreState(); return h*s

def svg_markup(kind, colorway='principal', padding=0):
    w,h,groups=compose(kind); content=[]
    for group in groups:
        data=' '.join(cmd[0]+' '+','.join(f'{n:.3f}' for n in cmd[1:]) for cmd in group['commands'])
        content.append(f'<path fill="{role_color(group["role"],colorway)}" fill-rule="evenodd" d="{data}"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-padding} {-padding} {w+2*padding:.2f} {h+2*padding:.2f}" role="img" aria-label="Fast Limp - Limpeza de vidros">'
            f'<title>Fast Limp - {kind} - {colorway}</title>'+''.join(content)+'</svg>')

def export_logo(kind, colorway):
    stem=f'fast-limp-{kind}-{colorway}'
    (OUT/'svg'/f'{stem}.svg').write_text(svg_markup(kind,colorway),encoding='utf-8')
    w,h=get_size(kind); pdf=OUT/'pdf'/f'{stem}.pdf'
    c=canvas.Canvas(str(pdf),pagesize=(w,h),pageCompression=1)
    c.setTitle('Fast Limp | '+kind+' | '+colorway); draw_logo(c,kind,0,0,w,colorway);c.showPage();c.save()
    doc=fitz.open(pdf); target=1200 if kind.startswith('simbolo') else 2400
    pix=doc[0].get_pixmap(matrix=fitz.Matrix(target/w,target/w),alpha=True)
    pix.save(OUT/'png'/f'{stem}.png');doc.close()
    return {'composicao':kind,'cor':colorway,'svg':f'svg/{stem}.svg','pdf':f'pdf/{stem}.pdf','png':f'png/{stem}.png','largura_png':pix.width,'altura_png':pix.height}

def rect(c,x,y,w,h,color):
    c.setFillColor(HexColor(color));c.rect(x,y,w,h,stroke=0,fill=1)

def text(c,t,x,y,size=18,color=None,font='Manrope'):
    c.setFillColor(HexColor(color or COLORS['navy']));c.setFont(font,size);c.drawString(x,y,t)

def render_pdf_to_png(pdf,png,target=None):
    d=fitz.open(pdf);p=d[0];s=(target/p.rect.width) if target else 1
    p.get_pixmap(matrix=fitz.Matrix(s,s),alpha=False).save(png);d.close()

def make_avatar(light=False):
    size=1024;name='avatar-claro' if light else 'avatar-principal';pdf=OUT/'aplicacoes'/f'{name}.pdf'
    c=canvas.Canvas(str(pdf),pagesize=(size,size));rect(c,0,0,size,size,COLORS['white'] if light else COLORS['navy'])
    w,h=get_size('simbolo');aw=size*.64;ah=aw*h/w
    draw_logo(c,'simbolo',(size-aw)/2,(size-ah)/2,aw,'principal' if light else 'negativa');c.save()
    for px in [1024,512,256]: render_pdf_to_png(pdf,OUT/'digital'/f'{name}-{px}.png',px)
    pdfmicro=OUT/'aplicacoes'/f'{name}-micro.pdf';c=canvas.Canvas(str(pdfmicro),pagesize=(size,size))
    rect(c,0,0,size,size,COLORS['white'] if light else COLORS['navy'])
    draw_logo(c,'simbolo-micro',(size-aw)/2,(size-ah)/2,aw,'principal' if light else 'negativa');c.save()
    for px in [16,24,32,48,64,128]: render_pdf_to_png(pdfmicro,OUT/'digital'/f'{name}-micro-{px}.png',px)

def create_design(name,w,h,draw):
    p=OUT/'aplicacoes'/f'{name}.pdf';c=canvas.Canvas(str(p),pagesize=(w,h));c.setTitle('Fast Limp | '+name);draw(c,w,h);c.save()
    folder='digital' if name.startswith(('post','story','capa-perfil')) else 'aplicacoes'
    render_pdf_to_png(p,OUT/folder/f'{name}.png')

def diagonal(c,w,h,color,offset=0):
    c.setFillColor(HexColor(color));p=c.beginPath();p.moveTo(w*.68+offset,0);p.lineTo(w,0);p.lineTo(w,h*.6);p.lineTo(w*.68+offset,h*.33);p.close();c.drawPath(p,fill=1,stroke=0)

def social_one(c,w,h):
    rect(c,0,0,w,h,COLORS['ice']);diagonal(c,w,h,COLORS['blue']);lw,lh=get_size('horizontal');draw_logo(c,'horizontal',76,h-76-620*lh/lw,620)
    text(c,'Vidros limpos.',76,666,77,font='Manrope-Bold');text(c,'Boa impressão.',76,568,77,font='Manrope-Bold')
    text(c,'Para sua casa ou empresa.',80,470,33);text(c,'LIMPEZA DE VIDROS',80,105,20,font='Manrope-SemiBold')

def social_two(c,w,h):
    rect(c,0,0,w,h,COLORS['navy']);diagonal(c,w,h,COLORS['glass']);lw,lh=get_size('horizontal');draw_logo(c,'horizontal',76,h-76-620*lh/lw,620,'negativa')
    text(c,'Seu espaço.',76,658,86,COLORS['white'],'Manrope-Bold');text(c,'Outro olhar.',76,552,86,COLORS['white'],'Manrope-Bold')
    text(c,'Limpeza de vidros para',80,446,34,COLORS['ice']);text(c,'residências e empresas.',80,398,34,COLORS['ice'])
    rect(c,80,180,600,100,COLORS['blue']);text(c,'Solicite um orçamento',114,215,34,COLORS['navy'],'Manrope-Bold')

def story(c,w,h):
    rect(c,0,0,w,h,COLORS['navy']);diagonal(c,w,h,COLORS['glass']);draw_logo(c,'horizontal',96,h-300,800,'negativa')
    for line,y in [('Mais clareza',1250),('para o seu',1144),('ambiente.',1038)]:text(c,line,96,y,85,COLORS['white'],'Manrope-Bold')
    text(c,'Limpeza de vidros',100,900,38,COLORS['ice']);text(c,'para casas e empresas.',100,844,38,COLORS['ice'])
    rect(c,100,410,880,120,COLORS['blue']);text(c,'Solicite um orçamento',160,451,49,COLORS['navy'],'Manrope-Bold')

def proposal(c,w,h):
    rect(c,0,0,w,h,COLORS['ice']);lw,lh=get_size('horizontal');draw_logo(c,'horizontal',48,h-48-(w-96)*lh/lw,w-96);rect(c,0,0,w,265,COLORS['navy'])
    text(c,'Proposta',48,510,49,font='Manrope-Bold');text(c,'comercial',48,447,49,font='Manrope-Bold')
    text(c,'Limpeza de vidros',50,390,18);text(c,'Para residências e empresas',50,360,13)
    text(c,'FAST LIMP',48,96,13,COLORS['white'],'Manrope-Bold');text(c,'Clareza, cuidado e apresentação profissional.',48,66,10,COLORS['ice'])

def business(c,w,h):
    rect(c,0,0,w,h,COLORS['navy']);draw_logo(c,'horizontal',22,71,211,'negativa')
    text(c,'Limpeza de vidros',23,29,9,COLORS['white']);text(c,'Residencial e comercial',23,15,7,COLORS['ice'])

def profile_cover(c,w,h):
    rect(c,0,0,w,h,COLORS['ice']);diagonal(c,w,h,COLORS['blue']);draw_logo(c,'horizontal',90,245,900)
    text(c,'Limpeza de vidros para casas e empresas.',94,132,31)

def graphic_pattern():
    tile=[]
    for y in range(0,1200,200):
        for x in range(0,1200,200):tile.append(f'<path d="M{x+35} {y+155} V{y+35} H{x+155} M{x+35} {y+155} L{x+155} {y+35}" fill="none" stroke="#D1D3D4" stroke-width="3"/>')
    s='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1200"><rect width="1200" height="1200" fill="#EFF0F0"/>'+''.join(tile)+'</svg>'
    (OUT/'svg'/'grafismo-janela-diagonal.svg').write_text(s,encoding='utf-8')

def run_exports():
    variants=[]
    for kind in ['horizontal','compacta','vertical','simbolo','simbolo-micro']:
        for cw in ['principal','negativa','escura','branca','preta']:variants.append(export_logo(kind,cw))
    for cw in ['principal','negativa','escura']:variants.append(export_logo('assinatura',cw))
    for light in [False,True]:make_avatar(light)
    micro=Image.open(OUT/'digital/avatar-principal-micro-128.png');micro.save(OUT/'digital/favicon.ico',sizes=[(16,16),(24,24),(32,32),(48,48),(64,64),(128,128)])
    for name,w,h,fn in [('post-institucional-1080',1080,1080,social_one),('post-orcamento-1080',1080,1080,social_two),('story-1080x1920',1080,1920,story),('capa-proposta-a4',595.276,841.89,proposal),('cartao-institucional-90x50mm',255.118,141.732,business),('capa-perfil-1640x624',1640,624,profile_cover)]:create_design(name,w,h,fn)
    graphic_pattern()
    (OUT/'matriz'/'contornos.json').write_text(json.dumps({k:{'width':compose(k)[0],'height':compose(k)[1],'groups':compose(k)[2]} for k in ['horizontal','compacta','vertical','simbolo','simbolo-micro','assinatura']},ensure_ascii=False),encoding='utf-8')
    (OUT/'diretrizes'/'cores.json').write_text(json.dumps(COLORS,indent=2),encoding='utf-8')
    (OUT/'diretrizes'/'tokens.css').write_text(':root {\n'+''.join(f'  --fast-limp-{k}: {v};\n' for k,v in COLORS.items())+'  --fast-limp-font: "Manrope", Arial, sans-serif;\n}\n',encoding='utf-8')
    provenance={'status':'Versão 1.0 para validação do brandbook. Site não iniciado.','selection':'Símbolo do estudo03 + lettering e descritor do estudo01, conforme escolha do cliente.','method':'Reconstrução vetorial dos contornos raster, cores sólidas padronizadas; composição e versão óptica novas para validação.','sources':[{'file':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [source_type,source_symbol]],'font':{'name':'Manrope','source':'https://github.com/google/fonts/tree/main/ofl/manrope','license':'SIL OFL 1.1; OFL.txt incluído'},'logos':variants}
    (OUT/'manifesto.json').write_text(json.dumps(provenance,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'logo_variations':len(variants),'dimensions':{k:get_size(k) for k in ['horizontal','compacta','vertical','simbolo','simbolo-micro']},'output':str(OUT)},ensure_ascii=False))

if __name__=='__main__':run_exports()
