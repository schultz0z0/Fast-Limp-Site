# Fast Limp — entrega local concluída

**Atualização16/10/2026:** telefone, região e serviços foram confirmados; blog removido; contato agora é WhatsApp direto. Relatório atual em [ATUALIZACAO-COMERCIAL.md](ATUALIZACAO-COMERCIAL.md). O conteúdo abaixo documenta a entrega original e suas pendências daquela data; não deve ser usado como inventário comercial atual.

15 de outubro de 2026. Etapas00–06 concluídas. Sem publicação. Implementação e revisão delegadas a quatro subagentes, com propriedade de arquivos separada e coordenação no quadro `ISSUES.md`.

## Abrir e manter

`npm run dev`, depois http://127.0.0.1:4173. Instruções completas em `../README.md`. O servidor inicia somente em loopback. Fontes em `site/`, saída gerada em `dist/`. Após edição, `npm run build` e recarregar. O app não depende de CDN ou conexão externa para fonte, fotos, marca ou interações.

## Resultado

Onze áreas implementadas em ordem: hero/conversão, Sobre em colagem, serviços em carrossel, referências bento, processo/mídia, diferenciais, depoimentos, equipe, FAQ, editorial e contato/rodapé único. Logos oficiais em contornos, Manrope local,183 tokens resolvidos do JSON,60 WebP com procedência e originais preservados. Sem stack anterior de aplicação, foi seguida a solução HTML/CSS/JS prevista nos documentos.

## Verificações finais

| Verificação | Resultado / evidência |
|---|---|
| Build, sintaxe e integridade | Passaram;11 áreas, IDs únicos, âncoras válidas e62 referências de assets locais verificadas |
|320/360/390/768/1024/1440/1920px | Todas sem overflow horizontal, imagens quebradas ou falha de fonte; results.json |
|1440 e390px, página inteira | Capturas full-1440/full-390 e recortes de todas seções abertos e revisados |
|Revisão independente |13 larguras na revisão inicial,9 no re-review; RF01–05 encerrados, aceite em REVISAO-FINAL.md |
|Menu e navegação |Clique, teclado, toque emulado, Escape, fechamento e foco no destino passaram |
|Carrossel de serviços |Setas, limites desabilitados, Home/End, teclado, scroll-snap e swipe emulado234px passaram; sem autoplay |
|Galeria e diálogos |6 fotos; legendas; Tab/Shift+Tab; Escape; restauração; regressões de fechamento/reabertura passaram |
|FAQ |6 perguntas por teclado; expansão exclusiva e recolhimento passaram |
|Contato e conteúdo pendente |15 CTAs desktop +5 controles de conteúdo abrem painéis reais locais; contato mobile também verificado por toque |
|Contraste textual |191 trechos medidos sobre superfícies sólidas;0 falhas, mínimo4,88:1; contrast.json |
|Foco, redução de movimento, reflow |Contorno2px; skip link; movimento reduzido sem transições; reflow720CSSpx equivalente a200% de1440px e corpo ampliado200% sem overflow |
|Console/rede |0 erros de app/HTTP no QA; nenhuma requisição externa no fluxo touch |
|Estabilidade |A suíte de acessibilidade completa passou3 vezes consecutivas após correção da corrida assíncrona |

Comandos reproduzíveis: `npm run build`, `npm run check`, `npm test`, `node scripts/a11y.mjs`, `node scripts/qa.mjs`. Os testes de navegador usam Playwright já disponível no runtime local, sem instalar dependências no projeto. Resultados em `../output/site-validation/`.

## Capturas

- [Página inteira1440px](../output/site-validation/full-1440.png)
- [Página inteira390px](../output/site-validation/full-390.png)
- [Primeira dobra desktop](../output/site-validation/viewport-1440.png)
- [Primeira dobra mobile](../output/site-validation/viewport-390.png)
- [Painel de contato mobile](../output/site-validation/contact-mobile.png)

Também há capturas completas das outras cinco larguras e recortes de cada seção em1440/390px. O artefato de composição do Chromium em screenshots de elementos altos foi tratado somente na captura; o skip link real continua funcionando e foi testado separadamente.

## Conteúdo comercial ainda pendente

Telefone/WhatsApp; cidade/região; redes oficiais; catálogo específico, condições, processo e diferenciais operacionais; fotografias reais autorizadas; depoimentos e fonte; equipe/nome/função/foto/autorização; vídeo/legendas; artigos/autoria/revisão/destinos; domínio e privacidade.

Slots de equipe, depoimentos e artigos estão implementados e identificados. Não há pessoas, avaliações ou resultados fabricados. Catálogo e processo são propostas declaradas. Todas fotografias são ilustrativas de banco. Sem vídeo, poster estático; depoimentos sem conteúdo mantêm controles desabilitados; contato/privacidade abrem informação local, sem coleta ou envio simulado. Essas dependências não impedem a revisão completa do site local, mas precisam ser resolvidas antes de solicitar publicação.

## Limites dos ensaios

Ensaios em Chromium desktop com emulação de viewport e toque. Não houve aparelho físico, leitor de tela, auditoria WCAG certificada ou verificação em todos os motores. O teste de200% registrou reflow equivalente e ampliação de texto; não equivale a inspeção manual de zoom nativo em todos navegadores. A revisão visual conserva composição e identidade, com diferenças deliberadas nos módulos sem dados reais. Nenhuma publicação automática foi realizada.
