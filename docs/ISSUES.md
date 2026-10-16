# Fast Limp — quadro de execução

Atualização inicial: 15/10/2026. Modo: revisão local. Solicitação atual autoriza 00–06 e substitui paradas históricas por revisão interna. Sem publicação.

| Issue | Escopo | Dependências | Responsável | Aceite | Status / evidência |
|---|---|---|---|---|---|
| FL-00 | Ler fontes, inventariar stack, marca e lacunas | — | Coordenador | Documentos/PDF/referências lidos, stack preservada | Concluída: apenas documentação, sem app ou Git preexistente; HTML/CSS/JS estático conforme roteiro |
| FL-01 | Tokens, fonte, assets, contratos, header, hero e conversão | FL-00 | Coordenador + assets | Marca oficial, Manrope, diagonais e mobile acessível | Concluída: 183 tokens; logo 208/156px; hero desktop/mobile revistos; capturas inicio-1440/390 |
| FL-02 | Colagem Sobre + carrossel Serviços | Base FL-01 | agente sections-middle | 3 fotos; carrossel manual, 3+peek desktop e 86% mobile | Concluída: ETAPAS-02-03.md; capturas sobre/servicos; testes de limites/teclado e swipe touch234px |
| FL-03 | Bento + processo e mídia | Base FL-01 | agente sections-middle + assets | 6 imagens distintas, lightbox, 4 etapas e poster | Concluída: seis fontes distintas,60 WebP validados; galeria/foco/Escape; processo proposto sem play |
| FL-04 | Diferenciais, depoimentos, equipe | Base FL-01 | agente sections-end | Badge neutro; slots honestos e completos | Concluída: ETAPAS-04-05.md; capturas diferenciais/depoimentos/equipe; módulos pendentes explícitos |
| FL-05 | FAQ, editorial, CTA e rodapé | Base FL-01 | agente sections-end | 6 respostas, 3 editoriais, rodapé único, contato local | Concluída:6 FAQs teclado;5 controles de conteúdo pendente;15 CTAs desktop; rodapé global único |
| FL-06 | Integração, revisão, responsividade, acessibilidade e entrega | FL-01–05 | Coordenador + final_review | 7 larguras; interações; build; capturas 1440/390; correções | Concluída: build/check/test; QA7larguras; a11y3rodadas; RF01–05 encerrados; ENTREGA.md |

## Retomada

## FL-16 · Versionamento inicial no GitHub

- Autorização: enviar o projeto para `https://github.com/schultz0z0/Fast-Limp-Site.git`, diretamente na branch `main`. Repositório remoto confirmado vazio e acesso administrativo disponível.
- Escopo: código, assets oficiais, fontes/licenças, documentação, referências, panfletos e evidências. Builds `dist/`/`dist-production/`, `tmp/`, dependências, logs, estado local do detector e arquivos de credenciais ficam ignorados. Esses arquivos permanecem locais quando existentes.
- Validação anterior ao commit: integridade das duas saídas passou; revisão de padrões de credenciais nos arquivos preparados. Não configurar deploy, GitHub Pages ou domínio nesta etapa.
- O commit inicial e seu envio serão verificados comparando `HEAD` com `refs/heads/main` no remoto. O resultado e hash podem ser consultados pelo histórico Git.

## FL-15 · Aplicação das melhorias de UX mobile — concluída

- Escopo autorizado: UX-01/02/03 da FL-14 e ajustes de ritmo/leitura; preservar hero aprovado e composição desktop. Responsável: coordenador.
- Implementação: cinco atalhos com estado e posição no carrossel mobile; orçamento após o processo; convite geral de serviços abre WhatsApp; FAQ antes do suporte; contato antes dos menus no rodapé; equipe em linhas compactas; galeria320px com duas colunas; textos auxiliares14px.
- Aceite: atalhos funcionam com clique/teclado e refletem swipe/setas/Home/End; controle de foco não causa salto vertical; todos os serviços visíveis no índice; ordem visual/DOM mobile coerente; hero intacto; builds/checks/testes/capturas e revisão visual.
- Evidências: builds/checks local e público, testes de interação e acessibilidade passaram; QA7larguras sem overflow/fotos quebradas/erros. Hero390/1440 idêntico byte a byte. Revisor mobile_technical_audit aceitou após verificar cinco escolhas por toque sem salto vertical, sincronização por setas/Home/End/swipe, rolagem vertical na faixa, nova ordem FAQ/rodapé, equipe3×148px e galeria320 com6tiles em2colunas. Relatórios em `output/site-validation/mobile-ux-improvements/`; resumo `docs/UX-MOBILE-MELHORIAS.md`. UX-01/02/03 e observações de ritmo/leitura da FL-14 atendidos. Nada publicado.

