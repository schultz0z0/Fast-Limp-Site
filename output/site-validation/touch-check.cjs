const {chromium}=require('C:/Users/rapha/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'),assert=require('assert/strict');
(async()=>{
 const browser=await chromium.launch();
 try{
  const page=await browser.newPage({viewport:{width:390,height:844},hasTouch:true,isMobile:true,reducedMotion:'reduce'});
  await page.goto('http://127.0.0.1:4173',{waitUntil:'networkidle'});
  assert.match(await page.title(),/Fast Limp/);
  await page.locator('#menu-toggle').tap();await page.locator('#mobile-menu').waitFor({state:'visible'});
  await page.locator('#mobile-menu a[href="#servicos"]').tap();await page.locator('#mobile-menu').waitFor({state:'hidden'});
  await page.locator('#servicos').scrollIntoViewIfNeeded();
  const track=page.locator('[data-track]').first();await track.scrollIntoViewIfNeeded();
  const box=await track.boundingBox(),y=Math.min(700,Math.max(160,box.y+100));
  const cdp=await page.context().newCDPSession(page);
  await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:320,y}]});
  for(let x=300;x>=70;x-=20)await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x,y}]});
  await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});
  await page.waitForFunction(()=>document.querySelector('[data-track]').scrollLeft>0);
  const swipe=await track.evaluate(el=>el.scrollLeft);
  // Novo fluxo de contato: elimina a inércia do gesto CDP anterior.
  await page.goto('http://127.0.0.1:4173',{waitUntil:'networkidle'});
  await page.locator('.hero-panel [data-contact]').tap();
  await page.locator('#contact-dialog').waitFor({state:'visible'});
  await page.screenshot({path:'output/site-validation/contact-mobile.png'});
  await page.locator('#contact-dialog [data-close]').first().tap();await page.locator('#contact-dialog').waitFor({state:'hidden'});
  const data={title:await page.title(),menuTap:true,navigationTap:true,carouselTouchSwipe:{passed:true,scrollLeft:swipe},contactTap:true,resources:await page.evaluate(()=>performance.getEntriesByType('resource').map(r=>({name:r.name.split('/').pop(),transfer:r.transferSize,origin:new URL(r.name).origin}))),note:'Touch emulado em Chromium, sem aparelho físico'};
  fs.writeFileSync('output/site-validation/touch.json',JSON.stringify(data,null,2));
  console.log(JSON.stringify({title:data.title,menuTap:true,navigationTap:true,swipe,contactTap:true,externalResources:data.resources.filter(r=>r.origin!=='http://127.0.0.1:4173').length}));
 }finally{await browser.close();}
})().catch(error=>{console.error(error);process.exit(1)});
