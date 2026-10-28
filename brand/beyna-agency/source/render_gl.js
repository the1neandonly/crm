const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});
await p.goto('file://'+process.argv[2],{waitUntil:'load'});await p.evaluate(()=>document.fonts.ready);
await p.pdf({path:process.argv[3],width:'1920px',height:'1080px',printBackground:true});await b.close();})();
