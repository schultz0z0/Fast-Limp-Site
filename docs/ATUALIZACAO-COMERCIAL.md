# Fast Limp · conteúdo comercial atualizado

Revisão posterior FL-10: a pedido do cliente, os rótulos visíveis de banco de imagens, demonstração e perfis fictícios foram retirados da prévia local. Galeria e lightbox usam somente descrições das fotografias. Nomes, funções e relato aparecem como na composição final. Os dados continuam sendo exemplos documentados; os marcadores internos e a exclusão dos dois módulos no build público foram preservados. As descrições abaixo registram a rodada anterior à limpeza dos rótulos.

16/10/2026. Solicitação implementada localmente, sem publicação. Este registro substitui as pendências equivalentes dos relatórios de 15/10/2026; os relatórios antigos permanecem como histórico.

## Mudanças

- 21 links diretos para WhatsApp 5521967643628, com texto pré-preenchido geral ou por serviço, funcionando sem JavaScript. Abrir o link não envia a mensagem; o visitante confirma o envio no WhatsApp.
- Cinco serviços confirmados e atendimento inicial no Rio de Janeiro. Escopo, acesso, preço e agenda são alinhados pelo atendimento, sem promessas não confirmadas.
- Fotos existentes preservadas; avisos repetitivos de “ilustrativa” retirados. Galeria descrita como banco de imagens, sem atribuir os registros à Fast Limp.
- Oito FAQs com temas pesquisados em concorrentes. Fontes e limites em `FAQ-PESQUISA.md`.
- Blog/artigos excluídos. Sem links para matérias inexistentes ou redes sociais não fornecidas.
- Um depoimento fictício e três perfis fictícios com nomes/fotos para visualizar o layout, explicitamente identificados na prévia. As fotos dos perfis reutilizam três masters de banco já licenciados; não há alteração de uniforme ou logotipo.
- Build separado para publicação: `npm run build:production` gera `dist-production/`, sem depoimento, equipe ou fotos de perfil de demonstração. O build normal `dist/` é a prévia local.

## Verificações

| Verificação | Resultado |
|---|---|
| Build e integridade | `build`, `build:production`, `check`, `check:production` passaram; 10 áreas na prévia e 8 na saída pública |
| Contrato de conteúdo | `test:content` passou: número com país/DDD, acentos da mensagem, links estáticos e exclusão das demonstrações |
| Contato | 21 destinos e mensagens conferidos. Clique real abre popup; requisição ao WhatsApp interceptada no teste, sem mensagem enviada. CTA do menu mobile fecha o menu sem erro |
| Menu, carrossel, FAQ e galeria | `npm test` passou; Escape/foco, limites/setas/Home/End; FAQ exclusiva; lightbox |
| Acessibilidade | 162 trechos de texto sobre superfícies sólidas, zero falhas; menor contraste 4,88:1. Oito FAQs por teclado; seis fotos com foco contido; Escape; corridas de fechamento/reabertura; skip link e contorno de 2px; redução de movimento e reflow de 200% passaram |
| Responsividade |320/360/390/768/1024/1440/1920px: zero overflow horizontal, imagens quebradas, falha de fonte, erros de console ou HTTP |
| Capturas | Página inteira em todas as sete larguras; recortes das 10 áreas em 1440/390px. Revisão visual manual da página completa e dos recortes de serviços/equipe/FAQ/hero |
| Build público no navegador | 390/1440px com JavaScript ligado e desligado: nenhuma demonstração ou blog; cinco serviços e 21 links reais. FAQ funcional com JavaScript |

Evidências em `output/site-validation/commercial/`: `results.json`, `contrast.json`, `accessibility.json`, capturas `full-1440.png`, `full-390.png` e recortes por área. Os testes usam o runtime de navegador já disponível, sem nova dependência instalada.

A delegação ao agente `sections_end` falhou por limite de uso antes de qualquer edição. Implementação, integração e revisão desta atualização foram realizadas pelo coordenador. **Não houve nova revisão independente nesta rodada**; a revisão com subagente registrada anteriormente continua sendo apenas a da entrega original.

## Para abrir e publicar futuramente

`npm run local` mantém a prévia em http://127.0.0.1:4173. Recarregue a aba. `npm run local:stop` encerra somente o servidor deste projeto. Nenhum deploy foi executado.

Pendências para publicação: domínio e hospedagem/HTTPS; configuração de indexação e URLs definitivas; conferência comercial final do atendimento; revisão das informações de privacidade conforme o tratamento real dos contatos. Se quiser exibir equipe e depoimento, são necessários dados e relatos reais autorizados; os módulos já são excluídos da saída pública enquanto isso. Formulário, blog, vídeo, redes sociais e fotos próprias não são requisitos para este lançamento pelo WhatsApp.
