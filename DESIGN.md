# Fast Limp — design system do site

Versão 1.0 · 15 de outubro de 2026 · Handoff para implementação.

O brandbook foi validado pelo cliente nesta conversa em 15/10/2026. Este sistema traduz a identidade aprovada para a composição das duas capturas fornecidas. A entrega atual é documental; a construção do site começa com o prompt de [PROMPT-INICIAR-SITE.md](PROMPT-INICIAR-SITE.md).

## 1. Fontes e precedência

| Fonte | Função |
|---|---|
| [Brandbook aprovado](output/pdf/fast-limp-brandbook-v1-validacao.pdf) | Identidade, logo, cores, tipografia e regras de aplicação. O nome do arquivo conserva o estado histórico “validação”; a aprovação foi registrada em [aprovacao-brandbook.md](marca/brandbook-v1/diretrizes/aprovacao-brandbook.md). |
| [Diretrizes da marca](marca/brandbook-v1/diretrizes/manual-identidade.md) | Consulta textual complementar ao PDF. |
| [Captura completa](referencias/site-modelo-completo.png) | Ordem das seções, silhueta da página, alternância de superfícies e composição desktop. Original: 752 × 5173 px. |
| [Captura de detalhes](referencias/site-modelo-detalhes.png) | Detalhes do hero, Sobre, diferenciais, depoimentos, equipe e FAQ. Original: 1024 × 768 px. É uma montagem de recortes desktop, não um layout mobile. |
| [design-system.json](design-system.json) | Tokens numéricos, aliases, componentes, inventário de seções, estados e critérios verificáveis. |
| [prompts-site-fast-limp.md](prompts-site-fast-limp.md) | Execução por etapas, conteúdo, imagens e validação. |

Instruções explícitas mais recentes do cliente prevalecem. O brandbook governa a identidade; este Markdown governa a composição e o comportamento; o JSON governa os valores. Os dois arquivos devem permanecer coerentes. Se houver divergência, registrá-la e corrigir a especificação antes de criar uma interpretação nova.

Não importar do modelo: identidade Cleanx, roxos/lilases, piscinas, textos em inglês, contatos, preços, funcionários, avaliações ou números. Preservar a arquitetura visual e os tipos de componente. A fotografia de água que aparece fora da página na segunda captura é moldura da demonstração, não fundo obrigatório do site.

### Evidência e decisões

**Observado:** header sobreposto à fotografia; painel de título com topo diagonal; conversão à direita; fotos sobrepostas; cards horizontais; galeria bento; processo escuro; badge sobre foto; depoimentos; retratos; FAQ; blog; rodapé escuro.

**Definido para implementar:** medidas CSS abaixo, pontos de quebra, empilhamento mobile, navegação sem sticky inicialmente, carrosséis manuais sem autoplay, estados de foco e tratamento de dados pendentes. As capturas não revelam o CSS original nem provam esses comportamentos. Seus pixels não equivalem diretamente a pixels CSS da futura página.

## 2. Direção visual

Uma página institucional fotográfica, com presença comercial e leitura clara. Fotografias grandes sustentam as seções; títulos curtos têm peso e contraste. Blocos de informação são predominantemente retangulares, planos e alinhados a um mesmo container. A energia visual vem do azul, das sobreposições e das diagonais, com poucos efeitos.

Preservar a composição inteira do modelo: não substituir por um hero convencional com texto sobre a foto, uma grade genérica de quatro serviços ou uma sequência curta de blocos iguais. Também não transformar tudo em cards arredondados, glassmorphism, sombras fortes ou animações de entrada.

O azul elétrico substitui o roxo de destaque. O branco gelo substitui as superfícies lilases. Azul petróleo substitui as grandes áreas quase pretas da referência. A marca continua sendo de limpeza especializada de vidros, para residências e empresas em igual importância.

## 3. Marca e arquivos oficiais

