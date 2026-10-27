// Render the PDF (and PNG when missing) for every catalog item.
const {chromium}=require('playwright'); const fs=require('fs'); const path=require('path');
const MM=96/25.4;
(async()=>{
  const [,,catFile,OUT]=process.argv; const cat=JSON.parse(fs.readFileSync(catFile)); const b=await chromium.launch();
  const page=async(w,h,dpr)=>{const c=await b.newContext({viewport:{width:Math.max(1,Math.round(w)),height:Math.max(1,Math.round(h))},deviceScaleFactor:dpr});return [c,await c.newPage()];};
  let n=0;
  for(const it of cat.items){
    const dir=path.join(OUT,it.dest); fs.mkdirSync(dir,{recursive:true});
    const k=it.unit==='mm'?MM:1, W=it.w*k, Hh=it.h*k;
    const pdf=path.join(dir,it.name+'.pdf'), png=path.join(dir,it.name+'.png');
    const dpr=it.unit==='mm'?Math.min(3.125,4000/Math.max(W,Hh)):1;
    const [c,p]=await page(W,Hh,dpr); await p.goto('file://'+it.html,{waitUntil:'load'}); await p.evaluate(()=>document.fonts.ready);
    await p.pdf({path:pdf,width:`${it.w}${it.unit}`,height:`${it.h}${it.unit}`,printBackground:true,pageRanges:'1'});
    if(it.png&&fs.existsSync(it.png)) fs.copyFileSync(it.png,png); else await p.screenshot({path:png,clip:{x:0,y:0,width:W,height:Hh},omitBackground:it.alpha});
    await c.close(); n++;
  }
  for(const it of cat.svgitems){
    const dir=path.join(OUT,it.dest); fs.mkdirSync(dir,{recursive:true});
    let svg=fs.readFileSync(it.svg,'utf8'); const vb=svg.match(/viewBox="([\d.\-]+) ([\d.\-]+) ([\d.]+) ([\d.]+)"/);
    const vw=+vb[3], vh=+vb[4]; const W=it.w||1000, Hh=it.h||Math.round(W*vh/vw);
    svg=svg.replace(/<svg([^>]*?) width="[^"]*" height="[^"]*"/,`<svg$1 width="${W}" height="${Hh}"`);
    const html=`<!doctype html><html><head><style>@page{size:${W}px ${Hh}px;margin:0}html,body{margin:0;background:transparent}svg{display:block}</style></head><body>${svg}</body></html>`;
    const png=path.join(dir,it.name+'.png'), pdf=path.join(dir,it.name+'.pdf');
    if(it.png&&fs.existsSync(it.png)) fs.copyFileSync(it.png,png);
    if(it.pdf&&fs.existsSync(it.pdf)) fs.copyFileSync(it.pdf,pdf);
    if(!fs.existsSync(png)||!fs.existsSync(pdf)){
      const [c,p]=await page(W,Hh,1); await p.setContent(html);
      if(!fs.existsSync(png)) await p.screenshot({path:png,clip:{x:0,y:0,width:W,height:Hh},omitBackground:true});
      if(!fs.existsSync(pdf)) await p.pdf({path:pdf,width:`${W}px`,height:`${Hh}px`,printBackground:true,pageRanges:'1'});
      await c.close();
    }
    n++;
  }
  await b.close(); console.log('rendered',n);
})();
