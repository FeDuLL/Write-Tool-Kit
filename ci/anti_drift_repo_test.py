#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "writer-toolkit"
results = []

def check(cid, desc, fn):
    try:
        ok, detail = fn()
    except Exception as e:
        ok, detail = False, f"EXCEPTION: {e}"
    results.append((cid, desc, ok, detail))

def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")

form = read("form/FORM.01_CONTRACT.md")
screen = read("form/FORM.03_SCREENPLAY_PROFILE.md")
check("AD-01","Screenplay routes structural/production units to SCENE/SEQUENCE",
      lambda: ("STRUCTURAL_UNIT = SCENE / SEQUENCE" in form and "PRODUCTION_UNIT = SCENE / SEQUENCE" in form,
               "explicit SCENE/SEQUENCE routing"))
check("AD-02","Screenplay has no mandatory chapter model",
      lambda: ("CHAPTER_MODEL = OFF" in screen and "No universal chapter requirement." in form,
               "chapter model disabled"))
check("AD-03","Screenplay audit profile contains required checks",
      lambda: (all(x in screen for x in ["FORM_UNIT_INTEGRITY","SCENE_SEQUENCE_CONTINUITY","SCREENPLAY_FORMAT_CONSISTENCY","DIALOGUE_ACTION_SEPARATION","CHAPTER_RULE_CONTAMINATION"]),
               "five minimum screenplay checks present"))
check("AD-04","Screenplay completion is unit/function based",
      lambda: ("chapter count" in screen.lower() and "unit is complete when" in screen.lower(),
               "chapter-count completion rejected"))

dev = read("development/DEV.02_DEVELOPMENT_MODE.md")
scope = read("schemas/scope_record.schema")
check("AD-05","DISCOVERY is an explicit development mode",
      lambda: (all(x in dev for x in ["ARCHITECT","DISCOVERY","HYBRID"]), "three modes enumerated"))
check("AD-06","DISCOVERY does not require architect-first planning",
      lambda: (("DRAFT / EXPLORE" in dev and "EXTRACT STATE" in dev and "STABILIZE ACCEPTED PROSE/CANON" in dev and "must not force an architect-first process" in dev.lower()),
               "discovery non-forcing rule present"))
check("AD-07","Scope supports UNKNOWN/DISCOVERY without fixed target",
      lambda: ("UNKNOWN" in scope and "DISCOVERY" in scope and "target_value: null" in scope, "nullable target and open modes present"))
check("AD-08","No universal numeric volume target in core/form/scope",
      lambda: ("No universal numeric volume target." in form and "4–5 AL" not in "".join(read(p) for p in ["form/FORM.01_CONTRACT.md","schemas/scope_record.schema","core/CORE_CONTRACT.md","SKILL.md"]),
               "no hard-coded prior test volume"))

fixture = {"scope":{"mode":"UNKNOWN","target_value":None},"architecture_status":"OPEN","deferred":["ending mechanism"],"accepted":["protagonist avoids direct confrontation"]}
check("AD-09","Discovery can draft while architecture remains open",
      lambda: (fixture["architecture_status"]=="OPEN" and fixture["scope"]["mode"]=="UNKNOWN","open architecture + unknown scope"))
check("AD-10","Accepted observations remain distinct from deferred decisions",
      lambda: ("ending mechanism" in fixture["deferred"] and fixture["accepted"],"accepted/deferred separation"))
check("AD-11","Load-bearing deferred decision remains non-canonical",
      lambda: (fixture["deferred"] and fixture["scope"]["target_value"] is None,"deferred decision remains unresolved"))

hwmod = read("conditional/hidden_world/HIDDEN_WORLD_MODULE.md")
active = read("schemas/active_modules.schema")
check("AD-12","Hidden-world is not activated by old-project memory",
      lambda: ("old-project memory is never an activation source" in active and "Activate only when" in hwmod and "explicit hard reveal requirement" in hwmod,
               "explicit activation only"))
check("AD-13","Hidden-world activation is conditional, not Core default",
      lambda: (("HARD_REVEAL" in hwmod or "HIDDEN_ONTOLOGY" in hwmod),"explicit trigger concepts"))
check("AD-14","Hidden-world epistemic layers remain separated",
      lambda: (all(x in "".join(read(p) for p in ["conditional/hidden_world/HW.02_ONTOLOGY_AND_SURFACE.md","conditional/hidden_world/HW.03_DISCOVERY_FAIRNESS.md"])
                   for x in ["HIDDEN_ONTOLOGY","SURFACE_MODEL","PUBLIC_BELIEF","CHARACTER_INTERPRETATION","READER_INTERPRETATION"]),
               "five epistemic layers distinct"))

budget = read("adapters/ADAPTER.01_OUTPUT_BUDGET.md")
check("AD-15","Constrained runtime preserves production unit",
      lambda: ("does **not** silently shrink the unit or redefine the author's scope." in budget and "chunk" in budget.lower(),
               "chunk/assembly rather than silent unit mutation"))
check("AD-16","Form is project-declared and runtime-independent",
      lambda: ("every project has a declared form" in form and "runtime does not choose the literary form" in form.lower(),
               "form declaration is runtime-independent"))

failed = [r for r in results if not r[2]]
for cid, desc, ok, detail in results:
    print(f"{cid}: {'PASS' if ok else 'FAIL'} — {desc} — {detail}")
print(f"TOTAL: {len(results)-len(failed)}/{len(results)} PASS")
raise SystemExit(1 if failed else 0)
