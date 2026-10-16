const { chromium } = require('C:/Users/rapha/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs = require('node:fs');
(async () => {
 const browser=await chromium.launch({headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:1000},reducedMotion:'reduce'});
 const errors=[];page.on('pageerror',e=>errors.push(e.message));page.on('response',r=>{if(r.status()>=400)errors.push(`${r.status()} ${r.url()}`)});
 await page.goto('http://127.0.0.1:4173',{waitUntil:'networkidle'});
 await page.evaluate(async()=>{document.querySelectorAll('img').forEach(i=>i.loading='eager');await Promise.all([...document.images].filter(i=>i.src).map(i=>i.decode().catch(()=>{})));});
 const images=await page.evaluate(()=>[...document.images].filter(i=>i.src).map(i=>({src:i.currentSrc.split('/').pop(),natural:[i.naturalWidth,i.naturalHeight],attributes:[+i.getAttribute('width'),+i.getAttribute('height')],ratioError:Math.abs(i.naturalWidth/i.naturalHeight-(+i.getAttribute('width'))/(+i.getAttribute('height')))})));
 const checks=[];
 for(const width of [320,360,390,640,767,768,900,1023,1024,1100,1280,1440,1920]){
  await page.setViewportSize({width,height:900});
  await page.evaluate(()=>scrollTo(0,0));
  checks.push(await page.evaluate(()=>{const h=document.querySelector('.site-header'),n=document.querySelector('.desktop-nav'),a=document.querySelector('.header-action');const r=e=>{const b=e.getBoundingClientRect();return {x:b.x,y:b.y,w:b.width,h:b.height,right:b.right,bottom:b.bottom}};return {width:innerWidth,scrollWidth:document.documentElement.scrollWidth,header:r(h),nav:r(n),cta:r(a),heroSubject:document.querySelector('.hero-photo img').currentSrc,active:document.activeElement.outerHTML.slice(0,150),skip:r(document.querySelector('.skip-link')),teamLabels:[...document.querySelectorAll('.team-art-label,.team-nameplate')].map(r)};}));
  if([640,768,1024].includes(width)) await page.screenshot({path:`output/site-validation/review-${width}.png`,fullPage:true});
 }
 await page.setViewportSize({width:390,height:844});
 await page.locator('#menu-toggle').click();await page.keyboard.press('Escape');
 const menuReturn=await page.locator('#menu-toggle').evaluate(e=>document.activeElement===e);
 await page.locator('.hero-panel [data-contact]').focus();await page.keyboard.press('Enter');
 const contactOpen=await page.locator('#contact-dialog').isVisible();
 const modalFocus=[];for(let i=0;i<5;i++){await page.keyboard.press('Tab');modalFocus.push(await page.evaluate(()=>({tag:document.activeElement.tagName,inModal:!!document.activeElement.closest('#contact-dialog')})));}
 await page.keyboard.press('Escape');
 const returnContact=await page.locator('.hero-panel [data-contact]').evaluate(e=>document.activeElement===e);
 await page.locator('[data-gallery]').first().focus();await page.keyboard.press('Enter');await page.keyboard.press('Tab');
 const galleryTab=await page.evaluate(()=>document.activeElement.outerHTML);await page.keyboard.press('Escape');
 const returnGallery=await page.locator('[data-gallery]').first().evaluate(e=>document.activeElement===e);
 await page.locator('[data-accordion]').nth(5).focus();await page.keyboard.press('Enter');
 const faqOpen=await page.locator('[data-accordion]').evaluateAll(es=>es.map(e=>e.getAttribute('aria-expanded')));
 await page.setViewportSize({width:720,height:500});
 await page.screenshot({path:'output/site-validation/review-200-equivalent.png',fullPage:true});
 const result={images,checks,menuReturn,contactOpen,modalFocus,returnContact,galleryTab,returnGallery,faqOpen,errors};
 fs.writeFileSync('output/site-validation/independent-review.json',JSON.stringify(result,null,2));
 console.log(JSON.stringify(result,null,2));await browser.close();
})().catch(e=>{console.error(e);process.exit(1)});
