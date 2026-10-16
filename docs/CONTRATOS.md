# Contratos da implementação

## Arquivos e propriedade

- Coordenador: `site/index.html`, `site/partials/start.html`, `site/styles/base.css`, `site/styles/tokens.css`, `site/scripts/app.js`, scripts de build/servidor e quadro.
- sections-middle: `site/partials/middle.html`, `site/styles/middle.css`, relatório `docs/ETAPAS-02-03.md`.
- sections-end: `site/partials/end.html`, `site/styles/end.css`, relatório `docs/ETAPAS-04-05.md`.
- assets: `site/assets/photos/`, `site/assets/originals/`, `docs/ASSETS.md`, `scripts/prepare-photos.py`.
- Revisor posterior: revisão/testes e relatório próprio, sem editar implementação até delegação explícita.

## Composição estática

Build integra cinco fragmentos em `site/index.html`: `header`, `start`, `middle`, `end`, `footer`. Header e footer são globais, fora do main; start contém hero/H1 dentro do main. A separação adicional foi aplicada na revisão semântica final, mantendo a geometria por `styles/layout.css`. Não inserir header/footer em mais de um fragmento. Conteúdo real no HTML, JS apenas aprimora controles. `index.html` contém os diálogos compartilhados.

## Classes compartilhadas

`.container` 1200px, `.wide-container` 1320px; `.section` padding 56/72/96; `.surface-alt` gelo, `.surface-dark` petróleo; `.section-heading` h2/descrição; `.centered`; `.eyebrow`; `.muted`; `.small`; `.button` azul/petróleo; `.button-light`; `.button-dark`; `.text-link`; `.round-button` 44px; `.section-top` título+ação; `.pending-label`; `.sr-only`.

Tokens gerados de JSON: `--semantic-color-surface`, `--semantic-color-surface-alt`, `--semantic-color-surface-inverse`, `--semantic-color-surface-accent`, `--semantic-color-text`, `--semantic-color-text-muted`, `--semantic-color-text-inverse`, `--semantic-color-link`, `--semantic-color-link-inverse`, `--semantic-color-border-subtle`, `--primitive-color-*`; todos nomes kebab-case.

## Assets

Marca em `assets/brand/` com nomes oficiais; Manrope em `assets/fonts/Manrope-Variable.ttf`. Fotos em `assets/photos/{nome}-{640|1280|1920}.webp`. IDs: hero, about-01..03, service-01..04, gallery-01..06, process, why, article-01..03. Todos fotos ilustrativas: legendas visíveis por seção, nenhuma apresentada como equipe/portfólio. `img` com alt, width/height, loading lazy exceto hero; srcset e sizes. Equipe sem retratos: slots gráficos identificados, proporção 3:4.

## Comportamentos (coordenador implementa JS)

- CTAs pendentes: `button data-contact` opcional `data-context="Residências"`; abre dialog `#contact-dialog`. Nenhum href vazio/WhatsApp fictício.
- Carrossel: wrapper `[data-carousel]`, pista `[data-track]` (tabindex=0, role=region, aria-label), botões `[data-prev]`/`[data-next]`. Atualização de disabled no scroll/resize. Sem autoplay.
- Galeria: `button[data-gallery]` com `data-full="assets/photos/gallery-01-1920.webp"`, `data-caption` e img alt. Abre `#gallery-dialog` compartilhado.
- FAQ: `.faq-item`, h3>button `[data-accordion]` com aria-controls/expanded e painel id correspondente, role=region, aria-labelledby. Primeira aberta, restantes hidden. JS mantém uma aberta.
- Pendências editoriais/equipe: `button[data-pending]` e `data-pending-title`, `data-pending-message` abre dialog explicativo compartilhado.
- Depoimentos sem dados: painel pendente; setas disabled e estado explicado, não fabricar múltiplas avaliações para fazê-las girar.
- Ano: `[data-year]`.

## Conteúdo e aceite

Ordem: inicio,sobre,servicos,referencias,como-funciona,diferenciais,depoimentos,equipe,duvidas,conteudos,contato. Uma h1 no start. H2 por seção. Serviços específicos em rascunho identificados; processo proposto; diferenciais linguagem de proposta; depoimentos/equipe/artigos explicitamente pendentes. Sem formulários sem destino, play sem vídeo, links falsos ou dados comerciais inventados. Contato real e produção dependem de conteúdo, sem bloquear a estrutura local. Página sem overflow-x hidden global. Redução de movimento e foco visíveis pela base.
