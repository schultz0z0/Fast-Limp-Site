import assert from 'node:assert/strict';

const origin = process.argv[2] || 'http://127.0.0.1:4180';
const paths = ['/about', '/contact', '/privacy'];

async function expect(path, accept, status, type, pattern, vary = false) {
  const response = await fetch(new URL(path, origin), {
    headers: accept ? { Accept: accept } : {},
    redirect: 'manual',
  });
  assert.equal(response.status, status, path);
  if (type) assert.match(response.headers.get('content-type') || '', type, path);
  if (vary) assert.match(response.headers.get('vary') || '', /\bAccept\b/i, path);
  const body = await response.text();
  if (pattern) assert.match(body, pattern, path);
  return body;
}

const markdown = /^text\/markdown;\s*charset=utf-8/i;
const html = /^text\/html/i;
await expect('/', 'text/markdown', 200, markdown, /^# Fast Limp/, true);
await expect('/', 'text/html;q=0.9, text/markdown;q=0.5', 200, html, /<h1>/i, true);
await expect('/', 'text/html;q=0.2, text/markdown;q=0.8', 200, markdown, /^# Fast Limp/, true);
await expect('/', 'text/*;q=1, text/markdown;q=0', 200, html, /<h1>/i, true);
await expect('/', 'text/*;q=0.8, text/html;q=0, text/markdown;q=0', 406, html, /406/, true);
await expect('/', 'application/json', 406, html, /406/, true);
await expect('/', 'text/markdown; charset="utf-8"', 200, markdown, /^# Fast Limp/, true);
const home = await expect('/', 'text/html', 200, html, /<title>Fast Limp — Limpeza de vidros/, true);
await expect('/', null, 200, html, /<h1>/i, true);
await expect('/?origem=teste', 'text/markdown', 200, markdown, /WhatsApp/, true);
await expect('/index.md', 'text/html', 200, markdown, /^# Fast Limp/);
await expect('/url-inexistente?origem=teste', 'text/markdown', 404, markdown, /.{20,}\[.*\]\(\/sitemap\.xml\)/s, true);
await expect('/url-inexistente', 'text/html', 404, html, /404/, true);
await expect('/assets/inexistente.webp', 'text/markdown', 404, markdown, /404/, true);

const business = JSON.parse(home.match(/<script type="application\/ld\+json">(.*?)<\/script>/s)[1]);
assert.ok(business.keywords.includes('limpeza de vidros'));
assert.equal(business.contactPoint.telephone, '+5521967643628');
assert.ok(business.contactPoint.contactType);
assert.equal(business.hasOfferCatalog.itemListElement[0].itemOffered.serviceType, 'Limpeza de vidros');

const robots = await expect('/robots.txt', null, 200, /^text\/plain/i, /Sitemap: https:\/\/fastlimpbrasil\.com\.br\/sitemap\.xml/);
assert.match(robots, /Allow: \//);
const sitemap = await expect('/sitemap.xml', null, 200, /xml/i, /<loc>https:\/\/fastlimpbrasil\.com\.br\/<\/loc>/);
assert.equal((sitemap.match(/<loc>/g) || []).length, 4);
const llms = await expect('/llms.txt', null, 200, /^text\/plain/i, /^# Fast Limp\n\n> .+\n/);
assert.match(llms, /Quando usar/i);
for (const path of paths) {
  const page = await expect(path, 'text/html', 200, html, /<main/);
  assert.ok(page.match(/<main[^>]*>(.*?)<\/main>/s)[1].replace(/<[^>]+>/g, '').trim().length >= 500, path);
  assert.ok(page.includes(`rel="canonical" href="https://fastlimpbrasil.com.br${path}"`), path);
  assert.ok(home.includes(`href="${path}"`), path);
  assert.ok(sitemap.includes(`<loc>https://fastlimpbrasil.com.br${path}</loc>`), path);
  assert.ok(llms.includes(`(https://fastlimpbrasil.com.br${path}.md)`), path);
  await expect(`${path}.md`, null, 200, markdown, /^# /);
  await expect(`${path}/`, null, 301);
  await expect(`${path}.html`, null, 301);
}
await expect('/assets/brand/fast-limp-social.jpg', null, 200, /^image\/jpeg/i);
const image = await fetch(new URL('/assets/brand/fast-limp-social.jpg', origin), { method: 'HEAD' });
assert.match(image.headers.get('cache-control') || '', /\bmax-age=86400\b/);
await expect('/favicon.ico', null, 200, /^image\//i);
console.log('HTTP: negociação, 404, sitemap, robots, llms.txt, schema, páginas institucionais e assets verificados.');
