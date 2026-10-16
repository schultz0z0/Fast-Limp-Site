# Prompts para o site da Fast Limp — Limpeza de Vidros

Versão 2.0 · 15 de outubro de 2026 · Brandbook validado + novo design system + referências desktop.

Este é o roteiro de implementação futura do site. Ele deve ser usado junto com `DESIGN.md`, `design-system.json`, o brandbook aprovado e as duas capturas de referência. A versão anterior, com outra estrutura de página e logo ainda provisória, foi preservada em `docs/historico/prompts-site-fast-limp-v1-anterior-ao-design-system.md` apenas como histórico.

## 1. Leitura obrigatória e fonte de cada decisão

Antes de implementar, ler nesta ordem:

1. Instruções do projeto e solicitação mais recente do cliente.
2. `output/pdf/fast-limp-brandbook-v1-validacao.pdf` — brandbook aprovado em 15/10/2026; consultar também `marca/brandbook-v1/diretrizes/aprovacao-brandbook.md` e `marca/brandbook-v1/diretrizes/manual-identidade.md`.
3. `DESIGN.md` — composição, UI/UX, regras de uso e adaptação responsiva.
4. `design-system.json` — tokens, medidas, componentes, estados, fontes de assets e sequência canônica de seções.
5. `referencias/site-modelo-completo.png` e `referencias/site-modelo-detalhes.png`, ou os mesmos arquivos anexados à conversa. A primeira é a página completa; a segunda é uma montagem de detalhes desktop, não uma referência mobile.
6. Este arquivo e a ficha de conteúdo abaixo.

O brandbook governa identidade. As imagens governam a arquitetura visual; não fornecem fatos da Fast Limp. O Markdown e o JSON traduzem a combinação em regras executáveis. Instruções antigas que pedem monograma, escolha livre de fonte, duas imagens na galeria ou outra ordem de seções foram substituídas.

Não reabrir a escolha da logo ou da paleta já aprovadas. Não usar o nome “para validação” do arquivo PDF como motivo para pedir nova aprovação do brandbook.

## 2. Contrato de execução para todas as etapas

```text
Atue como desenvolvedor front-end sênior, com atenção à reprodução fiel de interfaces, responsividade e acessibilidade.

Use obrigatoriamente prompts-site-fast-limp.md, DESIGN.md, design-system.json, o brandbook aprovado da Fast Limp e as duas imagens de referência.

Inspecione os arquivos antes de editar. Preserve a stack, os padrões e o trabalho existente. Sem projeto de site, use HTML semântico, CSS e JavaScript modular adequados a uma página institucional estática; não imponha framework, backend ou CMS.

Implemente a etapa solicitada nos arquivos, em vez de entregar apenas explicações. Preserve as dobras já aprovadas. Organize estilos e comportamentos por seção. A imagem de referência não pode ser usada como uma página achatada: textos, cards, links, botões e controles devem ser elementos reais.

Mantenha a composição do template: hero com painel assimétrico sobreposto e conversão adjacente; Sobre em colagem; carrossel de serviços; bento; processo escuro; diferenciais com badge; depoimentos; equipe; FAQ; blog; CTA e rodapé único.

Troque a identidade visual e o tema do modelo pelos da Fast Limp. Não importar roxo/lilás, piscinas, Cleanx, copy em inglês, dados comerciais ou estatísticas da referência. Não redesenhar a interface como um site genérico de limpeza.

Use apenas a logo oficial com vidro e rodo e o lettering aprovados. Use Manrope 400/600/700 e os tokens do JSON. A assinatura com descritor não pode ser diminuída abaixo de 320 px; no header, usar a versão compacta oficial em 208 px desktop e 156 px mobile.

Não invente telefone, região, serviços específicos, preços, promoções, anos de atuação, clientes, nota, avaliações, equipe, certificações ou garantias. Distinga revisão local de produção conforme a política de conteúdo. Registre pendências e avance no que for independente delas.

Não gerar uma nova marca. Não iniciar uma exploração de estilos ou novas opções de layout: a referência e a identidade já foram escolhidas. Não publicar automaticamente.
```

### Cores, fonte e composição

