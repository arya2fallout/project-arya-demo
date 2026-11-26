import json, unittest, io
from unittest.mock import patch
import benchmark as b
class Tests(unittest.TestCase):
    def test_baseline(self):
        rows=b.baseline();self.assertEqual(len(rows),35);self.assertTrue(all(r[3] for r in rows))
    def test_eval(self):
        q=b.load()['questions'][0];self.assertEqual(b.evaluate(q['expected_answer']+' '+q['expected_id'],q),(True,True));self.assertEqual(b.evaluate(q['expected_answer'],q),(True,False))
        absent=b.load()['questions'][-1];self.assertEqual(b.evaluate('UNKNOWN',absent),(True,None));self.assertEqual(b.evaluate('invented',absent),(False,None))
    def test_prompt(self):
        f=b.load(); q=f['questions'][0];d=f['documents'][0];self.assertIn(d['id'],b.prompt_for(q['question'],d,True));self.assertNotIn(d['id'],b.prompt_for(q['question'],d,False))
    def test_mock_inference(self):
        payload={'response':'sample','eval_count':20,'eval_duration':1000000000,'done':True}
        with patch.object(b.OPENER,'open',return_value=io.BytesIO(json.dumps(payload).encode())) as op:
            row=b.local_generate('fixture-model','fixture question',5)
            self.assertEqual(row['decode_tokens_per_second'],20.0);self.assertEqual(op.call_args.args[0].full_url,'http://127.0.0.1:11434/api/generate')
            self.assertEqual(json.loads(op.call_args.args[0].data)['options']['temperature'],0)
    def test_invalid_response(self):
        with patch.object(b.OPENER,'open',return_value=io.BytesIO(b'{"response":"partial","done":false}')):
            with self.assertRaises(ValueError): b.local_generate('fixture-model','fixture',5)
    def test_csv_formula_protection(self):
        self.assertEqual(b.safe_csv_row({'response':'=1+1','error':'  @SUM(1)','number':-2,'fact_match':True,'text':'ordinary text'}),{'response':"'=1+1",'error':"'  @SUM(1)",'number':-2,'fact_match':True,'text':'ordinary text'})
    def test_port(self):
        with self.assertRaises(ValueError): b.local_generate('fixture-model','fixture',5,70000)
if __name__=='__main__': unittest.main()
