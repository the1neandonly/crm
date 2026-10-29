const {chromium}=require('playwright'); const fs=require('fs'); const path=require('path');
// Render SVG/HTML jobs with Geist + Plex Arabic available as web fonts.
const F='file://'+path.resolve(__dirname,'../fonts/ttf/');
const css='';
module.exports={css};
if(require.main===module){(async()=>{
  const jobs=JSON.parse(fs.readFileSync(process.argv[2])); const b=await chromium.launch(); const p=await b.newPage();
  for(const j of jobs){ fs.mkdirSync(path.dirname(j.out),{recursive:true});
    const body=j.svg?fs.readFileSync(j.svg,'utf8').replace(/<svg([^>]*?) width="[^"]*" height="[^"]*"/,`<svg$1 width="${j.w}" height="${j.h}"`):'';
    await p.setViewportSize({width:j.w,height:j.h});
    const tmp=path.join(__dirname,'_shot.html'); fs.writeFileSync(tmp,`<!doctype html><html><head><meta charset="utf-8"><style>${css}html,body{margin:0;background:transparent}svg{display:block}@page{size:${j.w}px ${j.h}px;margin:0}</style></head><body>${body}</body></html>`); await p.goto('file://'+tmp);
    await p.evaluate(()=>document.fonts.ready);
    if(j.type==='png') await p.screenshot({path:j.out,omitBackground:true,clip:{x:0,y:0,width:j.w,height:j.h}});
    else await p.pdf({path:j.out,width:`${j.w}px`,height:`${j.h}px`,printBackground:true,pageRanges:'1'});
  } await b.close(); console.log('rendered',jobs.length);
})();}
