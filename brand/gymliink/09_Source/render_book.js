// Book: one PDF (1920x1080 per page) + optional low-res page previews.
const {chromium}=require('playwright'); const fs=require('fs'); const path=require('path');
(async()=>{
  const [,,html,pdf,prevDir]=process.argv; const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1920,height:1080}});
  await p.goto('file://'+html,{waitUntil:'load'}); await p.evaluate(()=>document.fonts.ready);
  await p.pdf({path:pdf,width:'1920px',height:'1080px',printBackground:true});
  if(prevDir){fs.mkdirSync(prevDir,{recursive:true}); const n=await p.locator('section.pg').count();
    for(let i=0;i<n;i++) await p.locator('section.pg').nth(i).screenshot({path:path.join(prevDir,`p${String(i+1).padStart(2,'0')}.png`)});}
  await b.close(); console.log('ok');
})();
