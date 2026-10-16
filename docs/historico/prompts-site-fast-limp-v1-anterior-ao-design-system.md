# Prompts para o site da Fast Limp — Limpeza de Vidros

Guia adaptado para VS Code + Antigravity, Codex, Claude Code ou outro assistente de desenvolvimento.

Este documento mantém a lógica de construção por etapas do template original, mas foi atualizado especificamente para a **Fast Limp — Limpeza de Vidros**, com linguagem, imagens, seções, SEO e identidade visual voltados ao serviço de limpeza profissional de vidros.

> Importante: a logo atual é provisória. Preserve-a enquanto ela for a referência aprovada, mas mantenha a implementação preparada para trocar o arquivo da marca sem refazer o layout.

---

## Como usar

1. Preencha os dados ainda pendentes da Fast Limp na ficha abaixo.
2. Anexe a logo provisória/oficial, o mockup aprovado e as fotografias disponíveis.
3. Execute um prompt por vez.
4. Compare o resultado com a referência na mesma largura de tela antes de avançar.
5. Use os prompts de refinamento apenas quando houver diferenças concretas.
6. Escolha um rodapé: o básico da etapa 05 ou a alternativa detalhada da etapa 09. Não implemente os dois simultaneamente.
7. Não invente serviços, tempo de mercado, garantias, avaliações, certificações, endereço ou regiões de atendimento que não tenham sido confirmados.

Os campos `[[CAMPO]]` continuam sendo variáveis a substituir antes da publicação.

---

# Identidade visual da Fast Limp

A identidade deve comunicar **limpeza, transparência, brilho, precisão, agilidade e profissionalismo**.

A Fast Limp deve parecer uma empresa especializada em limpeza de vidros, e não uma empresa de limpeza genérica. Evite linguagem visual baseada em baldes, espuma excessiva, produtos domésticos ou elementos infantis.

## Paleta de cores

| Papel | Cor | HEX |
|---|---|---|
| Preto profundo | Fundo principal e contraste | `#010202` |
| Azul elétrico | Cor principal / CTA / destaques | `#1C94F0` |
| Azul médio | Links e elementos secundários | `#1274C2` |
| Azul claro | Reflexos, detalhes e gradientes discretos | `#5AB7F5` |
| Azul petróleo | Fundos escuros e seções premium | `#092131` |
| Azul acinzentado | Vidro, superfícies e elementos neutros | `#2D546F` |
| Branco gelo | Fundos claros e textos sobre escuro | `#EFF0F0` |
| Prata | Bordas, divisórias e detalhes neutros | `#D1D3D4` |
| Branco puro | Contraste máximo quando necessário | `#FFFFFF` |

### Regras da paleta

- Use `#1C94F0` como principal cor de destaque.
- Em fundos claros, prefira `#1274C2` ou uma variação mais escura para textos pequenos quando o contraste do azul elétrico não for suficiente.
- Use `#092131` ou `#010202` nas seções escuras.
- Use `#5AB7F5` apenas para pequenos reflexos, detalhes ou gradientes discretos.
- Não transforme o site em um layout neon.
- Evite gradientes chamativos. Quando usados, devem remeter a vidro/reflexo de forma sutil.
- Não introduza cores quentes como laranja, amarelo ou vermelho sem aprovação.
- Preserve bastante branco e espaço negativo para reforçar sensação de limpeza.
- O visual deve ser moderno, técnico e premium, mas acessível.

---

## Ficha de personalização

| Campo | Preencher com |
|---|---|
| `[[MARCA]]` | **Fast Limp** |
| `[[SEGMENTO]]` | **Limpeza profissional de vidros** |
| `[[CIDADE]]` | Cidade da empresa |
| `[[UF]]` | Sigla do estado |
| `[[REGIAO]]` | Região de atendimento confirmada |
| `[[TELEFONE_EXIBICAO]]` | Telefone formatado para exibição |
| `[[WHATSAPP_URL]]` | URL completa do WhatsApp, com código do país e DDD |
| `[[INSTAGRAM_URL]]` | URL oficial do Instagram |
| `[[FACEBOOK_URL]]` | URL oficial do Facebook, se houver |
| `[[INSTAGRAM_USUARIO]]` | Identificador com @ |
| `[[DOMINIO]]` | Domínio definitivo, quando confirmado |
| `[[PRIVACIDADE_URL]]` | Destino real da política de privacidade |
| `[[SOBRE_DESTINO]]` | Página institucional ou perfil oficial para o link Conheça a Fast Limp |
| `[[COR_ACENTO]]` | `#1C94F0` |
| `[[COR_ACENTO_SECUNDARIA]]` | `#1274C2` |
| `[[COR_ACENTO_CLARA]]` | `#5AB7F5` |
| `[[COR_ESCURO]]` | `#092131` |
| `[[COR_PRETO]]` | `#010202` |
| `[[COR_VIDRO]]` | `#2D546F` |
| `[[COR_CLARA]]` | `#EFF0F0` |
| `[[COR_PRATA]]` | `#D1D3D4` |
| `[[COR_ACENTO_TEXTO]]` | `#0B67AE` ou outra variação aprovada com contraste adequado |
| `[[FONTE]]` | Família tipográfica aprovada. Sugestão inicial: **Manrope** ou **Inter** |
| `[[HERO_EYEBROW]]` | Ex.: “LIMPEZA PROFISSIONAL DE VIDROS” |
| `[[HERO_TITULO]]` | Ex.: “Vidros limpos. Ambientes que fazem outra impressão.” |
| `[[HERO_DESCRICAO]]` | Ex.: “Cuidado profissional para vidros de residências e empresas, com atenção aos detalhes e ao acabamento.” |
| `[[SOBRE_TEXTO]]` | Texto institucional com fatos confirmados |
| `[[MARCA_DESCRICAO]]` | Descrição curta para o rodapé, em até duas linhas |
| `[[DIFERENCIAL_1_TITULO]]` e `[[DIFERENCIAL_1_TEXTO]]` | Primeiro diferencial real |
| `[[DIFERENCIAL_2_TITULO]]` e `[[DIFERENCIAL_2_TEXTO]]` | Segundo diferencial real |
| `[[DIFERENCIAL_3_TITULO]]` e `[[DIFERENCIAL_3_TEXTO]]` | Terceiro diferencial real |
| `[[SERVICO_1]]` a `[[SERVICO_4]]` | Quatro serviços realmente oferecidos |
| `[[MONOGRAMA]]` | Símbolo “FL” ou outro elemento isolável da logo |

