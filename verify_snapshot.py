from pathlib import Path
import json, hashlib
r=Path(__file__).resolve().parent
manifest=json.loads((r/'HASHES.json').read_text(encoding='utf-8'))
for name,digest in manifest.items():
 p=(r/name).resolve()
 assert p.parent==r, 'Unsafe manifest path'
 assert hashlib.sha256(p.read_bytes()).hexdigest()==digest, name
d=json.loads((r/'OPV2V_EXECUTION_INVENTORY.json').read_text(encoding='utf-8'))
assert len(d['jobs'])==d['completed_execution_jobs']==74
assert sum(not x['job'].startswith('latency_') for x in d['jobs'])==69
assert all(x['status']=='COMPLETED' and x['counts']['completed']==2170 for x in d['jobs'])
t=json.loads((r/'OPV2V_PAPER_TARGETS.json').read_text(encoding='utf-8'))
assert len(t['rows'])==214 and all(x['dataset']=='OPV2V' for x in t['rows'])
print('PASS: exported hashes and metadata counts; no model inference or AP recomputation performed.')
