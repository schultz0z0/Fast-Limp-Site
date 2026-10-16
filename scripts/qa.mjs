import { createRequire } from 'node:module';
import { homedir } from 'node:os';
import { resolve } from 'node:path';
import { mkdir, writeFile } from 'node:fs/promises';
import assert from 'node:assert/strict';
const require = createRequire(import.meta.url);
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || resolve(homedir(), '.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright'));
const dir = 'output/site-validation/commercial';
await mkdir(dir,{recursive:true});
const browser = await chromium.launch({headless:true});
const page = await browser.newPage({reducedMotion:'reduce'});
const consoleErrors=[], failedRequests=[];
page.on('pageerror',error=>consoleErrors.push(error.message));
page.on('console',message=>{if(message.type()==='error')consoleErrors.push(message.text());});
page.on('response',response=>{if(response.status()>=400)failedRequests.push({url:response.url(),status:response.status()});});
const results=[];
try{
 for(const width of [320,360,390,768,1024,1440,1920]){
  await page.setViewportSize({width,height:width<768?844:1000});
  await page.goto('http://127.0.0.1:4173',{waitUntil:'networkidle'});
  await page.evaluate(async()=>{await document.fonts.ready;for(const image of document.images)image.loading='eager';await Promise.all([...document.images].filter(img=>img.src).map(img=>img.decode().catch(()=>{})));});
  const result=await page.evaluate(()=>{
   const overflow=[...document.querySelectorAll('body *')].filter(el=>{const r=el.getBoundingClientRect();return r.width>0&&(r.right>innerWidth+1||r.left< -1)&&!el.closest('[data-track],dialog')&&!el.classList.contains('skip-link');}).map(el=>({tag:el.tagName,class:el.className,right:el.getBoundingClientRect().right,left:el.getBoundingClientRect().left}));
   return {width:innerWidth,scrollWidth:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight,overflow,brokenImages:[...document.images].filter(img=>img.src&&(!img.complete||!img.naturalWidth)).map(img=>img.src),font:document.fonts.check('700 40px Manrope'),sections:[...document.querySelectorAll('section[id],footer[id]')].map(el=>({id:el.id,top:Math.round(el.getBoundingClientRect().top+scrollY),height:Math.round(el.getBoundingClientRect().height)})),logoWidth:document.querySelector('.brand-logo').getBoundingClientRect().width};
  });
  results.push(result);
  await page.evaluate(()=>document.activeElement?.blur());
  await page.screenshot({path:`${dir}/full-${width}.png`,fullPage:true});
  if([390,1440].includes(width)){
   // Chromium pode compor elementos fixed fora da tela em screenshots de elementos altos.
   // Oculta somente o skip link já fora da tela e sem foco, apenas durante a captura.
   for(const id of ['inicio','sobre','servicos','referencias','como-funciona','diferenciais','depoimentos','equipe','duvidas','contato']) { await page.evaluate(()=>document.activeElement?.blur()); await page.locator('#'+id).screenshot({path:`${dir}/${id}-${width}.png`,style:'.skip-link:not(:focus){visibility:hidden!important}'}); }
   await page.evaluate(()=>scrollTo(0,0));
   await page.screenshot({path:`${dir}/viewport-${width}.png`});
  }
 }
 const summary={browser:'Chromium / Playwright bundled runtime',routing:'Browser plugin not available; existing bundled Playwright used, no dependency installed',results,consoleErrors,failedRequests};
 await writeFile(`${dir}/results.json`,JSON.stringify(summary,null,2));
 console.log(JSON.stringify(summary,null,2));
 assert.ok(results.every(r=>r.scrollWidth===r.width&&r.overflow.length===0),'Overflow encontrado');
 assert.ok(results.every(r=>r.brokenImages.length===0&&r.font),'Imagens e fontes');
 assert.equal(consoleErrors.length,0,'Console sem erros');assert.equal(failedRequests.length,0,'Sem 404');
 console.log('QA das sete larguras passou.');
}finally{await browser.close();}