### Sugestões de serviços — confirmar antes de publicar

- Limpeza de vidros residenciais
- Limpeza de vitrines e fachadas
- Limpeza de vidros pós-obra
- Limpeza/manutenção periódica

Se algum item não fizer parte da operação da Fast Limp, substitua pelo serviço real.

### Sugestões de diferenciais — usar somente se forem verdadeiros

- Atendimento residencial e comercial
- Cuidado com acabamento e detalhes
- Orçamento rápido pelo WhatsApp
- Equipe especializada
- Atendimento programado

Não publique um diferencial apenas porque aparece nesta lista.

---

## Organização sugerida das imagens

| Arquivo | Uso |
|---|---|
| `logo-principal.png` | Logo Fast Limp para fundos claros/escuros conforme versão aprovada |
| `logo-branca.png` | Versão branca da logo, se necessária |
| `hero.png` | Hero com profissional limpando uma grande superfície de vidro |
| `residencial.png` | Card de limpeza residencial |
| `fachada-comercial.png` | Card de vitrines/fachadas |
| `pos-obra.png` | Card de limpeza de vidros pós-obra |
| `manutencao.png` | Card de manutenção recorrente |
| `resultado-01.png` | Foto real ou referência visual de resultado |
| `resultado-02.png` | Foto real ou referência visual de resultado |
| `detalhe-limpeza.png` | Seção Sobre |
| `favicon.png` | Símbolo quadrado da Fast Limp |

Preserve os originais. Gere formatos otimizados para publicação sem substituir os arquivos-fonte.

Fotografias geradas por IA são **ilustrativas**. Para apresentar serviços realizados, antes/depois, clientes ou obras reais, use apenas fotografias reais e autorizadas da Fast Limp.

---

# 01 — Estrutura visual, header, hero e faixa de confiança

**Anexar:** ficha preenchida, logo Fast Limp, mockup desktop e `hero.png`.

```text
Atue como desenvolvedor front-end sênior especializado em reprodução fiel de interfaces.

Vamos construir o site institucional da Fast Limp — Limpeza de Vidros, em [[CIDADE]]/[[UF]], por etapas. Use a ficha de personalização preenchida, a logo anexada e o mockup desktop aprovado como referências.

Nesta etapa, implemente somente a estrutura base, o header, o hero e a faixa de confiança.

EXECUÇÃO
Inspecione o projeto antes de editar. Preserve a stack existente. Se a pasta estiver vazia, use HTML semântico, CSS e JavaScript modular, adequados a um site institucional estático.
Implemente diretamente nos arquivos; não entregue apenas sugestões.
O mockup orienta o layout, mas não pode substituir a página como uma imagem. Textos, botões e navegação devem ser elementos reais.

DIRETRIZES PERMANENTES
- Preserve composição, hierarquia e proporções do mockup.
- Use as fotografias individuais fornecidas.
- Não acrescente seções, efeitos decorativos ou afirmações comerciais sem solicitação.
- Preserve as dobras aprovadas nas próximas etapas.
- Organize componentes e estilos por seção, evitando alterações globais acidentais.
- Não publique automaticamente.
- A estética deve comunicar limpeza, transparência, brilho, precisão e profissionalismo.
- Evite aparência genérica de empresa de limpeza doméstica.

IDENTIDADE VISUAL
Use a seguinte paleta da Fast Limp:
- Preto profundo: #010202
- Azul elétrico principal: #1C94F0
- Azul médio: #1274C2
- Azul claro: #5AB7F5
- Azul petróleo: #092131
- Azul acinzentado/vidro: #2D546F
- Branco gelo: #EFF0F0
- Prata: #D1D3D4
- Branco: #FFFFFF

Regras:
- Use #1C94F0 para CTAs e destaques.
- Use #092131 ou #010202 em seções escuras.
- Sobre branco, use #1274C2 ou #0B67AE em textos pequenos quando necessário para garantir contraste.
- Use #5AB7F5 apenas como detalhe, brilho ou reflexo sutil.
- Não use cores quentes sem aprovação.
- Não use visual neon.
- Gradientes, quando necessários, devem ser discretos e lembrar reflexos de vidro.
- Preserve bastante espaço em branco.
- Carregue efetivamente [[FONTE]] e seus pesos.
- Botões com cantos discretos, sem sombras pesadas.
- Em 1440px, comece com container central próximo de 1240–1280px e ajuste pela comparação visual.

HEADER
- Fundo predominantemente branco ou #EFF0F0.
- Altura inicial de 80–92px, ajustável à referência.
- Logo Fast Limp à esquerda com proporção e desenho preservados.
- Considere as margens transparentes internas do arquivo ao dimensionar a marca.
- Links: Início, Serviços, Resultados e Sobre.
- Botão em #1C94F0: “Solicitar orçamento” à direita, com ícone correto do WhatsApp.
- No celular: logo e menu compacto que abre, fecha e funciona por teclado.

HERO
- Use hero.png em largura total, sem moldura externa.
- Altura desktop inicial próxima de 560px, ajustável ao mockup.
- A imagem deve mostrar vidro como elemento principal e transmitir serviço profissional.
- Preserve o profissional, o rodo e a superfície envidraçada sem cortes ruins.
- Escurecimento em CSS concentrado atrás do texto, diminuindo na direção da área visual principal.
- Não aplique blur nem duplique camadas de escurecimento.

Conteúdo:
Eyebrow: [[HERO_EYEBROW]]
H1: [[HERO_TITULO]]
Descrição: [[HERO_DESCRICAO]]
Botão: “Solicitar meu orçamento”
Link secundário: “Conheça nossos serviços”

Ajuste as quebras do título por largura; não copie quebras do desktop para o mobile indiscriminadamente.

FAIXA DE CONFIANÇA
Fundo branco, três itens com ícones lineares e separadores discretos:
1. [[DIFERENCIAL_1_TITULO]] — [[DIFERENCIAL_1_TEXTO]]
2. [[DIFERENCIAL_2_TITULO]] — [[DIFERENCIAL_2_TEXTO]]
3. [[DIFERENCIAL_3_TITULO]] — [[DIFERENCIAL_3_TEXTO]]

Prefira ícones relacionados a cuidado, precisão, atendimento e vidro. Não use emojis.
No celular, empilhe os três itens em linhas alinhadas.

FUNCIONALIDADE
Centralize os dados de contato:
Telefone: [[TELEFONE_EXIBICAO]]
WhatsApp: [[WHATSAPP_URL]]
Mensagem: “Olá! Vim pelo site da Fast Limp e gostaria de solicitar um orçamento para limpeza de vidros.”

Codifique a mensagem na URL e conecte a navegação aos IDs das seções à medida que forem implementadas.

CONFERÊNCIA
Abra no navegador, se disponível. Compare largura da logo, altura do header, enquadramento do hero, quebras de texto, botões e faixa de confiança.
Verifique 1440px e 390px.
Não use overflow-x: hidden para disfarçar problemas de largura.
Informe arquivos alterados, verificações e diferenças restantes. Não avance para outras dobras.
```

