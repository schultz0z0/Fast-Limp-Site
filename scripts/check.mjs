import { readFile, access } from 'node:fs/promises';
import { resolve } from 'node:path';
import assert from 'node:assert/strict';
const folder = process.argv.includes('--production') ? 'dist-production' : 'dist';
const html = await readFile(`${folder}/index.html`, 'utf8');
const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map(match => match[1]);
assert.equal(new Set(ids).size, ids.length, 'IDs devem ser únicos');
assert.equal((html.match(/<h1\b/g) || []).length, 1, 'Uma H1');
assert.equal((html.match(/<footer id="contato"/g) || []).length, 1, 'Um rodapé global');
assert.ok(html.indexOf('<main ') < html.indexOf('<h1>'), 'Hero no conteúdo principal');
assert.ok(html.indexOf('</main>') < html.indexOf('<footer id="contato"'), 'Rodapé global externo ao main');
assert.ok(html.includes('lang="pt-BR"'));
assert.ok(!html.includes('<!-- INCLUDE:'), 'Todos os fragmentos integrados');
assert.ok(!/href=["']#["']/.test(html), 'Sem links vazios');
assert.ok(!html.includes('id="conteudos"'), 'Sem blog');
assert.ok(!html.includes('id="contact-dialog"'), 'Sem painel de contato pendente');
const contacts = [...html.matchAll(/<a\b[^>]*data-contact[^>]*href="([^"]+)"/g)];
assert.ok(contacts.length >= 20, 'CTAs convertidas em links reais');
for (const [, href] of contacts) { const url = new URL(href.replaceAll('&amp;', '&')); assert.equal(url.hostname, 'wa.me'); assert.equal(url.pathname, '/5521967643628'); assert.ok(url.searchParams.get('text')?.startsWith('Olá, Fast Limp!')); }
assert.equal((html.match(/class="service-card"/g)||[]).length, 5, 'Cinco serviços confirmados');
if (folder === 'dist-production') { assert.ok(!/id="(?:depoimentos|equipe)"|perfil fictício|relato fictício|Mariana Costa/.test(html), 'Demonstrações ausentes no build público'); }
const expected = ['inicio','sobre','servicos','referencias','como-funciona','diferenciais', ...(folder === 'dist' ? ['depoimentos','equipe'] : []),'duvidas','contato'];
let previous = -1;
for (const id of expected) { const index = html.indexOf(`id="${id}"`); assert.ok(index > previous, `Ordem de ${id}`); previous = index; }
for (const match of html.matchAll(/href="#([^"]+)"/g)) assert.ok(ids.includes(match[1]), `Âncora: ${match[1]}`);
const local = new Set();
for (const match of html.matchAll(/(?:src|href|data-full)="([^"#]+)"/g)) if (!/^(https?:|data:)/.test(match[1])) local.add(match[1]);
for (const match of html.matchAll(/srcset="([^"]+)"/g)) for (const item of match[1].split(',')) local.add(item.trim().split(/\s/)[0]);
for (const path of local) await access(resolve(folder, path));
for (const name of ['base','middle','end']) {
  const css = await readFile(`${folder}/styles/${name}.css`, 'utf8');
  assert.ok(!/(?:html|body)\s*\{[^}]*overflow-x:\s*hidden/s.test(css), 'Não mascarar overflow');
}
console.log(`Check ${folder}: ${expected.length} seções, ${contacts.length} links WhatsApp, cinco serviços, IDs/âncoras válidos, ${local.size} assets locais.`);