- Fonte definida: **Manrope**, arquivos locais em `marca/brandbook-v1/fontes/` e licença OFL incluída.
- Cores mestras: azul `#1C94F0`, petróleo `#092131` e branco `#FFFFFF`. Apoios e papéis estão no JSON; não criar outro azul de texto avulso.
- Azul principal com texto petróleo para botões e painéis de texto normal. Branco sobre azul principal não é padrão de texto pequeno. Links em fundo branco usam azul médio `#1274C2`.
- Container principal máximo de 1200 px; header largo máximo de 1320 px. Gutters: 20 px mobile, 32 px tablet, 40 px desktop; ver breakpoints no JSON.
- Sobreposições e diagonais são intencionais. Não achatá-las por uma regra genérica contra margens negativas; também não usar deslocamentos arbitrários para esconder erros.
- Cores, tamanhos e estados vêm dos tokens. O layout específico de cada seção vem de `DESIGN.md`, seção 6, e de `sections` no JSON.

## 3. Ficha de conteúdo e pendências

Os campos `[[CAMPO]]` são dados internos a preencher, não textos a publicar literalmente. No modo de revisão local, usar indicações legíveis de conteúdo pendente; não fabricar valores para preencher a composição.

| Campo | Estado / orientação |
|---|---|
| `[[MARCA]]` | Fast Limp — confirmado. |
| `[[SEGMENTO]]` | Limpeza de vidros para residências e empresas — confirmado. |
| `[[FONTE]]` | Manrope 400/600/700 — definida pelo brandbook. |
| `[[SIMBOLO_MARCA]]` | Vidro e rodo, arquivos oficiais de `marca/brandbook-v1/svg/`. |
| `[[CIDADE]]`, `[[UF]]`, `[[REGIAO]]` | Pendente de confirmação. Não copiar localização da referência. |
| `[[TELEFONE_EXIBICAO]]`, `[[WHATSAPP_URL]]` | Número e destino reais; não inferir DDD ou usar número de demonstração. |
| `[[INSTAGRAM_URL]]`, `[[INSTAGRAM_USUARIO]]` | Perfil real, se fornecido. |
| `[[FACEBOOK_URL]]`, outras redes | Usar apenas canais existentes. |
| `[[DOMINIO]]`, `[[PRIVACIDADE_URL]]` | Confirmar antes da publicação; privacidade requer página real. |
| `[[SOBRE_DESTINO]]` | Âncora interna ou página real; não inventar link institucional. |
| `[[HERO_EYEBROW]]` | Proposta: “LIMPEZA DE VIDROS”. |
| `[[HERO_TITULO]]` | Proposta: “Vidros limpos. Uma nova impressão do seu espaço.” |
| `[[HERO_DESCRICAO]]` | Proposta: “Limpeza de vidros para residências e empresas, com atenção aos detalhes e à apresentação de cada ambiente.” |
| `[[CONVERSAO_TITULO]]` | Proposta: “Cuidado para o seu espaço”. |
| `[[CONVERSAO_RESIDENCIAL]]`, `[[CONVERSAO_COMERCIAL]]` | Textos curtos dos dois públicos, sem inventar planos ou preços. |
| `[[SOBRE_TEXTO]]`, `[[MARCA_DESCRICAO]]` | Texto factual ou apresentação neutra, coerente com o brandbook. |
| `[[SERVICOS]]` | Catálogo real; quatro cards são alvo visual, não confirmação de oferta. |
| `[[BENEFICIOS_SOBRE]]` | Dois itens reais ou textos neutros sobre a proposta da marca. |
| `[[DIFERENCIAIS]]` | Até quatro itens confirmados. Não apresentar intenção como certificação. |
| `[[PROCESSO_ETAPAS]]` | Fluxo de atendimento a confirmar; quatro etapas são alvo de composição. |
| `[[VIDEO_URL]]`, `[[VIDEO_LEGENDAS]]` | Somente se houver vídeo real e autorizado. |
| `[[DEPOIMENTOS]]`, `[[FONTE_AVALIACOES]]` | Texto, nome, autorização e fonte verificável; pendentes. |
| `[[EQUIPE]]` | Nomes, funções, fotografias reais e autorização; pendentes. |
| `[[FAQ]]` | Perguntas e respostas revisadas com fatos da operação. |
| `[[ARTIGOS]]` | Conteúdo existente/revisado, metadados e destinos reais; pendentes. |

Limpeza residencial, vitrines/fachadas, pós-obra e manutenção periódica eram sugestões do briefing anterior. Só podem virar catálogo publicado quando confirmadas. Não sugerir acesso por cordas ou trabalho em altura sem confirmação explícita.

