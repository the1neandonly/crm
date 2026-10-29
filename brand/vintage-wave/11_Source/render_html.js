// Render HTML artboards: PNG (scale k) and optional PDF. jobs: [{html,w,h,png,pdf,scale,alpha}]
const {chromium}=require('playwright'); const fs=require('fs'); const path=require('path');
(async()=>{
  const jobs=JSON.parse(fs.readFileSync(process.argv[2])); const b=await chromium.launch();
  for(const j of jobs){
    const ctx=await b.newContext({viewport:{width:j.w,height:j.h},deviceScaleFactor:j.scale||1}); const p=await ctx.newPage();
    await p.goto('file://'+j.html,{waitUntil:'load'}); await p.evaluate(()=>document.fonts.ready);
    if(j.png){fs.mkdirSync(path.dirname(j.png),{recursive:true}); await p.screenshot({path:j.png,omitBackground:!!j.alpha,clip:{x:0,y:0,width:j.w,height:j.h}});}
    if(j.pdf){fs.mkdirSync(path.dirname(j.pdf),{recursive:true}); await p.pdf({path:j.pdf,width:`${j.w}px`,height:`${j.h}px`,printBackground:true,pageRanges:'1'});}
    await ctx.close();
  } await b.close(); console.log('rendered',jobs.length);
})();
