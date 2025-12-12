# Thesis A: The Governance Paper

**Working Title:** *Trail-Native Infrastructure: Governance, Repair, and the Capability Cliff in LLM-Mediated Creative Systems*

---

## PART 1: Paper Skeleton

### §1. Introduction (800 words)

**Goal:** Frame the problem as governance failure, not feature absence.

| Paragraph | Content | Theory Hook |
|-----------|---------|-------------|
| 1.1 | The "disclosure theatre" opening: ACM asks for itemized AI use, but symbiotic use resists itemization | Scott 1998: legibility vs mētis |
| 1.2 | The "complexity grey" failure: generative systems collapse under cumulative modification | Meadows 2008: reinforcing loops |
| 1.3 | The "haunted tools" pathology: ethics instruments perform without transferring resources | Barthes 1957: mythology |
| 1.4 | **Thesis statement:** Trails are not documentation—they are governance infrastructure. Without them, accountability diffuses, repair becomes global, ethics reduces to performance. | — |
| 1.5 | Contributions preview (C1, C2, C3) | — |
| 1.6 | Paper structure roadmap | — |

**Key Sentence (1.4):**
> "When trails are absent, artifacts become self-certifying—they claim validity by existing, without evidence of the process that produced them."

---

### §2. Related Work (1000 words)

**Goal:** Position the trail stack as synthesis of three existing traditions.

| Subsection | Content | Key Citations |
|------------|---------|---------------|
| 2.1 Ethics Engagement as Practice | Ethics as flow, not checkpoint; situated action; soft resistance | Wong et al. 2024 (Ethics Pathways), Suchman 1987, Wong 2021 |
| 2.2 Trace Summarization | Linkography; fuzzy linkography for LLM; semantic similarity | Goldschmidt 1990, Fuzzy Linkography 2025 |
| 2.3 Constraint-Based Design | Hoare logic; void management; defensive programming | Hoare 1969/2009, Dijkstra 1968, Parnas 1972 |
| 2.4 Values in Design | Values levers; leverage points; regulatory modes | Shilton 2013, Meadows 2008, Lessig 2006 |

**Gap Statement (end of §2):**
> "These traditions remain siloed: ethics engagement does not incorporate structural postconditions; trace summarization does not address affect/power; constraint-based design does not surface reflective barriers. We synthesize them into a multi-layer trail stack."

---

### §3. The Trail Stack Model (1200 words)

**Goal:** Define the three trail types and their governance functions.

| Subsection | Content |
|------------|---------|
| 3.1 Trail Type I: Reflective/Narrative | What happened, who involved, what constrained, what it felt like. Ethics Pathways structure. |
| 3.2 Trail Type II: Graph/Trace | Design moves, sequence, semantic links. Fuzzy Linkography structure. |
| 3.3 Trail Type III: Contract/Integrity | Postconditions, ownership invariants, export gates. Hoare Logic structure. |
| 3.4 What Trails *Do* (verbs) | Gate export, enable repair, allocate responsibility |
| 3.5 The Shared Failure Mode | Invisible labor → unaccountable artifacts → self-certification |

**Figure 1:** Trail Stack Diagram (3 layers with example anchors from WAG)

---

### §4. System: WAG/DCE-GYO (1500 words)

**Goal:** Present the toolkit as trail-native by construction.

| Subsection | Content |
|------------|---------|
| 4.1 Design Context | 150+ hours, single author, 20+ tools, LMC-6650 course frame |
| 4.2 The Void Management Pattern | 9×9 grid + tetrad operators + chat layer. TILTH failure as motivation. |
| 4.3 Type I Trails in WAG | SHUFFLE corpus, pyramids, reflection essays |
| 4.4 Type II Trails in WAG | Git commits, POML invocation chains, artifact modification sequences |
| 4.5 Type III Trails in WAG | stud_skeleton.json, MASTER validation, export gating |
| 4.6 The WERE/WEAVER/MASTER Labs | Visualize → Rebuild → Validate pattern |

**Figure 2:** WAG/DCE-GYO System Architecture
**Figure 3:** stud_skeleton Ownership Graph (before/after repair)

---

### §5. The Capability Cliff (1000 words)

**Goal:** Transform "confession" into "design implication."

