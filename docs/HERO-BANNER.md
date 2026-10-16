# Hero com degradê · FL-12

**Revisão vigente FL-13:** desktop ocupa a altura da janela com `min-height:100svh`; em telas baixas, o conteúdo pode ampliar o banner sem cortes. A faixa utilitária foi removida do cabeçalho em todas as versões e o menu desktop fica a24px do topo. No mobile, a fotografia/pessoa fica na parte superior, com degradê para o azul da área de conteúdo abaixo. O botão usa largura natural, aproximadamente244px, com limite à largura disponível. Em390px o banner tem726px de altura e a foto superior390px. As capturas e os JSONs foram atualizados; as descrições a seguir registram a direção inicial da FL-12, anterior a esses ajustes.

16/10/2026. Nova solicitação substitui a direção anterior: banner tradicional tanto no desktop quanto no mobile, com conteúdo sobre o degradê do azul oficial e a pessoa na imagem de fundo. Não há mais painel azul separado ou cartões de conversão sobrepostos.

O desktop usa azul `#1C94F0` à esquerda e transparência progressiva aproximadamente no meio da composição, revelando a foto existente à direita. A tipografia Manrope em petróleo permanece sobre a região mais opaca; o botão branco recebe texto petróleo. Os dois atalhos de casa/empresa ficam como links secundários abaixo do orçamento.

No mobile, a mesma linguagem usa degradê vertical. A fotografia ocupa o fundo inferior, com o rosto abaixo do conteúdo; a transição integra texto e pessoa no mesmo banner. A foto não é um bloco ou cartão separado. O cabeçalho branco flutua no topo, o título tem três linhas e o CTA principal permanece na primeira tela. Os atalhos secundários são ocultos no celular para manter a hierarquia do orçamento.

Fontes alteradas: `site/partials/start.html` e `site/styles/layout.css`. Marca, fontes, tokens e fotografias preservados. Os outros módulos e os21 links de WhatsApp continuam no HTML. A composição anterior foi preservada em `tmp/hero-before-banner.html` e `tmp/layout-before-banner.css` para referência local.

## Evidências

- Capturas da primeira tela em320/360/390/486/767/768/1440px e coordenadas em `output/site-validation/hero-banner/`. Em390px, o CTA fica entre409 e463px do topo; o banner tem783px de altura.
- Página inteira nas sete larguras principais em `output/site-validation/commercial/`. Sem overflow horizontal, imagens quebradas, falhas de fonte ou erros de console/HTTP.
- Builds/checks local e público, testes de interação e teste do build público passaram. Menu mobile, Escape/foco, WhatsApp, FAQ, carrossel e galeria preservados.
- A suíte de acessibilidade passou:154 trechos sobre superfícies sólidas, zero falhas, menor relação4,88:1; movimento reduzido e reflow200%. A leitura de contraste sólido não mede a fotografia inteira; o conteúdo foi mantido sobre a porção opaca do degradê, com revisão visual dos recortes.

Nada foi publicado. A saída pública continua sendo `dist-production/`, com as exclusões de dados temporários já existentes.
