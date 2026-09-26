import unittest
from run_example import collect, csv_text, identifier

class ApiFake:
    def __init__(self, status='SUCCEEDED'):
        self.calls=[]
        self.status=status
    def request(self, path, method='GET', body=None):
        self.calls.append((path,method,body))
        if method=='POST':return {'data':{'id':'Run1','status':self.status,'defaultDatasetId':'Dataset1'}}
        return [{'title':'Engineer','metadata':{'remote':True}}]

class RunnerTests(unittest.TestCase):
    def test_one_bounded_run_and_export(self):
        api=ApiFake()
        rows=collect(api,{'actor':'peerless_columbine~multi-ats-jobs-scraper','input':{'maxJobsPerCompany':5}})
        self.assertEqual(rows[0]['title'],'Engineer')
        self.assertIn('maxTotalChargeUsd=0.15',api.calls[0][0])
        self.assertEqual(sum(c[1]=='POST' for c in api.calls),1)
    def test_failed_run_does_not_export(self):
        api=ApiFake('FAILED')
        with self.assertRaises(RuntimeError):collect(api,{'actor':'peerless_columbine~multi-ats-jobs-scraper','input':{}})
        self.assertEqual(len(api.calls),1)
    def test_csv_escapes_formula_and_nested_data(self):
        text=csv_text([{'title':'=1+1','metadata':{'a':1}}])
        self.assertIn("'=1+1",text)
        self.assertIn('metadata',text)
    def test_identifiers_cannot_change_destination(self):
        for value in ['../other','https://evil.example','a?token=x']:
            with self.assertRaises(RuntimeError):identifier(value)
