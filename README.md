# Fast Limp — site institucional

Site completo em **revisão local**, baseado nas duas referências fornecidas e na identidade aprovada. HTML semântico, CSS e JavaScript modular; sem dependências de produção, backend ou CMS. Não foi publicado.

## Abrir

No terminal desta pasta, com Node.js 20 ou superior:

```powershell
npm run dev
```

Abra **http://127.0.0.1:4173**. O servidor fica restrito ao computador local. Se já estiver aberto nesta porta, use a instância existente. Para outra porta: `$env:PORT=4174; npm run dev`.

No Windows, para manter o site disponível depois de fechar o terminal ou encerrar a sessão do agente, use **`npm run local`**. Ele inicia o servidor em segundo plano, sem janela e sem tarefa no login. Para encerrá-lo: **`npm run local:stop`**. `npm run dev` continua sendo a opção de terminal interativo; esse terminal precisa permanecer aberto para fotos e demais arquivos continuarem acessíveis.

O comando monta `dist/` antes de servir. Após editar as fontes, rode `npm run build` e recarregue o navegador. Para encerrar o servidor no terminal, pressione Ctrl+C.

## Comandos

```powershell
npm run build
npm run build:production
npm run check
npm run check:production
npm run test:content
npm test
npm run test:production
node scripts/a11y.mjs
node scripts/qa.mjs
```

`build` resolve os 183 tokens e integra os cinco fragmentos estáticos. `check` verifica seções, semântica principal, IDs, âncoras e assets. Os testes de navegador exigem o servidor ativo e usam o Playwright já disponível no runtime local do Codex; `PLAYWRIGHT_MODULE` pode apontar para outra instalação existente. Nenhum pacote de navegador foi instalado no projeto. `qa` renova capturas nas sete larguras, e `a11y` verifica os comportamentos de teclado, modais, FAQ, reflow e contrastes sólidos renderizados.

## Estrutura

- `site/partials/`: cabeçalho, hero, seções intermediárias, seções finais e rodapé.
- `site/styles/`: tokens gerados e estilos por frente de implementação.
- `site/scripts/app.js`: menu, carrossel, galeria, acordeão e painéis locais.
- `site/assets/brand/` e `fonts/`: arquivos oficiais preservados, com licença OFL.
- `site/assets/photos/`: fotografias WebP locais com srcset e corte mobile próprio.
- `site/assets/originals/`: masters fotográficos; não são copiados pelo build.
- `dist/`: versão estática gerada.
- `docs/ISSUES.md`: quadro de etapas e histórico de execução.
- `docs/CONTRATOS.md`: responsabilidades e interfaces compartilhadas.
- `docs/ASSETS.md`: fontes, licença e uso ilustrativo de cada fotografia.
- `docs/REVISAO-FINAL.md`: revisão independente e correções.
- `output/site-validation/`: capturas, resultados e evidências.

## Conteúdo confirmado e versão pública

Em16/10/2026 foram confirmados WhatsApp **(21)96764-3628**, atendimento no **Rio de Janeiro** e cinco serviços: vidros residenciais, vidros comerciais, pós-obra em residências/comércios, fachadas de vidro e vitrines. As23 CTAs abrem `wa.me/5521967643628` com uma mensagem editável. Nenhuma mensagem é enviada automaticamente. Foi escolhida a alternativa autorizada de WhatsApp direto, sem formulário ou backend.

A revisão FL-15 aplicou as melhorias de UX mobile: índice dos cinco serviços com posição, orçamento no fim do processo, perguntas antes do suporte, contato antes dos menus, equipe compacta e galeria de duas colunas em320px. O hero aprovado foi preservado. Estilos em `site/styles/mobile-ux.css` e evidências em `docs/UX-MOBILE-MELHORIAS.md`.

A prévia local em `dist/` mantém um depoimento e três perfis de equipe com fotos e nomes de exemplo, sem rótulos de revisão na interface, conforme solicitado. A natureza provisória dos dados fica registrada nos documentos e nos marcadores internos. **Para preparar arquivos públicos, use `npm run build:production`: a saída correta é `dist-production/`, que exclui esses dois módulos e suas fotos de perfil.** Não publique `dist/` como versão final. Para apresentar equipe ou depoimentos na versão pública, substitua por conteúdo real autorizado e remova deliberadamente os marcadores `PREVIEW-ONLY` daqueles módulos após revisão.

As fotos existentes foram mantidas, sem rótulos de banco de imagens na interface. A procedência e as licenças ficam em `docs/ASSETS.md`; a galeria não afirma documentar trabalhos realizados. Blog/artigos foram removidos. Oito FAQs foram adaptadas a partir da pesquisa registrada em `docs/FAQ-PESQUISA.md`, sem copiar condições comerciais de concorrentes. Privacidade e contato descrevem o funcionamento atual da página e do redirecionamento ao WhatsApp.

O `noindex` permanece deliberadamente nas duas saídas enquanto o domínio e a publicação não forem definidos. Antes de publicar: configurar domínio/hospedagem/HTTPS, revisar o conteúdo final e o tratamento de dados no atendimento, ajustar indexação/canonical/sitemap para o domínio real e conferir o destino no WhatsApp instalado. Redes sociais, preços, avaliações, certificações e resultados não foram inventados. A versão pública pode funcionar sem equipe ou depoimento; fotos próprias são opcionais, com autorização quando usadas. Evidências atuais em `output/site-validation/commercial/` e resumo em `docs/ATUALIZACAO-COMERCIAL.md`.
