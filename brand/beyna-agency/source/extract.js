// For each template: capture every .t text block (position, font, runs) and an art-only render with text hidden.
const {chromium}=require('playwright'); const fs=require('fs'); const path=require('path');
(async()=>{
  const [,,tplFile,artDir,outJson]=process.argv; const tpls=JSON.parse(fs.readFileSync(tplFile));
  fs.mkdirSync(artDir,{recursive:true}); const b=await chromium.launch(); const res=[];
  for(const t of tpls){
    const ctx=await b.newContext({viewport:{width:t.w,height:t.h}}); const p=await ctx.newPage();
    await p.goto('file://'+t.html,{waitUntil:'load'}); await p.evaluate(()=>document.fonts.ready);
    const boxes=await p.evaluate(()=>[...document.querySelectorAll('.t')].map(el=>{
      const cs=getComputedStyle(el), r=el.getBoundingClientRect(); const up=cs.textTransform==='uppercase';
      const runs=[]; const walk=(n)=>{ for(const c of n.childNodes){
        if(c.nodeType===3){ const s=getComputedStyle(c.parentElement); let tx=c.textContent.replace(/\s+/g,' '); if(up) tx=tx.toUpperCase();
          if(tx) runs.push({text:tx,color:s.color,weight:s.fontWeight,family:s.fontFamily.split(',')[0].replace(/['"]/g,'').trim()}); }
        else if(c.nodeName==='BR') runs.push({br:true}); else walk(c); } }; walk(el);
      const bg=cs.backgroundColor, bc=cs.borderTopColor, bw=parseFloat(cs.borderTopWidth);
      return {x:r.left,y:r.top,w:r.width,h:r.height,size:parseFloat(cs.fontSize),lh:cs.lineHeight==='normal'?null:parseFloat(cs.lineHeight),
        ls:cs.letterSpacing==='normal'?0:parseFloat(cs.letterSpacing),align:cs.textAlign,dir:cs.direction,runs,
        padL:parseFloat(cs.paddingLeft),padT:parseFloat(cs.paddingTop),bg,border:bw>0?bc:null,bw,radius:parseFloat(cs.borderTopLeftRadius)};}));
    await p.addStyleTag({content:'.t{visibility:hidden!important}'});
    const art=path.join(artDir,`${t.group}-${t.name}.png`); await p.screenshot({path:art});
    res.push({...t,art,boxes}); await ctx.close();
  }
  fs.writeFileSync(outJson,JSON.stringify(res)); await b.close(); console.log('extracted',res.length);
})();
