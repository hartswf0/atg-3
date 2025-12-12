# Trail-Native Infrastructure: A DIS/CHI Paper Outline

*Fusing Ethics Pathways + Fuzzy Linkography + Liberty Machines + WAG/DCE-GYO*

---

## Answers to the 13 Binding Questions

---

### PART 1: Core Framing Questions (Intro + Contribution)

#### Q1: What is a "trail" in your ecosystem—log, narrative, graph, contract, or all three?

**Answer: All three, structured as a sedimentary archive with multiple read modes.**

A trail in WAG/DCE-GYO is:

1. **Log**: Timestamped sequence of design moves (`stud_skeleton.json` records brick-stud ownership at each modification; `disc-data.json` records narrative states)

2. **Narrative**: Thick description layer that gives *intent* to the log (why this brick, why this stud, what the creator was trying to accomplish)

3. **Graph**: Linkographic structure where moves connect to prior moves (the primitive reference pattern in LDraw: `3001.dat` references `stud.dat` which references `cyl1.dat`)

4. **Contract**: Postcondition assertions that must hold for export to be valid (no orphan studs, no overlapping ownership, no null references—the Hoare Logic layer)

**Taxonomy:**

| Trail Type | Example in WAG | Fuzzy Linkography Term | Ethics Pathways Term |
|------------|----------------|------------------------|---------------------|
| **Log** | Git commits, `stud_skeleton.json` | "Design moves" | "Actions taken" |
| **Narrative** | Intent annotations, SHUFFLE quotes | "Episode context" | "Reflection walkthrough" |
| **Graph** | Primitive reference tree, DCE ownership graph | "Linkograph" | "Stakeholder map" |
| **Contract** | MASTER validator postconditions | N/A (not in paper) | "Institutional constraints" |

---

#### Q2: What breaks without trails? Name the shared failure mode across:

**Answer: The Three Failure Modes Share a Common Structure: *Invisible Labor Producing Unaccountable Artifacts***