---

# 02 — Nossos serviços

**Anexar:** mockup desktop e fotografias dos quatro serviços.

```text
Continue o site da Fast Limp seguindo as diretrizes da etapa anterior.
Implemente somente a seção Nossos serviços, abaixo da faixa de confiança.
Preserve as áreas já aprovadas.

REFERÊNCIA
Reproduza uma seção branca, limpa e editorial com quatro colunas fotográficas.
Não transforme os itens em caixas pesadas com sombras, fundos coloridos ou grandes bordas arredondadas.
Use o mesmo container e os mesmos alinhamentos.

CABEÇALHO
Eyebrow: “NOSSOS SERVIÇOS”
Título: “Cuidado profissional para cada superfície de vidro.”
Apoio: “Soluções para manter vidros, vitrines e superfícies envidraçadas com aparência limpa e bem cuidada.”

Desktop: título à esquerda e apoio à direita.
Mobile: textos empilhados.

ITENS
1. [[SERVICO_1]] — residencial.png
2. [[SERVICO_2]] — fachada-comercial.png
3. [[SERVICO_3]] — pos-obra.png
4. [[SERVICO_4]] — manutencao.png

Use somente serviços confirmados na ficha.
Se o catálogo real da Fast Limp for diferente, substitua títulos e imagens correspondentes.

ESTRUTURA
- Quatro colunas iguais no desktop.
- Fotografias com alturas consistentes e proporções próximas ao mockup.
- Títulos alinhados abaixo das imagens.
- Link “Saiba mais →” abaixo de cada título.
- Espaçamento horizontal inicial de 18–24px.
- object-fit: cover e object-position individual por fotografia.
- Nenhuma imagem deformada para caber no card.
- Superfícies de vidro devem parecer transparentes e realistas, sem exagero artificial de reflexos.

Cada link deve abrir [[WHATSAPP_URL]] com mensagem referente ao serviço:
“Olá! Vim pelo site da Fast Limp e gostaria de saber mais sobre [nome do serviço].”

INTERAÇÕES
Hover discreto: ampliação da fotografia de no máximo 3%, contida no recorte, e destaque no link.
Inclua foco visível.
Tablet: duas colunas quando adequado.
Celular: uma coluna com imagens de altura suficiente.

CONFERÊNCIA
Compare alinhamentos, proporções das fotos, distância entre cabeçalho e grid e posição dos links.
Teste as quatro mensagens de WhatsApp.
Confirme que as seções anteriores não foram alteradas.
```

---

# 03 — Resultados e referências

**Anexar:** mockup e `resultado-01.png` e `resultado-02.png`, preferencialmente fotos reais autorizadas.

```text
Continue o site da Fast Limp.
Implemente somente a seção de resultados e referências, abaixo de Nossos serviços.
Preserve todas as áreas anteriores.

COMPOSIÇÃO
Fundo #092131 em toda a largura.
Conteúdo alinhado ao container principal.
Eyebrow em #1C94F0, título branco e duas fotografias grandes lado a lado, com larguras próximas de 58% e 42% e alturas iguais.

TEXTOS
Eyebrow: “CUIDADO QUE APARECE NO RESULTADO”
Título: “Mais transparência, brilho e boa apresentação para o seu espaço.”
Link: “Ver resultados →”

Foto esquerda: resultado-01.png
Foto direita: resultado-02.png

As legendas devem descrever somente o que é realmente mostrado na fotografia.
Exemplos neutros:
- “Vidros com acabamento limpo e uniforme”
- “Cuidado nos detalhes e nas bordas”

IMPORTANTE
Se as imagens forem geradas ou apenas ilustrativas, não apresente a seção como portfólio real.
Nesse caso:
- altere o eyebrow para “REFERÊNCIAS DE SERVIÇO”
- altere o link para “Ver referências →”
- não mencione clientes, endereços, obras ou resultados executados pela Fast Limp.

Use legendas na base das fotos com contraste discreto.
Não escureça toda a imagem.

FUNCIONALIDADE
Selecionar uma foto abre sua versão ampliada, sem distorção, em visualizador acessível.
Inclua botão de fechar, Escape e retorno do foco ao elemento de origem.
Não acrescente fotografias inventadas ou repetidas para preencher espaço.

MOBILE
Empilhe título, link e fotografias.
Preserve os assuntos principais e a legibilidade das legendas.

CONFERÊNCIA
Verifique a transição entre fundos, proporção das imagens, contraste do link e espaçamento interno.
Teste abertura, fechamento e navegação por teclado.
```

---

# 04 — Sobre a Fast Limp

**Anexar:** mockup e `detalhe-limpeza.png`.

