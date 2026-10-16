"""Fast Limp A5 v2: composição de panfletagem, Manrope e marca oficial.

Imagem ilustrativa gerada separadamente; logo, copy, serviços e QR em vetor.
Não altera o site nem a edição anterior do panfleto.
"""
from pathlib import Path
import json
import pymupdf as fitz
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.graphics.barcode import qrencoder

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output/pdf'
ART=ROOT/'output/panfleto'
TMP=ROOT/'tmp/pdfs/panfleto-v2'
BRAND=ROOT/'marca/brandbook-v1'
ASSET=ART/'assets/ilustracao-profissional-v2.png'
for directory in [OUT,ART,TMP]:directory.mkdir(parents=True,exist_ok=True)
for name,file in [('Regular','Manrope-static.ttf'),('SemiBold','Manrope-SemiBold-static.ttf'),('Bold','Manrope-Bold-static.ttf')]:
    pdfmetrics.registerFont(TTFont('Manrope-'+name,str(BRAND/'fontes'/file)))
COLORS={key:HexColor(value) for key,value in json.loads((BRAND/'diretrizes/cores.json').read_text(encoding='utf8')).items()}
W,H=148*mm,210*mm
PHONE='(21) 96764-3628'
WHATSAPP='https://wa.me/5521967643628'
qr=qrencoder.QRCode(None,qrencoder.QRErrorCorrectLevel.M)
qr.addData(WHATSAPP);qr.make()
matrix=[[False]*(len(qr.modules)+8) for _ in range(4)]
matrix += [[False]*4+row+[False]*4 for row in qr.modules]
matrix += [[False]*(len(qr.modules)+8) for _ in range(4)]

