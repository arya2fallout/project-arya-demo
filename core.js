(function(root){
  'use strict';
  const stop=new Set('a an the is are was were what which who when where how many much long me tell give for of to in on at by under before does do used uses with be and or it this that specified example fictional target day scheduled period duration number method size due routine policy'.split(' '));
  const tokens=s=>new Set((String(s).toLowerCase().match(/[a-z0-9]+/g)||[]).filter(w=>!stop.has(w)));
  function retrieve(question, docs){
    const q=tokens(question);
    const ranked=docs.map(d=>({doc:d,score:[...q].filter(t=>tokens(d.title+' '+d.text).has(t)).length})).sort((a,b)=>b.score-a.score||a.doc.id.localeCompare(b.doc.id));
    if(!ranked.length||ranked[0].score<1||(ranked[1]&&ranked[1].score===ranked[0].score))return null;
    return ranked[0].doc;
  }
  const allowedPaths=new Set(['docs/lab-notes.txt','docs/benchmark.txt']);
  function policy(req,seen=new Set(),now=0){
    if(!req||typeof req.request_id!=='string'||!req.request_id.trim()||typeof req.expires_at!=='number'||!Number.isFinite(req.expires_at))return {allowed:false,reason:'Malformed request'};
    if(req.expires_at<=now)return {allowed:false,reason:'Expired request'};
    if(seen.has(req.request_id))return {allowed:false,reason:'Duplicate request'};
    if(!['read','write'].includes(req.operation))return {allowed:false,reason:'Unsupported operation'};
    if(!allowedPaths.has(req.path))return {allowed:false,reason:'Path is outside the synthetic allowlist'};
    if(req.operation==='write'&&req.approved!==true)return {allowed:false,reason:'Explicit write approval missing'};
    return {allowed:true,reason:'Simulated policy permits request; no action executed'};
  }
  const api={retrieve,policy}; if(typeof module==='object'&&module.exports)module.exports=api; else root.AryaDemo=api;
})(globalThis);
