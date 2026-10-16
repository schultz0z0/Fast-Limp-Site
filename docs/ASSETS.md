# Assets fotográficos — Fast Limp

Atualização16/10/2026 (FL-10): fotografias existentes preservadas. Por solicitação do cliente, a interface local não exibe rótulos de banco de imagens ou revisão; a procedência permanece documentada aqui. Três derivados `team-01/02/03-640.webp` usam os masters6197122,6195281 e37440103 para perfis de exemplo na prévia local; os módulos e esses derivados não entram em `dist-production/`. Não são fotos de funcionários ou endossos à marca. Artigos foram removidos do site, com masters e derivados anteriores preservados nas fontes. As descrições anteriores deste documento sobre rótulos visíveis pertencem à entrega original.

Seleção e inspeção visual: 15/10/2026. Todas as fotografias são **ilustrativas de banco de imagens**. Não representam funcionários, clientes, instalações atendidas ou serviços executados pela Fast Limp. Não há montagem de antes/depois. Nenhuma fotografia foi gerada por IA ou teve uniforme/logotipo alterado.

## Proveniência e licença

As imagens foram baixadas do CDN oficial `images.pexels.com`. A [licença oficial Pexels](https://www.pexels.com/license/) foi consultada. Ela permite uso e adaptação em sites comerciais; atribuição é opcional. Não se deve sugerir endosso das pessoas retratadas, usar as imagens como marca ou revender o arquivo isolado. O uso nesta entrega é exclusivamente ilustrativo, acompanhado dessa identificação no site.

| Original preservado | Autor / fonte oficial | Conteúdo verificado |
|---|---|---|
| `6197122.jpg` | Tima Miroshnichenko — [Pexels](https://www.pexels.com/photo/6197122/); [download oficial creditado](https://images.pexels.com/photos/6197122/pexels-photo-6197122.jpeg?cs=srgb&dl=pexels-tima-miroshnichenko-6197122.jpg&fm=jpg) | Profissional com rodo em grande vidro residencial, ao nível do chão. |
| `6197123.jpg` | Tima Miroshnichenko — [Pexels](https://www.pexels.com/photo/man-wearing-an-orange-coveralls-6197123/) | Detalhe da ferramenta e das mãos durante a limpeza. |
| `6195281.jpg` | Tima Miroshnichenko — [Pexels](https://www.pexels.com/de-de/foto/frau-fenster-zimmer-drinnen-6195281/) | Limpeza de janela residencial com pano. |
| `4440538.jpg` | Polina Tankilevitch — [download oficial creditado](https://images.pexels.com/photos/4440538/pexels-photo-4440538.jpeg?cs=srgb&dl=pexels-polina-tankilevitch-4440538.jpg&fm=jpg) relacionado na [página da mesma sessão](https://www.pexels.com/photo/a-person-cleaning-a-glass-window-4440540/) | Detalhe de mão limpando vidro e caixilho. |
| `4440536.jpg` | Polina Tankilevitch — [download oficial creditado](https://images.pexels.com/photos/4440536/pexels-photo-4440536.jpeg?cs=srgb&dl=pexels-polina-tankilevitch-4440536.jpg&fm=jpg) relacionado na [página da mesma sessão](https://www.pexels.com/photo/a-person-cleaning-a-glass-window-4440540/) | Acabamento de base de janela. |
| `37440103.jpg` | Cihat Dede — [Pexels](https://www.pexels.com/photo/professional-window-cleaner-at-work-outdoors-37440103/) | Limpeza externa de vidro comercial, pessoa no piso, sem cordas ou acesso em altura. |
| `1571460.jpg` | Viaceslav Kat — [Pexels](https://www.pexels.com/photo/interior-design-of-a-house-1571460/) | Ambiente residencial com entrada de luz natural. |
| `380768.jpg` | Marc Mueller — [Pexels](https://www.pexels.com/photo/green-leafed-plants-380768/) | Ambiente de escritório com janelas e luz natural. |

Os originais adquiridos ficam em `site/assets/originals/`. São os masters de download do Pexels em até 2400 px de largura; não foram sobrescritos com recortes. O CDN preserva a proporção do arquivo fonte. Os derivados são locais e não geram requisições externas em execução.

## Contrato dos derivados

Diretório: `site/assets/photos/`. Cada nome abaixo tem os sufixos `-640.webp`, `-1280.webp` e `-1920.webp`. Compressão WebP qualidade 82; os cortes usam Pillow/Lanczos. Não há alteração de cor, de rosto ou de conteúdo. O script reprodutível é `scripts/prepare-photos.py` e requer Pillow. `contact-sheet.jpg` permite revisar os oito masters selecionados.

| Nome lógico | Original | Proporção | 640w | 1280w | 1920w |
|---|---:|---|---|---|---|
| hero | 37440103 | 16:9 | 640×360 | 1280×720 | 1920×1080 |
| hero-mobile | 37440103 | 1:1 | 640×640 | 1280×1280 | 1920×1920 |
| about-01 | 6195281 | 3:4 | 640×853 | 1280×1707 | 1920×2560 |
| about-02 | 4440538 | 4:3 | 640×480 | 1280×960 | 1920×1440 |
| about-03 | 6197123 | 4:3 | 640×480 | 1280×960 | 1920×1440 |
| service-01 | 1571460 | 4:3 | 640×480 | 1280×960 | 1920×1440 |
| service-02 | 380768 | 4:3 | 640×480 | 1280×960 | 1920×1440 |
| service-03 | 37440103 | 4:3 | 640×480 | 1280×960 | 1920×1440 |
| service-04 | 4440536 | 4:3 | 640×480 | 1280×960 | 1920×1440 |
| gallery-01 | 37440103 | 3:4 | 640×853 | 1280×1707 | 1920×2560 |
| gallery-02 | 4440538 | 1:1 | 640×640 | 1280×1280 | 1920×1920 |
| gallery-03 | 1571460 | 1:1 | 640×640 | 1280×1280 | 1920×1920 |
| gallery-04 | 6197122 | 16:9 | 640×360 | 1280×720 | 1920×1080 |
| gallery-05 | 6195281 | 1:1 | 640×640 | 1280×1280 | 1920×1920 |
| gallery-06 | 4440536 | 1:1 | 640×640 | 1280×1280 | 1920×1920 |
| process | 6197123 | 16:9 | 640×360 | 1280×720 | 1920×1080 |
| why | 6197122 | 4:3 | 640×480 | 1280×960 | 1920×1440 |
| article-01 | 4440538 | 3:2 | 640×427 | 1280×853 | 1920×1280 |
| article-02 | 380768 | 3:2 | 640×427 | 1280×853 | 1920×1280 |
| article-03 | 4440536 | 3:2 | 640×427 | 1280×853 | 1920×1280 |

## Direção e reuso

O hero tem cortes desktop e celular próprios para preservar profissional e ferramenta. Na revisão integrada, o original 6197122 foi substituído por 37440103 apenas no hero: a distância vertical entre rosto e rodo na fotografia anterior impedia preservar ambos entre header e painel. O novo corte desktop usa gravidade `(0.5, 0.42)`; o mobile quadrado usa `(0.5, 0.35)`. A galeria contém seis originais distintos; seus assuntos não simulam seis resultados executados. O reuso fora da galeria é intencional e está explicitado na tabela. Artigos usam apenas imagens de apoio em slots editoriais pendentes, sem sugerir autoria ou publicação real.

Fotos candidatas de trabalho em altura, retratos de equipe, desinfecção geral e outros assuntos foram rejeitadas e não integram os derivados finais. Os três slots da equipe devem permanecer declaradamente pendentes, sem retratos de stock.

As assinaturas oficiais, favicon e Manrope são copiados sem alteração a partir de `marca/brandbook-v1/` pelo coordenador. Seus originais e a licença OFL permanecem preservados no pacote da marca.

## Verificações

`prepare-photos.py --validate-only` confirmou 60 arquivos WebP decodificáveis, dimensões iguais ao manifesto e seis masters diferentes na galeria. Foram inspecionados visualmente o contact sheet, os dois recortes do hero e o card da limpeza comercial. Hero 1920w: 211.640 bytes; hero mobile 640w: 56.590 bytes. O navegador deve selecionar uma variante por `srcset`/`picture` e usar lazy loading abaixo da dobra.

Após a substituição, o hero foi renderizado sobre a interface real com Playwright em 1440×1000 e 390×844, interceptando somente os novos arquivos de imagem para evitar um build concorrente. As capturas de revisão mostram rosto e rodo abaixo do header e acima/ao lado do painel azul nos dois tamanhos. Nenhum CSS foi alterado nessa correção. O coordenador deve repetir as capturas finais após o rebuild normal.
