const {chromium}=require('playwright'); const fs=require('fs'); const path=require('path'); const {execFileSync}=require('child_process');
const MM=96/25.4;
(async()=>{
  const jobs=JSON.parse(fs.readFileSync(process.argv[2])); const b=await chromium.launch();
  let n=0; for(const j of jobs){ if(process.env.SKIP && fs.existsSync(j.out)) continue; n++;
    fs.mkdirSync(path.dirname(j.out),{recursive:true});
    const k=j.unit==='mm'?MM:1, W=Math.round(j.w*k), H=Math.round(j.h*k);
    const ctx=await b.newContext({viewport:{width:W,height:H},deviceScaleFactor:j.scale||1}); const p=await ctx.newPage();
    await p.goto('file://'+j.html,{waitUntil:'load'}); await p.evaluate(()=>document.fonts.ready);
    if(j.type==='pdf') await p.pdf({path:j.out,width:`${j.w}${j.unit}`,height:`${j.h}${j.unit}`,printBackground:true});
    else if(j.type==='png') await p.screenshot({path:j.out,clip:{x:0,y:0,width:W,height:H},omitBackground:!!j.alpha});
    else { const tmp=j.out+'.tmp.png'; await p.screenshot({path:tmp,clip:{x:0,y:0,width:W,height:H}});
      execFileSync('convert',[tmp,'-quality','94','-sampling-factor','4:4:4',j.out]); fs.unlinkSync(tmp); }
    await ctx.close();
  }
  await b.close(); console.log('rendered',jobs.length);
})();