| Subsection | Content |
|------------|---------|
| 5.1 Where the Cliffs Were | 3D transforms (quaternions), multi-agent coordination, WebGL debugging |
| 5.2 What Failures Exposed | Error messages without fixable locations; prerequisites not surfaced; silent failures |
| 5.3 Scaffolding That Would Have Mattered | Tests, validators, better logs, stronger invariants, expertise locators |
| 5.4 The Ethical Significance | Expertise asymmetry; accountability diffusion; trail-less systems entrench power |

**C2 Claim (5.4):**
> "Tools that reveal their own inadequacies are not 'better error messages'—they are governance features. They redistribute the capability cliff's cost from user to system."

**Figure 4:** Capability Cliff Taxonomy (3 cliffs × what revealed × what would help)

---

### §6. Discussion (800 words)

**Goal:** Generalize from WAG to design principles.

| Subsection | Content |
|------------|---------|
| 6.1 Trail-Native vs Trail-Appended | Design for trails from inception vs retrofit. Trail-native is cheaper. |
| 6.2 When Trail Types Conflict | Reflective ambiguity (I) vs integrity gating (III). How to handle. |
| 6.3 Algorithmic vs Interpretive | What can be automated (II) vs what requires human judgment (I). |
| 6.4 Limitations | Single author; no user study; API dependency; technical threshold not overcome. |

---

### §7. Conclusion (300 words)

**Goal:** Restate thesis + contributions + call to action.

| Content |
|---------|
| Restate: Trails are governance, not documentation |
| C1: Trail-first account with three types |
| C2: "Tools that reveal their own inadequacies" as design requirement |
| C3: Capability cliff as research site |
| Call to action: Build trail-native infrastructure before the crisis, not after |

---

## PART 2: Claim Cards (5 Major Artifacts)

---

### CLAIM CARD 1: Privacy Value Labels

**Claim:**
> Contextual Integrity's 14 dimensions can be operationalized as a mobile-first worksheet, enabling values articulation *in the meeting*, not after.

**Artifact Pointer:**
`https://hartswf0.github.io/privacy-value-labels/`

**Trail Pointers:**
- I (Reflective): Mulligan/Koopman/Doty reading → "CI is multidimensional" insight → "what if mobile?"
- II (Graph): 3 commits building initial interface; 2 commits adding export
- III (Contract): JSON export with all 14 dimensions validated present

**Theory Hook:**
Nissenbaum 2010: Contextual Integrity; Mulligan et al. 2016: multidimensional privacy

**Boundary:**
No user testing. Designed for myself as UX researcher audience.

---

### CLAIM CARD 2: Haunted Tools

**Claim:**
> Ethics toolkits share a mythological structure: form (what it looks like) occludes concept (what it claims) occludes twist (what it actually transfers). Trail visibility disrupts this mythology.

**Artifact Pointer:**
`https://hartswf0.github.io/haunted-tools/`
`/docs/paragon-essay.md` (§ Barthesian Scalpel)

**Trail Pointers:**
- I (Reflective): Shannon Mattern reading → "toolkit critique" → cataloging 7 haunted types
- II (Graph): POML `mythos.poml` generating ideal-type descriptions; 5 revision commits
- III (Contract): N/A (conceptual artifact—no structural invariants)

**Theory Hook:**
Barthes 1957: mythology as semiotic structure; Mattern 2021: "Unboxing the Toolkit"

**Boundary:**
Catalog, not empirical study. No validation that others perceive the same "twist."

---

### CLAIM CARD 3: Thousand-Tetrad

**Claim:**
> The 9×9 grid with tetrad operators provides bounded complexity that scales without accumulation—void management operationalized.

**Artifact Pointer:**
`https://hartswf0.github.io/1000-small-futures/thousand-tetrad.html`

**Trail Pointers:**
- I (Reflective): TILTH collapse → "build the key first" insight → grid as invariant
- II (Graph): 67 scenario templates; 15 commits refining tetrad operator logic
- III (Contract): Grid state always serializable to JSON; no undefined cells

**Theory Hook:**
McLuhan 1988: tetrad (Enhance/Obsolesce/Retrieve/Reverse); Stevens 1919: "Anecdote of the Jar"

**Boundary:**
Tested with 4 collaborators (Tehri, Jordan, Kayla, Shuruq). No controlled evaluation.

---

