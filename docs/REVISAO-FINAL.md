# Fast Limp — revisão independente final

Data: 15/10/2026. Escopo: implementação estática em revisão local, etapas 00–06. Nenhum código de implementação foi alterado pelo revisor. Nenhuma publicação foi realizada.

## Base e método

Foram lidos DESIGN.md, prompts-site-fast-limp.md, design-system.json, manual de identidade e cores da marca, CONTRATOS.md, ISSUES.md, os três fragmentos, os três estilos, tokens, app.js e scripts de build/servidor/QA. As duas referências locais foram abertas e comparadas à página inteira e às capturas de seção, principalmente em 1440 e 390 px. A segunda referência foi tratada como montagem desktop.

Teste independente com Chromium/Playwright já disponível: 320, 360, 390, 640, 767, 768, 900, 1023, 1024, 1100, 1280, 1440 e 1920 px. Evidência: `output/site-validation/independent-review.json`, `review-details.cjs` e capturas `review-640.png`, `review-768.png`, `review-1024.png`. O reflow equivalente a uma janela de 1440 px com zoom de 200% foi observado em 720 CSS px; não foi uma certificação de zoom nativo em todos os navegadores.

## Achados priorizados

### RF-01 · P2 · Profissional oculto no primeiro hero — corrigido visualmente

Arquivos envolvidos: `site/styles/base.css:4` (recorte do hero), `scripts/prepare-photos.py:18` (origem e gravidade do corte), derivados `hero*`.

Na captura inicial `inicio-1440.png`, o card azul encobria quase todo o profissional; a cabeça terminava na diagonal do painel. Em `inicio-390.png`, o header cobria a cabeça. Isso enfraquecia a ação de limpeza e a composição da referência, que reserva o lado direito para o assunto fotográfico.

A substituição/corte em `hero-fix-desktop.png` e `hero-fix-mobile.png` foi inspecionada: profissional, vidro e ferramenta estão reconhecíveis fora das sobreposições. Aceite visual cumprido nessas duas capturas; manter o novo recorte no build final e renovar as capturas antigas.

### RF-02 · P2 · Hero fora do main e footer dentro dele — corrigido e retestado

Arquivos: `site/index.html:21–25`, `site/partials/start.html:1`, `site/partials/end.html:81` (linhas da versão revisada inicialmente; localizar também pelos elementos).

O template abre `<main id="conteudo">` depois de incluir start, deixando H1, apresentação e conversão fora do conteúdo principal. O skip link salta esses elementos e vai diretamente para Sobre. O include end contém o footer antes de `</main>`; desse modo ele não oferece o landmark implícito global de rodapé. O header também está dentro de section, comprometendo o landmark global de cabeçalho.

Aceite cumprido no re-review: `body>header` e `body>footer` presentes, H1 dentro do main, footer fora do main. O skip link acionado por Enter transferiu foco para `#conteudo`. A geometria do hero foi novamente inspecionada em 1440 e 390 px. A estrutura final usa `site/partials/header.html` e `footer.html`, com posicionamento em `site/styles/layout.css`.

### RF-03 · P2 · Ciclo de foco dos diálogos — corrigido e retestado

Arquivo: `site/scripts/app.js:35` e inicialização dos diálogos; template dos diálogos em `site/index.html:27`.

No teste independente, Tab após o último controle produziu `document.activeElement === BODY` no contato; a galeria com um único controle também passou por BODY. Escape e retorno ao acionador funcionaram. Embora o modal nativo torne o fundo inerte, o requisito específico exige foco contido e visível no visualizador.

Aceite cumprido no re-review independente: quatro Tab e quatro Shift+Tab mantiveram o foco contido em cada um dos três diálogos (contato, galeria e pendência). Escape fechou e devolveu foco ao acionador nos três casos. Não houve queda para BODY neste teste final. A proteção explícita de foco está no app.js.

### RF-04 · P3 · Topbar extrapola sua própria altura em 360/390 px — corrigido e retestado

Arquivo: `site/styles/base.css:4`, regras `.utility-bar` e `.utility-inner`.

A faixa tem 32 px fixos, mas os dois textos quebram em 38,375 px de altura: `top=-3,1875`, `bottom=35,1875`, confirmado por DOM nas duas larguras. A faixa perde o respiro e invade o início da viewport/fotografia.

Aceite cumprido no re-review: link auxiliar oculto no mobile, texto principal integralmente dentro da faixa, sem extravasamento, nas nove larguras de 320 a 1920 px. Em 360/390 px a linha fica entre y=6,40625 e y=25,59375 dentro da faixa de 32 px.

### RF-05 · P3 · Algumas capturas de seção estão contaminadas pelo skip link — corrigido na captura e retestado

Arquivo: `scripts/qa.mjs` (loop de capturas de seção).