```text
Continue o site da Fast Limp.
Implemente somente a seção Sobre, abaixo da galeria.
Preserve as demais dobras.

LAYOUT
Fundo branco ou #EFF0F0.
Fotografia à esquerda e texto à direita.
Colunas próximas de 50%/50%, alinhamento vertical cuidadoso e espaçamento compacto.

Use detalhe-limpeza.png em enquadramento horizontal.
A fotografia deve mostrar um detalhe realista do serviço: rodo profissional, pano técnico ou acabamento em uma superfície de vidro.
Evite excesso de espuma, embalagens de produtos e aparência de limpeza doméstica genérica.

CONTEÚDO
Eyebrow: “SOBRE A FAST LIMP”
Título: “Cuidado nos detalhes. Clareza no resultado.”
Texto: [[SOBRE_TEXTO]]
Link: “Conheça a Fast Limp →”
Destino: [[SOBRE_DESTINO]]

Se o destino for externo, abra em nova aba com atributos de segurança apropriados.
Não acrescente anos de mercado, quantidade de clientes, garantias, certificações, avaliações ou promessas que não estejam confirmadas.

MOBILE
Uma coluna na ordem: imagem, eyebrow, título, texto e link.
Não comprima foto e texto lado a lado no celular.

VALIDAÇÃO
Compare altura da seção, proporção entre imagem e texto, quebras do título e consistência da tipografia.
```

---

# 05 — CTA final e rodapé básico

**Anexar:** mockup desktop e versão adequada da logo. Alternativa: usar diretamente a etapa 09 para o rodapé final.

```text
Continue o site da Fast Limp.
Implemente a faixa de contato e o rodapé básico conforme o mockup escolhido.
Preserve as seções anteriores.

FAIXA DE CONTATO
Fundo #1C94F0 em largura total.
Desktop: título à esquerda, apoio ao centro e botão escuro à direita.

Título: “Quer seus vidros com outra aparência?”
Apoio: “Fale com a Fast Limp e solicite seu orçamento.”
Botão escuro: “Falar no WhatsApp →”, com ícone correto.

Use [[WHATSAPP_URL]] e a mensagem centralizada do projeto.
Mantenha a faixa compacta.
O botão pode usar #092131 ou #010202, com texto branco.

RODAPÉ
Fundo #092131 ou #010202 uniforme, sem brilhos exagerados ou gradientes decorativos.
Mesmo container do site.
Três colunas, aproximadamente 40%/24%/36%, ajustando para o telefone caber.

COLUNA 1
Logo Fast Limp.
Descrição: [[MARCA_DESCRICAO]]
Ícones de Instagram e Facebook em pequenos botões de contorno.
Texto: [[INSTAGRAM_USUARIO]]
Destinos: [[INSTAGRAM_URL]] e [[FACEBOOK_URL]].
Omita redes não existentes.

COLUNA 2
Título: “EXPLORE”
Links: Início; Nossos serviços; Resultados; Sobre a Fast Limp.
Conecte aos IDs reais das seções.

COLUNA 3
Título: “FALE COM A FAST LIMP”
Telefone: [[TELEFONE_EXIBICAO]]
Texto: “Solicite seu orçamento →”
Localização: [[CIDADE]] • [[UF]]
Telefone com destaque, sem compressão de fonte ou cortes.

BASE
Linha horizontal discreta em #2D546F ou rgba equivalente.
Esquerda: “© Fast Limp. Todos os direitos reservados.”
Direita: “Política de privacidade”, conectada a [[PRIVACIDADE_URL]].

Se a política não existir, registre a pendência para publicação, sem inventar destino.

MOBILE
CTA em uma coluna com botão amplo.
Rodapé na ordem: marca/redes; navegação; contato; base.
Remova separadores verticais e evite espaços excessivos.

CONFERÊNCIA
Compare tamanho da logo, início das colunas, telefone, espaços e altura total.
Teste os links disponíveis.
```

---

# 06 — Revisão visual, mobile e preparação técnica

**Anexar:** mockup desktop aprovado, referência mobile e captura atual.

```text
Faça a revisão final do site da Fast Limp.
O desktop aprovado é a referência principal.
Corrija divergências localizadas sem redesenhar o site.

IDENTIDADE
Confirme que o projeto utiliza consistentemente:
#010202, #1C94F0, #1274C2, #5AB7F5, #092131, #2D546F, #EFF0F0, #D1D3D4 e #FFFFFF.

Não introduza novas cores sem necessidade.
Não transforme o layout em neon.
O conjunto deve parecer limpo, técnico, moderno e profissional.

VISUAL
Compare container, alinhamentos entre dobras, altura do header/hero, títulos, cores, recortes das fotos, espaçamento e proporções do CTA/rodapé.
Não resolva diferenças comprimindo elementos ou reduzindo todas as fontes.

RESPONSIVIDADE
Confira larguras de 1440, 1024, 768, 430, 390 e 360px.
No celular:
- menu acessível
- hero legível
- confiança empilhada
- serviços em uma coluna
- resultados empilhados
- Sobre com foto acima
- CTA amplo
- rodapé em grupos verticais

Elimine textos cortados, telefone quebrado incorretamente e rolagem horizontal.
A referência mobile orienta a hierarquia; corrija limitações do mockup para garantir usabilidade real.

INTERAÇÕES
Transições discretas em links e botões.
Entrada suave das seções, com deslocamento pequeno e sem atrasar leitura.
Respeite prefers-reduced-motion.
Conteúdo visível se JavaScript falhar.
Não adicione parallax, cursor personalizado, brilhos contínuos ou animações chamativas.

IMAGENS
Preserve originais.
Gere WebP/AVIF quando houver ferramentas disponíveis.
Não amplie artificialmente arquivos para alegar resolução maior.
Use tamanhos responsivos, width/height ou aspect-ratio para evitar saltos.
Priorize o hero; lazy loading nas imagens abaixo da primeira dobra.
Confira todos os arquivos no build final.

ACESSIBILIDADE E METADADOS
Documento pt-BR.
Um H1.
Hierarquia de títulos.
Textos alternativos.
Foco visível.
Contraste adequado.
Menu e galeria por teclado.

Título sugerido:
“Fast Limp | Limpeza de Vidros em [[CIDADE]]”

Descrição sugerida:
“Limpeza profissional de vidros em [[CIDADE]] e região. Conheça os serviços da Fast Limp e solicite seu orçamento pelo WhatsApp.”

Ajuste a descrição aos serviços e região realmente confirmados.
Use [[DOMINIO]] somente quando confirmado.
Não invente endereço, avaliações, certificações ou dados estruturados.

BUILD E CAMINHOS
Valide caminhos públicos conforme stack e hospedagem.
Não use caminhos locais do Windows, referências à pasta src no HTML publicado ou capitalização inconsistente.
Se houver bundler, respeite os caminhos gerados por ele.
Execute o build aplicável e sirva sua saída localmente.
Verifique CSS, JS, fontes e imagens sem erros 404.
Teste navegação, WhatsApp e recarregamento.
Não publique automaticamente.

ENTREGA
Informe correções, larguras e funcionalidades verificadas, resultado do build e pendências reais.
Inclua domínio, privacidade e fotos reais quando ainda pendentes.
Não alegue verificações que não conseguiu executar.
```

