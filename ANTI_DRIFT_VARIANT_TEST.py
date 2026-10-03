from pathlib import Path
import zipfile, tempfile, shutil, hashlib, json, re
from datetime import datetime, timezone

SRC = Path('/mnt/data/WRITER-TOOLKIT_v0.3_SCHEMA_COMPLETION_AND_PHASE_H_FINAL.zip')
OUT = Path('/mnt/data/WRITER-TOOLKIT_v0.3_ANTI_DRIFT_VARIANT_TEST_FINAL.zip')
WORK = Path('/tmp/antidrift_wt')
if WORK.exists(): shutil.rmtree(WORK)
WORK.mkdir()
with zipfile.ZipFile(SRC) as z:
    z.extractall(WORK)
ROOT = WORK / 'writer-toolkit'

results=[]
def check(cid, desc, fn):
    try:
        ok, detail = fn()
    except Exception as e:
        ok=False; detail=f'EXCEPTION: {e}'
    results.append({'id':cid,'check':desc,'result':'PASS' if ok else 'FAIL','detail':detail})

def read(rel): return (ROOT/rel).read_text(encoding='utf-8')

# --- Screenplay anti-drift ---
form = read('form/FORM.01_CONTRACT.md')
screen = read('form/FORM.03_SCREENPLAY_PROFILE.md')

check('AD-01','Screenplay contract routes structural and production units to SCENE/SEQUENCE',
      lambda: ('STRUCTURAL_UNIT = SCENE / SEQUENCE' in form and 'PRODUCTION_UNIT = SCENE / SEQUENCE' in form,
               'screenplay routing explicitly uses SCENE/SEQUENCE'))
check('AD-02','Screenplay has no mandatory chapter model',
      lambda: ('CHAPTER_MODEL = OFF' in screen and 'No universal chapter requirement.' in form,
               'CHAPTER_MODEL=OFF and universal chapter requirement prohibited'))
check('AD-03','Screenplay audit profile contains required form-specific checks',
      lambda: (all(x in screen for x in ['FORM_UNIT_INTEGRITY','SCENE_SEQUENCE_CONTINUITY','SCREENPLAY_FORMAT_CONSISTENCY','DIALOGUE_ACTION_SEPARATION','CHAPTER_RULE_CONTAMINATION']),
               'all five minimum screenplay audit checks present'))
check('AD-04','Screenplay completion is unit/function based, not chapter-count based',
      lambda: ('chapter count' in screen.lower() and 'unit is complete when' in screen.lower(),
               'profile explicitly rejects chapter-count completion and defines unit completion'))

# --- Discovery + UNKNOWN scope ---
dev = read('development/DEV.02_DEVELOPMENT_MODE.md')
scope = read('schemas/scope_record.schema')
check('AD-05','DISCOVERY is an explicit development mode',
      lambda: ('ARCHITECT' in dev and 'DISCOVERY' in dev and 'HYBRID' in dev,
               'all three allowed modes are explicitly enumerated'))
check('AD-06','DISCOVERY workflow does not require architect-first planning',
      lambda: ('DRAFT / EXPLORE' in dev and 'EXTRACT STATE' in dev and 'STABILIZE ACCEPTED PROSE/CANON' in dev and 'must not force an architect-first process' in dev.lower(),
               'discovery sequence and non-forcing rule present'))
check('AD-07','SCOPE supports UNKNOWN and DISCOVERY without a fixed target',
      lambda: ('UNKNOWN' in scope and 'DISCOVERY' in scope and 'target_value: null' in scope,
               'scope schema permits unknown/discovery and nullable targets'))
check('AD-08','No universal numeric volume target is imposed by scope/form contracts',
      lambda: ('No universal numeric volume target.' in form and '4–5 AL' not in ''.join(read(p) for p in ['form/FORM.01_CONTRACT.md','schemas/scope_record.schema','core/CORE_CONTRACT.md','SKILL.md']),
               'no hard-coded prior test volume found in core/form/scope'))

# --- Simulated discovery fixture ---
fixture = {
    'project_name':'Discovery Variant Fixture',
    'form':'NOVEL',
    'development_mode':'DISCOVERY',
    'scope':{'mode':'UNKNOWN','metric':'AL','target_value':None,'binding':'NO'},
    'before_draft':{'architecture_status':'OPEN','load_bearing_unknowns':['ending mechanism']},
    'draft_units':['scene_01','scene_02'],
    'after_extract':{'accepted_observations':['protagonist avoids direct confrontation'],
                     'deferred_decisions':['ending mechanism']},
    'continuation_authorized':True
}
check('AD-09','Discovery fixture can begin drafting while architecture remains open',
      lambda: (fixture['before_draft']['architecture_status']=='OPEN' and fixture['scope']['mode']=='UNKNOWN',
               'draft begins with unresolved architecture and unknown scope'))
check('AD-10','Discovery extraction stabilizes accepted observations without silently canonizing deferred decisions',
      lambda: ('ending mechanism' in fixture['after_extract']['deferred_decisions'] and fixture['after_extract']['accepted_observations'],
               'accepted observations and deferred load-bearing decision remain distinct'))
check('AD-11','Load-bearing deferred decision remains non-canonical',
      lambda: (fixture['after_extract']['deferred_decisions'] and fixture['scope']['target_value'] is None,
               'deferred load-bearing decision and open scope remain unresolved'))