`duvidas-390.png` e `como-funciona-390.png`, entre outras, mostram o skip link sobre os títulos. No carregamento independente ele fica fora da viewport como previsto; não foi confirmado como defeito normal da página. O re-review reproduziu o artefato em novas capturas de elemento alto mesmo com blur: `reviewer-final-duvidas-390.png` e `reviewer-final-como-funciona-390.png`. Logo após a captura o DOM informa `focused=false`, `top=-67,35px` e transform de `-79,35px`. Isso indica artefato de composição da captura, em vez de foco real.

Aceite da entrega: gerar as capturas de apresentação com o link inativo invisível apenas no estilo de screenshot, ou recortar uma captura de página completa. Conservar separadamente a evidência de teclado; não esconder o skip link na implementação.

Aceite cumprido: QA usa `.skip-link:not(:focus){visibility:hidden!important}` apenas no argumento `style` do screenshot de seção, sem alterar o produto. As capturas renovadas `duvidas-390.png` e `como-funciona-390.png` foram abertas e inspecionadas; títulos e eyebrows estão livres da sobreposição. RF-05 encerrado.

## Aspectos aceitos na revisão

- A ordem completa das onze áreas e os tipos de composição estão presentes: hero/conversão, colagem de três fotos, carrossel, bento de seis imagens, processo escuro, foto com badge, depoimentos, equipe, FAQ, editorial e rodapé único.
- A silhueta normalizada conserva a arquitetura da referência; adaptações de cor/tipografia são coerentes com a Fast Limp. As diferenças nos módulos de pessoas/depoimentos são deliberadas e honestas, pois não há conteúdo real autorizado.
- Container desktop de 1200 px, header de 1320 px, marca compacta de 208/156 px, cantos retos, azul/petróleo e Manrope estão aplicados. Não houve reprodução da moldura de água, marca Cleanx, roxo, preços ou estatísticas da referência.
- Os 13 tamanhos testados não apresentaram expansão horizontal da página. Layout intermediário de header não colide em 1024 px. Fotos preservam as proporções de seus slots; o manifesto registra derivados próprios, e a galeria usa seis fontes distintas.
- Menu abre/fecha e devolve foco via Escape. Contato abre indicação local sem coleta/envio. FAQ mantém apenas um item aberto por ação. Galeria abre com legenda, fecha por Escape e retorna ao acionador. Carrossel tem controles manuais, região nomeada e comandos de teclado; o teste do projeto verifica limites e setas desabilitadas.
- Movimento reduzido está contemplado e foi usado no teste independente. Não há autoplay ou reveal que esconda conteúdo inicial. Não houve pageerror ou resposta HTTP de erro no teste independente.
- Conteúdo distingue ilustração de serviço executado, propostas de catálogo/fluxo de fatos confirmados e módulos pendentes de depoimentos/equipe/artigos. Não foram encontrados preços, clientes, certificações, região, contatos ou avaliações inventados.
- SEO local não inventa endereço ou avaliações; há idioma pt-BR, descrição coerente, noindex da prévia e ausência de canonical fictício.

## Re-review focado das correções

`rtk node output/site-validation/final-review-check.cjs` executado após as correções com saída 0. Resultado completo: `output/site-validation/final-review-results.json`. Nove larguras (320, 360, 390, 640, 767, 768, 1024, 1440, 1920 px) sem expansão horizontal, com conteúdo da topbar contido e landmarks corretos; três ciclos modais aprovados; skip link focou main; nenhum pageerror nem resposta HTTP de erro. Hero final inspecionado em `reviewer-final-1440.png` e `reviewer-final-390.png`, mantendo assunto fotográfico e ferramenta visíveis. RF-01–04 encerrados.

## Aceite final e limites

Aceite final concedido para a estrutura completa em revisão local, com RF-01–05 encerrados e sem achado bloqueante restante nesta revisão. O re-review independente confirmou hero, landmarks, skip link, topbar, contenção/retorno de foco e ausência de expansão horizontal nas larguras indicadas. As duas capturas problemáticas foram renovadas e inspecionadas. O coordenador verificou separadamente contraste e a corrida assíncrona no fechamento dos diálogos; esses resultados constam da suíte final sob sua responsabilidade.

Não confundir esse aceite com prontidão para publicação: telefone/WhatsApp, região, catálogo/condições, evidências reais, equipe, artigos, domínio e privacidade continuam pendentes conforme o roteiro. A entrega aprovada continua sendo prévia local, sem publicação.

Não foi alegada certificação WCAG, teste em aparelho real, leitor de tela ou compatibilidade entre todos os navegadores. As capturas independentes de página inteira usadas para diagnóstico precedem os ajustes finais do coordenador e não substituem as capturas finais renovadas.
