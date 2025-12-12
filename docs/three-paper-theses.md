# Three Competing Paper Theses

*Trail Stack Framework: Choose Your Spine*

---

## The Trail Stack Model (Shared Foundation)

| Trail Type | Name | What It Captures | Method Anchor | Tool Anchor |
|------------|------|------------------|---------------|-------------|
| **I** | Reflective/Narrative | "What happened, who involved, what felt, what constrained" | Ethics Pathways | SHUFFLE corpus, pyramids |
| **II** | Graph/Trace | "What moves, in what sequence, with what semantic links" | Fuzzy Linkography | Git commits, POML chains |
| **III** | Contract/Integrity | "What must be true for export to be safe" | Hoare Logic | stud_skeleton, MASTER |

**Synthesis Claim (all three theses share this):**

> WAG is trail-native because it supports all three trail types simultaneously: reflective (I), summarizable (II), and enforceable (III).

---

## THESIS A: The **Governance Paper**

### Core Argument

> Trails are not documentation—they are governance infrastructure. Without multi-layer trails (I+II+III), accountability diffuses, repair becomes global, and ethics engagement reduces to performance.

### Contributions

1. **C1 (Conceptual):** Trail-first account of creative AI work where integrity/ethics are *flows in practice* enforced by the trail stack, not checklists appended post-hoc

2. **C2 (Design Implication):** "Tools that reveal their own inadequacies"—second-order features that surface the capability cliff instead of hiding it

3. **C3 (Method):** Capability cliff as research site: where expertise gaps appear, what they reveal, what scaffolding would matter

### What Goes in Paper vs Notes

| In Paper | In Notes (Trailbook) |
|----------|---------------------|
| The governance claim + three failure modes | Full TILTH postmortem with screenshots |
| Capability cliff taxonomy (3 cliffs) | Complete error log transcripts |
| Design implication: "reveal inadequacies" | Raw "I got over my head" diary entries |
| Shilton/Meadows/Lessig hooks | All SHUFFLE quotes (60+) |
| stud_skeleton as postcondition example | Full JSON schemas |
| Figure: governance loop diagram | Linkograph of all 150+ hours |

### Key Question This Thesis Answers

> **What is the ethical significance of being over your head?**

### Why Choose A

- Strongest alignment with LMC-6650 "values in design" frame
- The "confession" becomes a contribution
- Ethics Pathways does the heavy lifting on the reflective layer
- Less technical implementation burden in the paper itself

---

## THESIS B: The **Systems Paper**

### Core Argument

> Export gating via postconditions is the missing mechanism in LLM-mediated creative tools. The WERE/WEAVER/MASTER pattern (visualize → rebuild → validate) operationalizes "parse, don't validate" in 3D geometry—and the pattern generalizes to any domain where structural coherence matters.

### Contributions

1. **C1 (Systems):** A three-tool repair pipeline (WERE/WEAVER/MASTER) that gates export via Hoare-style postconditions on ownership graphs

2. **C2 (Pattern):** The "void management" design pattern: bounded possibility space (9×9 grid) + tetrad operators + chat layer = complexity cannot grow unboundedly

3. **C3 (Evaluation):** Falsifiable prediction: void-managed systems sustain >20 modifications without coherence collapse; scene-managed systems collapse at 10–15

### What Goes in Paper vs Notes

| In Paper | In Notes (Trailbook) |
|----------|---------------------|
| Full WERE/WEAVER/MASTER architecture | Implementation diffs and bug fixes |
| stud_skeleton JSON spec | All edge cases encountered |
| Hoare pre/post formalization | Failed validation attempts |
| Void vs scene comparison table | TILTH full collapse log |
| Evaluation protocol (20+ mods test) | Raw testing session transcripts |
| Figure: ownership graph visualization | 50+ screenshots of broken states |

### Key Question This Thesis Answers

> **What makes export safe?**

### Why Choose B

- Strongest technical contribution
- Clear evaluation path (falsifiable)
- Less reliance on "I felt confused" (more on "the system detected error")
- Could submit to CHI Engineering track or UIST

---

## THESIS C: The **Method Paper**

### Core Argument

> Creative AI work generates traces too big to inspect directly. We adapt Fuzzy Linkography to LLM-mediated design and layer in Ethics Pathways as a reflective annotation scheme—creating a two-layer summarization method that is both *automatic* (II: semantic graphs) and *interpretive* (I: stakeholder/barrier/affect mapping).

### Contributions

1. **C1 (Method):** Hybrid summarization: Fuzzy Linkography (automated, graph) + Ethics Pathways (manual, reflective) = legible overview with affective grounding

2. **C2 (Application):** Application to 150+ hours of LLM-mediated creative work: 4 project phases (TILTH → Thousand-Tetrad → HOLO → TRACTOR) as linkograph with Ethics Pathways annotation

3. **C3 (Claim):** Reflective trails (I) cannot replace trace trails (II), and vice versa—both are needed for *legibility at scale + meaning in context*

### What Goes in Paper vs Notes