---

# 07 — Refinamento visual após a primeira implementação

**Usar quando:** o resultado existe, mas está distante do mockup.  
**Anexar:** print atual e referência aprovada.

```text
Atue como especialista sênior em refinamento visual.
Aproxime o site da Fast Limp do mockup aprovado com ajustes de proporção, enquadramento, espaçamento e legibilidade.
Identifique os anexos antes de editar.
Preserve estrutura, identidade, copy e funcionalidades.

DIAGNÓSTICO
Inspecione container, largura máxima, padding lateral, fonte raiz, zoom/transform, carregamento e pesos de [[FONTE]], alturas, proporções das imagens, breakpoints e sobrescritas.
Compare em larguras equivalentes.
Não deduza pixels CSS diretamente de um print reduzido.
Corrija causas; evite !important e overrides sucessivos.

AMPLITUDE
Se o conteúdo estiver estreito, ajuste o container fluidamente.
Em 1440px, avalie 1240–1280px.
Em telas maiores permita crescimento moderado.
Mobile: margens de 20–24px.
Alinhe header, hero, serviços, resultados, Sobre, CTA e rodapé ao mesmo eixo.
Não use zoom ou transform: scale para ampliar a página.

HEADER
Se a logo estiver pequena, ajuste pela largura visual real considerando margens transparentes internas.
Preserve proporção e mantenha o header compacto.

HERO
Concentre o overlay atrás do texto e reduza gradualmente sobre a área principal da fotografia.
Verifique escurecimento duplicado em filtros e pseudo-elementos.
Recupere luminosidade da fotografia sem perder contraste.
Vidro deve continuar visualmente transparente, com reflexos plausíveis.
Ajuste recorte e quebras do título por largura, sem comprimir letras.

CONFIANÇA
Se a faixa estiver ausente, verifique omissão, CSS, sobreposição e animação não concluída.
Restaure sem duplicar, usando os três diferenciais confirmados da ficha.

TIPOGRAFIA
Revise tamanhos reais.
Pontos iniciais:
- leitura: 16–18px
- navegação/links: 14–16px
- títulos de serviços: 17–20px
- eyebrows: 12–13px

Use pesos carregados.
Não aplique opacidade ao container inteiro.
Sobre branco, use #1274C2 ou #0B67AE para textos pequenos.
Sobre escuro, links legíveis em branco ou #1C94F0.

SERVIÇOS
Preserve quatro colunas editoriais.
Reequilibre largura dos cards, altura das fotos, posições de recorte e alinhamento dos títulos/links.
Evite caixas, sombras pesadas e elementos adicionais.

RESULTADOS
Preserve assimetria e alturas iguais.
Ajuste contraste do link, distância título/galeria, legendas e padding.
Não apresente material ilustrativo como serviço executado.

SOBRE
Se estiver muito alta, use foto horizontal entre 16:10 e 16:9.
Texto centralizado verticalmente e padding controlado.
Mobile com imagem acima.

CTA/RODAPÉ
Preserve a composição.
Refine leitura, botão, colunas, logo, linha inferior e contraste.
Evite alturas fixas ou espaços artificiais.

VALIDAÇÃO
Confira 1440, 1920 e 390px.
Verifique ausência de cortes, distorções e rolagem horizontal.
Teste menu e links.
Conteúdo deve continuar visível sem animações.
Se houver navegador, capture e compare.
Informe causas, correções, verificações e diferenças restantes.
Não publique nem adicione seções.
```

---

# 08 — Redução do espaçamento entre dobras

**Usar quando:** houver espaço vazio excessivo.  
**Anexar:** captura atual completa.

```text
Refine o espaçamento vertical do site da Fast Limp.
Aproxime as seções mantendo separação visual confortável e preservando layout, paleta, fontes, textos, imagens e funcionalidades.

DIAGNÓSTICO
Inspecione padding, margin, gap, height e min-height.
Verifique padding inferior somado ao superior seguinte, margens padrão, wrappers vazios, alturas fixas e elementos invisíveis ocupando espaço.
Corrija regras originais.
Não use margens negativas ou transformações para esconder o problema.

PONTOS DE PARTIDA

Desktop:
- Seções principais: padding superior/inferior 48–56px.
- Eyebrow até título: 10–12px.
- Título até descrição: 12–16px.
- Cabeçalho até imagens/cards: 24–32px.

Mobile:
- Seções principais: padding superior/inferior 32–40px.
- Cabeçalho até imagens/cards: 20–24px.
- Cards empilhados: gap 24–28px.

Adapte à referência.
Não aplique o mesmo padrão indiscriminadamente ao header, hero, confiança, CTA e rodapé.

SERVIÇOS
Reduza espaço acima do eyebrow, aproxime cabeçalho/grid e reduza o vazio após “Saiba mais”.
Preserve as imagens alinhadas.

RESULTADOS
Reduza padding acima do título e abaixo da galeria.
Use cerca de 24–32px entre cabeçalho e fotos, sem sacrificar a leitura.

SOBRE
Use foto horizontal próxima de 16:10.
Centralize o texto verticalmente.
Avalie padding de 48px acima/abaixo no desktop.
Remova min-height desnecessário.
No celular, imagem acima e aproximadamente 24px até o texto.

CTA/RODAPÉ
CTA compacto, avaliando padding vertical de 32–40px no desktop, sem reduzir a área clicável do botão.
No rodapé, reduza o excesso antes da linha inferior, sem comprimir links, telefone ou ícones.

PRESERVAÇÃO
Não altere altura do header e hero nesta rodada.
Preserve a faixa de confiança existente.

VALIDAÇÃO
Compare capturas antes/depois na mesma largura.
Deve haver menos vazio, transições mais próximas, mesma hierarquia, fotos bem enquadradas e nenhum corte.
Não reduza fontes, botões ou todas as imagens apenas para encurtar a página.
Informe seções ajustadas e os valores finais de padding e gap.
```

---

# 09 — Rodapé final, com CTA integrado

