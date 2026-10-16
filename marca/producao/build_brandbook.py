"""Build the 24-page Fast Limp identity manual and visual QA renders.

Run only after brand_assets.py has exported its digital/application assets.
The editable vector artwork is supplied by brand_assets.draw_logo.
"""
from pathlib import Path
import math
import re

import fitz
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics

from brand_assets import ROOT, OUT, COLORS, FONT_DIR, draw_logo, get_size


W, H = landscape(A4)
M = 42
CW = W - M * 2
PDF = ROOT / 'output' / 'pdf' / 'fast-limp-brandbook-v1-validacao.pdf'
RENDERS = ROOT / 'tmp' / 'pdfs' / 'fast-limp'
C = {k: HexColor(v) if isinstance(v, str) else v for k, v in COLORS.items()}
NAVY, BLUE, WHITE = C['navy'], C['blue'], C['white']
ICE, SILVER, MID = C['ice'], C['silver'], C['mid']
GLASS, BLACK = C['glass'], C['black']
BODY = 'Manrope'
BOLD = 'Manrope-Bold'
SEMI = 'Manrope-SemiBold'


class Book:
    def __init__(self):
        PDF.parent.mkdir(parents=True, exist_ok=True)
        self.c = canvas.Canvas(str(PDF), pagesize=(W, H), pageCompression=1)
        self.c.setTitle('Fast Limp | Manual de identidade visual | Versão 1.0 para validação')
        self.c.setAuthor('Fast Limp')
        self.c.setSubject('Diretrizes de identidade visual, aplicações e validação da marca')
        self.n = 0
        self.dark = False

    def page(self, chapter, title=None, subtitle=None, bg='white'):
        if self.n:
            self.footer()
            self.c.showPage()
        self.n += 1
        self.dark = bg == 'navy'
        self.bg = C[bg]
        self.fg = WHITE if self.dark else NAVY
        self.muted = C['light'] if self.dark else GLASS
        self.rect(0, 0, W, H, self.bg)
        self.text(M, 26, 'FAST LIMP  /  IDENTIDADE VISUAL', 8, SEMI, self.fg)
        self.text(W-M, 26, chapter.upper(), 8, SEMI, self.fg, align='right')
        self.line(M, 47, W-M, 47, self.fg, .45, alpha=.25)
        if title:
            self.text(M, 69, title, 32, BOLD, self.fg)
        if subtitle:
            self.para(M, 119, subtitle, CW, 11, color=self.muted, leading=16)

    def footer(self):
        self.line(M, H-44, W-M, H-44, self.fg, .45, alpha=.25)
        self.text(M, H-30, 'Versão 1.0  |  Para validação', 8, color=self.muted)
        self.text(W-M, H-30, f'{self.n:02d} / 24', 8, SEMI, self.fg, align='right')

    def rect(self, x, top, width, height, fill, stroke=None, radius=0):
        c = self.c
        c.setFillColor(fill)
        c.setStrokeColor(stroke or fill)
        if radius:
            c.roundRect(x, H-top-height, width, height, radius, fill=1, stroke=bool(stroke))
        else:
            c.rect(x, H-top-height, width, height, fill=1, stroke=bool(stroke))

    def line(self, x1, top1, x2, top2, color=None, width=1, alpha=1, dash=None):
        c = self.c
        c.saveState()
        c.setStrokeColor(color or self.fg)
        c.setLineWidth(width)
        c.setStrokeAlpha(alpha)
        if dash:
            c.setDash(*dash)
        c.line(x1, H-top1, x2, H-top2)
        c.restoreState()

    def text(self, x, top, value, size=11, font=BODY, color=None, align='left'):
        c = self.c
        c.setFillColor(color or self.fg)
        c.setFont(font, size)
        y = H-top-size
        fn = c.drawRightString if align == 'right' else c.drawCentredString if align == 'center' else c.drawString
        fn(x, y, str(value))

    def para(self, x, top, value, width, size=11, font=BODY, color=None, leading=None):
        leading = leading or size * 1.5
        y = top
        for paragraph in value.split('\n'):
            words = paragraph.split()
            line = ''
            for word in words:
                test = f'{line} {word}'.strip()
                if pdfmetrics.stringWidth(test, font, size) > width and line:
                    self.text(x, y, line, size, font, color)
                    y += leading
                    line = word
                else:
                    line = test
            if line:
                self.text(x, y, line, size, font, color)
                y += leading
            else:
                y += leading * .6
        return y

    def logo(self, kind, x, top, width, colorway='principal'):
        sw, sh = get_size(kind)
        height = width * sh / sw
        draw_logo(self.c, kind, x, H-top-height, width, colorway)
        return height

    def pill(self, x, top, label, width=None, fill=None, color=None):
        width = width or pdfmetrics.stringWidth(label, SEMI, 8) + 20
        self.rect(x, top, width, 22, fill or BLUE, radius=11)
        self.text(x+width/2, top+5, label, 8, SEMI, color or WHITE, 'center')

    def note(self, x, top, label, body, width, color=None):
        self.text(x, top, label, 12, BOLD, color)
        return self.para(x, top+24, body, width, 10.5, color=color, leading=16)

    def image(self, path, x, top, width, height, bg=None):
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f'Required application preview missing: {path}')
        if bg is not None:
            self.rect(x, top, width, height, bg)
        im = Image.open(path)
        rw, rh = im.size
        factor = min(width/rw, height/rh)
        iw, ih = rw*factor, rh*factor
        self.c.drawImage(str(path), x+(width-iw)/2, H-top-height+(height-ih)/2,
                         iw, ih, preserveAspectRatio=True, mask='auto')

    def circle(self, x, top, diameter, fill, stroke=None, stroke_width=1):
        self.c.setFillColor(fill)
        self.c.setStrokeColor(stroke or fill)
        self.c.setLineWidth(stroke_width)
        self.c.circle(x+diameter/2, H-top-diameter/2, diameter/2, fill=1, stroke=bool(stroke))

    def path(self, pts, fill, stroke=None, width=1, close=True):
        p = self.c.beginPath()
        p.moveTo(pts[0][0], H-pts[0][1])
        for x, y in pts[1:]:
            p.lineTo(x, H-y)
        if close:
            p.close()
        self.c.setFillColor(fill)
        self.c.setStrokeColor(stroke or fill)
        self.c.setLineWidth(width)
        self.c.drawPath(p, fill=bool(fill), stroke=bool(stroke))

    def corner(self, x, top, width, height, color, weight=3):
        d = min(width, height)*.22
        for a, b, e, f, g, h in [
            (x+d, top, x, top, x, top+d),
            (x+width-d, top, x+width, top, x+width, top+d),
            (x, top+height-d, x, top+height, x+d, top+height),
            (x+width-d, top+height, x+width, top+height, x+width, top+height-d),
        ]:
            self.line(a,b,e,f,color,weight)
            self.line(e,f,g,h,color,weight)

    def finish(self):
        assert self.n == 24, f'Expected 24 pages, created {self.n}'
        self.footer()
        self.c.save()


