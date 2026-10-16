# Hero mobile · FL-11

**Direção substituída pela FL-12:** o cliente solicitou posteriormente um banner com degradê no desktop e mobile. Consulte `HERO-BANNER.md` para o estado atual. O registro abaixo é histórico.

Revisão de 16/10/2026 a pedido do cliente. Desktop aprovado preservado; composição específica até 767px.

No celular, o cabeçalho entra no fluxo normal da página, sem topbar repetida ou logo sobre a fotografia. O conteúdo abre em branco, com texto curto e alinhamento à esquerda, Manrope e cores oficiais. A chamada tem três linhas deliberadas; o botão azul de orçamento ocupa a largura útil antes da fotografia. A foto existente permanece, seguida dos dois atalhos compactos de residência/empresa.

A mesma H1 oferece textos responsivos com `display:none` para ocultar a alternativa fora do breakpoint, inclusive da árvore de acessibilidade. As CTAs continuam sendo links estáticos de WhatsApp, com os mesmos contextos. O menu mantém seus comportamentos de teclado e foco. A ordem visual mobile coincide com a ordem dos controles no teclado; a fotografia é um elemento não interativo entre o botão principal e os atalhos.

Fontes: `site/partials/start.html` e bloco FL-11 em `site/styles/layout.css`. Não foram trocados fotos, tokens, fonte, logo ou componentes fora do hero/header mobile. Evidências de geometria e capturas em `output/site-validation/mobile-hero/`; QA geral e acessibilidade atualizados em `output/site-validation/commercial/`.

Verificações: builds e checks local/público; interações; acessibilidade; sete larguras principais. Inspeções adicionais em 486 e 767px, transição para 768px e desktop1440px. Em390px, o botão fica entre355 e409px do topo; a composição principal cabe na primeira tela844px. O CTA não depende de rolar até o final de um painel alto. Sem publicação.