### CLAIM CARD 4: DCE-GYO Labs (WERE/WEAVER/MASTER)

**Claim:**
> Export gating via postconditions prevents invalid artifacts from escaping the creative session. The visualize→rebuild→validate pattern makes repair local instead of global.

**Artifact Pointer:**
`WERE.html`, `WEAVER.html`, `MASTER.html`
`stud_skeleton.json` schema

**Trail Pointers:**
- I (Reflective): "Orphan stud" discovery → "something is wrong with ownership" → 3-week debugging arc
- II (Graph): 23 commits across `9c8d...` → `b3e1...` fixing stud ownership
- III (Contract): MASTER validation log; 7 blocked exports with genuine errors

**Theory Hook:**
Hoare 2009: "Null References: The Billion Dollar Mistake"; Parnas 1972: information hiding

**Boundary:**
Only tested on single-author models < 500 bricks. No multi-user validation.

---

### CLAIM CARD 5: POML Library

**Claim:**
> Prompts are infrastructure, not transactions. Versioned, composed, inherited prompt files represent accumulated mētis that cannot be itemized into discrete "prompts I used."

**Artifact Pointer:**
`/docs/poml-library.md`
9 POML files (1,374 lines total)

**Trail Pointers:**
- I (Reflective): Disclosure double-bind → "what if prompts were versionable?" → POML design
- II (Graph): 9 files with include/inheritance relationships; Git history of refinements
- III (Contract): POML parser validates structure; invalid syntax blocks execution

**Theory Hook:**
Scott 1998: mētis vs techne; Wong 2021: soft resistance as tactical accumulation

**Boundary:**
Personal infrastructure. No community adoption. Format not standardized.

---

## PART 3: Notes Structure (Trailbook)

---

### Trailbook Section 1: Incidents

*Matches Paper §5 (Capability Cliff)*

| Incident | Date Range | What Broke | What I Tried | What Worked | What I Learned |
|----------|------------|------------|--------------|-------------|----------------|
| TILTH collapse | Weeks 1–4 | Coherence under cumulative modification | More context, more prompts | Pivot to void management | "Build the key first" |
| Orphan stud discovery | Week 8 | Missing ownership in stud_skeleton | Manual inspection | WERE visualizer | Trails must be visual |
| Quaternion debugging | Weeks 9–11 | Camera rotation bugs | Stack Overflow copy-paste | Finally understood matrix composition | "Over my head" is structural, not personal |
| WebGL black screen | Week 12 | Silent GPU failure | Console.log everywhere | Eventually found shader compile error | Error messages need locations |

---

### Trailbook Section 2: Stakeholders

*Matches Paper §2.1 + §5.4 (Ethics Engagement)*

| Stakeholder | Role | Power Position | What They Needed | What I Could Offer |
|-------------|------|----------------|------------------|-------------------|
| Self | Creator | High (author of system) | Clarity, completed project | Sustained effort |
| LLM (GPT/Claude/Gemini) | Tool | High (capability), Low (agency) | Good prompts, clear context | POML infrastructure |
| Collaborators (Tehri, Jordan, Kayla, Shuruq) | Testers | Medium | Working tools, clear instructions | Prompt guides, screen shares |
| Institution (GT, ACM) | Regulator | High (grades, publication) | Legible disclosure | Trail artifacts |
| Future Users | Audience | Low (not yet present) | Exportable, documented tools | Trail-native design |

---

### Trailbook Section 3: Barriers

*Matches Paper §5.3 (Scaffolding)*

| Barrier Type | Example | What Would Have Helped |
|--------------|---------|------------------------|
| Technical threshold | Quaternion math | Interactive visualizer + prerequisite map |
| Error legibility | WebGL black screen | Shader error → line number → suggested fix |
| Documentation gap | Three.js TransformControls | "Common mistakes" section in docs |
| Cost constraint | API token budget | Local LLM fallback |
| Time constraint | 16-week semester | More realistic scope for single author |

---

### Trailbook Section 4: Raw Reflections

*Matches Paper §5 (Capability Cliff) + §6.4 (Limitations)*

**Week 4 Entry:**
> "TILTH is dead. I spent three weeks on a speculative company that nobody can navigate, including me. The problem isn't the content—it's that every addition makes the whole harder to maintain. I need a different architecture."