## FL-14 · Auditoria UX mobile — concluída, sem alteração de UI

- Escopo: composição da página inteira, navegação, leitura, descoberta dos serviços, continuidade do orçamento e consulta no mobile. Responsáveis: coordenador + agentes mobile_design_review (A) e mobile_technical_audit (B), avaliações isoladas.
- Evidências: `docs/REVISAO-UX-MOBILE.md`; relatórios, detector, gestos e métricas em `output/site-validation/mobile-ux/`. Swipe horizontal e rolagem vertical confirmados com toque CDP em Chromium. Nenhum defeito técnico bloqueante confirmado; detector teve2+4 avisos contextualmente descartados.
- Resultado: base responsiva boa;3 oportunidades P2 em descoberta, continuidade da ação e ordem FAQ/rodapé. Nota heurística27/32 em8 heurísticas aplicáveis; sem pretensão de pesquisa com usuários ou certificação.
- Backlog proposto, não implementado: UX-01 visão rápida dos5serviços/posição; UX-02 CTA ao terminar processo e unificar destino geral; UX-03 FAQ antes do suporte e contato antes dos menus no footer. Observações P3: ritmo de galeria/equipe e textos auxiliares pequenos. Preservar identidade e hero aprovados.

## FL-13 · Altura e ordem do banner — concluída

- Solicitação: desktop com altura de uma tela; mobile com pessoa acima e conteúdo abaixo, CTA proporcional ao texto; remover faixa utilitária acima do menu.
- Responsável: coordenador. Dependência: FL-12. Escopo: header e geometria/gradiente do hero; demais áreas preservadas.
- Aceite: hero desktop com `100svh` e expansão natural quando necessária; faixa ausente do HTML; rosto antes do conteúdo no mobile, degradê para o azul inferior e CTA sem largura total; navegação, foco, imagens e builds preservados.
- Evidências: no viewport desktop1440×1000, hero1000px; mobile390px com foto superior390px e botão244px em área útil350px. Menu/faixa: a faixa foi removida do fragmento, não apenas ocultada. Builds/checks local e público, interações, produção e acessibilidade passaram;152 trechos sólidos, zero falhas de contraste. QA das sete larguras sem overflow, imagens quebradas ou erros. Capturas e coordenadas atualizadas em `output/site-validation/hero-banner/`, página inteira em `output/site-validation/commercial/`.

## FL-12 · Banner com degradê no desktop e mobile — concluída

- Solicitação substitui a direção FL-11: banner comum nas duas versões, conteúdo sobre o azul do KV que se dissipa até a fotografia da pessoa ao fundo. Responsável: coordenador.
- Escopo: banner contínuo, foto existente preservada; degradê lateral no desktop e vertical no mobile; chamada e orçamento no próprio banner, sem painéis separados. Menu/links WhatsApp e demais áreas preservados.
- Aceite: composição em 1440/390px e larguras adicionais, fotografia/rosto legíveis, texto e botão com contraste, sem overflow, navegação e build local/público funcionando. Sem publicação.
- Evidências: builds/checks local e público, teste de produção, interações e acessibilidade passaram (154 trechos sólidos, zero falhas, mínimo4,88:1). QA sete larguras sem overflow, imagens quebradas ou erros. Capturas adicionais de320 a1440px em `output/site-validation/hero-banner/`; página completa em `output/site-validation/commercial/`; resumo atual em `HERO-BANNER.md`. FL-11 foi substituída por esta direção a pedido do cliente.

## FL-11 · Hero exclusivo para mobile — concluída