A marca vigente combina o **símbolo com vidro e rodo do estudo 03** com o lettering e descritor do estudo 01. Não usar o monograma FL nem o símbolo de dois planos do estudo 02. Não redesenhar, redigitar, recolorir livremente ou extrair a marca de uma captura do manual.

| Uso | Arquivo |
|---|---|
| Header desktop e mobile | `marca/brandbook-v1/svg/fast-limp-compacta-principal.svg` |
| Assinatura completa em fundo claro | `marca/brandbook-v1/svg/fast-limp-horizontal-principal.svg` |
| Assinatura completa em fundo escuro | `marca/brandbook-v1/svg/fast-limp-horizontal-negativa.svg` |
| Rodapé com largura reduzida | `marca/brandbook-v1/svg/fast-limp-compacta-negativa.svg` |
| Símbolo isolado | `marca/brandbook-v1/svg/fast-limp-simbolo-principal.svg` |
| Ícone pequeno | `marca/brandbook-v1/svg/fast-limp-simbolo-micro-principal.svg` |
| Favicon | `marca/brandbook-v1/digital/favicon.ico` |
| Avatar | `marca/brandbook-v1/digital/avatar-principal-1024.png` |

No header, usar a assinatura compacta sem descritor: 208 px no desktop e 156 px no celular. Isso respeita o mínimo de 150 px da compacta e evita reduzir a versão com descritor abaixo de 320 px. No rodapé, a compacta também pode ser usada quando uma coluna não comportar a assinatura completa.

Preservar proporção e área livre **x = altura visível do símbolo / 4** ao redor de toda a assinatura. A largura CSS deve medir a arte visível, não uma margem transparente inventada. Os SVGs entregues têm caixa justa; o layout fornece o respiro. A versão horizontal tem proporção aproximada 4,3693:1.

## 4. Arquitetura dos tokens

O JSON usa três camadas em `tokens`: `primitive` → `semantic` → `component`. Cada token tem `$type`, `$value` e descrição opcional. Aliases como `{primitive.color.blue}` são caminhos relativos a `tokens` e devem ser resolvidos recursivamente, sem ciclos.

É um formato próprio de especificação, com notação inspirada em sistemas de tokens; não é um arquivo declarado como estritamente compatível com DTCG. Valores como `48px` e `clamp(...)` são expressões CSS; os breakpoints são números em pixels usados nas media queries. O documento não obriga instalar uma biblioteca de tokens.

Na implementação, converter os valores em variáveis CSS e fazer componentes consumirem nomes semânticos. Exemplo de mapeamento: `semantic.color.surfaceAccent` → `--color-surface-accent`; `component.button.primary.background` → `--button-primary-bg`. Não espalhar valores de cor independentes nos componentes.

### Cores primitivas

| Token `primitive.color.*` | HEX | Papel |
|---|---|---|
| `blue` | `#1C94F0` | Destaques, painéis do hero e ações principais. |
| `navy` | `#092131` | Textos, processo, rodapé e contraste sobre azul. |
| `white` | `#FFFFFF` | Superfície principal e texto sobre petróleo. |
| `mid` | `#1274C2` | Links em fundos brancos. |
| `light` | `#5AB7F5` | Detalhes e links sobre petróleo. |
| `glass` | `#2D546F` | Texto secundário em fundo claro, bordas de controles. |
| `ice` | `#EFF0F0` | Seções alternadas, cards leves e fundos de apoio. |
| `silver` | `#D1D3D4` | Divisórias e bordas decorativas. |
| `black` | `#010202` | Apoio pontual; não substitui petróleo como fundo escuro padrão. |

Não adicionar lilás, roxo, dourado de estrelas, verde de WhatsApp ou novas cores quentes. O ícone de WhatsApp pode usar a cor semântica do botão; sua forma deve permanecer reconhecível.

### Cores semânticas principais

