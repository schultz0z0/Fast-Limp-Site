import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { createRequire } from 'node:module';
import { resolve } from 'node:path';
import { homedir } from 'node:os';
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || resolve(homedir(), '.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright'));
const html = await readFile('dist-production/index.html', 'utf8');
const browser = await chromium.launch();
try {
  for (const javaScriptEnabled of [true, false]) {
    const context = await browser.newContext({ javaScriptEnabled, reducedMotion: 'reduce' });
    // Serve the public HTML through the existing local server. All its referenced
    // assets have already been verified inside dist-production by check.mjs.
    await context.route('http://127.0.0.1:4173/', route => route.fulfill({ status: 200, contentType: 'text/html; charset=utf-8', body: html }));
    const page = await context.newPage();
    for (const width of [390, 1440]) {
      await page.setViewportSize({ width, height: 900 });
      await page.goto('http://127.0.0.1:4173/', { waitUntil: 'networkidle' });
      assert.equal(await page.locator('[data-content-mode="production"]').count(), 1);
      assert.equal(await page.locator('#depoimentos,#equipe,#conteudos').count(), 0);
      assert.equal(await page.locator('[data-contact]').count(), 23);
      assert.equal(await page.locator('.service-card').count(), 5);
      const href = await page.locator('.hero-panel [data-contact]').getAttribute('href');
      assert.equal(new URL(href).pathname, '/5521967643628');
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth === innerWidth), true);
      if (javaScriptEnabled) {
        await page.locator('#faq-question-3').click();
        assert.equal(await page.locator('#faq-answer-3').isVisible(), true);
      }
    }
    await context.close();
  }
  console.log('Build público: 390/1440px, sem blocos fictícios ou blog, 23 links WhatsApp com/sem JS, cinco serviços, FAQ e reflow passaram.');
} finally { await browser.close(); }