### Dois modos de conteúdo

**Revisão local:** preservar os slots e a densidade visual das seções. Depoimentos, equipe e artigos sem material ficam identificados como conteúdo pendente; não usar pessoas ou afirmações fictícias. Sem WhatsApp confirmado, um CTA pode abrir painel local explicativo de contato pendente ou levar a uma área real de contato pendente; não criar `href="#"` ou um WhatsApp inventado.

**Produção:** somente dados confirmados e destinos reais. Não publicar placeholders. Módulos que dependem de prova ficam retidos até receber conteúdo; manter a implementação e registrar as retenções em vez de apagar silenciosamente seções do modelo. Essa regra também vale para a prova social do hero, números do badge, vídeo e newsletter.

## 4. Assets obrigatórios

### Marca — reutilizar os arquivos existentes

| Aplicação | Fonte |
|---|---|
| Header | `marca/brandbook-v1/svg/fast-limp-compacta-principal.svg` |
| Assinatura completa clara | `marca/brandbook-v1/svg/fast-limp-horizontal-principal.svg` |
| Assinatura completa escura | `marca/brandbook-v1/svg/fast-limp-horizontal-negativa.svg` |
| Rodapé compacto | `marca/brandbook-v1/svg/fast-limp-compacta-negativa.svg` |
| Símbolo e micro | `marca/brandbook-v1/svg/fast-limp-simbolo-principal.svg` e `fast-limp-simbolo-micro-principal.svg` |
| Favicon | `marca/brandbook-v1/digital/favicon.ico` |
| Fonte | `marca/brandbook-v1/fontes/Manrope-Variable.ttf` ou arquivos estáticos listados no JSON. |

Na implementação, copiar derivados necessários para a pasta pública do projeto, preservando os arquivos de origem. Não remover fundo, recolorir ou gerar uma logo novamente: as variações já existem.

### Fotografias e conteúdo de mídia — inventariar antes de construir

| Asset lógico | Quantidade / proporção | Função |
|---|---|---|
| `hero` | Foto ampla + corte mobile revisado | Profissional e vidro, sem interface incorporada. |
| `sobre-01..03` | Três enquadramentos complementares | Ambiente, profissional e detalhe para colagem. |
| `servico-01..04` | Até quatro fotos 4:3 | Catálogo confirmado. |
| `galeria-01..06` | Vertical, quadradas e horizontais | Bento conforme as áreas definidas no JSON. |
| `processo-poster` | 16:9 | Vídeo real ou imagem estática de referência. |
| `diferenciais` | 4:3 | Foto com área adequada ao badge inferior. |
| `equipe-01..03` | Retratos 3:4 reais | Apenas equipe real; não gerar identidades. |
| `artigo-01..03` | Três fotos 3:2 | Conteúdo editorial real e revisado. |

Preservar originais. Gerar derivados WebP/AVIF e `srcset` na implementação, com largura/altura intrínsecas e corte individual. Não usar a mesma imagem repetida para simular seis resultados. Fotos ilustrativas não representam trabalhos executados.

## 5. Etapas de implementação

Cada etapa herda integralmente o contrato da seção 2. Rodar uma etapa por vez; a próxima só começa quando solicitada ou aprovada. Quando o prompt de início for utilizado, fazer **00 e 01 no mesmo turno**, sem implementar as demais seções.

### 00 — Contexto, inventário e preparação

```text
Leia todas as fontes obrigatórias deste roteiro, incluindo o PDF do brandbook e as duas imagens. Inspecione a stack e os arquivos existentes.

Registre brevemente: fontes lidas; identidade vigente; sequência das seções; assets disponíveis; lacunas de conteúdo; modo local de revisão; comandos de desenvolvimento/verificação que realmente existirem.

Reconheça que a print1 é a página inteira e a print2 é uma montagem desktop. Preserve o desenho do modelo, mas adapte tudo para Fast Limp e limpeza de vidros. Não copiar a moldura externa de água do demonstrativo.

Use as regras existentes para resolver escolhas técnicas rotineiras. Não interrompa só porque cidade, telefone, avaliações ou retratos ainda estão ausentes: isole essas dependências e avance na etapa 01 em modo de revisão local. Não invente dados.
```