| Tokens `semantic.color.*` | Resultado |
|---|---|
| `surface`, `surfaceAlt`, `surfaceInverse`, `surfaceAccent` | Branco, gelo, petróleo, azul principal. |
| `text`, `textMuted` | Petróleo e azul acinzentado em fundo claro. |
| `textInverse`, `textInverseMuted` | Branco e gelo em fundo petróleo. |
| `textOnAccent` | Petróleo sobre azul principal. |
| `link`, `linkInverse` | Azul médio em claro; azul claro em petróleo. |
| `borderSubtle`, `borderControl` | Prata decorativa; azul acinzentado em contornos funcionais. |
| `focusOnLight`, `focusOnDark` | Petróleo e azul claro. |
| `errorText`, `errorBorder` | Petróleo, acompanhado de mensagem e ícone; não depender de vermelho. |

**Contraste:** petróleo/azul principal ≈ 5,14:1; azul médio/branco ≈ 4,88:1; branco/petróleo ≈ 16,49:1. Branco/azul principal ≈ 3,21:1: reservar a texto grande, não usar como padrão em corpo, legendas ou botões pequenos. No painel azul do hero, o texto fica petróleo; o botão claro usa texto petróleo. Isso adapta a cor do template sem perder legibilidade.

### Tipografia

Manrope é a única família principal, com pesos 400, 600 e 700 e fallback `Arial, sans-serif`. Carregar o arquivo variável local `marca/brandbook-v1/fontes/Manrope-Variable.ttf` ou os três arquivos estáticos indicados no JSON. Preservar a licença OFL. Usar `font-display: swap` e dimensões estáveis para evitar saltos.

| Estilo semântico | Tamanho | Entrelinha | Peso | Tracking |
|---|---|---|---|---|
| `display` / H1 | `clamp(40px, 4.6vw, 64px)` | 1,04 | 700 | -0,04em |
| `h2` | `clamp(28px, 3vw, 40px)` | 1,12 | 700 | -0,03em |
| `h3` | `clamp(20px, 1.8vw, 24px)` | 1,25 | 700 | -0,02em |
| `body` | 16 px | 1,6 | 400 | 0 |
| `small` | 14 px | 1,5 | 400 | 0 |
| `eyebrow` | 13 px | 1,4 | 600 | 0,02em |
| `button` | 15 px | 1,25 | 700 | 0 |

Eyebrows curtos com ícone linear discreto; não transformar todos os textos em caixa alta. Corpo limitado normalmente a 52–65 caracteres por linha. H1 com largura aproximada de 12–16 caracteres por linha; ajustar a largura do bloco antes de inserir quebras. Não transportar `<br>` do desktop para o mobile sem revisão.

### Espaçamento, forma, profundidade e movimento

- Escala primitiva: 0, 4, 8, 12, 16, 20, 24, 32, 40, 48, 56, 64, 72, 80, 96, 120 e 160 px.
- Seções: 96 px de padding vertical no desktop; 72 px em tablet; 56 px no celular. Ajustar apenas quando uma sobreposição intencional exigir, mantendo o ritmo da página.
- Cards de conteúdo e fotografias: cantos retos. Botões e inputs: raio de 4 px. Outros contornos pequenos podem usar 8 px. Header externo pode ter raio superior de 20 px no desktop. Círculos são reservados a controles e avatares.
- Sombras: nenhuma nos cards comuns. Header: `0 8px 24px rgba(9,33,49,.08)`; pequeno painel flutuante, se necessário: `0 12px 32px rgba(9,33,49,.10)`.
- Transições de cor: 150 ms; deslocamento e acordeão: 220 ms; teto usual: 320 ms. Respeitar `prefers-reduced-motion`. Não adotar parallax, autoplay ou reveals que ocultam conteúdo inicialmente.

## 5. Grid e comportamento responsivo

| Faixa | Condição | Gutter mínimo | Grid lógico |
|---|---|---|---|
| Mobile | abaixo de 768 px | 20 px | 4 colunas |
| Tablet | a partir de 768 px | 32 px | 8 colunas |
| Desktop | a partir de 1024 px | 40 px | 12 colunas |

