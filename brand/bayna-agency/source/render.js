const {chromium}=require('playwright'); const fs=require('fs'); const path=require('path');
(async()=>{
  const jobs=JSON.parse(fs.readFileSync(process.argv[2]));
  const b=await chromium.launch(); const ctx=await b.newContext(); const page=await ctx.newPage();
  for(const j of jobs){
    fs.mkdirSync(path.dirname(j.out),{recursive:true});
    let svg=fs.readFileSync(j.svg,'utf8').replace(/<svg([^>]*?) width="[^"]*" height="[^"]*"/, `<svg$1 width="${j.w}" height="${j.h}"`);
    const html=`<!doctype html><html><head><style>@page{size:${j.w}px ${j.h}px;margin:0}html,body{margin:0;padding:0;background:transparent}svg{display:block}</style></head><body>${svg}</body></html>`;
    await page.setViewportSize({width:j.w,height:j.h});
    await page.setContent(html);
    if(j.type==='png') await page.screenshot({path:j.out,omitBackground:true,clip:{x:0,y:0,width:j.w,height:j.h}});
    else await page.pdf({path:j.out,width:`${j.w}px`,height:`${j.h}px`,printBackground:true,pageRanges:'1'});
  }
  await b.close(); console.log('rendered',jobs.length);
})();
