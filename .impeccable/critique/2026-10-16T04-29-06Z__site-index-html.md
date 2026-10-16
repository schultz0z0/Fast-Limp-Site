---
target: UX e composição mobile da página inteira Fast Limp
total_score: 27
max_score: 32
na_heuristics: 7,9
p0_count: 0
p1_count: 0
target_identity: "file:D:\\Projetos SaaS\\Portfolio de Sites\\Fast Limp - Limpeza de Vidros\\site\\index.html"
target_fingerprint: "sha256:6dab092f1cf064d145578de6d2f4eb355b5c198958bf6e64de20ebb5daecf5e4"
target_path: "D:\\Projetos SaaS\\Portfolio de Sites\\Fast Limp - Limpeza de Vidros\\site\\index.html"
timestamp: 2026-10-16T04-29-06Z
slug: site-index-html
---
# Fast Limp — revisão de UX mobile
Method: dual-agent (A: /root/mobile_design_review · B: /root/mobile_technical_audit)

16/10/2026. Alvo: site/index.html e implementação vinculada, http://127.0.0.1:4173/. Modo Persuade: reconhecer o serviço, consultar dúvidas e solicitar orçamento. Auditoria somente leitura; nenhuma alteração na interface ou publicação.

## Parecer
Boa base responsiva e identidade coesa. O percurso ainda pode priorizar melhor a descoberta dos serviços, a continuidade da ação e a consulta rápida de informações no celular. Não recomendo outro redesenho do hero aprovado: pessoa acima, conteúdo abaixo, CTA proporcional ao texto. As oportunidades são ajustes locais no decorrer da página.

A inspeção em Chromium emulado e por capturas não equivale a pesquisa com usuários, teste de aparelho físico, leitor de tela ou comprovação de melhora de conversão.

## O que funciona
- Logo, Manrope, azul e petróleo consistentes. Alternância de superfícies e fotografias mantém capítulos reconhecíveis; corpo de texto principal e alinhamentos são legíveis em390px.
- Hero aprovado apresenta orçamento na primeira tela de390×844px. CTA mede aproximadamente244×54px. Menu, FAQ e galeria têm estados e fechamento/foco operáveis.
- Todos os alvos medidos na página de390px têm ao menos44px nas duas dimensões; não foi confirmado alvo pequeno. A marca de expansão32px da galeria é apenas o ícone: o botão é a fotografia inteira.
- Navegação por serviço leva ao WhatsApp com mensagem e bairro, sem formulário longo ou envio automático.

## Prioridades
### UX-01 · P2 — catálogo pouco reconhecível antes de explorar o carrossel
Em390px, o primeiro card mede301px; o próximo começa em x345px e aparece só parcialmente. Pós-obra, fachadas e vitrines exigem avanços; o último serviço aparece após quatro avanços. As setas e a borda do próximo card são bons indícios, mas não comunicam nomes nem total/posição.
Ajuste: manter o carrossel e acrescentar visão compacta dos cinco serviços com acesso ao card e posição1de5. O problema é descoberta, não gesto quebrado.
Fonte: site/partials/middle.html, .services-track e .service-card; captura commercial/servicos-390.png.

### UX-02 · P2 — processo de orçamento sem ação ao final
Galeria978px + processo1103px somam cerca de2081px sem CTA de contato. O processo orienta clicar no orçamento, mas não possui esse botão. O próximo WhatsApp está em diferenciais, depois de outro título, texto e lista. O convite geral de serviços aponta para #contato, ao passo que os cards abrem WhatsApp.
Ajuste: orçamento direto após os quatro passos; alinhar o convite geral dos serviços ao mesmo caminho. Não há necessidade demonstrada de impor botão flutuante.
Fonte: site/partials/middle.html, #como-funciona e .services-bottom.

### UX-03 · P2 — informação procurada vem depois de blocos auxiliares
No FAQ, as perguntas começam cerca de519px após o início da seção, porque o convite “Ainda tem uma dúvida?” aparece antes delas. O rodapé tem1484px e telefone/região aparecem depois dos dois menus; o número fica aproximadamente1202px após o começo do rodapé. O CTA de orçamento do início do rodapé compensa parte da distância, portanto não há bloqueio.
Ajuste: perguntas antes do card de ajuda no mobile; agrupar região, número/WhatsApp e CTA no começo do rodapé, seguidos dos menus. Identificar que o link do número abre WhatsApp.
Fonte: site/partials/end.html #duvidas e site/partials/footer.html; commercial/duvidas-390.png e contato-390.png.

### Observações secundárias
- P3 — ritmo: na prévia, três perfis verticais ocupam1869px, mais de duas telas. Uma apresentação mais compacta no mobile preservaria os três nomes e o desktop. Este trecho não entra no build público atual. A galeria mede1729px em320px contra978px em390px, pelo empilhamento das seis fotos em uma coluna; merece revisão específica de composição se320px for uma prioridade.
- P3 — leitura: descrições dos benefícios e das quatro etapas usam13px; nomes de função usam12px. Não há ilegibilidade comprovada, mas textos de orientação podem ganhar conforto com14–16px e hierarquia mais distinta das legendas.

