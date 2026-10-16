# Fast Limp — implementação das etapas 04 e 05

Responsável: subagente `sections-end`. Data: 15/10/2026. Modo: revisão local.

## Escopo e arquivos

- `site/partials/end.html`: fragmento estático completo, sem outro `main`, com seis módulos consecutivos.
- `site/styles/end.css`: estilos das seis seções, consumindo os tokens compartilhados e a fonte Manrope da base.
- Este relatório registra entrega e pendências. O coordenador controla o quadro de issues.

## FL-04 — Diferenciais, depoimentos e equipe

Implementação disponível para integração e revisão visual:

- `#diferenciais`: duas colunas, quatro itens de proposta da marca, CTA local, foto 4:3 e badge azul sobreposto com a frase neutra “Cuidado nos detalhes”. Diferenciais operacionais identificados como pendentes; imagem explicitamente ilustrativa.
- `#depoimentos`: faixa gelo com título centralizado, painel de até 720 px, controles laterais de 44 px no desktop e inferiores no celular. Sem avaliações, estrelas, citações ou pessoas inventadas. Setas nativamente desabilitadas e justificativa textual associada por `aria-describedby`.
- `#equipe`: três slots gráficos 3:4, com placas sobrepostas e centro em azul/petróleo. Sem retratos humanos, nomes, cargos ou redes fictícias. Em celular, uma coluna; a partir de 640 px, três colunas. Botão “Sobre a equipe” usa o diálogo compartilhado de pendências.

## FL-05 — FAQ, conteúdo e rodapé

Implementação disponível para integração e revisão visual:

- `#duvidas`: split de introdução e apoio à esquerda / acordeão à direita, seis perguntas canônicas; primeira resposta aberta. Cada botão tem ID, `aria-controls` e `aria-expanded`; cada painel tem ID, `role="region"` e `aria-labelledby`. O CSS usa o estado de `aria-expanded` para a superfície azul/petróleo. Respostas distinguem dados confirmados e pendentes.
- `#conteudos`: três slots editoriais com imagens responsivas 3:2, identificação de prévia e conteúdo pendente. Sem datas, autoria, artigos publicados ou links falsos. Botões explicam a pendência via hook compartilhado. Fotografia ilustrativa declarada na seção.
- `#contato`: um único `footer` petróleo reúne CTA superior, divisor, quatro colunas e base legal. Logo compacta negativa oficial; navegação com destinos internos reais. Contatos ausentes acionam o diálogo local. Privacidade usa diálogo explicativo em vez de destino fictício. Ano via `[data-year]`. Colunas reduzem a duas e uma no mobile.

## Contratos de integração

- `button[data-contact]`, com `data-context` quando útil, abre `#contact-dialog`.
- `button[data-pending]`, `data-pending-title` e `data-pending-message` preenchem `#pending-dialog`.
- `[data-accordion]` exige que o script atualize `aria-expanded` e `hidden`, mantendo uma resposta aberta por vez.
- Botões de depoimento continuam desabilitados enquanto não houver registros autorizados. Sem autoplay.
- Foco visível, cores de botões, Manrope, gutters e movimento reduzido são herdados da base comum.

## Auto-revisão estática executada

- Ordem confirmada: `diferenciais`, `depoimentos`, `equipe`, `duvidas`, `conteudos`, `contato`.
- Zero IDs duplicados na composição de `index.html` e fragmentos; durante a revisão, o título do rodapé foi renomeado para `footer-contact-title` para evitar colisão com o diálogo de contato.
- Seis controles de FAQ; primeiro `aria-expanded="true"` e primeiro painel visível.
- Um único `footer` na composição.
- Todos os tokens CSS usados em `end.css` existem em `tokens.css`; zero tokens indefinidos.
- Todas as referências locais de `src`/`srcset` do fragmento existem, incluindo os três tamanhos de cada fotografia e a logo oficial negativa.
- CSS com delimitadores balanceados (151 pares).
- Sem contatos, preços, avaliações, funcionários, certificações, métricas ou resultados reais inventados.

## Verificação integrada e pendências

O coordenador executará build, teste de hooks, revisão final independente e capturas em 1440/390, além das larguras de 320, 360, 768, 1024 e 1920 px. Estes testes não são declarados concluídos por este relatório antes de sua execução.

Dependências comerciais remanescentes: catálogo e diferenciais operacionais, canais de orçamento, cobertura e agenda, procedimentos, relatos autorizados, nomes/funções/fotos e consentimento da equipe, textos editoriais revisados com destinos reais, redes e política de privacidade. Essas pendências não bloqueiam a composição e os comportamentos locais; os módulos permanecem explicitamente em revisão e o site não é publicado automaticamente.

## Correções delegadas após revisão integrada

O coordenador delegou exclusivamente `site/styles/base.css` a este agente para as seguintes correções de FL-06:

- Links de conversão e `.surface-alt .text-link` passaram a consumir `--semantic-color-text` (petróleo) sobre gelo. Azul médio foi preservado nos demais links sobre branco. A combinação anterior azul médio/gelo havia medido 4,27:1 na revisão do coordenador.
- A faixa utilitária omite o link secundário de prévia abaixo de 768 px, preservando a frase de apresentação.
- Botões de conversão usam fonte de 13 px, padding horizontal zero e `text-wrap: balance`, evitando seta sozinha quando há quebra. O padding horizontal dos cards foi reduzido para 12 px no celular; os alvos continuam com 44 px de altura mínima.
- Posição do header não foi alterada; a correção correspondente pertence ao coordenador em stylesheet separado.

Build e nova captura devem ser executados pelo coordenador após integrar estas correções, evitando builds concorrentes.

## Encerramento integrado
Capturas1440/390, sete larguras, FAQ por teclado, painéis locais, rodapé global e contrastes verificados pelo coordenador. Revisão independente final aceita; ver ENTREGA.md e REVISAO-FINAL.md. Pendências restantes são exclusivamente conteúdo comercial e os limites de validação declarados.
