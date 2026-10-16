# FL-02 / FL-03 — implementação

Responsável: subagente `sections_middle`. Data: 15/10/2026.

## Escopo entregue

- FL-02: `#sobre` com colagem de três fotografias, texto, dois benefícios neutros por público e CTA; `#servicos` gelo com quatro propostas identificadas, controles manuais, pista rolável e scroll-snap.
- FL-03: `#referencias` com seis fontes fotográficas diferentes, composição bento e hooks para o visualizador compartilhado; `#como-funciona` petróleo com quatro etapas propostas, conectores, cards claros e poster estático 16:9.
- Propriedade respeitada: apenas `site/partials/middle.html`, `site/styles/middle.css` e este relatório foram criados/editados.

## Contratos de integração

Carrossel: `data-carousel`, `data-track`, `data-prev`, `data-next`, região nomeada e botões de 44 px. O JavaScript global integra teclado, rolagem e estado dos limites, sem autoplay.

Galeria: seis `button[data-gallery]` com `data-full` e `data-caption`. Alt e legendas distinguem referências ilustrativas de resultados reais. O diálogo global integra fechamento, Escape e retorno do foco.

CTAs: `data-contact` e `data-context` para abrir a informação local de contato. A âncora `#contato` é o destino da chamada abaixo dos serviços.

## Revisão interna estática

- Ordem, títulos H2/H3, IDs, textos e áreas conforme documentos e as duas referências.
- Sem biblioteca ou dependência nova; sem contatos, avaliações, preços, funcionários ou métricas inventadas.
- Sem play sem fonte de vídeo. Os quatro passos declaram explicitamente que o processo é proposto.
- Fotografia ilustrativa declarada em todas as seções; seis originais diferentes no bento.
- Tokens semânticos para cores; azul/petróleo nos controles, branco/petróleo na seção escura; imagens retangulares sem sombras ou cantos genéricos.
- Colagem cabe na sua caixa de proporção, sem deslocamento externo; grid e flex com `min-width:0`; overflow restrito à pista do carrossel. Nenhum `overflow-x:hidden` aplicado à página.
- Mobile: colagem acima; serviço com 86% e próximo visível; bento duas colunas e uma abaixo de 360 px; processo vertical com conectores. Desktop: três serviços completos e próximo parcial; bento 520 px; quatro etapas horizontais.
- Imagens com `width`/`height`, carregamento lazy, decodificação assíncrona, `srcset` e `sizes` por slot.
- Verificação executada com Node: sequência exata dos quatro IDs, 14 imagens com atributos obrigatórios, seis gatilhos de galeria, quatro cards de serviço, quatro etapas e nenhuma variável CSS sem token correspondente. Saída concluída com código 0.
- Dimensões intrínsecas conferidas com o agente de assets: retratos 1280×1707, fotos 4:3 1280×960, quadradas 1280×1280 e paisagens 1280×720; poster 1920×1080.
- Ajustado respiro de 6 px na pista para acomodar o contorno de foco de 2 px com offset de 3 px sem corte lateral.

## Validação integrada pendente

Build, abertura/renderização em 1440/390 e demais larguras, navegação de teclado, limites do carrossel e visualizador serão executados pelo coordenador após integrar os fragmentos e assets. Este relatório não afirma testes de navegador ainda não executados.

## Pendências comerciais

Catálogo específico, operação/etapas, contato e fotografias reais autorizadas. As propostas e cenas ilustrativas preservam a estrutura completa em revisão local e precisam de validação comercial antes da publicação.

## Correção delegada de foco — integração FL-06

Escopo adicional autorizado pelo coordenador: somente `site/scripts/app.js` e este relatório. A falha foi reproduzida antes da alteração: no lightbox com um único botão, o navegador alternava o foco entre o botão de fechamento e `BODY` ao pressionar Tab. O comportamento nativo de `showModal()` não bastava para o aceite de contenção explícita.

Foi adicionado ciclo explícito de Tab/Shift+Tab ao diálogo modal aberto. A lista é recalculada por evento e exclui itens sem tabulação, invisíveis, ocultos, inertes, desabilitados nativos ou `aria-disabled`. Primeiro e último elementos envolvem o ciclo, e o foco fora da lista retorna à extremidade apropriada. Escape, fechamento nativo e restauração do acionador foram preservados.

Evidência após a correção:

- `rtk proxy npm run build`: código 0, 183 tokens resolvidos, dist gerado.
- Regressão Playwright em linha, sem alterar os scripts de teste: três diálogos (`gallery`, `contact`, `pending`), quatro Tabs para frente e quatro Shift+Tabs para trás em cada um; recuperação após blur, Escape e restauração passaram. Código 0.
- Itens ocultos, desabilitados, inertes e `aria-disabled` inseridos temporariamente no DOM para o ensaio foram ignorados pelo ciclo. Código 0.
- `rtk proxy node scripts/a11y.mjs` ultrapassou o ponto de falha original e concluiu os ensaios de foco/galeria, FAQ, menu, reflow e movimento reduzido. A execução completa encontrou quatro linhas de contraste 4,27:1 sobre gelo nos links da conversão e no link inferior de serviços; coordenador avisado para a correção CSS. Este subagente não alterou os estilos nesta rodada.

## Encerramento integrado
Validação integrada concluída pelo coordenador: QA7larguras, carrossel/galeria/FAQ/menu e contraste passaram. Proteção contra callback close atrasado aplicada; regressões de foco e foto reaberta passaram em3rodadas completas. Consulte ENTREGA.md e output/site-validation/accessibility.json. As pendências descritas acima como futuras são registro histórico da entrega inicial do agente e estão agora encerradas tecnicamente.