Breakpoints auxiliares: 640, 1280 e 1600 px. Container principal: `width: min(1200px, calc(100% - 2 * gutter))`, centralizado. Container largo do header: máximo 1320 px. Em 1440 px, o conteúdo principal tem 120 px de margem lateral. A página e os fundos de seção continuam em largura total, sem moldura fotográfica externa.

O menu compacto entra abaixo de 1024 px. O header não é sticky inicialmente; esse comportamento não pode ser deduzido das capturas. Em telas largas, não esticar indefinidamente títulos e fotografias. Em telas pequenas, empilhar componentes e reordenar por leitura, sem reduzir um desktop inteiro por escala.

Sobreposições são parte do desenho, não defeitos: painel do hero, colagem do Sobre, badge da fotografia e identificações da equipe. Usar grid e margens de composição controladas. O recorte diagonal pertence a uma camada decorativa de fundo; não cortar textos, focos e áreas clicáveis com `clip-path` no conteúdo inteiro.

## 6. Sequência canônica e composição de cada seção

Os IDs e a ordem abaixo correspondem a `sections` no JSON. Topbar, header e hero formam o primeiro grupo; a chamada final e o rodapé formam o último. Preservar também os módulos condicionais na arquitetura e na revisão local.

### 01 · `#inicio` — topbar, header, hero e conversão

- Topbar de 32 px, azul com texto petróleo: contato/localização reais à esquerda e redes confirmadas à direita. Pode ser simplificada ou ocultada no celular; não publicar dados da referência.
- Navegação branca flutuante sobre a foto, inset superior de 24 px no desktop, altura de 84 px; 76 px no celular. Logo à esquerda, links no centro e CTA à direita. Links sugeridos: Sobre, Serviços, Referências, Como funciona e Dúvidas. Não criar dropdowns vazios para imitar setas.
- Fotografia ampla: altura inicial 680 px desktop, 520 px tablet e 360 px mobile. Vidro e profissional são os assuntos; revisar o ponto focal em cada largura. Borda inferior com diagonal decorativa aproximada de 56 px no desktop.
- Abaixo da fotografia, grid principal de duas colunas `1.2fr 1fr`, gap de 32 px, subindo 220 px sobre a área da foto no desktop e 160 px em tablet. O card principal à esquerda tem topo diagonal de 32 px, fundo azul, texto petróleo, padding de 48 px e padding superior de 72 px. Altura é determinada pelo conteúdo.
- O painel comercial à direita alinha pela base do painel principal. Preservar o cabeçalho integral e duas colunas do template, adaptadas para **Residências / Empresas** com texto neutro e ação de orçamento. Não inventar planos, promoção, preço ou condições. Cabeçalho azul/petróleo, corpo branco/gelo e divisória discreta.
- Mobile: fluxo de foto → card de texto → painel de conversão. Sobreposição de 48 px apenas no início do card; padding 24 px e topo 48 px; diagonal de 16 px. Não manter texto em posição absoluta. As duas colunas internas do painel podem permanecer lado a lado se legíveis, ou empilhar abaixo de 360 px.
- O CTA principal do painel azul pode ser claro, com texto petróleo. A prova social do original só aparece com dados verificáveis; na sua ausência, usar apoio neutro “Para residências e empresas”, sem avatares fictícios ou estrelas.
- Não acrescentar uma faixa de confiança independente entre hero e Sobre: ela não faz parte desta referência.

### 02 · `#sobre` — colagem e apresentação

Duas colunas `0.95fr 1.05fr`. À esquerda, três fotografias deslocadas dentro de uma composição aproximadamente quadrada, com respiro e sobreposições entre retângulos. À direita, eyebrow, H2, parágrafo curto, dois benefícios com ícones e CTA. Abaixo de 768 px, colagem acima dos textos; reduzir os deslocamentos para caber sem overflow. Não trocar por uma única imagem ao lado de texto genérico.

### 03 · `#servicos` — faixa horizontal de cards

