"""Validate the rendered exports and package the reviewable brand identity."""
from pathlib import Path
import sys, json, zipfile, hashlib, shutil, io
import xml.etree.ElementTree as ET
import numpy as np
from PIL import Image
import fitz
from brand_assets import ROOT, OUT, COLORS, masks, bbox, source_symbol, source_type

def validate_assets():
    checks=[]
    svgs=list((OUT/'svg').glob('*.svg'))
    for svg in svgs:
        root=ET.parse(svg).getroot()
        assert len(root.findall('.//{http://www.w3.org/2000/svg}image'))==0,svg
        assert len(root.findall('.//{http://www.w3.org/2000/svg}text'))==0,svg
        assert root.attrib.get('viewBox'),svg
    checks.append({'check':'SVG nativos sem raster embutido ou dependência de fonte','files':len(svgs),'passed':True})
    pngs=list((OUT/'png').glob('*.png'))
    for png in pngs:
        im=Image.open(png)
        assert im.mode=='RGBA',png
        alpha=np.asarray(im)[:,:,3]
        assert alpha.min()==0 and alpha.max()==255,png
    checks.append({'check':'PNG com canal alpha real e conteúdo opaco','files':len(pngs),'passed':True})
    for pdf in (OUT/'pdf').glob('*.pdf'):
        doc=fitz.open(pdf);assert len(doc)==1 and len(doc[0].get_images())==0,pdf;doc.close()
    checks.append({'check':'Logos PDF em vetor, sem imagem raster','files':len(list((OUT/'pdf').glob('*.pdf'))),'passed':True})
    for stem in ['fast-limp-horizontal-principal','fast-limp-vertical-principal','fast-limp-simbolo-principal','fast-limp-simbolo-branca']:
        sv=fitz.open(OUT/'svg'/f'{stem}.svg');sp=fitz.open('pdf',sv.convert_to_pdf());p=fitz.open(OUT/'pdf'/f'{stem}.pdf')
        w=p[0].rect.width;s=800/w
        a=np.frombuffer(p[0].get_pixmap(matrix=fitz.Matrix(s,s),alpha=True).samples,np.uint8)
        b=np.frombuffer(sp[0].get_pixmap(matrix=fitz.Matrix(s,s),alpha=True).samples,np.uint8)
        assert a.shape==b.shape,(stem,a.shape,b.shape)
        delta=float(np.abs(a.astype(float)-b.astype(float)).mean())
        assert delta<.8,(stem,delta)
        checks.append({'check':'SVG e PDF equivalentes','asset':stem,'mean_delta_0_255':round(delta,4),'passed':True})
    # Compare traced contours with source silhouettes, ignoring normalized color.
    for source,selection,stem in [(source_symbol,(0,793,0,580),'fast-limp-simbolo-principal'),(source_type,(0,809,600,1942),'fast-limp-assinatura-principal')]:
        _,n,b=masks(source);y0,y1,x0,x1=selection;mask=np.zeros_like(n);mask[y0:y1,x0:x1]=(n|b)[y0:y1,x0:x1]
        x,y,r,d=bbox(mask);ref=mask[y:d,x:r]>0
        pdf=fitz.open(OUT/'pdf'/f'{stem}.pdf');pix=pdf[0].get_pixmap(alpha=True)
        arr=np.frombuffer(pix.samples,np.uint8).reshape(pix.height,pix.width,4)[:,:,3]>127
        assert ref.shape==arr.shape,(stem,ref.shape,arr.shape)
        iou=float((ref & arr).sum()/(ref | arr).sum())
        assert iou>.98,(stem,iou)
        checks.append({'check':'Silhueta vetorial comparada à referência escolhida','asset':stem,'intersection_over_union':round(iou,5),'passed':True})
    for px in [1024,512,256]:
        assert Image.open(OUT/'digital'/f'avatar-principal-{px}.png').size==(px,px)
    for file,size in [('post-institucional-1080.png',(1080,1080)),('post-orcamento-1080.png',(1080,1080)),('story-1080x1920.png',(1080,1920)),('capa-perfil-1640x624.png',(1640,624))]:
        assert Image.open(OUT/'digital'/file).size==size,(file,Image.open(OUT/'digital'/file).size)
    checks.append({'check':'Dimensões de avatares, posts, story e capa','passed':True})
    out=ROOT/'output/pdf/fast-limp-brandbook-v1-validacao.pdf'
    doc=fitz.open(out);assert len(doc)==24
    alltext='\n'.join(p.get_text() for p in doc)
    for phrase in ['Fast Limp','Manrope','320','Para validação']:
        assert phrase.lower() in alltext.lower(),phrase
    overflows=[]
    for i,p in enumerate(doc):
        for line in p.get_text('dict')['blocks']:
            if 'lines' not in line:continue
            x0,y0,x1,y1=line['bbox']
            if x0<-.5 or y0<-.5 or x1>p.rect.width+.5 or y1>p.rect.height+.5:overflows.append((i+1,line['bbox']))
    assert not overflows,overflows
    checks.append({'check':'Brandbook 24 páginas, texto extraível e dentro da página','passed':True})
    (OUT/'diretrizes'/'verificacao.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(checks,ensure_ascii=False,indent=2))

def package():
    pdf=ROOT/'output/pdf/fast-limp-brandbook-v1-validacao.pdf'
    shutil.copy2(pdf,OUT/'Fast-Limp-Brandbook-v1.pdf')
    source=OUT/'fontes'
    # Keep only original variable font plus the correctly named static instances.
    for name in ['Manrope.ttf','Manrope-SemiBold.ttf','Manrope-Bold.ttf']:
        p=source/name
        if p.exists():p.unlink()
    dist=ROOT/'output'/'fast-limp-identidade-visual-v1.zip'
    with zipfile.ZipFile(dist,'w',zipfile.ZIP_DEFLATED) as z:
        for f in sorted(OUT.rglob('*')):
            if f.is_file():z.write(f,Path('Fast-Limp-Identidade-v1')/f.relative_to(OUT))
    receipt={'zip':str(dist),'bytes':dist.stat().st_size,'sha256':hashlib.sha256(dist.read_bytes()).hexdigest(),'files':len([p for p in OUT.rglob('*') if p.is_file()])}
    print(json.dumps(receipt,ensure_ascii=False))

if __name__=='__main__':
    validate_assets()
    if '--package' in sys.argv:package()
