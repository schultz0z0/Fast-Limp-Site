# Panfleto Fast Limp — A5

**Edição atual: v2**, refeita após o feedback do cliente com composição de panfletagem e títulos sem pontos. Use `../pdf/fast-limp-panfleto-a5-v2-impressao.pdf` para a gráfica e `../pdf/fast-limp-panfleto-a5-v2-visualizacao.pdf` para conferir. Prévia: `fast-limp-panfleto-a5-v2-previa.png`. Direção, procedência e especificações atuais em `DIRECAO-V2.md`; fonte atual em `scripts/build-flyer-v2.py`. As notas abaixo descrevem a primeira edição preservada.

16/10/2026. Arte de uma face, formato final148×210mm. Direção solicitada: clara, limpa, com foco em conversão. Identidade do brandbook aprovado; nenhuma identidade visual do anúncio antigo foi reutilizada.

## Arquivos

- `../pdf/fast-limp-panfleto-a5-impressao.pdf`: enviar à gráfica. Arte com3mm de sangria em todos lados, TrimBox/BleedBox e marcas de corte fora da sangria. Página total164×226mm; depois do corte148×210mm.
- `../pdf/fast-limp-panfleto-a5-visualizacao.pdf`: tamanho final A5, sem marcas; para visualizar ou imprimir em tamanho real100% em impressora compatível. Não escolher “ajustar à página” se o objetivo for preservar as medidas A5.
- `fast-limp-panfleto-a5-previa.png`: prévia da arte, não substituir o PDF vetorial por esta imagem na impressão.
- `especificacoes.json`: medidas, procedência e parâmetros.

A gráfica deve usar o TrimBox para o corte e manter a sangria. Cores RGB da identidade mestra; conversão para o perfil de impressão deve ser feita conforme a máquina/processo da gráfica. O arquivo não é declarado PDF/X nem usa perfil CMYK arbitrário. Logo/textos/QR permanecem vetoriais e fontes Manrope incorporadas. Foto com cerca430ppi efetivos no tamanho final. Solicitar uma prova antes da tiragem ajuda a conferir cores e leitura no papel.

## Conteúdo confirmado nesta solicitação

WhatsApp(21)96764-3628; vidros residenciais; vidros comerciais; pós-obra para residências e comércios; fachadas de vidro; vitrines. Número e serviços foram lidos da imagem enviada pelo usuário; a imagem foi explicitamente descartada como referência de design, logo, cores, foto ou promessas.

QR aponta diretamente para https://wa.me/5521967643628. Não depende de encurtador nem serviço de QR dinâmico. Nenhuma região, desconto, garantia, prazo ou alegação de treinamento/certificação foi adicionada. A fotografia é ilustrativa e usa o master licenciado já documentado em `docs/ASSETS.md` (Pexels37440103,CihatDede). O descritor e lettering vêm do PDF oficial da logo, sem redigitação.

## Conferência

Dois PDFs reabertos e renderizados. Telefone e cinco serviços presentes como texto real. Formato final148×210mm; sangria3mm; fontes incorporadas; nenhuma palavra fora da página. QR decodificado tanto no master quanto na página PDF renderizada a300dpi com o mesmo destino. Prévia inspecionada visualmente.

Fonte editável/reproduzível: `scripts/build-flyer.py`. Não houve alteração do site nem publicação.
