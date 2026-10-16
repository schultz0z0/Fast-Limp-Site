import { readFile, writeFile, mkdir, cp, rm } from 'node:fs/promises';
import { resolve, dirname, basename } from 'node:path';
import { renderContent } from './content.mjs';
await import('./tokens.mjs');
let html = await readFile('site/index.html', 'utf8');
for (const name of ['header', 'start', 'middle', 'end', 'footer']) html = html.replace(`<!-- INCLUDE:${name} -->`, await readFile(`site/partials/${name}.html`, 'utf8'));
const production = process.argv.includes('--production');
const folder = production ? 'dist-production' : 'dist';
html = renderContent(html, JSON.parse(await readFile('site/content.json', 'utf8')), production);
const output = resolve(folder);
if (dirname(output) !== process.cwd() || !['dist', 'dist-production'].includes(basename(output))) throw new Error('Diretório de build fora do projeto');
// Apenas a saída gerada; fontes e masters ficam preservados em site/.
await rm(output, { recursive: true, force: true });
await mkdir(output, { recursive: true });
await writeFile(`${folder}/index.html`, html);
for (const assetFolder of ['styles', 'scripts', 'assets']) await cp(`site/${assetFolder}`, `${folder}/${assetFolder}`, { recursive: true, filter: source => !source.includes('originals') && !['contact-sheet.jpg', 'manifest.json'].includes(basename(source)) && !(production && /(?:team-\d|article-\d)/.test(basename(source))) });
console.log(`Build estático concluído em ${folder}/. ${production ? 'Conteúdo de exemplo excluído. Indexação ainda bloqueada até definir o domínio.' : 'Prévia local para revisão visual.'}`);