Superfície gelo. Título à esquerda e controles circulares à direita. No desktop, mostrar aproximadamente três cards completos e uma parte do próximo. Foto 4:3, título, descrição curta e link abaixo; sem sombra pesada. Gap de 24 px. Base inicial do card desktop: `calc((100% - 48px) / 3.15)`; mobile: 86% da área disponível. Catálogo-alvo de quatro itens é uma meta de composição, não uma confirmação de quatro serviços.

Carrossel manual com scroll-snap e setas funcionais; sem autoplay. Conter o recorte na faixa de cards, sem `overflow-x: hidden` aplicado à página para esconder defeitos.

### 04 · `#referencias` — galeria bento

Cabeçalho centralizado sobre superfície branca. Meta de seis imagens: uma vertical alta à esquerda; duas menores ao centro; uma horizontal no topo à direita e duas menores abaixo. Usar quatro trilhas `1fr 0.72fr 0.64fr 0.64fr`, duas linhas e áreas `lead midTop wide wide` / `lead midBottom smallA smallB`. Altura inicial desktop: 520 px; gap: 16 px.

No celular, duas colunas com imagem principal destacada; reduzir para uma coluna abaixo de 360 px quando necessário. O visualizador deve manter proporção, legenda e retorno de foco. Não substituir a galeria por apenas duas fotos. Com fotos ilustrativas, nomear a seção “Referências de serviço”; reservar “Resultados” a trabalhos reais autorizados.

### 05 · `#como-funciona` — processo e mídia

Uma seção petróleo, com título centralizado, linha horizontal de quatro marcadores e quatro cards claros de etapas. Abaixo, mídia horizontal 16:9 com dimensão generosa. No celular, etapas em lista vertical e conectores verticais.

O fluxo operacional precisa de confirmação antes de virar promessa de atendimento. Na revisão local, pode ser identificado como proposta. Botão de reprodução só existe quando há vídeo real e reproduzível. Sem vídeo, preservar o quadro com foto estática e legenda apropriada; não desenhar um play sem ação. Sem autoplay; conteúdo falado requer legendas.

### 06 · `#diferenciais` — texto, foto e badge

Duas colunas equilibradas. À esquerda, título, parágrafo, quatro itens com marcadores e CTA; à direita, fotografia 4:3 e pequeno badge azul sobre sua base. O badge deve conter um atributo confirmado ou frase neutra, como “Cuidado nos detalhes”. Não transportar “10+ anos” da referência. Mobile: texto → foto → badge em fluxo ou com pequena sobreposição segura.

### 07 · `#depoimentos` — citação em destaque

Fundo gelo, título centralizado, conteúdo de até 720 px, uma citação por vez, identificação real e setas laterais. Estrelas azuis e nota só com avaliação e fonte verificadas. No celular, setas abaixo da citação e altura flexível. Sem rotação automática.

Na revisão local, sem conteúdo real, preservar o bloco como painel explicitamente identificado “Depoimentos — conteúdo pendente”, sem frase ou pessoa inventada. Em produção, manter o módulo no código e não publicar sua área até receber conteúdo autorizado; registrar a diferença na entrega.

### 08 · `#equipe` — três retratos com identificação sobreposta

Título à esquerda, ação à direita e três cards 3:4. Identificação branca sobre a base da foto; card central pode usar azul/petróleo como destaque. Links sociais só se reais. Acesso à identificação por toque e teclado; não depender de hover. Mobile pode usar faixa manual ou uma coluna.

Na revisão local, sem equipe real, usar slots declarados pendentes; não gerar retratos nem inventar nomes para representar funcionários. Em produção, segurar esse módulo até receber pessoas, funções, fotos e autorizações reais. A aprovação do brandbook não confirma esses dados.

### 09 · `#duvidas` — FAQ em duas colunas

Fundo gelo. Coluna esquerda com título, introdução e card claro de ajuda. Coluna direita com cerca de seis itens de acordeão, gap de 12 px e linha fechada com mínimo de 56 px. Primeiro item aberto é a configuração inicial proposta. Item aberto azul/petróleo; itens fechados claros/petróleo. No celular, introdução e ajuda acima do acordeão.