**Anexar:** mockup do novo rodapé, logo adequada e ficha de contatos.  
**Esta opção substitui o rodapé básico da etapa 05.**

```text
Atue como desenvolvedor front-end sênior especializado em reprodução fiel de layouts.
Atualize somente o rodapé do site da Fast Limp para reproduzir o mockup anexado.
Preserve todas as demais seções, inclusive a faixa de contato acima do rodapé, se existente.

INSPEÇÃO
Localize HTML/componente e estilos.
Reutilize logo Fast Limp, ícones, contatos, redes e IDs de navegação.
Corrija na origem, sem duplicar rodapé, acumular overrides ou afetar outras dobras.
Não use o mockup como imagem de fundo da interface.

COMPOSIÇÃO
Fundo #092131 ou #010202 uniforme.
Use #1C94F0 nos títulos pequenos, botão e linha superior.
#5AB7F5 pode aparecer apenas em pequenos detalhes.
Não reproduza ruídos, glow excessivo ou texturas artificiais.

Linha fina de destaque no limite superior, sem faixa vazia acima.
Três colunas: marca/redes à esquerda, navegação ao centro e contato à direita.
Mesmo container do site.
Avalie 40%/24%/36%, descontando gaps e ajustando à largura disponível.
Padding superior de 48–56px; conteúdo até linha inferior de 28–36px; barra inferior de 22–28px.
Não fixe a altura do rodapé.

COLUNA ESQUERDA
Logo Fast Limp em versão adequada ao fundo.
Descrição: [[MARCA_DESCRICAO]], em #D1D3D4 ou #EFF0F0, entrelinha próxima de 1.5.
Depois: “ACOMPANHE A FAST LIMP”, em maiúsculas, #1C94F0, semibold e tracking discreto.
Abaixo, Instagram, Facebook e [[INSTAGRAM_USUARIO]] na mesma linha, quando disponíveis.
Botões sociais com contorno discreto, cantos suaves, ícones centralizados e área de 40–44px.
URLs: [[INSTAGRAM_URL]] e [[FACEBOOK_URL]].
O identificador também abre o Instagram.

COLUNA CENTRAL
Título: “NAVEGUE”.
Links: “Início”, “Serviços”, “Resultados”, “Sobre a Fast Limp”.
Branco suave, peso regular, espaçamento uniforme e alinhamento à esquerda.
Sem ícones ou marcadores adicionais.
Use IDs reais, não href="#" genérico.
Alinhe o título ao “VAMOS CONVERSAR” da coluna direita.

COLUNA DIREITA
Título: “VAMOS CONVERSAR”.
Ícone de contorno do WhatsApp e [[TELEFONE_EXIBICAO]] em destaque.
Avalie 28–32px, sem comprimir letras.
Texto: “Solicite seu orçamento para limpeza de vidros.”

Botão:
“Solicitar orçamento”, com seta diagonal para cima e à direita.
Fundo #1C94F0.
Texto #010202 ou #092131 em negrito, desde que o contraste seja adequado.
Cantos de 4–6px.
Altura próxima de 52–56px.
Largura disponível da coluna.
Equilibre texto e seta.

Telefone e botão abrem [[WHATSAPP_URL]], com mensagem codificada:
“Olá! Vim pelo site da Fast Limp e gostaria de solicitar um orçamento para limpeza de vidros.”

Localização abaixo do botão:
ícone e “[[CIDADE]] • [[UF]]”.

BARRA INFERIOR
Linha fina na largura do conteúdo.
Esquerda: “© Fast Limp. Todos os direitos reservados.”
Direita: “Política de privacidade”, separador discreto e “Voltar ao topo ↑”.
Cinza-claro legível.
Política conectada a [[PRIVACIDADE_URL]], se existente.
Caso contrário, informe a pendência sem inventar destino.
Voltar ao topo funcional, respeitando movimento reduzido.

TIPOGRAFIA/INTERAÇÕES
Preserve [[FONTE]] e pesos reais.
Garanta contraste e foco visível.
Hover discreto em links e contornos sociais.
No CTA, pequena variação de tonalidade, sem brilho, pulsação ou sombras pesadas.
Ícones consistentes, não emojis.

RESPONSIVIDADE
Reorganize antes que telefone e textos fiquem apertados.
Mobile:
- marca/descrição
- redes
- navegação
- contato/botão/localização
- barra inferior

Margens de 20–24px.
Espaçamento controlado.
Botão amplo.
Telefone sem cortes.
Links confortáveis ao toque.
Permita linhas separadas na base.
Não preserve vazios herdados do desktop.

CONFERÊNCIA
Compare tamanho da logo, posição das colunas, títulos, telefone, CTA, redes, divisória, base e integração com a seção anterior.
Valide 1440px e 390px.
Não conclua apenas porque todos os elementos existem; corrija divergências visuais perceptíveis.
Informe arquivos alterados, verificações e pendências.
Não publique automaticamente.
```

---

# 10 — Prompts para as fotografias individuais

Use referências autorizadas da Fast Limp quando houver.

As imagens abaixo devem parecer fotografias comerciais realistas. Evite estética de banco de imagens artificial, excesso de espuma, reflexos impossíveis, mãos deformadas, ferramentas incoerentes ou superfícies de vidro que pareçam espelhos sólidos.

Não peça ao gerador para inventar um serviço realizado pela Fast Limp. As imagens geradas são ilustrativas.

## 10.1 — Hero

```text
Gere uma fotografia comercial ilustrativa de alta qualidade para o site de uma empresa especializada em limpeza profissional de vidros.

Imagem individual, sem textos, logos, botões, bordas ou interface.
Formato horizontal 16:9, na maior resolução nativa disponível.

Cena: profissional uniformizado realizando limpeza de uma grande superfície de vidro em ambiente contemporâneo e bem cuidado, usando rodo profissional de forma plausível.
O vidro deve ser claramente percebido por reflexos sutis e transparência realista.

Composição:
- profissional e ação principal no lado direito ou centro-direito;
- área visual mais calma no lado esquerdo para receber texto em CSS;
- ambiente brasileiro contemporâneo, residencial ou comercial neutro;
- luz natural suave;
- sensação de limpeza, precisão e profissionalismo.

Não mostrar logotipo inventado no uniforme.
Não adicionar textos.
Não exagerar espuma, brilho, HDR ou saturação.
Não representar trabalho em altura ou acesso por corda, a menos que esse serviço tenha sido explicitamente confirmado.
```

