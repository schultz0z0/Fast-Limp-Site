# Avaliação B — evidência técnica isolada

Data: 16/10/2026. Auditoria somente leitura de `http://127.0.0.1:4173/`, sem alteração de UI, publicação ou instalação de pacotes. Contexto próprio de Chromium; nenhum relatório de avaliação A foi consultado. Preservadas as escolhas aprovadas do hero mobile, personas e largura do CTA.

## Veredito

Não houve defeito técnico confirmado nas verificações delimitadas. Isso não equivale a certificação WCAG completa ou medição de Core Web Vitals de produção. O sistema de cores, imagens reais locais, controles semânticos e comportamento de navegação mantêm coerência. Não há justificativa técnica neste passe para redesenhar componentes.

## Detector mecânico

Executado uma vez sobre o diretório de markup `site`: `rtk proxy C:/Users/rapha/.codex/skills/impeccable/scripts/impeccable.cmd detect --json site`. Saída integral em `detector.json`.

Total CLI: **2 warnings**, nenhuma descoberta confirmada após inspeção contextual.

| Regra | Local indicado | Verificação | Resultado |
|---|---|---|---|
| `broken-image` | `site/index.html`, linha 0 do detector; elemento na linha 30 | `#gallery-image` permanece sem src dentro de diálogo fechado. O clique define src e alt antes de abrir. Imagem abriu e carregou 1920px no teste. | Falso positivo: não existe caixa de imagem quebrada visível. |
| `dark-glow` | `site/index.html`, linha 0 do detector | Tokens de sombra: `site/styles/tokens.css:44–45` são sombras direcionais de petróleo, opacidade 0,08/0,10. Há também anel sem blur de foco em `site/styles/base.css:2`. | Falso positivo: não representa halo cromático decorativo. |

## Detector no navegador

Nova aba em contexto isolado `mobile-ux-b`, sem reutilizar abas do coordenador/usuário. Preflight modificou o título para `[Human] Fast Limp — auditoria técnica B` e adicionou script em memória (`window.auditInjectPreflight=true`). Helper iniciou na porta 8400; `http://localhost:8400/detect.js` foi injetado e executou.

Console: **4 `body-text-viewport-edge`**, correspondentes aos parágrafos dos cards 2–5 do carrossel de serviços, em `site/partials/middle.html:48`, `:52`, `:56` e `:60`. A 390px, seus retângulos têm left/right 365/626, 690/951, 1015/1276 e 1340/1601. Todos pertencem a `.services-track` com `overflow-x:auto` (`site/styles/middle.css:23`); são conteúdo alcançável por rolagem, e a largura do documento permanece 390px. São falsos positivos de uma heurística que avalia a posição dos descendentes fora do viewport sem considerar a faixa intencional.

O detector executou e produziu console, mas não foi confirmado overlay visual persistente: inspeção posterior não encontrou hosts shadow ou nós com outline inline. Não afirmar ao usuário que marcações estão visíveis na aba. O helper foi parado; a limpeza automática relatou `config_missing` para uma configuração de edição live que não foi criada. Como a injeção ocorreu somente em memória, não há script incluído em fonte para remover. A aba isolada da avaliação B foi fechada; o browser privado do Playwright também foi encerrado. Nenhuma aba do usuário foi fechada.

## Reflow e alvos

| Viewport CSS | scrollWidth | Altura da prévia | Elementos interativos visíveis abaixo de 44px em alguma dimensão |
|---|---|---|---|
| 320 × 844 | 320 | 11331 | 0 |
| 360 × 844 | 360 | 10657 | 0 |
| 390 × 844 | 390 | 10832 | 0 |
| 768 × 844 | 768 | 8177 | 0 |

Nenhum overflow de documento ou elemento fora do viewport foi encontrado, excetuando conteúdo intencional de `[data-track]`. A medição de alvos usa retângulos reais de links, botões e tabindex=0 visíveis; não conta o pequeno glifo visual do botão de galeria como controle independente. O alvo é o tile inteiro. Os 44px são critério de conforto do projeto, e este relatório não inventa uma violação WCAG AA com base nesse limiar.

## Interações verificadas

- Menu abriu por toque; Escape fechou e devolveu foco ao acionador.
- FAQ abriu a segunda resposta e atualizou `aria-expanded`.
- Galeria abriu com imagem carregada e diálogo visível; Escape restaurou foco ao tile.
- CTA de orçamento acionado por toque. Popup foi interceptado localmente antes de navegar para WhatsApp; URL e mensagem codificada foram lidas sem envio de mensagem.
- Carrossel: Home/End funcionaram e desabilitaram a seta correspondente ao limite.
- Nenhum `pageerror` foi emitido no passe.

## Evidência de gesto

Playwright lançou Chromium com `isMobile:true`, `hasTouch:true`, viewport 390×844. `Input.dispatchTouchEvent` do CDP sintetizou uma sequência touchStart, 10 touchMove, touchEnd para cada gesto.

| Estado | scrollLeft da faixa | scrollY da página |
|---|---|---|
| Antes | 0 | 1676 |
| Após swipe horizontal para esquerda | 325 | 1676 |
| Após swipe vertical iniciado na faixa | 325 | 1841 |

O teste comprova mudança horizontal de card e preservação da rolagem vertical a partir do carrossel nesse engine. A faixa usa rolagem nativa e `touch-action:auto`, sem máquina de arraste customizada. Não foram testados aparelho físico, Safari/iOS, interrupção de gesto por sistema operacional, pinça ou rotacionar aparelho.

## Prévia e saída pública

A homepage pública foi servida em teste por interceptação de rota a partir de `dist-production/index.html`, mantendo os mesmos assets locais. Em 390×844: **8486px** de altura, scrollWidth 390, sem `#equipe` ou `#depoimentos`. A altura de **10832px** pertence à prévia; não atribuí-la à página pública. Não há discussão de autenticidade dos exemplos porque são módulos condicionais da prévia.

## Limites e evidências

`technical-results.json` contém as medições e estados; `technical-probe.mjs` permite reproduzir a prova; `technical-mobile-390.png` registra a página inteira da prévia. Este passe não mediu tráfego móvel real, hardware lento, WebKit, leitores de tela, contraste de cada pixel, browser zoom em 200% ou CWV de campo. Não se atribui nota 4/4 de acessibilidade sem esses ensaios. Recomendações cosméticas e de arquitetura ficam fora desta avaliação B; nenhum reparo foi implementado.
