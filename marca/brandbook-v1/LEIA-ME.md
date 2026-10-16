# Fast Limp | pacote de identidade visual

Versão 1.0 - 14 de outubro de 2026 - Para validação.

## Direção atual

O cliente escolheu o símbolo com vidro e rodo do estudo 03 e o desenho do nome e descritor do estudo 01. Esta entrega desenvolve essa combinação em uma matriz vetorial e suas aplicações. Os estudos com planos de vidro da opção 02 foram superados e não fazem parte deste pacote.

O brandbook e a nova combinação vetorial devem ser validados antes da construção do site. Não houve implementação, publicação ou alteração do site nesta etapa.

## Arquivo que usar

| Situação | Arquivo / versão |
|---|---|
| Fundo branco ou muito claro | `svg/fast-limp-horizontal-principal.svg` |
| Fundo azul petróleo | `svg/fast-limp-horizontal-negativa.svg` |
| Aplicação em uma tinta escura | `svg/fast-limp-horizontal-escura.svg` |
| Aplicação em uma tinta branca | `svg/fast-limp-horizontal-branca.svg` |
| Reprodução preta | `svg/fast-limp-horizontal-preta.svg` |
| Espaço estreito / leitura do descritor insuficiente | Versão `compacta` sem descritor |
| Composição centralizada | Versão `vertical` |
| Avatar WhatsApp / Instagram | `digital/avatar-principal-1024.png` |
| Avatar em fundo claro | `digital/avatar-claro-1024.png` |
| Ícone pequeno | Versão `simbolo-micro`, sem os três reflexos internos |
| Favicon futuro | `digital/favicon.ico` e arquivos `avatar-principal-micro-*` |

As variantes `assinatura` contêm apenas nome e descritor, para usos em que o símbolo já esteja presente no mesmo campo visual. Não substituir o nome por uma digitação semelhante.

## Formatos e pastas

- `svg/`: arquivos vetoriais com contornos, escaláveis e sem dependência de fontes para a logo.
- `pdf/`: logos vetoriais nas mesmas composições e cores. As versões brancas precisam ser visualizadas sobre fundo escuro; o PDF não inclui um fundo escuro embutido.
- `png/`: logos com canal alpha real. Largura de 2400 px para assinaturas e 1200 px para os símbolos. O arquivo justo não inclui área de proteção embutida; preservar o respiro no layout.
- `digital/`: avatares 1024, 512 e 256 px; ícones ópticos de 16 a 128 px; dois modelos de post 1080x1080, um story 1080x1920 e capa horizontal 1640x624.
- `aplicacoes/`: PDFs vetoriais dos modelos de comunicação e suas prévias PNG. As peças são aplicações conceituais da identidade, sem contato ou dados comerciais não confirmados.
- `fontes/`: Manrope em arquivo variável original, instâncias estáticas Regular/SemiBold/Bold e licença OFL. Manrope é a tipografia de apoio, não o lettering da logo.
- `diretrizes/`: regras, paleta JSON e variáveis CSS para o futuro projeto.
- `matriz/`: comandos vetoriais da reconstrução, para manter a procedência técnica.
- `manifesto.json`: origem dos estudos usados, hashes, método e inventário das variantes.

Há 28 combinações de composição/cor da logo, cada uma entregue em SVG, PDF vetorial e PNG. O grafismo de apoio é um SVG separado, não uma assinatura alternativa.

## Proteção e dimensões

Unidade x = 1/4 da altura do símbolo na aplicação. Deixar no mínimo x livre em todos os lados. O espaçamento interno entre símbolo e lettering faz parte do desenho e não deve ser alterado.

| Versão | Largura digital mínima proposta | Largura impressa inicial |
|---|---|---|
| Horizontal com descritor | 320 px | 72 mm |
| Compacta sem descritor | 150 px | 40 mm |
| Símbolo completo | 48 px | 12 mm |
| Símbolo óptico micro | 24 px | 6 mm |

As larguras digitais se referem à marca visível, sem a área de proteção. Os ícones de 16 px são uma exportação auxiliar para favicon, com menor detalhe; não constituem o tamanho mínimo recomendado. O perfil de 1024 px já incorpora respiro para o recorte circular. Em bordado, recorte de adesivo e impressão, confirmar o menor traço viável com o fornecedor e fazer prova física. Os limites de tela não substituem prova de impressão.

## Cuidados de produção

Não deformar, rotacionar, acrescentar efeitos ou trocar a tipografia. Usar a versão negativa sobre azul petróleo e a versão branca em uma tinta quando necessário. Não usar a versão principal sobre azul semelhante ao símbolo.

As cores RGB/HEX são referências exatas de tela. Conversão para CMYK, perfil ICC, sangria, acabamento, bordado e recorte dependem do processo de produção. Os modelos de papelaria estão no formato final, sem sangria ou marcas de corte; são bases editáveis para finalização com o fornecedor.

A logo foi reconstruída com curvas a partir das silhuetas dos estudos selecionados; cores e contornos foram regularizados. A versão óptica remove apenas os reflexos internos. Conferir essa matriz e as composições na validação do brandbook.

## Fonte de apoio

Manrope, origem oficial: https://github.com/google/fonts/tree/main/ofl/manrope

Licença incluída em `fontes/OFL.txt`. O pacote contém a fonte original e instâncias estáticas para uso consistente nas peças. As peças não atribuem à Fast Limp serviços, prazos, regiões, garantias ou certificações não confirmados.