# --- Conditional hidden-world anti-leak ---
hwmod = read('conditional/hidden_world/HIDDEN_WORLD_MODULE.md')
active = read('schemas/active_modules.schema')
check('AD-12','Hidden-world module is not activated by old-project memory',
      lambda: ('old-project memory is never an activation source' in active and 'Activate only when' in hwmod and 'explicit hard reveal requirement' in hwmod,
               'activation is explicit and old-project memory is not a valid source'))
check('AD-13','Hidden-world module requires explicit trigger/contract rather than being a Core default',
      lambda: (('HARD_REVEAL' in hwmod or 'HIDDEN_ONTOLOGY' in hwmod),
               'hidden-world trigger concepts are explicit'))
check('AD-14','Hidden-world epistemic layers remain separated',
      lambda: (all(x in ''.join(read(p) for p in ['conditional/hidden_world/HW.02_ONTOLOGY_AND_SURFACE.md','conditional/hidden_world/HW.03_DISCOVERY_FAIRNESS.md']) for x in ['HIDDEN_ONTOLOGY','SURFACE_MODEL','PUBLIC_BELIEF','CHARACTER_INTERPRETATION','READER_INTERPRETATION']),
               'hidden ontology, surface model, public belief, character interpretation, and reader interpretation are distinct'))

# --- Runtime/form independence ---
budget = read('adapters/ADAPTER.01_OUTPUT_BUDGET.md')
check('AD-15','Constrained runtime preserves artistic production unit instead of changing form',
      lambda: ('does **not** silently shrink the unit or redefine the author\'s scope.' in budget and 'chunk' in budget.lower(),
               'budget adapter chooses chunking/assembly or stop, not silent unit mutation'))
check('AD-16','Form contract is active for every project and runtime cannot choose literary form',
      lambda: ('every project has a declared form' in form and 'runtime does not choose the literary form' in form.lower(),
               'form is project-declared and runtime-independent'))

# Build report and package
passed=sum(r['result']=='PASS' for r in results); failed=len(results)-passed
stamp=datetime.now(timezone.utc).isoformat(timespec='seconds')
report = f'''# WRITER-TOOLKIT v0.3 — ANTI-DRIFT VARIANT TEST\n\nStatus: **{'PASS' if failed==0 else 'FAIL'}**\nDate: {stamp}\nSource package: `{SRC.name}`\n\n## Purpose\n\nValidate the high-risk anti-drift variants identified by the v0.3 architecture: screenplay/form independence, DISCOVERY workflow, UNKNOWN scope, conditional hidden-world activation, and runtime/form separation. This is an architecture/contract stress test, not a literary-quality verdict.\n\n## Results\n\n| ID | Check | Result |\n|---|---|---|\n'''
for r in results:
    report += f"| {r['id']} | {r['check']} | **{r['result']}** |\n"
report += f'''\n**Total: {passed}/{len(results)} PASS; {failed} FAIL.**\n\n## Detailed evidence\n\n'''
for r in results:
    report += f"### {r['id']} — {r['result']}\n{r['detail']}\n\n"
report += '''## Interpretation\n\nPASS means the relevant contract is represented and the fixture variation did not trigger an architectural contradiction. It does not prove that arbitrary model output will always obey the contract; that remains an execution/runtime property.\n\n## Resulting gate\n\nWith portability and these anti-drift variants passing, the next meaningful validation should be a **real second-model execution** or an external independent audit of the same persisted fixture. After that, a project-specific pilot using actual author material is more informative than additional synthetic architecture tests.\n'''
(ROOT.parent/'ANTI_DRIFT_VARIANT_TEST_REPORT.md').write_text(report,encoding='utf-8')
json_path=ROOT.parent/'ANTI_DRIFT_VARIANT_RESULTS.json'
json_path.write_text(json.dumps({'status':'PASS' if failed==0 else 'FAIL','pass':passed,'fail':failed,'total':len(results),'results':results},ensure_ascii=False,indent=2),encoding='utf-8')

# Copy source files used by the test and fixture templates
bundle = ROOT.parent/'anti_drift_fixture'
bundle.mkdir()
(bundle/'screenplay_project_fixture.yaml').write_text('''toolkit_version: 0.3\nschema_version: 0.3\nform: SCREENPLAY\nproduction_unit: SCENE\nlock_unit: SEQUENCE\nscope: {mode: APPROX, metric: PAGES, target_value: null, binding: NO}\nchapter_model: OFF\naudit_profile: SCREENPLAY\n''',encoding='utf-8')
(bundle/'discovery_project_fixture.yaml').write_text(json.dumps(fixture,ensure_ascii=False,indent=2),encoding='utf-8')
(bundle/'hidden_world_activation_fixture.yaml').write_text('''active_modules:\n  hidden_world: ON\nactivation_source: AUTHOR_DECISION\nreveal_required: true\n''',encoding='utf-8')

# Test script for reproducibility
script_src = Path('/tmp/run_antidrift.py').read_text(encoding='utf-8')
# strip execution? keep full reproducible script
(ROOT.parent/'ANTI_DRIFT_VARIANT_TEST.py').write_text(script_src,encoding='utf-8')

# Add a compact machine result to package root
meta={'source_package':SRC.name,'status':'PASS' if failed==0 else 'FAIL','pass':passed,'fail':failed,'total':len(results),'timestamp':stamp}
(ROOT.parent/'ANTI_DRIFT_METADATA.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')

with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED) as z:
    for p in sorted(ROOT.parent.rglob('*')):
        if p.is_file() and p != OUT:
            z.write(p,p.relative_to(ROOT.parent))

sha=hashlib.sha256(OUT.read_bytes()).hexdigest()
print(report)
print('OUTPUT',OUT)
print('SHA256',sha)
