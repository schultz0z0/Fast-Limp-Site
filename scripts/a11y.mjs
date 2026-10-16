import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import { homedir } from 'node:os';
import { resolve } from 'node:path';
import { writeFile, mkdir } from 'node:fs/promises';
const require=createRequire(import.meta.url);
const {chromium}=require(process.env.PLAYWRIGHT_MODULE||resolve(homedir(),'.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright'));
const browser=await chromium.launch();
const page=await browser.newPage({viewport:{width:1440,height:1000},reducedMotion:'reduce'});
await mkdir('output/site-validation/commercial',{recursive:true});
await page.addInitScript(()=>{
 window.__qaDialogCloses={};
 document.addEventListener('close',event=>{
  if(event.target instanceof HTMLDialogElement){const id=event.target.id;window.__qaDialogCloses[id]=(window.__qaDialogCloses[id]||0)+1;}
 },true);
});
async function escapeAndRestore(dialogSelector,trigger){
 const id=dialogSelector.slice(1);
 const before=await page.evaluate(id=>window.__qaDialogCloses[id]||0,id);
 await page.keyboard.press('Escape');
 await page.waitForFunction(({id,before})=>!document.getElementById(id).open&&(window.__qaDialogCloses[id]||0)>before,{id,before});
 await page.waitForFunction(element=>document.activeElement===element,await trigger.elementHandle());
 assert.equal(await trigger.evaluate(element=>document.activeElement===element),true,`${id}: Escape devolve foco ao acionador após evento close`);
}
try{
 await page.goto('http://127.0.0.1:4173');await page.evaluate(()=>document.fonts.ready);
 const contrast=await page.evaluate(()=>{
  const rgb=c=>c.match(/[\d.]+/g)?.slice(0,3).map(Number);
  const luminance=arr=>arr.map(v=>{v/=255;return v<=.04045?v/12.92:((v+.055)/1.055)**2.4}).reduce((sum,v,i)=>sum+v*[.2126,.7152,.0722][i],0);
  const ratio=(a,b)=>{const x=luminance(a),y=luminance(b);return(Math.max(x,y)+.05)/(Math.min(x,y)+.05)};
  const rows=[];
  for(const element of document.querySelectorAll('body *')){
   if(element.closest('dialog,svg')||element.matches('[disabled]')||!element.getClientRects().length||!getComputedStyle(element).visibility.includes('visible'))continue;
   const ownText=[...element.childNodes].filter(n=>n.nodeType===Node.TEXT_NODE).map(n=>n.textContent.trim()).join(' ').trim();
   if(!ownText)continue;
   const style=getComputedStyle(element);let parent=element,bg;
   while(parent){const color=parent.classList.contains('hero-panel')?getComputedStyle(parent,'::before').backgroundColor:getComputedStyle(parent).backgroundColor;if(color!=='rgba(0, 0, 0, 0)'&&color!=='transparent'){bg=color;break;}parent=parent.parentElement;}
   if(!bg)bg='rgb(255, 255, 255)';
   const value=ratio(rgb(style.color),rgb(bg));const large=parseFloat(style.fontSize)>=24||(parseFloat(style.fontSize)>=18.667&&parseInt(style.fontWeight)>=700);const threshold=large?3:4.5;
   rows.push({text:ownText.slice(0,80),tag:element.tagName,class:element.className,fg:style.color,bg,ratio:Math.round(value*100)/100,threshold,pass:value>=threshold});
  }
  return rows;
 });
 const failures=contrast.filter(row=>!row.pass);
 await writeFile('output/site-validation/commercial/contrast.json',JSON.stringify({checked:contrast.length,failures,rows:contrast},null,2));
 // Tab access, skip link and focus ring.
 await page.goto('http://127.0.0.1:4173');await page.keyboard.press('Tab');
 assert.equal(await page.locator('.skip-link').evaluate(el=>el===document.activeElement),true);
 const focusStyle=await page.locator('.skip-link').evaluate(el=>({style:getComputedStyle(el).outlineStyle,width:getComputedStyle(el).outlineWidth}));
 assert.equal(focusStyle.style,'solid');
 await page.keyboard.press('Enter');assert.equal(await page.locator('#conteudo').evaluate(el=>el===document.activeElement),true);
 // Every CTA has the confirmed WhatsApp number and a prefilled message.
 const count=await page.locator('[data-contact]').count();
 let contacts=0;
 for(let i=0;i<count;i++){const control=page.locator('[data-contact]').nth(i);const url=new URL(await control.getAttribute('href'));assert.equal(url.hostname,'wa.me');assert.equal(url.pathname,'/5521967643628');assert.ok(url.searchParams.get('text'));assert.equal(await control.getAttribute('target'),'_blank');contacts++;}
 const pendingCount=await page.locator('[data-pending]').count();
 for(let i=0;i<pendingCount;i++){const control=page.locator('[data-pending]').nth(i);await control.click();assert.equal(await page.locator('#pending-dialog').isVisible(),true);await escapeAndRestore('#pending-dialog',control);}
 // Focus containment in lightbox and keyboard opening.
 const tile=page.locator('[data-gallery]').first();await tile.focus();await page.keyboard.press('Enter');
 for(const key of ['Tab','Tab','Tab','Tab','Shift+Tab','Shift+Tab','Shift+Tab','Shift+Tab']){await page.keyboard.press(key);assert.equal(await page.evaluate(()=>document.querySelector('#gallery-dialog').contains(document.activeElement)),true,`Lightbox mantém foco em ${key}`);}
 await escapeAndRestore('#gallery-dialog',tile);
 // All six photos open with distinct real source and truthful captions.
 for(let i=0;i<6;i++){const control=page.locator('[data-gallery]').nth(i);await control.click();await page.locator('#gallery-image').evaluate(img=>img.decode());assert.equal(await page.locator('#gallery-caption').innerText(),await control.getAttribute('data-caption'));await escapeAndRestore('#gallery-dialog',control);}
 // Deterministic race regressions: close fires asynchronously after synchronous focus/reopen.
 await tile.click();
 const focusAfterClose=await page.evaluate(async()=>{
  const dialog=document.querySelector('#gallery-dialog'),question=document.querySelector('[data-accordion]');
  const closed=new Promise(resolve=>dialog.addEventListener('close',()=>resolve(),{once:true}));
  dialog.close();question.focus();await closed;
  return document.activeElement===question;
 });
 assert.equal(focusAfterClose,true,'Callback close antigo não rouba foco da FAQ');
 await tile.click();
 const reopened=await page.evaluate(async()=>{
  const dialog=document.querySelector('#gallery-dialog'),trigger=document.querySelector('[data-gallery]');
  const closed=new Promise(resolve=>dialog.addEventListener('close',()=>resolve(),{once:true}));
  dialog.close();trigger.click();await closed;
  return {open:dialog.open,src:document.querySelector('#gallery-image').getAttribute('src'),expected:trigger.dataset.full};
 });
 assert.equal(reopened.open,true,'Reabertura permanece aberta após callback close antigo');
 assert.equal(reopened.src,reopened.expected,'Callback close antigo não limpa foto reaberta');
 await escapeAndRestore('#gallery-dialog',tile);
 // All FAQ states, including collapse of active question.
 for(const question of await page.locator('[data-accordion]').all()){await question.focus();if(await question.getAttribute('aria-expanded')==='true')await page.keyboard.press('Enter');await page.keyboard.press('Enter');assert.equal(await question.getAttribute('aria-expanded'),'true');assert.equal(await page.locator('[data-accordion][aria-expanded="true"]').count(),1);await page.keyboard.press('Enter');assert.equal(await question.getAttribute('aria-expanded'),'false');}
 // Native page navigation changes hash; mobile nav closes and moves focus.
 await page.setViewportSize({width:390,height:844});await page.goto('http://127.0.0.1:4173');await page.locator('#menu-toggle').click();await page.locator('#mobile-menu a[href="#sobre"]').click();assert.ok(page.url().endsWith('#sobre'));assert.equal(await page.locator('#mobile-menu').isVisible(),false);assert.equal(await page.locator('#sobre').evaluate(el=>el===document.activeElement),true);
 // Zoom 200% layout / responsive reflow at 720 CSS pixels, then text scaling 200%.
 await page.setViewportSize({width:720,height:500});await page.goto('http://127.0.0.1:4173');
 const zoomReflow=await page.evaluate(()=>document.documentElement.scrollWidth===innerWidth);assert.equal(zoomReflow,true);
 await page.addStyleTag({content:'body{font-size:200%}'});const textReflow=await page.evaluate(()=>document.documentElement.scrollWidth===innerWidth);assert.equal(textReflow,true);
 const reduced=await page.evaluate(()=>({media:matchMedia('(prefers-reduced-motion: reduce)').matches,scroll:getComputedStyle(document.documentElement).scrollBehavior,transition:getComputedStyle(document.querySelector('.gallery-tile img')).transitionDuration}));assert.equal(reduced.media,true);assert.equal(reduced.scroll,'auto');assert.equal(reduced.transition,'0s');
 const report={contrast:{checked:contrast.length,failures,minimum:Math.min(...contrast.map(x=>x.ratio))},focusStyle,contacts,infoControls:pendingCount,lightbox:'6 images + keyboard + Tab/Shift+Tab containment + Escape + restoration after close event',dialogRaces:{focusAfterClose,reopenKeepsPhoto:reopened.src===reopened.expected},faq:'8 keyboard controls + exclusive expansion + collapse',menu:'hash + closing + destination focus',zoomReflow,textReflow,reducedMotion:reduced};
 await writeFile('output/site-validation/commercial/accessibility.json',JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));assert.equal(failures.length,0,'Contraste deve passar');
}finally{await browser.close();}
