'use strict';const assert=require('node:assert/strict');const fs=require('node:fs');const path=require('node:path');const F=JSON.parse(fs.readFileSync(path.join(__dirname,'fixtures.json'),'utf8'));const D=require('./core.js');
let count=0;for(const q of F.questions){assert.equal(D.retrieve(q.question,F.documents)?.id||null,q.expected_id,q.id);count++}
const valid={request_id:'one',operation:'read',path:'docs/lab-notes.txt',approved:false,expires_at:10};
const checks=[[valid,new Set(),1,true],[{...valid,operation:'write'},new Set(),1,false],[{...valid,operation:'write',approved:true},new Set(),1,true],[{...valid,path:'../outside.txt'},new Set(),1,false],[{...valid,path:'private/secret.txt'},new Set(),1,false],[{...valid,operation:'delete'},new Set(),1,false],[valid,new Set(['one']),1,false],[valid,new Set(),10,false],[{...valid,expires_at:'10'},new Set(),1,false],[{...valid,request_id:''},new Set(),1,false]];
for(const [r,s,n,e] of checks)assert.equal(D.policy(r,s,n).allowed,e);
console.log(`${count} retrieval fixture checks and ${checks.length} policy cases passed (synthetic).`);