**Week 8 Entry:**
> "Found an orphan stud. It belongs to no brick. How did this happen? The MPD looks fine. The stud_skeleton says this stud exists but owner is null. This is exactly the 'billion dollar mistake' Hoare talked about."

**Week 11 Entry:**
> "Quaternions are not intuitive. I've read five tutorials. I can copy code that works but I don't understand *why* it works. This is the 'over my head' feeling I need to document, not hide."

**Week 15 Entry:**
> "The paper is about trails. The irony is that I've been keeping a trail (these notes, the commits, the pyramids) without knowing that's what I was doing. The trail was governance before I named it governance."

---

### Trailbook Section 5: Artifact Change Log

*Matches Paper §4 (System)*

| Artifact | Version | Date | Change | Commit |
|----------|---------|------|--------|--------|
| thousand-tetrad.html | 1.0 | Oct 12 | Initial 9×9 grid | a7f3bc2 |
| thousand-tetrad.html | 1.3 | Oct 19 | Added branching | c4d8e91 |
| stud_skeleton.json | 0.1 | Nov 2 | Initial schema | 9c8d... |
| stud_skeleton.json | 0.7 | Nov 18 | Added orphan detection | b3e1... |
| MASTER.html | 1.0 | Nov 22 | Export gating works | f7a2... |

---

## PART 4: Figure List

---

### Figure 1: Trail Stack Diagram

**Specification:**
- 3-layer vertical stack
- Type I (Reflective) at top: labeled "Ethics Pathways structure"
- Type II (Graph) in middle: labeled "Fuzzy Linkography structure"
- Type III (Contract) at bottom: labeled "Hoare Logic structure"
- Arrows showing: I annotates II; III gates export
- WAG examples in each layer

**Tool:** Mermaid or hand-drawn + Figma polish

---

### Figure 2: WAG/DCE-GYO System Architecture

**Specification:**
- Central: COURAGE (3D scene viewer)
- Left panel: File browser / MPD loader
- Right panel: Labs (WERE → WEAVER → MASTER flow)
- Bottom: Export gate (arrow to GLB only if MASTER passes)
- Annotations: Trail Type III for Labs; Trail Type II for activity log

**Tool:** Figma or draw.io

---

### Figure 3: stud_skeleton Ownership Graph

**Specification:**
- Before: Orphan stud (red), null owner
- After: Same stud, valid owner (green)
- Side-by-side or before/after carousel
- JSON snippet showing the ownership field

**Tool:** Screenshot from WERE + annotation

---

### Figure 4: Capability Cliff Taxonomy

**Specification:**
- 3 columns: Cliff, What Revealed, Scaffolding Needed
- Rows: 3D transforms, Multi-agent, WebGL debugging
- Color coding: Red = over my head; Yellow = partially solved; Green = would have helped

**Tool:** Table in paper (no separate figure file needed)

---

### Figure 5: Project Phase Linkograph

**Specification:**
- 4 nodes: TILTH → Thousand-Tetrad → HOLO → TRACTOR
- Edges: semantic similarity (what concepts carried over)
- Annotations: Ethics Pathways incident/barrier at each node
- This is the "steal from Thesis C" figure

**Tool:** Mermaid flowchart or custom SVG

---

### Figure 6: Ethics Pathways Mapping Table

**Specification:**
- 4 columns: Task, WAG Instance, Trail Type, Evidence Location
- Rows: Incident, Stakeholders, Actions/Alternatives, Reflection
- This is the "steal from Ethics Pathways" figure

**Tool:** Table in paper (no separate figure file needed)

---

## Summary: The Paper Machine

| Component | Location | Status |
|-----------|----------|--------|
| Paper Skeleton | This document, Part 1 | ✅ Complete |
| Claim Cards (5) | This document, Part 2 | ✅ Complete |
| Trailbook Structure | This document, Part 3 | ✅ Complete |
| Figure Specs (6) | This document, Part 4 | ✅ Complete |

**Next Steps:**
1. Fill in Trailbook Section 4 (Raw Reflections) from actual notes/memory
2. Generate Figure 1 (Trail Stack) and Figure 2 (Architecture)
3. Write Paper §1 (Introduction) using skeleton + claim cards
4. Compile → Review → Iterate

---

*This is the machine. The writing is now compilation, not invention.*