## 10.2 — Limpeza residencial

```text
Gere uma fotografia ilustrativa vertical 4:5 de limpeza profissional de vidros em uma residência contemporânea brasileira.

Mostre uma grande janela ou porta de vidro sendo limpa com rodo profissional.
O ambiente deve ser organizado, claro e realista.
Destaque transparência, acabamento e reflexos sutis do vidro.

A ferramenta deve estar corretamente posicionada.
Sem excesso de espuma.
Sem textos, marcas, logos ou interface.
Sem aparência de limpeza doméstica improvisada.
Alta qualidade e luz natural.
```

## 10.3 — Vitrine ou fachada comercial

```text
Gere uma fotografia comercial ilustrativa vertical 4:5 para representar limpeza profissional de vitrines ou fachadas de vidro.

Mostre uma vitrine ampla ou fachada térrea contemporânea sendo limpa por um profissional uniformizado.
O vidro deve apresentar transparência e reflexos plausíveis.
A superfície deve ser o elemento principal da composição.

Ambiente comercial elegante, mas realista.
Não mostrar nomes de lojas ou marcas identificáveis.
Sem trabalho em altura, andaimes ou cordas se isso não estiver confirmado nos serviços.
Sem textos, logos, bordas ou interface.
```

## 10.4 — Vidros pós-obra

```text
Gere uma fotografia ilustrativa vertical 4:5 para representar limpeza técnica de vidros após obra ou reforma.

Mostre uma grande superfície envidraçada em ambiente recém-finalizado, com profissional realizando acabamento cuidadoso.
O local deve parecer em fase final de entrega, sem entulho exagerado.
Mostre atenção às bordas, cantos e acabamento do vidro.

Não represente remoção de materiais perigosos.
Não mostre riscos, danos ou ferramentas inadequadas sobre o vidro.
Sem marcas, textos ou interface.
Visual profissional e realista.
```

## 10.5 — Manutenção periódica

```text
Gere uma fotografia ilustrativa vertical 4:5 que represente manutenção periódica de vidros em um ambiente comercial ou residencial bem cuidado.

Mostre um profissional realizando limpeza de rotina em grandes superfícies de vidro, com equipamento profissional simples e organizado.
A cena deve transmitir consistência, cuidado e manutenção preventiva da aparência do ambiente.

Luz natural suave.
Reflexos discretos.
Sem excesso de produtos, espuma ou elementos de limpeza doméstica.
Sem textos, logos ou interface.
```

## 10.6 — Resultados / referência 01

```text
Gere uma fotografia comercial ilustrativa horizontal 3:2 de uma grande superfície de vidro limpa em um ambiente contemporâneo brasileiro.

O foco deve ser o resultado visual:
- transparência;
- reflexos controlados;
- ausência de manchas visíveis;
- linhas arquitetônicas nítidas;
- sensação de ambiente claro e bem cuidado.

Sem pessoas quando não forem necessárias.
Sem textos, marcas ou interface.
Não apresente a imagem como um “antes e depois”.
```

## 10.7 — Resultados / referência 02

```text
Gere uma segunda fotografia comercial ilustrativa horizontal 3:2, coerente com a linguagem visual da primeira, em outro ambiente ou enquadramento.

Mostre vidro limpo em uma vitrine, janela ampla ou porta de vidro contemporânea.
Valorize luz, transparência e acabamento.
Composição adequada para galeria lado a lado.

Sem textos, marcas ou pessoas em destaque.
Sem HDR exagerado ou reflexos impossíveis.
```

## 10.8 — Detalhe da limpeza

```text
Gere uma fotografia ilustrativa horizontal 3:2 para a seção Sobre da Fast Limp.

Close elegante e realista de um rodo profissional passando sobre uma superfície de vidro.
Mostre parte da mão ou braço do profissional apenas se necessário para dar contexto.
Vidro com transparência e reflexo sutil.
Fundo suavemente desfocado.

A imagem deve transmitir precisão, cuidado e técnica.
Sem excesso de espuma.
Sem embalagens de produtos.
Sem textos, logos, marcas ou interface.
```

---

# 11 — Logo e favicon

A logo atual da Fast Limp é provisória. Não redesenhe nem altere automaticamente sua forma durante a implementação do site.

Para simples remoção de fundo ou recoloração, prefira edição direta dos pixels preservando desenho, canal alpha e proporções.

## 11.1 — Logo sem fundo

```text
Remova apenas o fundo da logo Fast Limp anexada.

Entregue PNG com transparência real, preservando exatamente:
- letras;
- símbolo FL;
- elemento gráfico relacionado ao vidro/rodo;
- espaçamento;
- proporções;
- gradientes e cores da marca.

Remova halos pretos desnecessários fora do desenho e resíduos entre os elementos.
Bordas limpas e suavizadas.
Não redesenhe, reinterprete ou substitua a tipografia.
Não acrescente sombra, contorno ou brilho novo.
Não desenhe quadriculado no fundo.
Confira o resultado sobre fundos claro e escuro.
```

## 11.2 — Versão branca simplificada da logo

```text
Crie uma versão monocromática branca da logo Fast Limp anexada apenas se for necessária para o rodapé.

Altere somente os elementos visuais para branco puro #FFFFFF, preservando integralmente desenho, posicionamento, proporções e transparência.

Entregue PNG com canal alpha real.
Não acrescente fundo, textura, sombra, contorno, manchas ou resíduos.
Não substitua a logo por uma recriação aproximada.
Confira sobre fundo #092131 e #010202.
```

## 11.3 — Favicon

```text
Crie um favicon quadrado a partir do símbolo “FL” da logo Fast Limp anexada.

Preserve a forma distintiva do símbolo.
Remova o texto “FAST LIMP” e “LIMPEZA DE VIDRO” quando necessário para manter legibilidade em tamanho pequeno.

Opção visual preferencial:
- símbolo branco ou #EFF0F0;
- fundo sólido #092131 ou #1C94F0;
- escolha a combinação com melhor legibilidade.

Centralize opticamente, com respiro aproximado de 12–16% nas bordas.
Sem sombras, texturas, ruídos ou pequenos detalhes que prejudiquem a leitura.

Entregue PNG de alta qualidade.
Se a ferramenta permitir exportação direta, gere também versões 16x16, 32x32 e 48x48 e favicon.ico a partir do mesmo desenho.
Verifique legibilidade em abas claras e escuras.
```

