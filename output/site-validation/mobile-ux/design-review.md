# Fast Limp — avaliação independente de composição e UX mobile

Método: Assessment A independente, somente leitura, em 16/10/2026. Inspeção visual das capturas por seção e navegação em contexto Chrome próprio, em `http://127.0.0.1:4173/`, com viewport 390 × 844, toque e movimento reduzido. Menu, avanço até o quinto serviço, abertura/fechamento da galeria e troca de pergunta do FAQ foram exercitados. Não houve detector, análise de outros agentes, edição da UI ou publicação. Isto é avaliação heurística profissional, não pesquisa com usuários.

## Parecer

A página está visualmente coesa, legível e reconhecível como uma empresa de limpeza de vidros. A base mobile é boa. O principal espaço de melhoria está na facilidade de encontrar a opção desejada e agir durante a rolagem, não em trocar a identidade ou redesenhar o hero aprovado.

A especificidade é **boa na identidade e moderada no argumento comercial**. Logo oficial, Manrope, azul/petróleo, fotografias grandes de vidro e ferramentas, colagem e sobreposições formam um conjunto consistente. A sequência de blocos institucionais ainda poderia pertencer a outra empresa do setor: “Sobre”, “Por que Fast Limp” e seus textos repetem principalmente casa/empresa e os tipos de serviço. Isso não é um defeito de funcionamento; é uma oportunidade editorial dependente de informações comerciais confirmadas.

## O que funciona

1. **Entrada clara e comercial.** O hero aprovado mantém a pessoa/fotografia em cima e texto azul embaixo. Em 390 px, o título informa a proposta em três linhas, a localização aparece antes dele e o botão tem largura do conteúdo. A ação de orçamento cabe no primeiro viewport de 844 px. Não há motivo observado para reabrir essa composição.
2. **Unidade visual com mudança de ritmo.** Branco, gelo e petróleo marcam capítulos sem excesso de efeitos. A galeria preserva variedade de proporções no celular; o processo escuro cria um capítulo reconhecível; títulos de 28 px e margens laterais de 20 px sustentam a leitura. Não foi observado transbordamento horizontal da página em 390 px.
3. **Contratação simples e contextual.** Os cinco cards têm nomes comuns, descrição curta e orçamento específico. Os destinos WhatsApp incluem o serviço e solicitam o bairro, sem exigir formulário. A galeria tem fechamento visível; o FAQ mostra estados claros e responde a acesso, resíduos, região, preço e preparo do ambiente.

## Problemas prioritários

### 1. P2 — Os cinco serviços existem, mas o conjunto não fica evidente

**Evidência:** em 390 px, há um card de 301 px e apenas um fragmento do seguinte. O primeiro quadro mostra “Vidros residenciais”; “Vitrines” só aparece após quatro avanços. Há setas de 44 px e um fragmento lateral, bons sinais de navegação, mas não existe total, posição ou lista dos cinco nomes junto ao ponto de escolha. No último card, a seta de avanço desabilita corretamente.

**Impacto provável:** quem chega procurando pós-obra ou vitrines precisa explorar para descobrir que sua categoria está disponível. Não é um problema de excesso de cinco opções; é baixa visibilidade do catálogo. A pessoa consegue concluir o caminho, portanto não considero bloqueio nem P1 sem evidência de usuários.

**Recomendação 1:** preservar o carrossel e acrescentar uma visão compacta dos cinco nomes, ou um índice de serviços que leve ao card correspondente. Informar também a posição (“1 de 5”). A prioridade é tornar o catálogo reconhecível antes de exigir quatro gestos; não criar mais decoração.

**Referência visual:** `../commercial/servicos-390.png`. Comportamento confirmado no browser próprio.

### 2. P2 — A seção que ensina a pedir orçamento não oferece a ação naquele ponto

**Evidência:** a galeria ocupa aproximadamente 978 px e “Como funciona”, 1.103 px. O processo diz “Abra uma conversa ... pelo botão de orçamento”, mas nenhum botão de orçamento está dentro da seção. O próximo WhatsApp direto aparece em “Por que Fast Limp”, depois do título, texto e lista. O link geral sob serviços, “Fale sobre o seu espaço”, pula para `#contato`; os outros convites semelhantes abrem WhatsApp diretamente. O header não acompanha a rolagem, de acordo com o comportamento vigente.

**Impacto provável:** no ponto em que a pessoa entende os quatro passos e decide agir, precisa continuar rolando ou voltar a um convite anterior. O salto para o rodapé também acrescenta um passo ao caminho geral de serviços. A ausência de botão fixo não é, isoladamente, um defeito; a questão é ter uma ação próxima à explicação.

**Recomendação 2:** incluir um orçamento direto ao terminar os quatro passos e alinhar o destino do convite geral de serviços ao seu texto. Isso resolve a continuidade sem exigir header fixo ou alterar o hero.

**Referências visuais:** `../commercial/como-funciona-390.png`, `../commercial/diferenciais-390.png`. Destinos conferidos na página atual; nenhuma conversa foi enviada.

### 3. P2 — FAQ e rodapé priorizam blocos de apoio antes da informação procurada

**Evidência:** o FAQ coloca o card “Ainda tem uma dúvida?” antes das perguntas. O primeiro acordeão só começa aproximadamente 519 px depois do início da seção. O visitante recebe o convite de ajuda antes de poder examinar as respostas. No rodapé de aproximadamente 1.484 px, o telefone e o bloco “Fale com a Fast Limp” aparecem depois de “Explore” e dos cinco serviços. O CTA inicial do rodapé compensa parte desse problema, mas o dado de contato fica quase no fim. O número exibido é também um link de WhatsApp.