### 01 — Base, topbar, header, hero e painel de conversão

```text
Execute somente a etapa 01 depois da preparação 00.

Crie a base semântica, carregue Manrope local e os assets oficiais, e traduza os tokens de design-system.json para variáveis CSS. Garanta lang="pt-BR", link para pular ao conteúdo e uma única H1.

Implemente o grupo #inicio conforme DESIGN.md, seção6.01, e sections[0] do JSON:
- topbar azul de contato/redes reais ou simplificada quando pendente;
- header branco flutuante sobre fotografia, logo compacta oficial, links centrais e ação de orçamento;
- hero fotográfico amplo com borda inferior diagonal;
- card azul de texto sobreposto à parte inferior esquerda, com topo diagonal e texto petróleo;
- painel de conversão adjacente, cabeçalho integral e duas colunas Residências/Empresas, alinhado à base do card principal;
- CTA claro/petróleo no card azul; nenhum preço, promoção, nota ou avatar fictício.

Não substituir por hero de texto branco sobre foto escurecida. Não acrescentar faixa de confiança independente. Não construir o Sobre nem as demais seções ainda.

No mobile, usar fluxo de foto→card→conversão, sobreposição reduzida e conteúdo sem posição absoluta. Revisar foco, recorte do profissional, altura livre do card e quebras do título. O menu compacto precisa abrir/fechar por toque e teclado, com estado acessível.

Se uma seção de destino ainda não existir, a navegação correspondente pode aparecer como texto sem ação na revisão local; conectar quando a seção for criada. Não criar links mortos nem seções vazias só para simular destinos. CTA sem contato real abre a indicação local de pendência, sem fabricar WhatsApp.

Abra a página no navegador disponível e confira 1440 px e 390 px; faça smoke check em 320 px e 768 px. Não declare conferência visual sem ter aberto/renderizado a página. Se uma ferramenta estiver indisponível, informe a limitação concreta.

Entregue arquivos alterados, como abrir, capturas quando disponíveis, verificações e pendências. Pare para revisão da etapa 01.
```

### 02 — Sobre em colagem e carrossel de serviços

```text
Continue a Fast Limp implementando somente a etapa 02, preservando a etapa 01 aprovada.

Siga DESIGN.md, seções 6.02–6.03 e os IDs #sobre e #servicos do JSON. A ordem é Sobre antes de Serviços.

Sobre: três fotos deslocadas em colagem à esquerda, e eyebrow, título, texto, dois benefícios e CTA à direita. No celular, colagem acima e deslocamentos reduzidos. Não simplificar para uma única foto 50/50.

Serviços: seção gelo, título à esquerda e setas circulares à direita. Cards fotográficos 4:3 com texto abaixo, faixa horizontal com três completos e parte do seguinte no desktop. Mobile mostra um card e parte do próximo, com scroll-snap e controles acessíveis. Sem autoplay. Não substituir por grade fixa de quatro cards.

Usar apenas catálogo confirmado; itens de revisão pendentes precisam estar identificados. Mensagens de WhatsApp referentes ao serviço só usam destino real. Testar setas, fim da faixa, toque, teclado e recortes.

Conferir 1440 px e 390 px e que o hero não mudou. Entregar verificações e parar para revisão.
```

### 03 — Galeria bento e processo/mídia

```text
Implemente somente a etapa 03, preservando as anteriores.

Siga DESIGN.md, seções 6.04–6.05 e #referencias e #como-funciona no JSON.

Galeria: cabeçalho centralizado e seis áreas assimétricas, com imagem vertical alta à esquerda, duas menores ao centro, uma horizontal em cima à direita e duas menores abaixo. Usar as áreas e trilhas definidas no JSON. Não criar uma galeria de apenas duas imagens. Diferenciar portfólio real de referência ilustrativa.

Abrir fotografia em visualizador acessível com legenda, fechamento, Escape e retorno de foco.

Processo: seção petróleo com título centralizado, quatro marcadores conectados e quatro cards claros. Abaixo, quadro de mídia 16:9. Etapas precisam ser confirmadas ou identificadas como proposta durante revisão. Sem vídeo real, usar foto estática com legenda; nenhum play sem ação.

No celular, reorganizar bento e transformar a sequência do processo em lista vertical. Testar contraste, navegação e mídia. Conferir 1440 px e 390 px, entregar verificações e parar para revisão.
```