- Solicitação: melhorar composição do hero no celular; preservar o desktop aprovado. Responsável: coordenador. Dependência: FL-10.
- Direção: cabeçalho branco no fluxo, sem faixa repetida; chamada curta em três linhas, CTA antes da foto, fotografia preservada e dois atalhos de atendimento compactos. Alterações visuais limitadas a até 767px.
- Aceite: orçamento na primeira tela; boa composição em 320/360/390px e transição em 767/768px; menu, foco e WhatsApp preservados; desktop de 1440px visualmente idêntico; sem overflow, imagens quebradas ou regressão de contraste.
- Evidências: build/check/test, acessibilidade e build/check/test público passaram. QA das sete larguras sem overflow, fotos quebradas ou erros. Capturas adicionais em 320/360/390/486/767/768/1440px e coordenadas em `output/site-validation/mobile-hero/layout.json`: CTA termina em 409px na largura390; hero tem663px de altura. Cabeçalho, título, CTA, foto e atalhos cabem no viewport390×844. Comparação desktop antes/depois registrada na revisão visual.

- FL-10: retirada dos rótulos da interface local por solicitação explícita. Preservar a separação técnica entre prévia e build público; dados de equipe e depoimento ainda precisam ser substituídos. Não recolocar avisos visíveis ao retomar.

## FL-10 · Prévia com aparência final — concluída

- Escopo: remover avisos visíveis e acessíveis de banco de imagens/ilustração/demonstração/perfis fictícios, mantendo fotos, nomes, relato, composição e contratos de interação. Responsável: coordenador. Dependência: FL-09.
- Prévia é local, sem publicação; blocos de equipe/depoimento continuam excluídos de `dist-production/`. Procedência de fotos e natureza provisória dos dados ficam na documentação interna.
- Aceite: rótulos ausentes inclusive nas legendas da galeria e alternativas textuais; apresentação local com aparência final; builds e verificações anteriores preservados.
- Evidências: builds/checks das duas saídas passaram; interações e acessibilidade passaram (158 trechos, contraste mínimo 4,88:1); sete larguras sem overflow/imagens quebradas/erros. Busca nas fontes de interface não encontra os rótulos solicitados. Capturas atualizadas em `output/site-validation/commercial/`; revisão visual dos módulos de depoimento/equipe concluída.

- Atualização 16/10/2026: FL-09 concluída. WhatsApp confirmado (21) 96764-3628, Rio de Janeiro, cinco serviços; conteúdo novo substitui pendências equivalentes das etapas anteriores. Blog removido por solicitação. Coordenador implementou e validou; tentativa de delegação a sections_end falhou por limite de uso antes de qualquer edição.

## FL-09 · Conteúdo comercial e conversão — concluída em16/10/2026

- Escopo: CTAs WhatsApp com mensagens por serviço, cinco categorias confirmadas, Rio de Janeiro, fotos mantidas sem avisos repetitivos, oito FAQs com pesquisa concorrencial, exclusão de artigos, um exemplo de relato e três perfis fictícios identificados apenas na prévia.
- Dependências: FL-06/07; dados fornecidos pelo usuário em16/10/2026. Responsável: coordenador; revisão independente indisponível por limite da conta.
- Aceite: todas CTAs usam 5521967643628 com texto pré-preenchido, navegação sem JavaScript para WhatsApp, menu/FAQ/galeria/carrossel/teclado preservados; nenhum artigo; três fotos locais de equipe de demonstração; `dist-production/` exclui relato e equipe fictícios; build/check nas duas saídas; QA sete larguras e capturas 1440/390.
- Decisões: WhatsApp direto (alternativa autorizada ao formulário), sem backend ou envio simulado. Não publicamos depoimento inventado como experiência real. Prévia mantém demonstrações identificadas; saída pública as remove no build. `noindex` continua até domínio e publicação autorizados.
- Evidências: ambos builds/checks, `test:content`, `npm test`, `test:production`, QA320/360/390/768/1024/1440/1920 e acessibilidade passaram;21 links WhatsApp, cinco serviços, oito FAQs, zero imagens quebradas/overflow/erros; contraste mínimo4,88:1 entre162 trechos. Capturas e resultados em `output/site-validation/commercial/`; `ATUALIZACAO-COMERCIAL.md` registra detalhes e limitação da revisão independente.

- Fontes: prompts-site-fast-limp.md, DESIGN.md, design-system.json, PDF de 24 páginas, diretrizes e manifesto da marca, duas referências desktop locais e anexadas.
- Não há stack existente nem repositório Git. Implementação estática em `site/`; build nativo Node em `dist/`; originais da marca preservados.
- `setup-agent`/`search_resources` não estão expostos na sessão (inventário das ferramentas consultado). Nenhuma skill, plugin, servidor ou ferramenta nova será criada ou recomendada. Reutilizamos recursos já disponíveis.
- Revisões intermediárias são internas por autorização expressa. Não solicitar nova aprovação de identidade.
- Somente coordenador edita este quadro. Agentes mantêm relatórios próprios.

