"""Panfleto Fast Limp A5: arte vetorial e PDF com sangria/marcas de corte.

Executar com Python do runtime Codex (ReportLab, Pillow, PyMuPDF).
Identidade e arquivos oficiais preservados; nenhum elemento visual do anúncio
antigo fornecido em 16/10/2026 foi reaproveitado.
"""
from pathlib import Path
import json

import pymupdf as fitz
from PIL import Image, ImageOps
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import mm
from reportlab.graphics.barcode import qrencoder

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf'
PREVIEW = ROOT / 'output/panfleto'
TMP = ROOT / 'tmp/pdfs/panfleto'
for folder in [OUT, PREVIEW, TMP]:
    folder.mkdir(parents=True, exist_ok=True)

BRAND = ROOT / 'marca/brandbook-v1'
for name, filename in [('Manrope','Manrope-static.ttf'), ('Manrope-SemiBold','Manrope-SemiBold-static.ttf'), ('Manrope-Bold','Manrope-Bold-static.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(BRAND / 'fontes' / filename)))

PALETTE = {name:HexColor(value) for name,value in json.loads((BRAND/'diretrizes/cores.json').read_text(encoding='utf8')).items()}
PHONE = '(21) 96764-3628'
URL = 'https://wa.me/5521967643628'
WIDTH, HEIGHT = 148*mm,210*mm

# Derivado do master licenciado, sem retoques, sem alterar pessoas ou uniforme.
photo = ImageOps.exif_transpose(Image.open(ROOT/'site/assets/originals/37440103.jpg')).convert('RGB')
photo = ImageOps.fit(photo,(2100,780),method=Image.Resampling.LANCZOS,centering=(.5,.34))
photo_path = TMP/'foto-panfleto.jpg'
photo.save(photo_path,quality=95,subsampling=0)

qr = qrencoder.QRCode(None,qrencoder.QRErrorCorrectLevel.M)
qr.addData(URL)
qr.make()
qr_matrix = [[False]*(len(qr.modules)+8) for _ in range(4)]
qr_matrix += [[False]*4+row+[False]*4 for row in qr.modules]
qr_matrix += [[False]*(len(qr.modules)+8) for _ in range(4)]

def make_base(print_mode):
    offset = 8*mm if print_mode else 0
    page_w,page_h = WIDTH+2*offset,HEIGHT+2*offset
    path = TMP/('base-impressao.pdf' if print_mode else 'base-leitura.pdf')
    c = canvas.Canvas(str(path),pagesize=(page_w,page_h),pageCompression=1)
    c.setTitle('Fast Limp | Panfleto A5 | ' + ('Impressão' if print_mode else 'Visualização'))
    c.setAuthor('Fast Limp')
    c.setSubject('Limpeza de vidros para residências e empresas. WhatsApp '+PHONE)
    def rect(x,y,w,h,color):
        c.setFillColor(PALETTE[color]);c.rect(offset+x*mm,offset+HEIGHT-(y+h)*mm,w*mm,h*mm,stroke=0,fill=1)
    def text(value,x,y,size=10,font='Manrope',color='navy'):
        c.setFont(font,size);c.setFillColor(PALETTE[color]);c.drawString(offset+x*mm,offset+HEIGHT-y*mm,value)
    def line(x1,y1,x2,y2,color='silver',width=.5):
        c.setStrokeColor(PALETTE[color]);c.setLineWidth(width);c.line(offset+x1*mm,offset+HEIGHT-y1*mm,offset+x2*mm,offset+HEIGHT-y2*mm)
    rect(-3,-3,154,216,'white')
    # Logo oficial será inserida em vetor, sem reconstrução nem redigitação.
    text('PARA SUA CASA',109,16,7.5,'Manrope-SemiBold','glass')
    text('OU SUA EMPRESA',109,20.5,7.5,'Manrope-SemiBold','glass')
    line(12,35,136,35)
    # Hierarquia simples: promessa de marca, fotografia, catálogo, contato.
    text('Vidros limpos.',12,54,31,'Manrope-Bold')
    text('Boa impressão.',12,67,31,'Manrope-Bold')
    text('Mais clareza para o seu espaço.',12,77,10.5,'Manrope','glass')
    c.drawImage(ImageReader(str(photo_path)),offset+12*mm,offset+HEIGHT-129*mm,width=124*mm,height=46*mm)
    # Legenda editorial discreta; foto nunca apresentada como equipe/resultado.
    text('Fotografia ilustrativa.',12,133,6.5,'Manrope','glass')
    text('LIMPEZA DE VIDROS',12,144,8.5,'Manrope-SemiBold','mid')
    for x,y,title in [(16,152,'Vidros residenciais'),(16,160,'Vidros comerciais'),(16,168,'Pós-obra'),(84,152,'Fachadas de vidro'),(84,160,'Vitrines')]:
        rect(x-4,y-2,1.2,1.2,'blue')
        text(title,x,y,10.2,'Manrope-SemiBold')
    text('Residências e comércios',16,173,7.1,'Manrope','glass')
    # Uma única área de conversão: número legível + QR real equivalente.
    rect(-3,178,154,35,'navy')
    rect(12,178,18,1.2,'blue')
    text('SOLICITE SEU ORÇAMENTO',12,187,8.8,'Manrope-Bold','light')
    text(PHONE,12,197,20,'Manrope-Bold','white')
    text('Chame no WhatsApp.',12,203.5,9.2,'Manrope','white')
    # QR vetorial com quiet zone de quatro módulos. Sem ícone sobre os dados.
    qr_x,qr_y,qr_size = 111,180,24
    module = qr_size*mm/len(qr_matrix)
    c.setFillColor(PALETTE['white'])
    c.rect(offset+qr_x*mm,offset+HEIGHT-(qr_y+qr_size)*mm,qr_size*mm,qr_size*mm,stroke=0,fill=1)
    c.setFillColor(PALETTE['navy'])
    for row, values in enumerate(qr_matrix):
        for col,on in enumerate(values):
            if on:c.rect(offset+qr_x*mm+col*module,offset+HEIGHT-qr_y*mm-(row+1)*module,module+.008,module+.008,stroke=0,fill=1)
    c.linkURL(URL,(offset+11*mm,offset+HEIGHT-208*mm,offset+136*mm,offset+HEIGHT-182*mm),relative=0,thickness=0)
    if print_mode:
        c.setStrokeColor(PALETTE['black']);c.setLineWidth(.3)
        for x in [offset,offset+WIDTH]:
            for y in [offset,offset+HEIGHT]:
                side = -1 if x == offset else 1
                c.line(x+side*3.7*mm,y,x+side*6.5*mm,y)
                side = -1 if y == offset else 1
                c.line(x,y+side*3.7*mm,x,y+side*6.5*mm)
    c.save()
    return path,offset

def finalize(print_mode):
    path,offset = make_base(print_mode)
    doc=fitz.open(path);page=doc[0]
    logo=fitz.open(BRAND/'pdf/fast-limp-horizontal-principal.pdf')
    logo_w=82*mm
    logo_h=logo_w*logo[0].rect.height/logo[0].rect.width
    page.show_pdf_page(fitz.Rect(offset+12*mm,offset+10*mm,offset+12*mm+logo_w,offset+10*mm+logo_h),logo,0)
    logo.close()
    if print_mode:
        page.set_trimbox(fitz.Rect(offset,offset,offset+WIDTH,offset+HEIGHT))
        page.set_bleedbox(fitz.Rect(offset-3*mm,offset-3*mm,offset+WIDTH+3*mm,offset+HEIGHT+3*mm))
    else:
        page.set_trimbox(page.rect)
    name='fast-limp-panfleto-a5-impressao.pdf' if print_mode else 'fast-limp-panfleto-a5-visualizacao.pdf'
    target=OUT/name
    doc.save(target,garbage=4,deflate=True)
    doc.close()
    return target

files=[finalize(False),finalize(True)]
for path in files:
    with fitz.open(path) as doc:
        page=doc[0]
        assert len(doc)==1
        assert abs(page.trimbox.width/mm-148)<.01 and abs(page.trimbox.height/mm-210)<.01
        content=page.get_text()
        for value in [PHONE,'Vidros residenciais','Vidros comerciais','Pós-obra','Fachadas de vidro','Vitrines']:
            assert value in content, value
        assert all(page.rect.contains(fitz.Rect(word[:4])) for word in page.get_text('words'))
        font_rows=page.get_fonts(full=True)
        embedded=[]
        for row in font_rows:
            if row[3].startswith('AAAAAA+Manrope') or 'Manrope' in row[3]:
                assert doc.extract_font(row[0])[3]
                embedded.append(row[3])
        assert len(embedded)>=3
        if 'visualizacao' in path.name:
            page.get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).save(PREVIEW/'fast-limp-panfleto-a5-previa.png')
        print(path.name,'validado',round(page.rect.width/mm,2),round(page.rect.height/mm,2),'mm')

qr_pixels=Image.new('RGB',(len(qr_matrix)*10,len(qr_matrix)*10),'white')
for row,values in enumerate(qr_matrix):
    for col,on in enumerate(values):
        if on:qr_pixels.paste((9,33,49),(col*10,row*10,(col+1)*10,(row+1)*10))
qr_pixels.save(TMP/'whatsapp-qr.png')
(PREVIEW/'especificacoes.json').write_text(json.dumps({'format':'A5 vertical, frente única','trimMm':[148,210],'bleedMm':3,'mediaWithMarksMm':[164,226],'safetyMm':5,'phone':PHONE,'whatsapp':URL,'logo':'marca/brandbook-v1/pdf/fast-limp-horizontal-principal.pdf','logoVisibleWidthMm':82,'type':'Manrope 400/600/700, fontes incorporadas','photo':'Pexels 37440103, Cihat Dede, master licenciado; fotografia ilustrativa','photoEffectivePpi':round(2100/(124/25.4)),'color':'RGB, HEX da marca; conversão para perfil de impressão pela gráfica; não declarado PDF/X','qrSizeMm':24,'qrQuietZoneModules':4,'servicesSource':'Dados extraídos exclusivamente da imagem enviada pelo usuário em16/10/2026; design ignorado'},ensure_ascii=False,indent=2),encoding='utf8')
