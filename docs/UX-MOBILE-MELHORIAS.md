# Melhorias de UX mobile · FL-15

16/10/2026. Implementação autorizada a partir da revisão FL-14, mantendo a identidade e o hero aprovados. Sem publicação.

## Resultado

- Cinco serviços aparecem em um índice compacto de botões com alvo mínimo de48px, acima do carrossel. Seleção leva diretamente ao card; estado e posição acompanham clique, setas, Home/End e rolagem. O foco permanece no acionador. Sem JavaScript, o índice não é apresentado; os cards e sua rolagem nativa continuam acessíveis.
- CTA proporcional ao texto após os quatro passos do processo, antes da imagem. Aparece no mobile. O convite geral sob serviços agora abre WhatsApp diretamente, como os cards.
- DOM da FAQ: introdução, perguntas e suporte. No mobile essa é também a ordem visual; no desktop a grade mantém introdução/suporte à esquerda e perguntas à direita.
- DOM do rodapé: marca, contato, navegação e serviços. No mobile o número/WhatsApp e a região precedem os menus. A grade desktop mantém suas quatro colunas. O número agora identifica explicitamente WhatsApp.
- Três perfis da equipe em linhas com fotografia lateral e nome/função, sem retirar pessoas ou fotos da prévia. Layout desktop de retratos preservado.
- Em320px, a galeria usa duas colunas e proporções menores, mantendo as seis fotos e o lightbox.
- Textos dos benefícios e etapas passam de13px para14px no mobile; funções da equipe de12px para14px.

## Medidas e validação

| Observação | Antes | Depois |
|---|---:|---:|
| Equipe em390px |1869px|728px|
| Galeria em320px |1729px|893px|
| Página da prévia em390px |10832px|9941px|
| Página da prévia em320px |11331px|9897px|
| Links WhatsApp estáticos |21|23|

Altura menor não representa uma medição de conversão. O índice dos serviços e a ação no processo acrescentam espaço útil; a redução vem principalmente da equipe e da galeria estreita.

Builds e checks local/público passaram. Testes de interação verificam seleção direta do quinto serviço, retorno por teclado, contador e estado, FAQ/rodapé na nova ordem, menu, galeria e carrossel. Teste público passou em390/1440px com e sem JavaScript, sem os módulos de dados temporários. Acessibilidade:152 textos sólidos, zero falhas, contraste mínimo4,88:1; foco, Escape, redução de movimento e reflow preservados.

QA320/360/390/768/1024/1440/1920px sem overflow horizontal, fotos quebradas, erro de fonte, console ou HTTP. Capturas da primeira tela do hero em390 e1440px são idênticas byte a byte às anteriores, confirmando a preservação da composição aprovada. Outras seções mobile e FAQ/rodapé desktop foram inspecionados visualmente. O detector mecânico encontrou os mesmos dois falsos positivos já analisados: imagem do diálogo sem src enquanto fechado e sombra/anel de foco petróleo.

Revisão independente final aceita pelo agente mobile_technical_audit: todos os cinco atalhos selecionam o card correto sem alterar scrollY; seleção/posição refletem teclado, setas e swipe. Toque sintetizado por CDP confirmou rolagem horizontal0→325 e vertical1675→1840 a partir da mesma faixa, sem prender gestos. Três fotos de equipe com148px de altura e seis tiles da galeria em duas colunas no320px confirmados. Nenhuma regressão ou pageerror encontrado.

Evidências atuais: `output/site-validation/commercial/` para capturas, `results.json`, `accessibility.json` e `contrast.json`; revisão independente, script e gestos de toque em `output/site-validation/mobile-ux-improvements/final-review.md` e `final-review-results.json`. Chromium emulado não substitui teste em aparelho físico ou Safari/iOS. Browser de revisão encerrado; servidor local do projeto permanece disponível.

Fontes principais: `site/styles/mobile-ux.css`, `site/partials/middle.html`, `site/partials/end.html`, `site/partials/footer.html`, `site/scripts/app.js`. Sem novas dependências, formulário, dados comerciais ou publicação.