### 04 — Diferenciais, depoimentos e equipe

```text
Implemente somente a etapa 04 conforme DESIGN.md, seções 6.06–6.08 e IDs #diferenciais, #depoimentos e #equipe.

Diferenciais: texto e quatro itens à esquerda, foto 4:3 à direita e badge azul sobre a base. Usar fatos confirmados ou frase neutra; nunca copiar “10+ anos” do modelo.

Depoimentos: faixa gelo, citação central, identificação e controles laterais. Só usar depoimentos autorizados, notas e fonte verificadas. Sem esse material, preservar um painel de revisão claramente pendente; não inventar clientes ou estrelas.

Equipe: três retratos 3:4 com identificações sobrepostas, título à esquerda e ação à direita. Usar apenas pessoas, funções, redes e fotos reais. Na ausência, manter slots de revisão explícitos; não gerar funcionários fictícios. Não ocultar informações exclusivamente em hover.

Aplicar a política produção/revisão dos documentos, sem remover silenciosamente os módulos. Conferir carrosséis, toque, teclado e mobile. Entregar verificações e parar para revisão.
```

### 05 — FAQ, conteúdo editorial, CTA e rodapé

```text
Implemente somente a etapa 05 conforme DESIGN.md, seções 6.09–6.11 e IDs #duvidas, #conteudos e #contato.

FAQ: seção gelo em duas colunas, texto/card de ajuda à esquerda e cerca de seis perguntas à direita. Um item aberto com azul/petróleo; demais claros. Botões e painéis com relação acessível, respostas revisadas e altura flexível.

Editorial: título centralizado e três cards com foto 3:2, metadados e destinos reais. Sem artigos, manter slots identificados na revisão. Não inventar datas, autores, páginas ou links.

CTA e rodapé: um único campo petróleo com chamada e botão, divisor, quatro colunas e base de privacidade. Marca/descrição/redes; navegação; serviços reais; contato/ação. Newsletter só com captação real; por padrão, usar contato/WhatsApp no lugar. Não criar outro rodapé nem uma faixa final azul adicional.

Conectar navegação às seções agora existentes. Usar o ano atual no copyright e destino real de privacidade. No mobile, empilhar CTA e reorganizar as colunas. Conferir 1440 px e 390 px, entregar verificações e parar para revisão.
```

### 06 — Integração e conferência final

```text
Faça a integração da Fast Limp preservando o layout aprovado.

Verifique a página completa contra as duas referências, normalizando a largura para comparar proporções, ritmo, imagens, diagonais, alinhamentos, sobreposições e sequência. As imagens não são uma amostra mobile: avalie a adaptação com os critérios do design system.

Teste 320/360/390/768/1024/1440/1920 px, zoom 200%, teclado, foco, menu, carrosséis, acordeão, galeria, mídia, links e contraste. Corrija overflow pela causa, sem esconder a página horizontalmente.

Conecte apenas contatos reais. Codifique as mensagens de WhatsApp. Remova ou retenha módulos sem conteúdo validado antes de produção, registrando cada retenção e sem publicar placeholders.

Verifique fonte carregada, imagens responsivas, dimensões intrínsecas, carregamento prioritário do hero e lazyload abaixo da dobra. Rode build e verificações apropriadas quando existirem. Procure404, erros de console e controles sem função.

SEO: H1 única, headings em ordem, título e descrição reais, idioma pt-BR, canonical somente com domínio confirmado, descrição social coerente e metadados locais somente com dados reais. Não criar schema de avaliações/endereço fictícios. Política de privacidade precisa de página real antes da publicação.

Entregue arquivos, comandos, capturas, resultados e pendências restantes. Não publique automaticamente.
```

## 6. Mensagens e destinos

Mensagem geral sugerida para um WhatsApp confirmado:

> Olá! Vim pelo site da Fast Limp e gostaria de solicitar um orçamento para limpeza de vidros.

Mensagem de serviço:

> Olá! Vim pelo site da Fast Limp e gostaria de saber mais sobre [serviço confirmado].

Codificar com `encodeURIComponent` ou equivalente. Centralizar telefone, URLs e textos em configuração; não replicar destinos divergentes por seção. Sem contato real, manter o comportamento local de pendência do design system.

## 7. Direção das fotografias e prompts auxiliares