| In Paper | In Notes (Trailbook) |
|----------|---------------------|
| Linkograph of 4 phases | Full commit-level linkograph |
| Ethics Pathways mapping table | Per-incident diary entries |
| Semantic similarity method | Raw cosine distances |
| Hybrid summarization figure | Complete annotation spreadsheet |
| What automated vs interpretive catches | Discrepancies between I and II |
| Figure: 4-phase linkograph with annotations | Full-resolution graph |

### Key Question This Thesis Answers

> **How do you make 150 hours of LLM collaboration legible?**

### Why Choose C

- Strongest method contribution (novel combination)
- Extends two recent papers (2024, 2025)
- Lower implementation burden (summarization, not systems)
- Could submit to CHI Methods track or DIS

---

## Decision Matrix

| Criterion | Thesis A (Governance) | Thesis B (Systems) | Thesis C (Method) |
|-----------|----------------------|--------------------|--------------------|
| **Technical depth required** | Low | High | Medium |
| **Evaluation burden** | Interpretive (reflection quality) | Empirical (20+ mod test) | Comparative (auto vs manual) |
| **Primary audience** | Ethics/values HCI | Engineering/systems HCI | Methods/design research |
| **Confession → contribution** | Central | Peripheral | Moderate |
| **Dependence on prior work** | Ethics Pathways | LDraw/Hoare | Fuzzy Linkography |
| **Figure-heaviness** | Moderate | High (architecture diagrams) | High (linkographs) |
| **Venue fit** | DIS, CHI subcommittee | UIST, CHI Engineering | CHI Methods, DIS |

---

## The Sintering Operator: Claim Cards

Whichever thesis you choose, use this format to promote Notes → Paper:

```markdown
## CLAIM CARD: [Short Claim Name]

**Claim (1–2 sentences):**
> [The claim to include in paper]

**Artifact Pointer:**
[File path or URL proving it exists]

**Trail Pointers:**
- I (Reflective): [incident / stakeholder / barrier / affect note]
- II (Graph): [commit range / linkograph node]  
- III (Contract): [validation log / postcondition check]

**Theory Hook:**
[Author Year]: [Concept that grounds the claim]

**Boundary / Limitation:**
[What you couldn't do / where you were over your head]
```

---

## Example Claim Cards (One Per Thesis)

### Thesis A Claim Card

**Claim:** Without trails, artifacts become self-certifying—they claim validity by existing, without evidence of process.

**Artifact Pointer:** `/docs/paragon-essay.md` (haunted tools section)

**Trail Pointers:**
- I: "Deck transfers design time, not budget" (SHUFFLE corpus + personal reflection)
- II: Git commit `a7f3bc2` where Haunted Tools list was finalized
- III: N/A (no contract trail for this conceptual claim)

**Theory Hook:** Barthes 1957: form/concept/signification mythology

**Boundary:** No user testing of Haunted Tools—conceptual contribution only

---

### Thesis B Claim Card

**Claim:** Export gating via postconditions prevents invalid artifacts from escaping the creative session.

**Artifact Pointer:** `stud_skeleton.json`, MASTER.html

**Trail Pointers:**
- I: "I got in over my head debugging orphan studs" (Notes)
- II: 23 commits in `9c8d...` → `b3e1...` range fixing stud ownership
- III: MASTER log showing 7 blocked exports with genuine errors

**Theory Hook:** Hoare 2009: precondition/postcondition assertions

**Boundary:** Only tested on single-author models < 500 bricks

---

### Thesis C Claim Card

**Claim:** Fuzzy Linkography can summarize LLM-mediated creative work into inspectable graphs, but reflective annotation (Ethics Pathways) is still needed for affect and power dimensions.

**Artifact Pointer:** Project phase linkograph (Fig. 3)

**Trail Pointers:**
- I: Ethics Pathways mapping of TILTH collapse (barrier: "complexity grey")
- II: Linkograph edges with semantic similarity > 0.7
- III: N/A (summarization, not validation)

**Theory Hook:** Wong et al. 2024: ethics engagement as flow-through-practice

**Boundary:** Manual annotation took 6 hours; no crowd-sourced validation

---

## My Recommendation

**Start with Thesis A (Governance)** because:

1. Your "over my head" experience is *central*, not embarrassing
2. The LMC-6650 frame (values in design) demands it
3. Ethics Pathways does the structural work for Type I trails
4. You already have the SHUFFLE corpus as reflective evidence
5. The confession becomes a **design implication** ("tools that reveal their own inadequacies")

Then **steal from B and C** as needed:
- From B: stud_skeleton as the **single worked example** of Type III
- From C: One **linkograph figure** of the 4-phase project arc as Type II evidence

---

## Next Move

Pick a thesis. I'll build:

1. **Paper skeleton** (section headings + paragraph-level goals)
2. **Claim Card template** pre-populated for your 5 major artifacts
3. **Notes structure** (Trailbook sections matching paper claims)
4. **Figure list** with specifications

Or: tell me to revise the theses themselves.