**Impacto provável:** a busca por uma resposta exige atravessar um convite redundante; a busca pelo número exige passar novamente por catálogos já vistos. Os elementos são legíveis e operáveis: trata-se de ordem de informação e eficiência de consulta, não de acessibilidade comprovadamente quebrada.

**Recomendação 3:** no mobile, colocar as perguntas antes do card de ajuda e aproximar telefone/região/WhatsApp do CTA inicial do rodapé. Deixar navegação e repetição do catálogo depois desse conjunto. Se o número continuar abrindo WhatsApp, identificar esse destino junto dele para reduzir ambiguidade.

**Referências visuais:** `../commercial/duvidas-390.png`, `../commercial/contato-390.png`; ordem confirmada no browser.

## Ritmo da página inteira e composição da prévia

O fluxo medido em 390 px foi: hero 726 px → Sobre 977 px → Serviços 878 px → Galeria 978 px → Processo 1.103 px → Diferenciais 956 px → Depoimento 477 px → Equipe 1.869 px → FAQ 1.385 px → Rodapé 1.484 px. A altura total é aproximadamente 10.832 px, ou 12,8 viewports de 844 px. Esses números descrevem densidade e distância, não comprovam cansaço ou abandono.

O começo tem sequência convincente: serviço percebido na imagem, proposta, contexto e escolha. O meio é o trecho mais lento, pela sucessão galeria/processo/foto grande e repetição das mesmas cenas e categorias. A repetição do profissional de macacão laranja na galeria, processo, diferenciais e equipe deixa a experiência mais previsível. É preferência editorial de composição, não falha funcional; variar os enquadramentos poderia ajudar, mas não está entre as três intervenções prioritárias.

A **equipe funciona como apresentação individual**: nomes visíveis, fotografia grande, cartão central azul como contraste e nenhuma dependência de hover. Em contrapartida, três retratos verticais empilhados ocupam mais de dois viewports e adiam o FAQ. Isso é observação da prévia, não problema atribuído ao site público: equipe e depoimento são módulos temporários e o build público os exclui. A exclusão de suas alturas remove aproximadamente 2.346 px, antes de diferenças de fluxo/âncoras; não atribuo ao público o trecho de rolagem da equipe. Não foi avaliada a veracidade desses dados temporários, por orientação do usuário.

A galeria é um ponto forte de composição, mas sua função é referência visual; ela não ajuda diretamente a comparar o escopo dos cinco serviços. O FAQ é a parte mais útil para reduzir incerteza comercial e merece ser mais rápido de alcançar e escanear. O final oferece uma chamada clara e mantém unidade de marca, embora a ordem das colunas possa atender melhor à tarefa de contato.

## Heurísticas de Nielsen — 0 a 4, maior é melhor

As notas se restringem aos estados observados e não equivalem a uma certificação de acessibilidade ou teste empírico.

| Heurística | Nota | Fundamentação |
|---|---:|---|
| 1. Visibilidade de estado | 3 | Menu, FAQ e limite do carrossel têm estado; falta posição/total dos serviços. |
| 2. Correspondência com o mundo real | 4 | Linguagem simples: bairro, fotos, medidas, acesso, orçamento e agenda. |
| 3. Controle e liberdade | 3 | Menu abre/fecha, galeria fecha, FAQ troca de pergunta e carrossel tem controles; revisão não cobriu todas as combinações de teclado/gesto. |
| 4. Consistência e padrões | 3 | Sistema visual coeso; convites semelhantes alternam WhatsApp direto e salto ao rodapé. |
| 5. Prevenção de erros | 3 | Mensagem contextualiza o serviço; acesso/altura e resíduos dependem de avaliação; nenhum envio automático foi feito. |
| 6. Reconhecimento em vez de memorização | 2 | Cards legíveis, mas o catálogo completo exige exploração e lembrança dos cards anteriores. |
| 7. Flexibilidade e eficiência de uso | n/a | Aceleradores, operações em lote e personalização não são exigências desta landing page. |
| 8. Estética e minimalismo | 3 | Identidade consistente e hierarquia clara; repetição de capítulos/fotos e distância entre informação e ação pesam no meio. |
| 9. Reconhecer, diagnosticar e recuperar erros | n/a | Não há formulário/transação interna ou estado de erro observado; abertura externa do WhatsApp não foi testada até o envio. |
| 10. Ajuda e documentação | 3 | FAQ cobre dúvidas concretas; o card de suporte precede o conteúdo que deveria complementar. |
| **Total aplicável** | **27/32** | **84% — boa base, com ajustes locais de descoberta, continuidade e ordem.** |

## Limitações e distinções

- Browser próprio em 390 × 844; avaliação visual adicional das capturas fornecidas. Não houve aparelho físico, VoiceOver/NVDA, rede lenta, análise de métricas ou entrevistas. As capturas comerciais foram usadas por seção; para o hero vale a versão banner atual aprovada e confirmada no DOM atual.
- A confirmação de cinco serviços e dos estados de menu/galeria/FAQ é observação direta. Impactos sobre descoberta/atenção são inferências heurísticas, não taxas medidas de abandono.
- Não foi executado o detector Impeccable, conforme escopo explícito desta avaliação independente. Não é uma execução completa do fluxo de critique com Assessment B, nem afirma equivalência a ele.
- Nenhuma skill, plugin, ferramenta, tutorial ou curso está sendo recomendado ou criado. Nenhum pacote foi instalado.
- Perguntas finais dispensadas: este relatório é uma avaliação independente delegada, para síntese pelo agente principal. As três recomendações são propostas de ajuste; nenhuma foi implementada.