Esta seção orienta uma futura produção de imagens quando solicitada. Não gerar imagens automaticamente ao ler o roteiro. Para trabalhos executados, equipe e antes/depois, usar apenas material real autorizado.

### Briefing comum para fotografia ilustrativa

```text
Crie uma fotografia comercial ilustrativa para Fast Limp, especializada em limpeza de vidros para residências e empresas.

Use luz natural, vidro plausível, reflexos controlados e ferramenta profissional. A composição deve combinar com a interface e o slot definidos em DESIGN.md e design-system.json. Sem texto, interface ou logotipos gerados. Sem piscinas, baldes domésticos, espuma exagerada, HDR artificial ou reflexos impossíveis.

Não representar a cena como serviço real da Fast Limp, resultado executado ou membro da equipe. Não mostrar trabalho em altura/acesso por cordas não confirmado. Preferir vestuário azul/petróleo sem recriar a logo.
```

### Complemento por slot

| Slot | Complemento de composição |
|---|---|
| Hero | Fotografia ampla de limpeza de grande vidro, profissional e ferramenta reconhecíveis no centro/direita; conteúdo não achatado na foto. Prever corte vertical independente para mobile. |
| Sobre | Três cenas complementares: ambiente com vidro, gesto de limpeza e detalhe do rodo. Proporções diferentes para colagem; sem repetir a mesma foto. |
| Serviços | Uma cena por serviço confirmado,4:3, com assunto central e recorte consistente. |
| Bento | Seis enquadramentos coerentes, incluindo uma vertical alta, uma horizontal larga e detalhes. Cada imagem corresponde à sua área, sem duplicações. |
| Processo | 16:9, ferramenta e vidro em ação; apenas foto estática se não existir vídeo real. |
| Diferenciais | 4:3, ambiente/profissional com leitura clara; preservar área inferior para badge da interface, sem gerar esse badge na fotografia. |
| Equipe | Não gerar como equipe. Solicitar posteriormente os retratos reais autorizados quando essa seção for implementada. |
| Conteúdo editorial | 3:2 relacionado ao artigo revisado, sem inventar portfólio ou autoria. |

## 8. Refinamento visual controlado

```text
Compare a implementação atual da Fast Limp com as capturas e os arquivos DESIGN.md/design-system.json.

Antes de editar, identifique diferenças concretas: largura do container, altura do hero, sobreposição do card, proporções do painel de conversão, colagem, trecho visível do próximo serviço, áreas do bento, timeline, badge, cartões sociais, acordeão ou rodapé.

Corrija somente o que causa essas diferenças, preservando a identidade e as dobras já aprovadas. Não faça um redesign global nem acrescente efeitos. Sobreposições intencionais devem ser mantidas; overflow acidental deve ser resolvido pela origem.

Confira novamente desktop e mobile e informe o que mudou, a evidência visual e qualquer diferença ainda dependente de conteúdo real.
```

## 9. Checklist de entrega e publicação

- Brandbook aprovado utilizado e marca correta com vidro/rodo?
- `DESIGN.md` e `design-system.json` consumidos e mantidos coerentes?
- Manrope local 400/600/700 efetivamente carregada?
- Ordem completa e composição dos slots preservadas na revisão?
- Logo compacta correta no header, mínimo e respiro respeitados?
- Hero assimétrico com conversão, Sobre em colagem e galeria bento?
- Estados, teclado, toque e movimento reduzido conferidos?
- Nenhum roxo, tema de piscina, dado ou marca do template importado?
- Contatos, serviços, região, avaliações, equipe, vídeo e artigos confirmados ou retidos?
- Fotografias ilustrativas diferenciadas de portfólio real?
- Sem placeholders públicos, `href="#"`, play falso, formulário sem destino ou sucesso simulado?
- Contraste, reflow e viewports do design system verificados?
- Imagens otimizadas, fonte estável, ausência de 404/erros de console e build conferidos quando aplicável?
- Um único CTA final/rodapé, links conectados e privacidade real?
- Pendências descritas e publicação aguardando solicitação explícita?

## 10. Prompt de início

Copiar o conteúdo de `PROMPT-INICIAR-SITE.md` e anexar novamente as duas capturas. Esse prompt inicia 00+01, usando este roteiro, os dois arquivos do design system e o brandbook. Não é necessário anexar novamente os assets que já estão no projeto, desde que seus caminhos continuem acessíveis.