def build():
    b = Book()

    # 01. A quiet cover that lets the selected mark carry the identity.
    b.page('Manual da marca', bg='navy')
    b.pill(M, 76, 'VERSÃO 1.0  /  PARA VALIDAÇÃO', 207, fill=BLUE, color=NAVY)
    b.logo('horizontal', M, 174, 585, 'negativa')
    b.text(M, 370, 'Clareza em cada detalhe.', 29, BOLD, WHITE)
    b.para(M, 419, 'Manual de identidade visual\nEstratégia, sistema visual e aplicações.', 460, 12, color=WHITE, leading=19)
    b.corner(685, 370, 112, 112, BLUE, 3)
    b.text(M, 493, 'A frase desta capa é editorial e não integra a assinatura da marca.', 8.5, color=C['light'])

    # 02. Navigable sections; page references are explicit and checked below.
    b.page('Como usar', 'Um sistema claro. Uma marca consistente.',
           'Consulte este manual antes de produzir peças. Use sempre os arquivos oficiais da identidade.')
    sections = [
        ('01', 'Fundamentos', 'Estratégia e conceito', '03-04'),
        ('02', 'Marca', 'Composições, proteção e uso', '05-11'),
        ('03', 'Linguagem', 'Cores, tipografia e expressão', '12-17'),
        ('04', 'Aplicações', 'Digital, papel e presença física', '18-22'),
        ('05', 'Produção', 'Arquivos e validação', '23-24'),
    ]
    for i, (num, title, desc, pages) in enumerate(sections):
        y = 172+i*64
        b.text(M, y, num, 11, BOLD, BLUE)
        b.text(M+46, y-4, title, 17, SEMI)
        b.text(M+250, y, desc, 11, color=GLASS)
        b.text(W-M, y, pages, 11, SEMI, align='right')
        b.line(M, y+43, W-M, y+43, SILVER, .6)
    b.para(M, 505, 'Esta edição apresenta a combinação vetorial do símbolo e do lettering selecionados para aprovação.', CW, 9.5, color=GLASS)

    # 03. Two equally important audiences.
    b.page('Fundamentos / 01', 'Cuidado visível. Confiança cotidiana.',
           'Fast Limp conecta a especialização em limpeza de vidros a uma comunicação simples e acessível.')
    col = (CW-28)/2
    for x, heading, body, n in [
        (M, 'Para sua casa', 'Ambientes acolhedores, vidros bem cuidados e atendimento que escuta o que cada pessoa precisa.', '01'),
        (M+col+28, 'Para sua empresa', 'Uma apresentação profissional para estabelecimentos e espaços de trabalho, com comunicação objetiva.', '02'),
    ]:
        b.rect(x, 174, col, 177, ICE)
        b.text(x+24, 193, n, 10, BOLD, MID)
        b.text(x+24, 225, heading, 23, BOLD)
        b.para(x+24, 272, body, col-48, 11, leading=17)
    b.text(M, 391, 'A personalidade em cinco palavras', 11, SEMI, GLASS)
    labels = [('Clara',95),('Cuidadosa',126),('Confiável',119),('Acessível',118),('Ágil',80)]
    x = M
    for label, width in labels:
        b.pill(x, 424, label, width, NAVY, WHITE)
        x += width+14
    b.para(M, 475, 'A agilidade aparece na linguagem direta e na organização visual. Não representa promessa de prazo.', CW, 10, color=GLASS)

    # 04. Real mark and annotation leaders.
    b.page('Fundamentos / 02', 'O serviço aparece no próprio símbolo.',
           'Uma janela e um rodo de limpeza: reconhecimento imediato, traço firme e sensação de clareza.', bg='navy')
    b.logo('simbolo', 320, 178, 225, 'negativa')
    b.note(M, 198, 'Janela', 'O contorno situa a marca no universo dos vidros e dos ambientes.', 200, WHITE)
    b.line(231, 243, 324, 243, BLUE, 1)
    b.circle(320, 239, 7, BLUE)
    b.note(598, 287, 'Rodo de limpeza', 'A ferramenta em diagonal comunica a especialidade do serviço.', 200, WHITE)
    b.line(535, 326, 580, 326, BLUE, 1)
    b.circle(531, 322, 7, BLUE)
    b.note(M, 426, 'Nome com presença', 'FAST LIMP em azul-marinho: lettering próprio, firme e legível.', 328, WHITE)
    b.note(438, 426, 'Assinatura descritiva', 'LIMPEZA DE VIDROS esclarece a atividade sem depender de um slogan.', 355, WHITE)

    # 05. Primary artwork.
    b.page('Marca / 01', 'A assinatura principal.',
           'Priorize a composição horizontal com o descritivo quando houver espaço e leitura confortável.')
    b.logo('horizontal', 115, 215, 610)
    b.line(M, 397, W-M, 397, SILVER, .65)
    b.note(M, 428, 'Símbolo', 'Janela e rodo formam uma unidade. Preserve a relação entre todos os elementos.', 215)
    b.note(308, 428, 'Lettering próprio', 'As letras da marca são desenho vetorial. Nunca substitua por uma fonte digitada.', 215)
    b.note(574, 428, 'Descritivo', 'Use o arquivo completo; não ajuste o espaçamento de LIMPEZA DE VIDROS.', 218)

    # 06. Four compositions in a proper comparison grid.
    b.page('Marca / 02', 'Uma identidade, diferentes encaixes.',
           'A escolha da composição acompanha o formato e a escala da aplicação.')
    cells = [
        (M,174,354,151,'horizontal','Horizontal principal',270),
        (M+382,174,376,151,'compacta','Horizontal compacta',270),
        (M,346,354,166,'vertical','Vertical',105),
        (M+382,346,376,166,'simbolo','Símbolo isolado',96),
    ]
    for x,y,w,h,kind,label,lw in cells:
        b.rect(x,y,w,h,ICE)
        lh = lw*get_size(kind)[1]/get_size(kind)[0]
        b.logo(kind,x+(w-lw)/2,y+17+(h-63-lh)/2,lw)
        b.text(x+18,y+h-31,label,10,SEMI)

    # 07. Official color treatments.
    b.page('Marca / 03', 'Cores da assinatura.',
           'Use as versões prontas. A versão negativa preserva o azul do símbolo sobre fundos escuros.')
    treatments = [
        (M,177,354,137,WHITE,'principal','Principal / fundo claro',NAVY),
        (M+382,177,376,137,NAVY,'negativa','Negativa / fundo escuro',WHITE),
        (M,338,354,137,ICE,'escura','Uma cor / azul-marinho',NAVY),
        (M+382,338,376,137,NAVY,'branca','Uma cor / branca',WHITE),
    ]
    for x,y,w,h,bg,cw,label,fg in treatments:
        b.rect(x,y,w,h,bg,stroke=SILVER if bg==WHITE else None)
        b.logo('horizontal',x+36,y+32,w-72,cw)
        b.text(x+18,y+h-29,label,9.5,SEMI,fg)
    b.para(M, 500, 'A versão preta destina-se a processos de uma só tinta quando o azul-marinho não puder ser reproduzido.', CW, 9.5, color=GLASS)

    # 08. Clear space, with measure and explicitly conservative complete-mark box.
    b.page('Marca / 04', 'Espaço para a marca respirar.',
           'Reserve uma margem mínima x em todos os lados, sem texto, bordas, imagens ou outros elementos.')
    lx, ly, lw = 225, 252, 405
    lh = lw*get_size('horizontal')[1]/get_size('horizontal')[0]
    # Horizontal artwork icon height is approximated by full artwork height.
    xunit = lh/4
    b.rect(lx-xunit,ly-xunit,lw+2*xunit,lh+2*xunit,ICE)
    b.line(lx-xunit,ly-xunit,lx+lw+xunit,ly-xunit,MID,.8,dash=(3,3))
    b.line(lx-xunit,ly+lh+xunit,lx+lw+xunit,ly+lh+xunit,MID,.8,dash=(3,3))
    b.line(lx-xunit,ly-xunit,lx-xunit,ly+lh+xunit,MID,.8,dash=(3,3))
    b.line(lx+lw+xunit,ly-xunit,lx+lw+xunit,ly+lh+xunit,MID,.8,dash=(3,3))
    b.logo('horizontal',lx,ly,lw)
    b.line(lx-10,ly,lx-10,ly-xunit,NAVY,.8)
    b.text(lx-27,ly-xunit/2-7,'x',11,SEMI)
    b.line(lx+lw,ly+lh+14,lx+lw+xunit,ly+lh+14,NAVY,.8)
    b.text(lx+lw+xunit/2,ly+lh+20,'x',11,SEMI,align='center')
    b.text(M, 432, 'x = 1/4 da altura do símbolo', 18, BOLD)
    b.para(M, 472, 'Aplique a mesma unidade nas versões vertical e compacta. Nas aplicações isoladas, meça x a partir da altura do próprio símbolo.', CW, 10.5, color=GLASS)

    # 09. Scale with honest screen/print caveats.
    b.page('Marca / 05', 'Reduzir sem perder reconhecimento.',
           'Mínimos propostos para esta edição. Confira a leitura no tamanho final e no processo de reprodução.')
    rows = [
        ('horizontal','Completa','320 px','72 mm',280),
        ('compacta','Compacta','150 px','40 mm',175),
        ('simbolo','Símbolo','48 px','12 mm',48),
        ('simbolo-micro','Micro','24 px','6 mm',25),
    ]
    b.text(M, 173, 'VERSÃO',8,SEMI,GLASS)
    b.text(206, 173, 'EXEMPLO DE ESCALA',8,SEMI,GLASS)
    b.text(593, 173, 'DIGITAL',8,SEMI,GLASS)
    b.text(704, 173, 'IMPRESSO',8,SEMI,GLASS)
    for i,(kind,label,px,mm,w) in enumerate(rows):
        y=202+i*67
        b.line(M,y-8,W-M,y-8,SILVER,.6)
        b.text(M,y+14,label,12,SEMI)
        h=w*get_size(kind)[1]/get_size(kind)[0]
        b.logo(kind,206,y+(55-h)/2,w)
        b.text(593,y+14,px,12,SEMI)
        b.text(704,y+14,mm,12,SEMI)
    b.para(M, 485, 'A versão micro simplifica os três pequenos traços de brilho. Não reduza a marca completa para usá-la como ícone. Os exemplos no PDF são comparativos; os valores em px orientam os arquivos digitais.', CW, 9.5, color=GLASS, leading=14)

    # 10. Background decision.
    b.page('Marca / 06', 'O fundo deve ajudar a leitura.',
           'Escolha a versão que mantém o nome e o símbolo claramente visíveis.')
    for i,(bg,cw,label) in enumerate([(WHITE,'principal','Branco: versão principal'),(NAVY,'negativa','Azul-marinho: negativa'),(BLUE,'escura','Azul: uma cor escura')]):
        x=M+i*260
        b.rect(x,184,238,179,bg,stroke=SILVER if i==0 else None)
        b.logo('horizontal',x+24,243,190,cw)
        b.para(x,383,label,235,12,SEMI,leading=17)
    b.rect(M,435,CW,78,ICE)
    b.text(M+20,449,'Sobre fotografias',11,BOLD)
    b.para(M+20,474,'Prefira uma área calma. Se o contraste variar, coloque a marca sobre um campo sólido branco ou azul-marinho, com a área de proteção.',CW-40,10,color=GLASS,leading=15)

    # 11. Actual forbidden transformations.
    b.page('Marca / 07', 'Consistência é preservar o desenho.',
           'Os exemplos abaixo mostram alterações que comprometem a identidade e devem ser evitadas.')
    cells=[(M,174,238,138,'Deformar a proporção','stretch'),(M+260,174,238,138,'Girar a assinatura','rotate'),
           (M+520,174,238,138,'Adicionar sombra','shadow'),(M,341,238,138,'Trocar as cores','color'),
           (M+260,341,238,138,'Contornar a marca','outline'),(M+520,341,238,138,'Usar contraste fraco','contrast')]
    for x,y,w,h,label,mode in cells:
        b.rect(x,y,w,h,ICE)
        c=b.c
        c.saveState()
        if mode=='stretch':
            c.translate(x+23,H-(y+89));c.scale(1,.52)
            draw_logo(c,'horizontal',0,0,192,'principal')
        elif mode=='rotate':
            c.translate(x+36,H-(y+96));c.rotate(13)
            draw_logo(c,'horizontal',0,0,180,'principal')
        elif mode=='shadow':
            c.setFillAlpha(.24)
            draw_logo(c,'horizontal',x+30,H-y-89,188,'preta')
            c.setFillAlpha(1)
            draw_logo(c,'horizontal',x+25,H-y-83,188,'principal')
        elif mode=='color':
            # A forbidden yellow ground and white mark is intentionally explicit.
            b.rect(x+12,y+15,w-24,80,HexColor('#E6BE39'))
            b.logo('horizontal',x+25,y+40,188,'branca')
        elif mode=='outline':
            # Multiple offset passes make an actual outline/effect around the mark.
            for dx,dy in [(-1.6,0),(1.6,0),(0,-1.6),(0,1.6)]:
                b.logo('horizontal',x+25+dx,y+40+dy,188,'escura')
            b.logo('horizontal',x+25,y+40,188,'branca')
        else:
            b.rect(x+12,y+15,w-24,80,C['light'])
            c.setFillAlpha(.25)
            b.logo('horizontal',x+25,y+40,188,'branca')
        c.restoreState()
        b.text(x+14,y+h-28,label,10,SEMI)
        b.text(x+w-14,y+9,'×',17,BOLD,MID,align='right')
    b.text(M,504,'Também não separe, redesenhe, reescreva ou reorganize os elementos do arquivo oficial.',9.5,color=GLASS)

    # 12. Brand colors.
    b.page('Linguagem / 01', 'Azul que comunica clareza.',
           'O azul traz presença. O azul-marinho sustenta confiança e leitura. O branco cria respiro.',bg='navy')
    swatches=[('AZUL FAST LIMP','blue','#1C94F0','28  148  240','88  38  0  6'),
              ('AZUL-MARINHO','navy','#092131','9  33  49','82  33  0  81'),
              ('BRANCO','white','#FFFFFF','255  255  255','0  0  0  0')]
    for i,(name,key,hx,rgb,cmyk) in enumerate(swatches):
        x=M+i*260
        b.rect(x,183,238,183,C[key],stroke=C['glass'] if key=='navy' else None)
        b.text(x,385,name,10,BOLD,WHITE)
        b.text(x,410,hx,20,SEMI,WHITE)
        b.text(x,448,'RGB  '+rgb,10,color=WHITE)
        b.text(x,470,'CMYK aprox.  '+cmyk,9,color=C['light'])
    b.text(M,510,'Referência mestra: HEX/RGB. Ajuste CMYK com o perfil e a prova da gráfica; os valores acima são aproximações.',8.5,color=C['light'])

    # 13. Supporting colors and measured contrast relationships.
    b.page('Linguagem / 02', 'Apoios discretos. Contraste intencional.',
           'As cores de apoio organizam conteúdos sem competir com a marca.')
    support=[('Azul médio','mid','#1274C2'),('Azul claro','light','#5AB7F5'),('Vidro','glass','#2D546F'),('Gelo','ice','#EFF0F0'),('Prata','silver','#D1D3D4'),('Preto','black','#010202')]
    for i,(label,key,hx) in enumerate(support):
        x=M+i*130
        b.rect(x,181,110,82,C[key])
        b.text(x,276,label,10,SEMI)
        b.text(x,296,hx,9,color=GLASS)
    b.line(M,337,W-M,337,SILVER,.7)
    contrast=[('Aa',NAVY,WHITE,'16,49:1','Marinho / branco'),('Aa',NAVY,BLUE,'5,14:1','Marinho / azul'),('Aa',WHITE,MID,'4,88:1','Branco / azul médio'),('Aa',WHITE,BLUE,'3,21:1','Branco / azul')]
    for i,(s,fg,bg,ratio,label) in enumerate(contrast):
        x=M+i*195
        b.rect(x,359,173,63,bg,stroke=SILVER if bg==WHITE else None)
        b.text(x+16,365,s,33,BOLD,fg)
        b.text(x+157,385,ratio,11,SEMI,fg,'right')
        b.text(x,435,label,9.5,SEMI)
    b.para(M,477,'Razões calculadas para as cores digitais. Prefira azul-marinho sobre branco para texto corrido; branco sobre azul principal exige atenção ao tamanho e ao peso. Estes exemplos não certificam uma peça ou interface.',CW,9.5,color=GLASS,leading=14)

    # 14. Supporting type; logo never typeset.
    b.page('Linguagem / 03', 'Manrope. Direta, aberta, versátil.',
           'A família tipográfica de apoio acompanha a geometria da identidade e favorece leitura simples.')
    b.text(M,173,'Aa',119,BOLD)
    b.text(259,191,'Manrope',41,BOLD)
    b.text(261,249,'Regular  /  Semibold  /  Bold',12,SEMI,GLASS)
    b.text(261,278,'ABCDEFGHIJKLMNOPQRSTUVWXYZ',13,SEMI)
    b.text(261,305,'abcdefghijklmnopqrstuvwxyz  0123456789',12)
    b.line(M,347,W-M,347,SILVER,.7)
    b.text(M,371,'Títulos',10,SEMI,GLASS)
    b.text(188,363,'Vidros limpos. Espaços que acolhem.',24,BOLD)
    b.text(M,421,'Texto',10,SEMI,GLASS)
    b.para(188,415,'Limpeza de vidros para sua casa ou empresa. Conte o que você precisa e solicite um orçamento.',520,11,leading=17)
    b.text(M,477,'Ação',10,SEMI,GLASS)
    b.pill(188,473,'Solicite um orçamento',171,NAVY,WHITE)
    b.text(M,513,'O lettering FAST LIMP é arte vetorial própria. A fonte de apoio não deve ser usada para recriar o logotipo.',9,color=GLASS)

    # 15. Voice written examples.
    b.page('Linguagem / 04', 'Falar com clareza também é cuidar.',
           'Uma voz profissional, próxima e objetiva. Explique o que faz e convide a pessoa para conversar.')
    examples=[('APRESENTAÇÃO','Limpeza de vidros para sua casa ou empresa.','Diz o serviço e acolhe os dois públicos.'),
              ('CONVERSA','Conte o que você precisa.','Abre espaço para compreender a demanda.'),
              ('CONVITE','Solicite um orçamento.','Indica o próximo passo de forma simples.')]
    for i,(tag,example,why) in enumerate(examples):
        y=176+i*99
        b.text(M,y,tag,8.5,SEMI,MID)
        b.text(M,y+21,example,20,BOLD)
        b.text(M,y+59,why,10,color=GLASS)
        b.line(M,y+83,W-M,y+83,SILVER,.6)
    b.para(M,492,'Evite superlativos, urgência artificial e promessas não comprovadas. Preços, prazos, região e condições só entram quando confirmados pela operação.',CW,9.5,color=GLASS,leading=14)

    # 16. Ancillary graphics, explicitly distinguished from the logo.
    b.page('Linguagem / 05', 'Enquadrar. Abrir espaço. Dar direção.',
           'Cantos de janela e uma diagonal de limpeza formam a linguagem gráfica de apoio.',bg='navy')
    b.corner(M+17,186,260,178,BLUE,4)
    b.line(M+38,332,M+254,213,WHITE,8)
    b.text(M+17,390,'Enquadramento + movimento',13,SEMI,WHITE)
    b.para(M+17,421,'Use poucos traços, espessura consistente e bastante área livre.',260,10.5,color=WHITE,leading=16)
    b.rect(391,174,407,300,WHITE)
    b.corner(414,197,361,254,BLUE,3)
    b.logo('compacta',435,214,171)
    b.text(435,300,'Seu espaço,',27,BOLD,NAVY)
    b.text(435,337,'mais claro.',27,BOLD,NAVY)
    b.pill(435,403,'Solicite um orçamento',165,NAVY,WHITE)
    b.para(M,504,'Elementos de apoio não substituem o símbolo. Evite excesso de brilhos, linhas ou efeitos de transparência.',CW,9.5,color=C['light'])

    # 17. No invented photography. An editorial shot plan is concrete and honest.
    b.page('Linguagem / 06', 'Fotografia com luz e cuidado reais.',
           'Direção para futuras captações. Esta página não apresenta portfólio fotográfico de serviços realizados.')
    shots=[('01','Ambiente','Luz natural, linhas arquitetônicas e vidro legível. Mostrar contexto residencial ou comercial.'),
           ('02','Gesto','Ferramenta correta em uso e atenção ao acabamento. Enquadrar o cuidado, sem encenações irreais.'),
           ('03','Detalhe','Reflexos controlados, transparência e superfícies bem apresentadas. Evitar brilho artificial.')]
    for i,(num,title,body) in enumerate(shots):
        x=M+i*260
        b.rect(x,177,238,160,ICE)
        b.corner(x+18,195,202,124,GLASS,1.5)
        b.text(x+119,225,num,34,BOLD,MID,'center')
        b.text(x+119,278,'PLANO DE CAPTAÇÃO',8,SEMI,GLASS,'center')
        b.text(x,357,title,19,BOLD)
        b.para(x,395,body,231,10.5,leading=16)
    b.para(M,488,'Equilibre casas e empresas no conjunto das imagens. Use fotografias autorizadas e mostre condições reais de trabalho, sem sugerir serviços ou resultados que não foram confirmados.',CW,9.5,color=GLASS,leading=14)

    # 18. Avatars at actual raster scale; contain plus circle clip.
    b.page('Aplicações / 01', 'Um símbolo que cabe no dia a dia.',
           'Avatares usam o símbolo isolado e centralizado. Em escalas pequenas, priorize a versão micro.')
    b.rect(M,176,323,257,ICE)
    b.image(OUT/'digital'/'avatar-principal-1024.png',M+65,195,192,192)
    b.text(M+20,414,'Quadrado / azul-marinho',12,SEMI)
    b.rect(392,176,406,257,ICE)
    b.c.saveState()
    p=b.c.beginPath();p.circle(595,H-291,96)
    b.c.clipPath(p,stroke=0,fill=0)
    b.image(OUT/'digital'/'avatar-principal-1024.png',499,195,192,192)
    b.c.restoreState()
    b.text(412,414,'Recorte circular / redes sociais',12,SEMI)
    # The next row intentionally uses real 32/48px rasters at 1pt per source pixel.
    b.text(M,476,'Escalas de',9.5,SEMI,GLASS)
    b.text(M,492,'conferência:',9.5,SEMI,GLASS)
    for px,x in [(32,230),(48,365),(96,560)]:
        source = OUT/'digital'/f'avatar-principal-micro-{px}.png' if px < 96 else OUT/'digital'/'avatar-principal-1024.png'
        b.image(source,x,489-px/2,px,px)
        b.text(x+px+12,482,f'{px} px',9.5,SEMI)

    # 19. Digital applications with original preview images.
    b.page('Aplicações / 02', 'Presença digital reconhecível.',
           'Peças conceituais com hierarquia simples, campos de cor e convites objetivos.')
    for path,x,top,w,h in [
        ('post-institucional-1080.png',M,179,228,228),
        ('post-orcamento-1080.png',302,179,228,228),
        ('story-1080x1920.png',601,179,128,228),
    ]:
        b.image(OUT/'digital'/path,x,top,w,h)
    b.text(M,427,'Post institucional',12,SEMI)
    b.text(302,427,'Convite para orçamento',12,SEMI)
    b.text(601,427,'Story',12,SEMI)
    b.text(M,454,'1080 × 1080 px',9.5,color=GLASS)
    b.text(302,454,'1080 × 1080 px',9.5,color=GLASS)
    b.text(601,454,'1080 × 1920 px',9.5,color=GLASS)
    b.para(M,493,'Adapte a área segura a cada plataforma. Confirme contatos e informações comerciais antes de publicar.',CW,9.5,color=GLASS)

    # 20. Stationery examples are reusable without fabricated contacts.
    b.page('Aplicações / 03', 'Do primeiro contato à proposta.',
           'Aplicações institucionais com marca evidente, informação organizada e espaço para o conteúdo.')
    b.rect(M,174,325,340,ICE)
    b.image(OUT/'aplicacoes'/'capa-proposta-a4.png',M+55,186,209,296)
    b.text(M+18,490,'Capa de proposta / A4',10,SEMI)
    b.rect(395,174,403,223,ICE)
    b.image(OUT/'aplicacoes'/'cartao-institucional-90x50mm.png',420,202,352,160)
    b.text(414,370,'Cartão institucional / 90 × 50 mm',10,SEMI)
    b.note(395,427,'Antes de imprimir', 'Incluir dados comerciais apenas depois de confirmados. A gráfica deve definir sangria, acabamento, papel e perfil de cor.',382)

    # 21. Uniform schematic with real logo applied.
    b.page('Aplicações / 04', 'Uma equipe com a mesma identidade.',
           'Conceito de aplicação em uniforme. Esquema vetorial ilustrativo; não é fotografia de produto.',bg='navy')
    # Front.
    b.path([(112,207),(181,180),(231,180),(299,207),(337,272),(286,298),(270,262),(270,447),(142,447),(142,262),(126,298),(75,272)],BLUE)
    b.path([(181,180),(206,214),(231,180)],NAVY)
    b.logo('compacta',198,243,62,'escura')
    b.text(205,475,'FRENTE',9,SEMI,WHITE,'center')
    # Back.
    b.path([(477,207),(546,180),(596,180),(664,207),(702,272),(651,298),(635,262),(635,447),(507,447),(507,262),(491,298),(440,272)],BLUE)
    b.path([(546,180),(571,197),(596,180)],NAVY)
    b.logo('horizontal',521,248,100,'escura')
    b.text(570,475,'COSTAS',9,SEMI,WHITE,'center')
    b.para(M,511,'A produção deve confirmar dimensões, tecido e técnica. Para bordado pequeno, use o símbolo ou uma versão sem descritivo.',CW,9.5,color=C['light'])

    # 22. Vehicle concept with wheels and recognisable side silhouette.
    b.page('Aplicações / 05', 'A marca em movimento.',
           'Conceito de identificação veicular. Esquema ilustrativo a ajustar ao modelo e às áreas reais de aplicação.')
    # Broad vehicle drawn to a geometric grid.
    b.path([(96,259),(112,231),(503,231),(553,250),(634,325),(724,340),(746,364),(746,427),(83,427),(83,305)],WHITE,GLASS,1.5)
    b.path([(531,260),(557,268),(615,323),(532,323)],C['ice'],GLASS,1)
    b.rect(112,264,390,127,NAVY)
    b.logo('horizontal',143,301,315,'negativa')
    b.line(520,245,520,410,GLASS,.7)
    b.line(104,410,724,410,GLASS,.7)
    b.rect(547,338,21,5,GLASS,radius=2)
    for x in [205,640]:
        b.circle(x-38,389,76,NAVY)
        b.circle(x-22,405,44,SILVER)
        b.circle(x-7,420,14,GLASS)
    b.text(M,484,'Leitura à distância',12,SEMI)
    b.para(239,482,'Mantenha a marca em áreas planas e evite recortes em portas, maçanetas ou vincos. Contatos e informações adicionais dependem de validação.',553,10,color=GLASS,leading=15)

    # 23. Delivery file guide.
    b.page('Produção / 01', 'O arquivo certo para cada uso.',
           'A pasta brandbook-v1 reúne versões da marca, exemplos digitais e diretrizes de produção.')
    rows=[('svg/','Marca vetorial editável','Use para layout, sinalização e ampliação.'),
          ('png/','Marca com transparência','Use em peças digitais; escolha a resolução adequada.'),
          ('pdf/','Marca vetorial para produção','Envie à gráfica com as especificações do trabalho.'),
          ('digital/','Avatares e peças de comunicação','Confira recorte, área segura e informações antes de publicar.'),
          ('aplicacoes/','Exemplos institucionais','Bases visuais; preparar o fechamento para cada fornecedor.'),
          ('fontes/','Manrope e licença OFL','Instale os pesos de apoio e preserve a licença.'),
          ('diretrizes/','Orientações e registros','Consulte a especificação e o estado de aprovação.')]
    for i,(folder,kind,body) in enumerate(rows):
        y=174+i*46
        b.text(M,y,folder,12,BOLD,MID)
        b.text(199,y,kind,10.5,SEMI)
        b.text(454,y+1,body,8.6,color=GLASS)
        b.line(M,y+31,W-M,y+31,SILVER,.5)
    b.text(M,509,'Nunca use uma captura de tela do manual como matriz da marca. Comece pelos arquivos oficiais.',9.5,SEMI)

    # 24. Concrete validation gate and source appendix.
    b.page('Produção / 02', 'Uma base pronta para validar.',
           'Esta versão organiza a identidade escolhida e seus usos. A implantação do site vem após a aprovação da marca.',bg='navy')
    checks=[('01','Marca principal','Confirmar a combinação do símbolo com o lettering e o descritivo.'),
            ('02','Sistema visual','Confirmar cores, composições, linguagem e aplicações conceituais.'),
            ('03','Produção','Aprovar provas e dimensões antes de imprimir, bordar ou adesivar.')]
    for i,(num,title,desc) in enumerate(checks):
        y=173+i*75
        b.circle(M,y+3,27,BLUE)
        b.text(M+13.5,y+9,num,8,SEMI,NAVY,'center')
        b.text(M+43,y,title,15,BOLD,WHITE)
        b.para(M+43,y+28,desc,660,10.5,color=WHITE,leading=16)
    b.line(M,413,W-M,413,WHITE,.5,alpha=.25)
    b.text(M,433,'FONTES E NOTAS DE PRODUÇÃO',8,SEMI,C['light'])
    b.para(M,456,'Briefing: prompts-site-fast-limp.md e escolhas visuais fornecidas pelo cliente.\nMatriz: reconstrução vetorial a partir dos contornos selecionados, com cores normalizadas.\nTipografia: Manrope, Google Fonts / OFL. Arquivo OFL.txt incluído na entrega.',CW,9.2,color=WHITE,leading=15)
    b.text(M,507,'github.com/google/fonts/tree/main/ofl/manrope',9,SEMI,C['light'])
    b.c.linkURL('https://github.com/google/fonts/tree/main/ofl/manrope',(M,H-522,400,H-505),relative=0,thickness=0)
    b.finish()
    return PDF