## Extensão e carga de leitura
Em390×844px: prévia10832px, aproximadamente12,8 telas; saída pública8486px, aproximadamente10,1 telas. Equipe e depoimento explicam2346px da diferença. Uma página longa não é automaticamente ruim; interessa reduzir repetição e aproximar ação da informação, mantendo as seções desejadas.
O meio alterna galeria, processo e outra fotografia grande, com repetição dos mesmos assuntos. É oportunidade editorial; não se deve inventar diferenciais ou promessas para preencher espaço.
A decisão do visitante é simples e compreensível (qual serviço / pedir orçamento). Cinco opções não constituem sobrecarga por si só; os nomes pouco visíveis dificultam o reconhecimento.

## Heurísticas de Nielsen (avaliação A)
| Heurística | Nota /4 | Evidência |
|---|---:|---|
|1 Visibilidade de estado|3|Menu, FAQ e limites funcionam; falta posição dos serviços|
|2 Linguagem do usuário|4|Bairro, fotos, acesso, orçamento e agenda claros|
|3 Controle e liberdade|3|Fechamento e controles observados; não é teste de toda tecnologia assistiva|
|4 Consistência|3|Sistema visual coeso; destinos de convites semelhantes diferem|
|5 Prevenção de erros|3|Mensagens contextualizadas, nenhuma confirmação falsa ou envio automático|
|6 Reconhecimento|2|Catálogo completo exige exploração dos cards|
|7 Flexibilidade e eficiência|n/a|Aceleradores e operações em lote não se aplicam à landing page|
|8 Estética e minimalismo|3|Boa unidade; repetição e distância entre informação e ação|
|9 Recuperação de erros|n/a|Sem transação/formulário interno ou erro observado|
|10 Ajuda|3|FAQ útil, mas ajuda oferecida antes das respostas|
|Total aplicável|27/32|Avaliação heurística; não é métrica de conversão nem certificação|

Primeira avaliação deste alvo neste fluxo; não há tendência histórica comparável.

## Evidência técnica independente
Detector CLI: uma execução em site/,2 warnings. Ambos falsos positivos:
1. broken-image, site/index.html:30: imagem do diálogo sem src antes da abertura; fonte é configurada ao abrir e foi carregada.
2. dark-glow: sombra do cabeçalho/anel de foco petróleo sobre fundo claro, sem brilho decorativo. Fonte efetiva tokens.css:44–45 e base.css:2.

Detector no navegador:4 avisos body-text-viewport-edge nos textos dos cards2–5, intencionalmente fora da janela da faixa horizontal. Fontes: site/partials/middle.html:48,52,56,60; middle.css:23 define overflow-x:auto. Largura do documento e gestos confirmaram que não é overflow da página.

Toque sintetizado por CDP em Chromium: swipe horizontal moveu scrollLeft0→325 sem mover a página; gesto vertical na mesma faixa moveu scrollY1676→1841, preservando scrollLeft325. As setas oferecem alternativa ao arraste. Sem overflow em320/360/390/768px. Menu, FAQ, galeria e CTA passaram no percurso verificado.

Não foram confirmados P0/P1 técnicos neste passe. Isso não declara conformidade WCAG completa nem Core Web Vitals de produção. O carregamento local não representa rede móvel real.
Referência técnica: W3C, SC2.5.8, mínimoAA24×24px com exceções;44px é a meta de conforto do projeto. W3C, SC2.5.7, alternativa ao arraste.
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html

## Percursos simulados
- Primeiro visitante: entende serviço/região, mas precisa explorar para saber que vitrines está no catálogo.
- Visitante com uma mão: controle e swipe funcionam; uma ação ao concluir o processo evitaria voltar/continuar procurando.
- Visitante em busca de uma resposta: conteúdo útil existe; FAQ e número são precedidos por blocos que não resolvem sua dúvida.
Essas são leituras heurísticas, não entrevistas ou relatos de usuários reais.

## Escopo, evidências e limpeza
Relatórios independentes design-review.md e technical-audit.md, dados technical-results.json e browser-metrics-390.json, captura technical-mobile-390.png. Imagens por seção em ../commercial/. Detector executou no navegador, mas não foi confirmado overlay visual persistente.
Servidor auxiliar do detector encerrado; aba e contexto B encerrados. A aba de leitura do coordenador também é encerrada. Localhost4173 do projeto permanece disponível, como já solicitado anteriormente. Nenhum pacote instalado ou deploy executado.
Falha de gravação de arquivo via ChromeDevtools foi contornada com arquivos locais normais; não afetou leitura da página. Nenhuma alteração nas fontes de produto.
As propostas UX-01–03 e observações P3 não foram implementadas nesta auditoria.