| Domain | Failure Without Trails | What Becomes Invisible |
|--------|------------------------|------------------------|
| **Haunted Ethics Tools** | Performance without transfer (Barthes' mythology) | The gap between *claimed* impact and *actual* resource movement |
| **Complexity Grey** | Scene management collapse (TILTH failure) | The accumulated context that makes editing impossible |
| **DCE-GYO Ownership Drift** | Orphan/null/illegal states (Hoare's billion-dollar mistake) | The ownership graph that determines export validity |

**The Shared Failure Mode:**

> "When trails are absent, artifacts become *self-certifying*—they claim to be valid/ethical/coherent by existing, without evidence of the process that produced them. This is the fundamental structure of both 'disclosure theatre' and 'complexity grey.'"

**Ethics Pathways Connection:**
> "Challenges persist in grasping the complexity of researchers' engagement with ethics—practices conducted to operationalize ethics—in situated institutional contexts."

Without trails, ethics engagement becomes *asserted* rather than *demonstrated*. The same applies to creative coherence and structural validity.

---

#### Q3: What do trails *do* (not represent)?

**Answer: Three Core Verbs**

1. **Gate Export**: Trails enable or block the transition from session-bound artifact to shareable infrastructure. An MPD file without valid `stud_skeleton` cannot export to GLB. A disclosure without trail evidence cannot satisfy symbiotic-use accountability.

2. **Enable Repair**: When coherence breaks (complexity grey), trails allow *localized* intervention rather than *global restart*. The WERE viewer shows exactly which brick owns which studs; repair targets that relationship, not the whole model.

3. **Allocate Responsibility**: Trails answer "who decided what when" in a way that post-hoc disclosure cannot. The `!AUTHOR` header in LDraw, the Intent type in WAG Genome, the stakeholder mapping in Ethics Pathways—all are responsibility-allocation mechanisms.

**Secondary Verbs:**

- **Compress Activity**: Fuzzy Linkography's contribution—trails can be *summarized* into legible structures without losing essential topology
- **Make Visible**: Trails surface the invisible labor (Jackson's "repair work") that haunted tools occlude

---

### PART 2: Binding Questions (WAG ↔ DCE-GYO Labs ↔ Pathfinders)

#### Q4: How does "Ethics Pathways" map onto your own practice?

**Answer: Direct Mapping Across Four Tasks**

| Ethics Pathways Task | WAG/DCE-GYO Instance |
|---------------------|---------------------|
| **Recalling ethical incidents** | TILTH collapse (complexity grey); orphan stud discovery in DCE; "disclosure theatre" double-bind |
| **Describing stakeholders** | Self as Creator, LLM as Tool, Collaborators (Tehri/Jordan/Kayla), Institution (GT/ACM), Future Users |
| **Recounting actions/alternatives** | Pivot from scene→void; decision to use POML; choice of single-file HTML; postcondition gating |
| **Reflection/emotion walkthrough** | "Over my head in code" anxiety; satisfaction at WERE/WEAVER/MASTER integration; frustration with API costs |

**Key Barriers Encountered:**

1. **Technical threshold**: Not enough expertise for multi-agent systems
2. **API dependency**: Cost barriers to sustained testing
3. **Codebase fragility**: Limited delegation to collaborators
4. **Disclosure framework mismatch**: ACM itemization model penalizes symbiotic use

**Alternate Actions (Speculative):**

- Could have used open-source LLMs from start (Tehri's push)
- Could have built with a team rather than solo
- Could have designed for web deployment rather than local-first

---

#### Q5: What is the DCE-GYO stud_skeleton in trail terms?

**Answer: A Rigid Integrity Trail (Ownership Graph) That Gates Export**

The `stud_skeleton.json` is:

1. **Semantically**: An ownership map (which brick owns which studs)
2. **Syntactically**: A JSON object with brick IDs as keys and stud arrays as values
3. **Functionally**: A Hoare postcondition that must be satisfied for GLB export

**The Hoare Logic Story:**

```
// Precondition: MPD file loaded
// Operation: User manipulates bricks
// Postcondition: ∀ stud ∈ model, ∃! brick : owns(brick, stud)
//              (every stud has exactly one owner)
```

If the postcondition fails (orphan studs, overlapping ownership, null references), MASTER blocks export. This is "parse, don't validate" applied to 3D geometry—structural errors are detected *before* they propagate to downstream tools.

**Trail Characteristics:**

| Property | stud_skeleton.json |
|----------|-------------------|
| **Temporality** | Snapshot (current state), versioned (via Git) |
| **Granularity** | Per-stud ownership |
| **Computability** | Fully derivable from MPD geometry |
| **Gating Function** | Export fails if invariants violated |

---

#### Q6: Where does automated summarization belong?

**Answer: Algorithmic for Structure, Interpretive for Meaning**

| Trail Layer | Summarization Mode | Why |
|-------------|-------------------|-----|
| **Log** (design moves) | Algorithmic (Fuzzy Linkography) | Moves are discrete, timestamped, comparable |
| **Graph** (primitive references) | Algorithmic | Structure is computable from file analysis |
| **Narrative** (intent) | Interpretive (autoethnography) | Intent requires thick description |
| **Ethics engagement** | Interpretive (Ethics Pathways) | Affect, power, barriers require human reflection |

**The Hybrid Application:**

1. Use Fuzzy Linkography to *generate* the graph structure from design moves
2. Use Ethics Pathways to *annotate* that structure with stakeholder/barrier/affect data
3. Export the combined representation as a "trail artifact" that is *legible at scale* but *meaningful in context*

---

#### Q7: What is the invariant indexing pattern across modalities?

**Answer: Tetrad Operators as Cross-Modal Index**

McLuhan's tetrad (Enhance/Obsolesce/Retrieve/Reverse) functions as an invariant operator across:

| Modality | Enhance | Obsolesce | Retrieve | Reverse |
|----------|---------|-----------|----------|---------|
| **Text** (POML) | Amplify specific registers | Suppress unwanted patterns | Invoke historical styles | Invert expected outcomes |
| **UI** (9×9 grid) | Highlight selected cell | Fade non-active regions | Fork to previous state | Swap axis positions |
| **Geometry** (DCE) | Grow brick count | Remove hidden faces | Restore deleted elements | Mirror/flip model |
| **Ethics** (Liberty Machines) | Strengthen one regulatory mode | Weaken competing mode | Recall historical precedent | Flip power relationship |

**The Invariant Pattern:**

```
transform(entity, operator) → entity'
where operator ∈ {Enhance, Obsolesce, Retrieve, Reverse}
and entity ∈ {text, ui_state, geometry, ethics_position}
```

This is the "vector field thinking" from Liberty Machines applied as a universal transformation algebra.

---

### PART 3: Method Questions (DIS/CHI Paper Format)

#### Q8: What trace data do you actually produce? (Enumerate)

**Trace Data Inventory:**

| Trace Type | Format | Location | Granularity |
|------------|--------|----------|-------------|
| **Commits** | Git log | `.git/` | Per-session |
| **Artifacts** | HTML, MD, POML, JSON | `/`, `/docs/`, `/data/` | Per-file |
| **Interaction logs** | Console logs, event traces | Local storage | Per-move |
| **Exports** | `disc-data.json`, `stud_skeleton.json`, GLB | `/exports/` | Per-model |
| **Breakdown moments** | SHUFFLE corpus annotations | `/SHUFFLE/markdown/` | Per-insight |
| **Repairs** | Commit diffs, version history | Git | Per-fix |
| **Annotations** | `!AUTHOR`, `!LICENSE`, POML headers | In-file | Per-artifact |
| **Intent records** | Essay reflections, pyramids | `/docs/pyramids/` | Per-concept |

**Total Trace Volume:**
- 58 markdown files in `/docs/`
- 27 SHUFFLE corpus files
- 18+ POML files
- 20+ HTML tools
- 150+ hours of interaction compressed into artifacts

---

#### Q9: What's your "Fuzzy Linkography" application claim?

**Claim:**

> "We can summarize WAG/DCE-GYO creative-repair activity as a graph of design moves, where each POML invocation, each artifact modification, and each breakdown-repair cycle represents a node, and semantic similarity between nodes constitutes edges. This enables *legible reflection at scale* on what would otherwise be an untraversable 150-hour interaction history."

**Specific Application:**

The Fuzzy Linkography paper applies to three domains: text-to-image prompting, LLM-supported ideation, researcher publication histories. WAG/DCE-GYO extends this to:

1. **Prompt-to-geometry journeys**: POML → MPD → GLB transformation chains
2. **Repair episodes**: Breakdown → diagnosis (WERE) → fix (WEAVER) → validation (MASTER)
3. **Toolkit evolution**: TILTH → Thousand-Tetrad → HOLO → TRACTOR (4 phases as linkograph)

---

#### Q10: What's your "Ethics Pathways" application claim?

**Claim:**

> "We treat ethics engagement as flow-through-practice rather than checkpoint-compliance, and make it inspectable via trail artifacts rather than post-hoc disclosure. The trail *is* the evidence of ethics engagement—not a separate 'ethics statement' appended to otherwise-opaque work."

**Specific Application:**

The Ethics Pathways four-task structure becomes:

1. **Incident**: TILTH collapse, disclosure theatre, orphan stud
2. **Stakeholders**: Creator, Tool (LLM), Collaborators, Institution, Users
3. **Actions**: Pivot to void management, postcondition gating, trail visibility
4. **Reflection**: "Over my head" confession, Lessig regulatory analysis, mētis/techne distinction

The trail artifacts (pyramids, essays, POML library) *embody* this reflection rather than reporting it separately.

---

### PART 4: Discussion Questions (Capability Cliff → Design Implications)

#### Q11: Where is the capability cliff?

**Answer: Three Cliffs Encountered**

| Cliff | What I Couldn't Do | Consequence |
|-------|-------------------|-------------|
| **Linear algebra for 3D transforms** | Quaternion rotations, matrix composition | MENTO camera bugs persisted for weeks |
| **Multi-agent coordination** | Message passing, persistent agent memory | Couldn't engage with emergentic.ai or NeurIPS panelists |
| **WebGL debugging** | GPU-side errors, shader compilation | Black screens with no diagnostic information |

**What Failures Exposed:**

The capability cliff becomes visible when:
- Error messages don't correspond to fixable code locations
- Documentation assumes prerequisites I don't have
- Fixes require understanding I can't acquire in available time

---

#### Q12: What scaffolding would have prevented the cliff?

**Answer: Tools That Surface Their Own Inadequacies**

**Design Implication:**

> "Second-order tools should *reveal* rather than *hide* the expertise required to use them. WERE/WEAVER/MASTER is an attempt at this: the Labs make visible the structural inadequacies (orphan studs, illegal states) that would otherwise be silent failures."

**Specific Scaffolds Needed:**

1. **Prerequisite mapping**: "This tool requires understanding of X, Y, Z"
2. **Failure annotation**: "This error typically means Q—try R"
3. **Expertise locator**: "This problem is best asked to someone who knows S"
4. **Escape hatch**: "If you can't fix this, here's how to export partial progress"

---

#### Q13: What is the ethical significance of being over your head?

**Answer: Trails Are Governance, Not Documentation**

> "If tools require invisible expert labor to remain safe/coherent, then trails are not 'nice to have'—they're governance. The absence of trails enables *accountability diffusion*: when things break, no one knows who decided what when, and repair becomes global rather than local."

**The Ethical Stakes:**

1. **Responsibility allocation**: Without trails, failures are attributed to "the system" rather than specific decisions
2. **Repair enablement**: Without trails, the only fix is restart—all accumulated progress is lost
3. **Power asymmetry**: Experts can navigate without trails; novices cannot. Trail-less tools *entrench* expertise asymmetry

**Ethics Pathways Connection:**

> "Ethics Pathways highlights connections between individual affective experiences, social interactions across power differences, and institutional goals."

Being "over your head" is an *affective experience* with *power implications* that trails can *make visible* rather than occlude.

---

## DIS/CHI Paper Outline

### Title

**Trail-Native Infrastructure: Design Moves, Ownership Graphs, and Ethics Engagement in LLM-Mediated Creative Systems**

---

### Abstract (250 words)

We present a framework for understanding creative work with AI as *trail-native infrastructure*—systems designed from inception to make their reasoning processes legible through trace artifacts. Drawing on Ethics Pathways [Wong et al. 2024] for conceptualizing ethics engagement as flow-through-practice, and Fuzzy Linkography [Author et al. 2025] for automatic summarization of creative activity traces, we articulate a three-layer trail model: log (design moves), graph (ownership structure), and contract (postcondition assertions). We ground this framework in WAG/DCE-GYO, a 150+ hour design research project that produced 20+ single-file HTML tools, a 9-file prompt infrastructure library (POML), and a three-tool repair pipeline (WERE/WEAVER/MASTER) for structural coherence validation.

Our contributions are: (1) a conceptual account of "trails" spanning log, narrative, graph, and contract modalities; (2) a systems architecture where export is gated by Hoare-style postconditions on ownership graphs; (3) a method for adapting linkographic summarization to LLM-mediated creative work; and (4) a reflexive analysis of the "capability cliff" in anti-bundler toolmaking, motivating tools that reveal their own inadequacies. We argue that trails are not documentation artifacts but governance infrastructure—without them, accountability diffuses, repair becomes global rather than local, and ethics engagement reduces to performance.

---

### 1. Introduction

- The "disclosure theatre" problem: ACM-style itemization cannot capture symbiotic AI use
- The "complexity grey" failure: generative systems collapse under cumulative modification
- The "haunted tools" pathology: ethics instruments perform deliberation without transferring resources

**Research Question:** How can we design AI-mediated creative systems that are *trail-native*—legible, repairable, and accountable by construction?

---

### 2. Related Work

#### 2.1 Ethics Engagement as Practice
- Ethics Pathways [Wong et al. 2024]: Four-task structure (incident → stakeholders → actions → reflection)
- Soft Resistance [Wong 2021]: Ethics work as tactical maneuvering
- Situated Action [Suchman 1987]: Plans as resources, not programs

#### 2.2 Trace Summarization
- Fuzzy Linkography [Author et al. 2025]: Automatic graph construction from design moves
- Linkography [Goldschmidt 1990]: Manual coding of design episodes
- Context Engineering [Karpathy 2025]: Prompt structuring for LLM coherence

#### 2.3 Constraint-Based Design
- Hoare Logic [Hoare 1969]: Precondition/postcondition contracts
- Void Management [this work]: Bounded possibility spaces vs. unbounded scene construction
- LDraw History [Jessiman 1995]: 30-year prototype of community-governed digital infrastructure

---

### 3. The Trail Model

#### 3.1 Trail Types
- Log, Narrative, Graph, Contract (with examples from WAG/DCE-GYO)

#### 3.2 What Trails Do
- Gate export, enable repair, allocate responsibility

#### 3.3 The Shared Failure Mode
- Invisible labor producing unaccountable artifacts

**Figure 1:** Trail taxonomy with examples from Ethics Pathways, Fuzzy Linkography, and WAG/DCE-GYO

---

### 4. System: WAG/DCE-GYO

#### 4.1 The Void Management Pattern
- 9×9 grid, tetrad operators, chat layer, branching mechanics
- Why scene management fails (TILTH case study)

#### 4.2 The WERE/WEAVER/MASTER Labs
- WERE: Visualize ownership graph
- WEAVER: Rebuild connectivity
- MASTER: Validate postconditions, gate export

#### 4.3 The POML Library
- Prompt infrastructure (9 files, 1,374 lines)
- Prompts that generate prompts

**Figure 2:** System architecture diagram (COURAGE → Labs → Export)

---

### 5. Method: Trace Collection and Summarization

#### 5.1 Trace Data Produced
- Enumeration of 8 trace types

#### 5.2 Fuzzy Linkography Application
- Graph construction from POML invocations and artifact modifications
- Semantic similarity as edge weight

#### 5.3 Ethics Pathways Application
- Incident/stakeholder/action/reflection mapping
- Annotation of linkograph with affective and power dimensions

**Figure 3:** Linkograph of project phases (TILTH → Thousand-Tetrad → HOLO → TRACTOR)

---

### 6. Findings

#### 6.1 The Capability Cliff
- Where expertise was insufficient
- What failures exposed the cliff

#### 6.2 Scaffolding for Capability Cliffs
- Design implication: Tools that reveal their own inadequacies

#### 6.3 Ethical Significance
- Trails as governance, not documentation
- Power asymmetry in trail-less systems

**Table 1:** Barriers encountered mapped to Ethics Pathways categories

---

### 7. Discussion

#### 7.1 Trail-Native vs. Trail-Appended Systems
- Design for trails from inception vs. retrofit

#### 7.2 Algorithmic vs. Interpretive Summarization
- Where each mode applies

#### 7.3 The Tetrad as Cross-Modal Index
- Invariant transformation algebra across text/UI/geometry/ethics

#### 7.4 Limitations
- Single-author design research
- API dependency
- Technical threshold not overcome

---

### 8. Conclusion

Trails are not "nice to have"—they are the governance infrastructure that makes creative AI work legible, repairable, and accountable. We propose trail-native design as an architectural principle for LLM-mediated creative systems.

---

### Figure List

1. Trail taxonomy with modality mappings
2. WAG/DCE-GYO system architecture
3. Project phase linkograph (4 phases)
4. stud_skeleton ownership graph visualization
5. Ethics Pathways four-task mapping to project incidents
6. Capability cliff barriers table

---

### Contribution Statements

- **C1 (Conceptual):** A trail-first account of generative design work where integrity and ethics are treated as flows in practice, not checklists
- **C2 (Systems):** A second-order toolkit pattern (visualize → rebuild → validate) that repairs structural coherence and gates export via postconditions
- **C3 (Method):** A trace summarization approach adapting linkography to LLM-mediated creative work
- **C4 (Practice):** A reflexive account of the capability cliff, motivating "tools that reveal their own inadequacies"

---

### Evaluation Plan

| Claim | Evaluation Method |
|-------|------------------|
| Trail-native systems enable localized repair | Compare repair time: trail-native vs. restart |
| Postcondition gating prevents export of invalid artifacts | Count blocked exports with genuine errors |
| Linkographic summarization produces legible overviews | Expert rating of summarized vs. raw traces |
| Ethics Pathways structure surfaces barriers | Participant reflection on mapped barriers |

---

### Works Cited (Partial)

- Ethics Pathways: Wong et al. 2024 (arXiv:2405.16654)
- Fuzzy Linkography: Author et al. 2025 (arXiv:2502.04599)
- Seeing Like a State: Scott 1998
- Plans and Situated Actions: Suchman 1987
- Code 2.0: Lessig 2006
- Thinking in Systems: Meadows 2008
- Mythologies: Barthes 1957/1972
- Null References: Hoare 2009
- LDraw: Jessiman 1995

---

*Ready for DIS 2026 / CHI 2026 submission track*
