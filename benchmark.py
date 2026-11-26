"""Project Arya: synthetic baseline and optional explicit local-only Ollama benchmark.
No third-party dependencies. No real file modifications apart from explicitly chosen CSV output.
"""
import argparse, csv, json, re, time, urllib.request, urllib.error
from pathlib import Path
from datetime import datetime, timezone
BASE=Path(__file__).resolve().parent
STOP=set('a an the is are was were what which who when where how many much long me tell give for of to in on at by under before does do used uses with be and or it this that specified example fictional target day scheduled period duration number method size due routine policy'.split())

def load():
    return json.loads((BASE/'fixtures.json').read_text(encoding='utf-8'))

def tokens(text):
    return set(re.findall(r'[a-z0-9]+', str(text).lower()))-STOP

def retrieve(question, docs):
    q=tokens(question)
    ranked=sorted(((len(q & tokens(d['title']+' '+d['text'])),d) for d in docs),key=lambda x:(-x[0],x[1]['id']))
    if not ranked or ranked[0][0]<1 or (len(ranked)>1 and ranked[1][0]==ranked[0][0]): return None
    return ranked[0][1]

def baseline():
    f=load(); rows=[]
    for q in f['questions']:
        d=retrieve(q['question'],f['documents']); actual=d['id'] if d else None
        rows.append((q['id'],q['expected_id'],actual,actual==q['expected_id']))
    return rows

def prompt_for(question, doc, context):
    if context:
        evidence=f"{doc['id']}: {doc['text']}" if doc else 'No matching evidence.'
        return ('Use only the provided fictional evidence. If the answer is not supported, respond exactly UNKNOWN. '
                'Otherwise answer with the exact fact followed by the source ID.\nEvidence: '+evidence+'\nQuestion: '+question)
    return ('Answer this question about a fictional lab. If you do not know, respond exactly UNKNOWN. '
            'If answering, give the exact fact and source ID if known.\nQuestion: '+question)

def evaluate(response, q):
    t=response.strip()
    if q['expected_id'] is None:
        return t.upper()=='UNKNOWN', None
    return q['expected_answer'].lower() in t.lower(), q['expected_id'].lower() in t.lower()

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        raise urllib.error.HTTPError(req.full_url,code,'Redirect disallowed',headers,fp)

# Fixed loopback endpoint; proxies and HTTP redirects disabled.
OPENER=urllib.request.build_opener(urllib.request.ProxyHandler({}),NoRedirect())

def local_generate(model,prompt,timeout,port=11434):
    if not 1<=port<=65535: raise ValueError('Invalid loopback port')
    payload={'model':model,'prompt':prompt,'stream':False,'options':{'temperature':0,'seed':42,'num_predict':128,'num_ctx':2048}}
    req=urllib.request.Request(f'http://127.0.0.1:{port}/api/generate',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'},method='POST')
    t=time.perf_counter()
    with OPENER.open(req,timeout=timeout) as response:
        data=json.load(response)
    elapsed=time.perf_counter()-t
    if data.get('error') or not isinstance(data.get('response'),str) or data.get('done') is not True:
        raise ValueError('Unexpected or incomplete generation response')
    count=data.get('eval_count'); duration=data.get('eval_duration')
    rate=count/(duration/1e9) if isinstance(count,(int,float)) and isinstance(duration,(int,float)) and duration>0 else None
    return {'response':data['response'],'wall_seconds':round(elapsed,6),'eval_count':count,'eval_duration_ns':duration,'decode_tokens_per_second':round(rate,4) if rate is not None else None,'prompt_eval_count':data.get('prompt_eval_count'),'prompt_eval_duration_ns':data.get('prompt_eval_duration'),'load_duration_ns':data.get('load_duration'),'done_reason':data.get('done_reason')}

FIELDS=['utc','fixture_version','model','condition','question_id','repeat','expected_id','retrieved_id','fact_match','citation_match','response','wall_seconds','eval_count','eval_duration_ns','decode_tokens_per_second','prompt_eval_count','prompt_eval_duration_ns','load_duration_ns','done_reason','error']

def safe_csv_row(row):
    # Preserve plain-text meaning while preventing spreadsheet formula interpretation.
    return {k:("'"+v if isinstance(v,str) and v.lstrip(' \t\r\n').startswith(('=','+','-','@')) else v) for k,v in row.items()}

def run_model(model,repeats,output,timeout,port):
    f=load()
    # Fail if output exists. Never overwrite prior measurement data.
    with Path(output).open('x',newline='',encoding='utf-8') as file:
        w=csv.DictWriter(file,fieldnames=FIELDS);w.writeheader()
        for repeat in range(1,repeats+1):
            for i,q in enumerate(f['questions']):
                d=retrieve(q['question'],f['documents'])
                # Alternate condition order to reduce fixed-order warmup bias.
                for ctx in ((False,True) if (repeat+i)%2 else (True,False)):
                    row={'utc':datetime.now(timezone.utc).isoformat(),'fixture_version':f['version'],'model':model,'condition':'retrieved_context' if ctx else 'no_context','question_id':q['id'],'repeat':repeat,'expected_id':q['expected_id'],'retrieved_id':d['id'] if d and ctx else None}
                    try:
                        r=local_generate(model,prompt_for(q['question'],d,ctx),timeout,port);row.update(r)
                        row['fact_match'],row['citation_match']=evaluate(r['response'],q)
                    except (OSError,ValueError,urllib.error.URLError) as e:
                        row['error']=type(e).__name__+': '+str(e)[:200]
                    w.writerow(safe_csv_row(row));file.flush()
    print(f'Saved results to {output}. Review errors and free-form quality; Expected-phrase matching is a screening metric.')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--model',help='Explicitly enable local-only Ollama inference using an already installed model')
    p.add_argument('--repeats',type=int,default=1);p.add_argument('--output');p.add_argument('--timeout',type=float,default=90);p.add_argument('--port',type=int,default=11434)
    a=p.parse_args()
    if not a.model:
        rows=baseline(); n=sum(r[3] for r in rows);print(f'Synthetic keyword smoke test: {n}/{len(rows)} expected source/abstention matches. No language model or network used.')
        for r in rows:
            if not r[3]: print('Mismatch:',r)
        return 0 if n==len(rows) else 1
    if not a.output or not 1<=a.repeats<=10 or not 1<=a.timeout<=600 or not 1<=a.port<=65535: p.error('Model mode needs a new --output path, repeats 1–10, timeout 1–600s, valid port')
    run_model(a.model,a.repeats,a.output,a.timeout,a.port);return 0
if __name__=='__main__': raise SystemExit(main())
