import {createRequire} from 'node:module';
import {mkdir,writeFile} from 'node:fs/promises';
const require=createRequire(import.meta.url);
const {chromium}=require('C:/Users/rapha/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const out='output/site-validation/mobile-ux-improvements'; await mkdir(out,{recursive:true});
const browser=await chromium.launch({headless:true});
const ctx=await browser.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true,reducedMotion:'no-preference'});
const page=await ctx.newPage();
const data={scope:'FL-15 final read-only; Chromium CDP touch; no external navigation',choices:[],sync:[],errors:[],layout:{}};
page.on('pageerror',e=>data.errors.push(e.message));
await ctx.route('https://wa.me/**',r=>r.abort());
const sleep=()=>page.waitForTimeout(700);
try{
 await page.goto('http://127.0.0.1:4173'); await page.evaluate(()=>document.fonts.ready);
 const choices=page.locator('[data-service-index]'); const track=page.locator('#services-track');
 await page.locator('[data-carousel]').scrollIntoViewIfNeeded(); await page.evaluate(()=>scrollBy(0,-20)); await sleep();
 const read=()=>page.evaluate(()=>{const t=document.querySelector('#services-track');return {left:t.scrollLeft,max:t.scrollWidth-t.clientWidth,top:scrollY,pressed:[...document.querySelectorAll('[data-service-index]')].filter(e=>e.getAttribute('aria-pressed')==='true').map(e=>Number(e.dataset.serviceIndex)),label:document.querySelector('[data-carousel-position]').textContent,prev:document.querySelector('[data-prev]').disabled,next:document.querySelector('[data-next]').disabled};});
 for(let i=0;i<await choices.count();i++){
  const before=await read();await choices.nth(i).tap();await sleep();const after=await read();
  const expected=await track.evaluate((e,i)=>{const c=e.querySelectorAll('.service-card');return Math.min(e.scrollWidth-e.clientWidth,c[i].offsetLeft-c[0].offsetLeft);},i);
  data.choices.push({index:i,before,after,expected,passed:after.pressed.length===1&&after.pressed[0]===i&&after.label.startsWith(`${i+1} de 5`)&&Math.abs(after.left-expected)<2&&Math.abs(after.top-before.top)<2});
 }
 async function check(name,action,index){await action();await sleep();const state=await read();data.sync.push({name,state,passed:state.pressed.length===1&&state.pressed[0]===index&&state.label.startsWith(`${index+1} de 5`)});}
 await track.focus();await check('Home',()=>page.keyboard.press('Home'),0);
 await check('ArrowRight',()=>page.keyboard.press('ArrowRight'),1);
 await check('ArrowLeft',()=>page.keyboard.press('ArrowLeft'),0);
 await check('End',()=>page.keyboard.press('End'),4);
 await check('previous-button',()=>page.locator('[data-prev]').tap(),3);
 await check('next-button',()=>page.locator('[data-next]').tap(),4);
 await track.focus();await page.keyboard.press('Home');await sleep();
 await track.scrollIntoViewIfNeeded();await page.evaluate(()=>scrollBy(0,-100));await sleep();
 const cdp=await ctx.newCDPSession(page);
 async function swipe(x1,y1,x2,y2){await cdp.send('Input.dispatchTouchEvent',{type:'touchStart',touchPoints:[{x:x1,y:y1}]});for(let i=1;i<=10;i++){await cdp.send('Input.dispatchTouchEvent',{type:'touchMove',touchPoints:[{x:x1+(x2-x1)*i/10,y:y1+(y2-y1)*i/10}]});await page.waitForTimeout(25);}await cdp.send('Input.dispatchTouchEvent',{type:'touchEnd',touchPoints:[]});await sleep();}
 const box=await track.boundingBox();const y=Math.min(650,Math.max(180,box.y+100));data.touch={before:await read()};
 await swipe(330,y,60,y);data.touch.horizontal=await read();await swipe(180,y,180,Math.max(80,y-180));data.touch.vertical=await read();
 data.touch.passed=data.touch.horizontal.left>data.touch.before.left&&data.touch.horizontal.top===data.touch.before.top&&data.touch.horizontal.pressed[0]===1&&data.touch.horizontal.label.startsWith('2 de 5')&&data.touch.vertical.top>data.touch.horizontal.top&&Math.abs(data.touch.vertical.left-data.touch.horizontal.left)<2;
 data.layout.mobile=await page.evaluate(()=>{const r=s=>{const e=document.querySelector(s);const b=e.getBoundingClientRect();return {y:b.y+scrollY,x:b.x,width:b.width,height:b.height,display:getComputedStyle(e).display};};return {faq:r('.faq-list'),help:r('.faq-support'),contact:r('.footer-contact'),menus:r('.footer-grid>nav'),services:r('.footer-services'),team:[...document.querySelectorAll('.team-card')].map(e=>({height:e.getBoundingClientRect().height,cols:getComputedStyle(e).gridTemplateColumns})),processCTA:r('.mobile-process-action'),contactCount:document.querySelectorAll('[data-contact]').length,scrollWidth:document.documentElement.scrollWidth,width:innerWidth};});
 await page.setViewportSize({width:320,height:844});await sleep();data.layout.gallery320=await page.locator('.gallery-bento').evaluate(e=>({cols:getComputedStyle(e).gridTemplateColumns,rows:getComputedStyle(e).gridTemplateRows,width:e.getBoundingClientRect().width,tiles:e.querySelectorAll('[data-gallery]').length,documentWidth:document.documentElement.scrollWidth}));
 await page.setViewportSize({width:1440,height:900});await sleep();data.layout.desktop=await page.evaluate(()=>({picker:getComputedStyle(document.querySelector('.service-picker')).display,position:getComputedStyle(document.querySelector('.service-position')).display,processCTA:getComputedStyle(document.querySelector('.mobile-process-action')).display}));
 data.accepted=data.choices.length===5&&data.choices.every(e=>e.passed)&&data.sync.every(e=>e.passed)&&data.touch.passed&&data.errors.length===0&&data.layout.mobile.faq.y<data.layout.mobile.help.y&&data.layout.mobile.contact.y<data.layout.mobile.menus.y&&data.layout.mobile.team.every(e=>e.height===148)&&data.layout.gallery320.cols.split(' ').length===2&&data.layout.mobile.contactCount===23;
 await writeFile(`${out}/final-review-results.json`,JSON.stringify(data,null,2));console.log(JSON.stringify(data,null,2));
}finally{await ctx.close();await browser.close();}