def render_and_check(pdf_path):
    """Render every page and produce compact sheets for mandatory visual QA."""
    RENDERS.mkdir(parents=True,exist_ok=True)
    doc = fitz.open(pdf_path)
    if len(doc) != 24:
        raise AssertionError(f'Unexpected PDF page count: {len(doc)}')
    pngs=[]
    text_chars=[]
    for i,page in enumerate(doc):
        pix=page.get_pixmap(matrix=fitz.Matrix(100/72,100/72),alpha=False)
        path=RENDERS/f'page-{i+1:02d}.png'
        pix.save(str(path))
        pngs.append(path)
        text_chars.append(len(page.get_text()))
        # Report text that physically escaped the page, ignoring drawing paths.
        for block in page.get_text('dict')['blocks']:
            for line in block.get('lines',[]):
                for span in line.get('spans',[]):
                    x0,y0,x1,y1=span['bbox']
                    if x0 < -1 or y0 < -1 or x1 > W+1 or y1 > H+1:
                        raise AssertionError(f'Off-page text on page {i+1}: {span["text"]}')
    # Four pages per contact sheet, 2 x 2. Full page PNGs remain available.
    thumb_w=840
    thumb_h=round(thumb_w*H/W)
    for start in range(0,24,4):
        sheet=Image.new('RGB',(thumb_w*2+36,thumb_h*2+68),'#D1D3D4')
        d=ImageDraw.Draw(sheet)
        for j,path in enumerate(pngs[start:start+4]):
            im=Image.open(path).convert('RGB')
            im.thumbnail((thumb_w,thumb_h),Image.Resampling.LANCZOS)
            x=12+(j%2)*(thumb_w+12)
            y=26+(j//2)*(thumb_h+26)
            sheet.paste(im,(x,y))
            d.text((x,y-17),f'{start+j+1:02d}',fill='#092131')
        sheet.save(RENDERS/f'contact-sheet-{start//4+1:02d}.png')
    doc.close()
    print(f'PDF created: {pdf_path}')
    print(f'Pages: 24; rendered at 100 dpi; contact sheets: 6; text chars/page: {min(text_chars)}-{max(text_chars)}')
    print(f'Visual QA: {RENDERS}')


if __name__=='__main__':
    render_and_check(build())
