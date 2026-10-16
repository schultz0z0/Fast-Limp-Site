const { chromium } = require('C:/Users/rapha/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs = require('node:fs');
const assert = require('node:assert/strict');
(async()=>{
 const browser=await chromium.launch({headless:true});
 const page=await browser.newPage({viewport:{width:390,height:844},reducedMotion:'reduce'});
 const errors=[];page.on('pageerror',e=>errors.push(e.message));page.on('response',r=>{if(r.status()>=400)errors.push(`${r.status()} ${r.url()}`)});
 const widths=[];
 for(const width of [320,360,390,640,767,768,1024,1440,1920]){
  await page.setViewportSize({width,height:width<768?844:1000});
  await page.goto('http://127.0.0.1:4173',{waitUntil:'networkidle'});
  widths.push(await page.evaluate(()=>{const u=document.querySelector('.utility-bar').getBoundingClientRect();return {width:innerWidth,scrollWidth:document.documentElement.scrollWidth,utilityContained:[...document.querySelectorAll('.utility-inner>*')].every(e=>{const r=e.getBoundingClientRect();return getComputedStyle(e).display==='none'||r.top>=u.top&&r.bottom<=u.bottom}),h1InsideMain:!!document.querySelector('main h1'),footerOutsideMain:!document.querySelector('main footer'),globalHeader:!!document.querySelector('body>header'),globalFooter:!!document.querySelector('body>footer'),heroSource:document.querySelector('.hero-photo img').currentSrc.split('/').pop(),skipTarget:document.querySelector('.skip-link').getAttribute('href')};}));
  if([390,1440].includes(width)){await page.screenshot({path:`output/site-validation/reviewer-final-${width}.png`});}
 }
 const dialogs=[];
 await page.setViewportSize({width:390,height:844});
 for(const [trigger,id] of [['.hero-panel [data-contact]','contact-dialog'],['[data-gallery]','gallery-dialog'],['.team-section [data-pending]','pending-dialog']]){
  const target=page.locator(trigger).first();await target.focus();await page.keyboard.press('Enter');
  const focus=[];for(const key of ['Tab','Tab','Tab','Tab','Shift+Tab','Shift+Tab','Shift+Tab','Shift+Tab']){await page.keyboard.press(key);focus.push(await page.evaluate(dialogId=>!!document.activeElement.closest(`#${dialogId}`),id));}
  await page.keyboard.press('Escape');dialogs.push({id,contained:focus.every(Boolean),returnFocus:await target.evaluate(e=>document.activeElement===e)});
 }
 await page.evaluate(()=>scrollTo(0,0));await page.locator('.skip-link').focus();await page.keyboard.press('Enter');
 const skipFocus=await page.evaluate(()=>document.activeElement.id);
 const result={widths,dialogs,skipFocus,errors};
 fs.writeFileSync('output/site-validation/final-review-results.json',JSON.stringify(result,null,2));
 console.log(JSON.stringify(result,null,2));
 assert.ok(widths.every(x=>x.width===x.scrollWidth&&x.utilityContained&&x.h1InsideMain&&x.footerOutsideMain&&x.globalHeader&&x.globalFooter));
 assert.ok(dialogs.every(x=>x.contained&&x.returnFocus));assert.equal(skipFocus,'conteudo');assert.equal(errors.length,0);
 await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