## Fechamento · 15/10/2026

Todas as etapas 00–06 concluídas para revisão local. **Não repetir implementação ou revisões encerradas ao retomar.** Próximas mudanças dependem de nova solicitação ou do fornecimento de conteúdo comercial. Ver `ENTREGA.md`, `REVISAO-FINAL.md`, `../README.md` e `../output/site-validation/`.

## FL-07 · Fotos indisponíveis após encerrar sessão — concluída

- Relato: fotos abaixo da dobra não carregavam na aba já aberta.
- Responsável: coordenador. Dependência: FL-06. Aceite: servidor disponível fora da sessão temporária;60 WebP HTTP200; galeria visível na aba do usuário.
- Causa reproduzida: nenhum processo escutando4173, requisição direta de gallery-03 falhou por conexão recusada; HTML/fotos iniciais continuavam em memória, fotos lazy não podiam ser buscadas.
- Correção: `npm run local` inicia servidor oculto via WMI fora da árvore do terminal temporário, restrito a127.0.0.1. Não cria agendamento/login automático. Idempotente; `npm run local:stop` encerra somente processo identificado como deste projeto.
- Evidências: primeira execução iniciou PID58852, segunda reutilizou o mesmo servidor;60 WebP respondendo200 com Content-Type correto. Aba real recarregada: seis fotos do bento com naturalWidth>0 e captura visual confirmada. README atualizado.

## FL-08 · Panfleto presencial A5 — concluída em16/10/2026

- Revisão v2: cliente pediu maior presença visual, títulos sem pontos e composição própria de panfletagem. Referência nova inspirou hierarquia/diagonal/figura, preservando identidade oficial. Dois PDFs v2, prévia e fonte separados; figura ilustrativa gerada com alpha302ppi efetivos, sem logo gerada ou representação de equipe real. Ver output/panfleto/DIRECAO-V2.md. Versão inicial preservada.

- Escopo: peça impressa clara e limpa, uma face, com identidade aprovada e foco em conversão. Responsável: coordenador. Dependências: marca/brandbook-v1 e catálogo/WhatsApp fornecidos nesta solicitação.
- Layout do anúncio enviado explicitamente ignorado; somente WhatsApp(21)96764-3628 e cinco serviços extraídos. Nenhuma promessa não confirmada reutilizada. Site não alterado nesta etapa.
- Entrega: PDFs de impressão com sangria3mm/marcas/TrimBox e de visualização A5 sem marcas; prévia PNG, fonte Python e especificações. Ver output/panfleto/LEIA-ME.md.
- Aceite: logo vetorial oficial, Manrope incorporada, texto real, A5final148×210mm, contato/serviços corretos, QR vetorial direto WhatsApp e decodificado no PDF a300dpi, revisão visual sem cortes ou sobreposições.

### Correções verificadas na integração

- ID de contato duplicado eliminado; todos IDs/âncoras/assets conferidos.
- Hero recortado com profissional/ferramenta visíveis fora das sobreposições em desktop/mobile.
- Header e footer extraídos para fragmentos globais; main inclui H1/hero; skip link correto.
- Topbar mobile simplificada e links sobre gelo em petróleo (14,44:1); menor contraste textual medido na página4,88:1.
- Trap explícito nos três diálogos; callback assíncrono de fechamento não rouba foco da FAQ nem apaga foto reaberta. Regressões determinísticas e três execuções completas da suíte passaram.
- Capturas de elementos altos tratam artefato de composição do Chromium escondendo apenas o skip link sem foco durante a captura; produto permanece inalterado, skip testado por teclado.
- Build limpa exclusivamente `dist/` após verificar caminho absoluto dentro do projeto; masters e arquivos de auditoria não entram na saída.

### Evidências

`output/site-validation/results.json`, `accessibility.json`, `contrast.json`, `a11y-run-1.log` a `3.log`, `touch.json`, `final-review-results.json`; capturas completas `full-1440.png`/`full-390.png`, todas as sete larguras e recortes por seção. Revisor independente concedeu aceite após re-review focado. Sem publicação, commits ou envio externo.