def build(print_mode):
    margin=8*mm if print_mode else 0
    base=TMP/('base-impressao.pdf' if print_mode else 'base-visualizacao.pdf')
    c=canvas.Canvas(str(base),pagesize=(W+2*margin,H+2*margin),pageCompression=1,pdfVersion=(1,4))
    c.setTitle('Fast Limp | Panfleto A5 v2 | '+('Impressão' if print_mode else 'Visualização'))
    c.setAuthor('Fast Limp')
    c.setSubject('Limpeza de vidros | '+PHONE)
    c.saveState()
    art_clip=c.beginPath()
    art_clip.rect(margin-3*mm,margin-3*mm,W+6*mm,H+6*mm)
    c.clipPath(art_clip,stroke=0,fill=0)
    def rect(x,y,w,h,color):
        c.setFillColor(COLORS[color]);c.rect(margin+x*mm,margin+H-(y+h)*mm,w*mm,h*mm,stroke=0,fill=1)
    def polygon(points,color):
        c.setFillColor(COLORS[color]);p=c.beginPath()
        p.moveTo(margin+points[0][0]*mm,margin+H-points[0][1]*mm)
        for x,y in points[1:]:p.lineTo(margin+x*mm,margin+H-y*mm)
        p.close();c.drawPath(p,fill=1,stroke=0)
    def text(value,x,y,size=10,font='Regular',color='navy'):
        c.setFillColor(COLORS[color]);c.setFont('Manrope-'+font,size)
        c.drawString(margin+x*mm,margin+H-y*mm,value)
    rect(-3,-3,154,216,'white')
    # Grandes campos chapados e diagonal derivada do vidro/rodo da marca.
    polygon([(-3,109),(151,83),(151,213),(-3,213)],'blue')
    polygon([(-3,117),(151,91),(151,213),(-3,213)],'navy')
    # A chamada fica totalmente livre do rosto e da ferramenta.
    text('LIMPEZA DE VIDROS',9,39,8.8,'SemiBold','mid')
    text('Seus vidros',9,53,29,'Bold')
    text('limpos',9,68,34,'Bold')
    text('de novo',9,83,34,'Bold')
    text('Para casas, comércios',9,96,10.5,'Regular','glass')
    text('e empresas',9,102,10.5,'Regular','glass')
    # Figura de publicidade: nenhum logotipo ou alegação de equipe real.
    with Image.open(ASSET) as image:
        ratio=image.height/image.width
    image_w=86
    image_h=image_w*ratio
    c.drawImage(ImageReader(str(ASSET)),margin+70*mm,margin+H-(53+image_h)*mm,width=image_w*mm,height=image_h*mm,mask='auto')
    # Catálogo curto, sem preços, garantias ou certificações não comprovadas.
    text('NOSSOS SERVIÇOS',9,123,8.7,'Bold','light')
    services=[(133,'Vidros residenciais'),(142,'Vidros comerciais'),(151,'Pós-obra'),(165,'Fachadas de vidro'),(174,'Vitrines')]
    for y,title in services:
        c.setStrokeColor(COLORS['light']);c.setLineWidth(1.2)
        c.line(margin+9*mm,margin+H-(y-1.3)*mm,margin+10.1*mm,margin+H-(y-.2)*mm)
        c.line(margin+10.1*mm,margin+H-(y-.2)*mm,margin+12.2*mm,margin+H-(y-2.5)*mm)
        text(title,15,y,10.3,'SemiBold','white')
    text('Residências e comércios',15,156,7.4,'Regular','ice')
    # Faixa única de conversão, à frente do recorte da fotografia.
    rect(-3,181,154,32,'blue')
    text('Peça seu orçamento',9,189.5,12.7,'Bold')
    text(PHONE,9,200,20.5,'Bold')
    text('Chame no WhatsApp e conte o que precisa limpar',9,206,7.5,'Regular')
    # QR com quiet zone; vetor e destino direto, sem serviço intermediário.
    qr_x,qr_y,qr_size=115,184,23
    rect(qr_x,qr_y,qr_size,qr_size,'white')
    cell=qr_size*mm/len(matrix)
    c.setFillColor(COLORS['navy'])
    for row,values in enumerate(matrix):
        for column,on in enumerate(values):
            if on:c.rect(margin+qr_x*mm+column*cell,margin+H-qr_y*mm-(row+1)*cell,cell+.008,cell+.008,stroke=0,fill=1)
    text('Imagem ilustrativa',109,178,6,'Regular','white')
    c.linkURL(WHATSAPP,(margin+8*mm,margin+H-208*mm,margin+139*mm,margin+H-183*mm),relative=0,thickness=0)
    c.restoreState()
    if print_mode:
        c.setStrokeColor(COLORS['black']);c.setLineWidth(.3)
        for x in [margin,margin+W]:
            for y in [margin,margin+H]:
                side=-1 if x==margin else 1
                c.line(x+side*3.7*mm,y,x+side*6.5*mm,y)
                side=-1 if y==margin else 1
                c.line(x,y+side*3.7*mm,x,y+side*6.5*mm)
    c.save()
    doc=fitz.open(base);page=doc[0]
    logo=fitz.open(BRAND/'pdf/fast-limp-horizontal-principal.pdf')
    logo_w=80*mm;logo_h=logo_w*logo[0].rect.height/logo[0].rect.width
    page.show_pdf_page(fitz.Rect(margin+9*mm,margin+9*mm,margin+9*mm+logo_w,margin+9*mm+logo_h),logo,0)
    logo.close()
    if print_mode:
        page.set_trimbox(fitz.Rect(margin,margin,margin+W,margin+H))
        page.set_bleedbox(fitz.Rect(margin-3*mm,margin-3*mm,margin+W+3*mm,margin+H+3*mm))
    else:page.set_trimbox(page.rect)
    output=OUT/('fast-limp-panfleto-a5-v2-impressao.pdf' if print_mode else 'fast-limp-panfleto-a5-v2-visualizacao.pdf')
    doc.save(output,garbage=4,deflate=True)
    doc.close()
    return output

if __name__=='__main__':
    outputs=[build(False),build(True)]
    for path in outputs:
        with fitz.open(path) as doc:
            page=doc[0]
            assert abs(page.trimbox.width/mm-148)<.01 and abs(page.trimbox.height/mm-210)<.01
            content=page.get_text()
            for title in [PHONE,'Seus vidros','limpos','de novo','Vidros residenciais','Vidros comerciais','Pós-obra','Fachadas de vidro','Vitrines','Peça seu orçamento']:
                assert title in content,title
                assert not (title+'.') in content
            assert all(page.rect.contains(fitz.Rect(word[:4])) for word in page.get_text('words'))
            if 'visualizacao' in path.name:page.get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).save(ART/'fast-limp-panfleto-a5-v2-previa.png')
            print(path.name,'A5 validado')
