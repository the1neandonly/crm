const {chromium}=require('playwright'); const fs=require('fs'); const path=require('path'); const {execFileSync}=require('child_process');
(async()=>{
  const vids=JSON.parse(fs.readFileSync(process.argv[2])); const only=process.argv[3]; const b=await chromium.launch();
  for(const v of vids){ if(only && !v.name.includes(only)) continue;
    const tmp=`/tmp/claude-0/-home-user-crm/9822160d-7d4c-5a0c-b763-6d89aa660c2f/scratchpad/frames/${v.name}`; fs.rmSync(tmp,{recursive:true,force:true}); fs.mkdirSync(tmp,{recursive:true});
    const ctx=await b.newContext({viewport:{width:v.w,height:v.h}}); const p=await ctx.newPage();
    await p.goto('file://'+v.html,{waitUntil:'load'}); await p.evaluate(()=>document.fonts.ready);
    const N=Math.round(v.dur*v.fps);
    for(let i=0;i<N;i++){ const t=i*1000/v.fps;
      await p.evaluate(t=>document.getAnimations().forEach(a=>{a.pause();a.currentTime=t;}),t);
      await p.screenshot({path:`${tmp}/f${String(i).padStart(4,'0')}.png`,omitBackground:v.alpha}); }
    await ctx.close(); fs.mkdirSync(v.out,{recursive:true}); const inp=['-y','-loglevel','error','-framerate',String(v.fps),'-i',`${tmp}/f%04d.png`];
    for(const o of v.outs){ const out=path.join(v.out,`${v.name}.${o}`);
      if(o==='mp4') execFileSync('ffmpeg',[...inp,'-c:v','libx264','-pix_fmt','yuv420p','-crf','17','-preset','slow','-movflags','+faststart',out]);
      if(o==='webm') execFileSync('ffmpeg',[...inp,'-c:v','libvpx-vp9','-pix_fmt','yuva420p','-b:v','0','-crf','24','-auto-alt-ref','0',out]);
      if(o==='mov') execFileSync('ffmpeg',[...inp,'-c:v','prores_ks','-profile:v','4444','-pix_fmt','yuva444p10le',out]);
      if(o==='gif') execFileSync('ffmpeg',[...inp,'-vf','fps=25,scale=400:-1:flags=lanczos,split[a][b];[a]palettegen=max_colors=96[p];[b][p]paletteuse=dither=sierra2_4a','-loop','0',out]);
    }
    // poster frame (last frame) for previews
    fs.copyFileSync(`${tmp}/f${String(N-1).padStart(4,'0')}.png`, path.join(v.out,`${v.name}-poster.png`));
    console.log('done',v.name,N);
  }
  await b.close();
})();