Perguntas e respostas devem ser úteis para contratação. A região, o preparo do ambiente, os procedimentos e as condições comerciais dependem de confirmação. Botões com `aria-expanded` e relação explícita com os painéis; permitir leitura de perguntas longas sem cortar.

### 10 · `#conteudos` — três cards editoriais

Cabeçalho centralizado; três colunas com fotografia 3:2, metadados discretos, título e destino real. Mobile em uma coluna, sem carrossel obrigatório. Na revisão, sem artigos, mostrar slots editoriais pendentes; não inventar datas, autoria, publicação ou links. Em produção, publicar apenas conteúdo existente e revisado, com leitura real acessível.

### 11 · `#contato` — CTA final e rodapé único

Um único campo petróleo: chamada/CTA no topo, divisor, quatro colunas e base legal. Colunas: marca/descrição/redes; navegação; serviços confirmados; contato e ação. Essa composição ocupa o lugar da newsletter do template enquanto não houver captação real integrada — não criar formulário que apenas simula inscrição.

Usar texto branco/gelo e links de apoio azul claro. Mobile: CTA empilhado; colunas passam a duas e depois uma. Copyright com ano atual; privacidade aponta para página real. Sem destino ou telefone confirmado, a revisão local mostra uma indicação de pendência sem link falso. Não produzir dois rodapés ou uma segunda faixa de CTA azul fora da composição.

## 7. Componentes, estados e UX

| Componente | Regra |
|---|---|
| Botão principal | Azul/petróleo; 48 px de altura, padding horizontal 24 px, gap 8 px, raio 4 px. Hover: petróleo/branco. Active: azul acinzentado/branco. |
| Botão sobre painel azul | Branco/petróleo ou petróleo/branco; manter contraste do texto normal. |
| Botão outline | Transparente, texto petróleo e borda azul acinzentado; hover gelo. |
| Controle circular | Área mínima 44 × 44 px, seta reconhecível e nome acessível. Não usar apenas glifo sem nome. |
| Link | Azul médio em claro, azul claro em escuro; indicador de hover/foco além da simples mudança de cor. |
| Card fotográfico | Retangular e plano; proporção definida por módulo; hover de imagem até 1,03, contido no recorte. |
| Input | Mínimo 48 px, fonte de 16 px, label visível, borda azul acinzentado. Só incluir se houver necessidade e destino reais. |
| Erro | Mensagem compreensível, ícone e borda petróleo; anunciar a mudança quando necessário. Não depender de cor. |
| Foco | Contorno de 2 px, offset de 3 px; petróleo em claro e azul claro em escuro. Acrescentar separação contrastante quando o próprio fundo for azul. |
| Desabilitado | Sem interação, sem link enganoso, opacidade 0,55; usar semântica nativa quando disponível. |
| Loading | Apenas em trabalho assíncrono real, mantendo texto compreensível e `aria-busy`. Não simular latência no WhatsApp. |

Menu mobile com botão real, estado expandido, fechamento por Escape e retorno do foco. Navegação por âncoras reais e IDs existentes. Carrosséis identificados e operáveis por teclado, ponteiro e toque; desabilitar setas sem destino no fim da faixa. Diálogos com fechamento visível, Escape, contenção e restauração de foco.

Não copiar do modelo interações que não foram observadas. Acessibilidade e responsividade são requisitos de adaptação, não justificativa para trocar a arquitetura visual.

## 8. Conteúdo, imagens e publicação

Dois modos devem ser explicitamente diferenciados:

1. **Revisão local:** manter a composição completa e identificar conteúdo ausente como rascunho ou pendência. Uma área vazia revisável é preferível a uma pessoa, avaliação ou contato inventados. CTA sem WhatsApp real pode levar a um painel local de contato pendente que explica a situação; nunca fabricar um número.
2. **Produção:** habilitar apenas dados confirmados e destinos reais. Módulos dependentes de evidência ficam retidos até receber material; listar as retenções. Não publicar placeholders nem remover silenciosamente seções da comparação.