---

# 12 — Mockups para aprovar a direção visual

Estes prompts são para gerar prévias de design, não para implementar o site.

## 12.1 — Desktop completo

```text
Crie um mockup de alta fidelidade da página inicial desktop da Fast Limp — Limpeza de Vidros, empresa localizada em [[CIDADE]]/[[UF]].

Use a logo Fast Limp anexada e a ficha preenchida.

IDENTIDADE
Estética moderna, limpa, técnica e profissional.
A marca deve transmitir transparência, brilho, cuidado e agilidade, sem parecer uma empresa de limpeza doméstica genérica.

Paleta obrigatória:
- #010202 preto profundo
- #1C94F0 azul elétrico principal
- #1274C2 azul médio
- #5AB7F5 azul claro
- #092131 azul petróleo
- #2D546F azul acinzentado
- #EFF0F0 branco gelo
- #D1D3D4 prata
- #FFFFFF branco

Use #1C94F0 nos CTAs e detalhes principais.
Use #092131 e #010202 nas áreas escuras.
Preserve bastante branco e espaço negativo.
Reflexos e transparências podem aparecer de forma sutil para remeter ao vidro.
Sem glow excessivo, estética neon ou gradientes chamativos.

Tipografia [[FONTE]].
Cantos discretos.
Sombras mínimas.
Fotos grandes e realistas.
Layout possível de reproduzir fielmente em código.

Uma imagem única da página completa, do header ao rodapé, vista frontal, sem moldura de computador ou navegador.

ORDEM
1. Header claro com logo Fast Limp, navegação e botão “Solicitar orçamento”.
2. Hero fotográfico de limpeza profissional de vidro com [[HERO_EYEBROW]], [[HERO_TITULO]], [[HERO_DESCRICAO]] e CTA de WhatsApp.
3. Faixa com os três diferenciais confirmados.
4. Nossos serviços em quatro colunas fotográficas.
5. Resultados/referências em fundo #092131, duas fotos assimétricas e legendas curtas.
6. Sobre a Fast Limp com detalhe de limpeza à esquerda e [[SOBRE_TEXTO]] à direita.
7. Faixa de contato em #1C94F0.
8. Rodapé escuro com marca/redes, navegação, contato, botão de orçamento e base de privacidade.

Use apenas dados confirmados.
Não invente avaliações, certificações, tempo de mercado, clientes ou serviços executados.
Não corte o rodapé.
Priorize texto legível, alinhamentos e uma composição profissional.
```

## 12.2 — Mobile completo

```text
Adapte o mockup desktop aprovado da Fast Limp para uma página mobile completa em uma única imagem vertical longa.

Preserve identidade, paleta, copy e ordem das seções.
O resultado deve representar uma tela de aproximadamente 390–430px de largura CSS, sem moldura de aparelho e sem uma página estreita dentro de grandes margens externas.

Header compacto com logo e menu.
Hero com enquadramento mobile e texto legível.
Benefícios em três linhas.
Serviços em uma coluna com fotos suficientemente altas.
Resultados/referências com imagens empilhadas.
Sobre com foto acima do texto.
CTA com botão amplo.
Rodapé em grupos verticais: marca/redes, navegação, contato e base.

Use margens internas próximas de 20–24px.
Leitura confortável.
Botões com pelo menos 44px de área de toque.
Permita que títulos quebrem naturalmente.

Não comprima o desktop para caber.
Não omita seções.
Não reduza a tipografia excessivamente.
Não use fotos como faixas muito baixas.
Inclua o rodapé inteiro.

Caso a ferramenta limite a altura, gere partes consecutivas identificadas, mantendo largura e escala.
Não apresente uma página cortada como completa.
```

## 12.3 — Segunda opção de rodapé

```text
Gere uma segunda proposta visual de rodapé para a Fast Limp, usando a logo anexada, a ficha de contatos e o print atual.

Mostre apenas o rodapé desktop em uma imagem horizontal nítida.
Ignore notificações do sistema ou outros elementos externos que apareçam no print.

Fundo #092131 ou #010202.
Linha superior fina em #1C94F0.
Espaçamento compacto.
Três colunas bem equilibradas.

Esquerda:
- logo Fast Limp
- [[MARCA_DESCRICAO]]
- título “ACOMPANHE A FAST LIMP”
- redes existentes
- [[INSTAGRAM_USUARIO]]

Centro:
- “NAVEGUE”
- Início
- Serviços
- Resultados
- Sobre a Fast Limp

Direita:
- “VAMOS CONVERSAR”
- WhatsApp e [[TELEFONE_EXIBICAO]]
- frase “Solicite seu orçamento para limpeza de vidros.”
- botão “Solicitar orçamento”
- localização [[CIDADE]] • [[UF]]

Base:
- direitos autorais
- privacidade
- “Voltar ao topo ↑”

Use #1C94F0 para destaques.
#5AB7F5 apenas em detalhes discretos.
Sem grandes vazios, gradientes chamativos, ruídos, sombras pesadas, dados inventados ou tipografia minúscula.
Use proporções que possam ser implementadas fielmente no site.
```

---

# Conferência antes de publicar

- Todos os campos pendentes foram substituídos por dados reais da Fast Limp?
- Os quatro serviços listados realmente são oferecidos?
- Os três diferenciais são verdadeiros?
- A paleta da Fast Limp está sendo respeitada?
- A logo utilizada é a versão aprovada mais recente?
- Telefones e redes sociais foram conferidos?
- O WhatsApp abre com a mensagem correta?
- A região de atendimento está confirmada?
- Fotos ilustrativas estão claramente diferenciadas de serviços realizados?
- Nenhuma imagem gerada está sendo apresentada como cliente ou trabalho real?
- O site evita aparência genérica de empresa de limpeza doméstica?
- O visual remete a vidro, transparência, brilho e cuidado profissional?
- O resultado foi comparado no desktop e no celular?
- O domínio e a política de privacidade estão configurados antes da publicação?
- A versão escolhida do rodapé está clara para o assistente?
