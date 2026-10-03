#!/usr/bin/env python3
import json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
native = ROOT / "writer-toolkit"
universal = ROOT / "writer-toolkit-universal"
expected = [
"creative_brief.schema","project_state.schema","scope_record.schema","style_baseline.schema",
"style_lock.schema","capability_profile.schema","active_modules.schema","hard_requirements.schema",
"deviation_record.schema","ai_decided.schema","audit_coverage.schema","evidence.schema",
"change_log.schema","manuscript.schema","handoff.schema"
]
fails=[]

for name in expected:
    p=native/"schemas"/name
    if not p.is_file(): fails.append(f"missing schema: {name}"); continue
    txt=p.read_text(encoding="utf-8")
    if not any(line.strip() in ('schema_version: "0.3"', "schema_version: '0.3'", "schema_version: 0.3") for line in txt.splitlines()):
        fails.append(f"schema_version != 0.3: {name}")
inv=(native/"schemas"/"SCHEMA_INVENTORY.md").read_text(encoding="utf-8")
for name in expected:
    if name not in inv: fails.append(f"inventory missing: {name}")
u=(universal/"40_SCHEMAS.txt").read_text(encoding="utf-8")
for name in expected:
    if name not in u: fails.append(f"universal parity missing: {name}")

result=json.loads((ROOT/"SCHEMA_AND_PHASE_H_RESULTS.json").read_text(encoding="utf-8"))
if result.get("overall")!="PASS" or result.get("pass")!=16 or result.get("fail")!=0:
    fails.append("SCHEMA_AND_PHASE_H_RESULTS.json is not 16/16 PASS")
required_ids={"SCHEMA-01","SCHEMA-02","SCHEMA-03",*(f"TEST-{i:02d}" for i in range(1,14))}
actual={x.get("id") for x in result.get("results",[])}
missing=sorted(required_ids-actual)
if missing: fails.append("missing result IDs: "+", ".join(missing))

print(f"SCHEMA/P H RESULT: {'PASS' if not fails else 'FAIL'}")
print(f"Canonical schemas checked: {len(expected)}")
print("Phase-H regression result: ", result.get("pass"), "/", result.get("pass",0)+result.get("fail",0))
for x in fails: print("FAIL:",x)
raise SystemExit(1 if fails else 0)
, txt, re.MULTILINE):
        fails.append(f"schema_version != 0.3: {name}")
inv=(native/"schemas"/"SCHEMA_INVENTORY.md").read_text(encoding="utf-8")
for name in expected:
    if name not in inv: fails.append(f"inventory missing: {name}")
u=(universal/"40_SCHEMAS.txt").read_text(encoding="utf-8")
for name in expected:
    if name not in u: fails.append(f"universal parity missing: {name}")

result=json.loads((ROOT/"SCHEMA_AND_PHASE_H_RESULTS.json").read_text(encoding="utf-8"))
if result.get("overall")!="PASS" or result.get("pass")!=16 or result.get("fail")!=0:
    fails.append("SCHEMA_AND_PHASE_H_RESULTS.json is not 16/16 PASS")
required_ids={"SCHEMA-01","SCHEMA-02","SCHEMA-03",*(f"TEST-{i:02d}" for i in range(1,14))}
actual={x.get("id") for x in result.get("results",[])}
missing=sorted(required_ids-actual)
if missing: fails.append("missing result IDs: "+", ".join(missing))

print(f"SCHEMA/P H RESULT: {'PASS' if not fails else 'FAIL'}")
print(f"Canonical schemas checked: {len(expected)}")
print("Phase-H regression result: ", result.get("pass"), "/", result.get("pass",0)+result.get("fail",0))
for x in fails: print("FAIL:",x)
raise SystemExit(1 if fails else 0)