Fotos necessárias: hero; três para Sobre; até quatro de serviços; seis da galeria; poster de processo; foto de diferenciais; três retratos reais; três imagens editoriais. Quantidades são alvos de composição e podem ser preenchidas por etapas. Não duplicar fotografias para disfarçar falta de material.

Fotografia ilustrativa deve ser identificada e nunca ser apresentada como cliente, resultado ou equipe reais. Mostrar vidro, rodo, luz e reflexos plausíveis. Não incluir piscinas nem operações em altura não confirmadas. Preservar originais e, na implementação, gerar derivados responsivos com dimensões intrínsecas e corte individual. Otimizar WebP/AVIF sem deformar.

Dados ainda pendentes: cidade, região, telefone, WhatsApp, redes, catálogo de serviços, operação, diferenciais, fotos, depoimentos, equipe, vídeo, artigos, domínio e privacidade. O brandbook validado não preenche essas lacunas.

## 9. Critérios de implementação e conferência

- Inspecionar e preservar a stack. Sem projeto existente, usar HTML semântico, CSS e JavaScript modular, adequados ao site institucional estático. Não introduzir backend ou CMS por inferência.
- Uma H1; H2/H3 em ordem; `lang="pt-BR"`; link para pular ao conteúdo. Texto e navegação reais, sem usar a captura como página pronta.
- Contraste mínimo de 4,5:1 para texto normal; 3:1 para texto grande, entendido como pelo menos 24 px regular ou 18,667 px em negrito. Controles e estados precisam de contraste visível. Não declarar conformidade de um site que ainda não foi testado.
- Alvos de toque projetados com mínimo de 44 px. Considerar zoom/reflow em 200%, teclado e redução de movimento.
- Testar 320, 360, 390, 768, 1024, 1440 e 1920 px. Comparação principal em 1440 px desktop e 390 px mobile, normalizando a largura da captura completa para avaliar proporções.
- Conferir a silhueta da página inteira e também cada dobra: hero sobreposto, colagem, faixa de serviços, bento, bloco escuro, badge, módulos sociais, FAQ, editorial e rodapé.
- Não esconder overflow horizontal da página para encobrir erros. Não haver texto/foco cortado por diagonais, foto esticada ou CTA sobrepondo conteúdo.
- Verificar navegação, mensagens de WhatsApp codificadas, controles, mídias, formulários e ausência de links mortos. Sem destino real, sinalizar pendência no modo local.
- Usar metadados e SEO local somente com fatos confirmados. Não criar dados estruturados de avaliação, endereço ou serviço fictícios.
- Executar build e verificações da stack quando existirem. Entregar capturas e lista de pendências. Não publicar automaticamente.

### Etapas compartilhadas com o arquivo de prompts

| Etapa | Entrega |
|---|---|
| 00 | Leitura das fontes, inventário do projeto, assets e dados pendentes. |
| 01 | Base, tokens, fonte, assets oficiais, topbar, header, hero e conversão. |
| 02 | Sobre em colagem e carrossel de serviços. |
| 03 | Galeria bento e processo/mídia. |
| 04 | Diferenciais, estrutura de depoimentos e equipe. |
| 05 | FAQ, conteúdo editorial, CTA final e rodapé único. |
| 06 | Integração, responsividade, acessibilidade, performance e SEO. |

Parar para revisão visual ao concluir cada etapa de implementação. A tarefa atual termina nos documentos, não no site.

## 10. Fontes técnicas consultadas

- [W3C — contraste mínimo](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
- [W3C APG — carrossel](https://www.w3.org/WAI/ARIA/apg/patterns/carousel/).
- [W3C APG — acordeão](https://www.w3.org/WAI/ARIA/apg/patterns/accordion/).

Os requisitos foram adaptados para este projeto; as capturas fornecidas não constituem evidência de que a referência já os atende.
