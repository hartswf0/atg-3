# The Failure of TILTH: A Project Journey Map
## Creator Trail Ontology Log (Olog)

> **Core Thesis**: Every time a creator works, they leave behind a *trail* of data. This document traces the trail from speculative world-building to trail-aware infrastructure—through failures, pivots, and collaborations.

---

## The Arc

```
TILTH ──────────► THOUSAND-TETRAD ──────────► HOLO-PROJECT ──────────► TRACTOR-DCE-GYO
(Failure)         (Discovery)                 (Transition)              (Synthesis)
│                 │                           │                         │
World-building    Design pattern              2D → 3D                   LLM as gatekeeper
that collapsed    that scales                 shareable outputs         managing the void
under its own     │                           │                         │
complexity        9×9 grid                    disc-data.json            ONYX STUDIO
                  LEGOS operators             prebaked narratives       exports that matter
                  branching mechanics
```

---

## PHASE 0: TILTH — The Failure

**URL**: [tilth-investigation.html](https://hartswf0.github.io/role-deck/tilth-investigation.html)

### What It Was
A speculative investigation of a speculative company—**Agronica/TILTH**—meant to explore operating systems in a low-stakes arena through role decks and scenario builders.

### Why It Failed

| Problem | Description |
|---------|-------------|
| **Convoluted speculation** | A world inside of a world. Speculative investigation of a speculative company. |
| **Coherency collapse** | Hard to show enough of the world for it to gain coherency. Scenarios quickly became convoluted. |
| **Exponential context growth** | As project context grew, ability to finish it got exponentially more challenging. |
| **Trough of quality** | Almost good enough to stand alone. Not quite. Stuck. |
| **Polish bottleneck** | The hard parts: final editing, coding, integration. |

### What It Taught

> **Key Insight**: Designing the tools that design the world vs. designing for designers.

TILTH became a pathfinding exercise—a chance to:
- Test my own tools
- Find opportunities for new collaborations
- Bootstrap other projects

**Motivators that emerged**:
- Must work on mobile phone
- Make prompting/simulation/exploring alternatives easier
- Became a place to understand **affordances**

### Trail Artifact

```
┌─────────────────────────────────────────────────────┐
│  TILTH: TRAIL LEVEL 0 — EXHAUST                     │
│                                                     │
│  Artifacts: Speculative scenarios, role cards       │
│  Metadata: Convoluted world-building logs           │
│  Decisions: Abandoned branches, sunken costs        │
│                                                     │
│  Pattern: COMPLEXITY_SPIRAL                         │
│  Each addition made the system harder to use        │
└─────────────────────────────────────────────────────┘
```

---

## PHASE 1: THOUSAND-TETRAD — The Discovery

### The Impetus

> Much better speculative worlds had already been created. I could be **parasitic** off of them—or they would allow me to focus on the more technical tool-building process instead of keeping track of the world itself.

**Inspirations**:
- **Ted Chiang's work** — always inspired
- **"Life After Bob"** — presents many AI ethics dilemmas in stunning detail
- **A Thousand Lives** (spinoff of Life After Bob) — worked with one of the main simulation architects

**Goals**:
- Improve and grow with simulations/world-watching
- Learn from both the technical project
- Reach a technical threshold to be recognized as a future collaborator
- Excited by the concept of **abundance**

### The Question

> How to deal with many branching worlds? How to build **infrastructures that get richer the more you use them** instead of—like TILTH—getting harder to use each time?

### The Solution: An Invariant Design Pattern

**BUILD A DESIGN PATTERN/DESIGN LANGUAGE** that can be scaled and operationalized across any scenario-building and stays invariant.

```
┌─────────────────────────────────────────────────────────┐
│                    THOUSAND-TETRAD UI                   │
├─────────────────────────────────────────────────────────┤
│  ┌─────┐                              ┌─────┐          │
│  │ BTN │     [  OPERATORS  ]          │ BTN │  HEADER  │
│  └─────┘                              └─────┘          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│              ┌───┬───┬───┬───┬───┬───┬───┬───┬───┐     │
│              │   │   │   │   │   │   │   │   │   │     │
│              ├───┼───┼───┼───┼───┼───┼───┼───┼───┤     │
│              │   │   │   │   │   │   │   │   │   │     │
│              ├───┼───┼───┼───┼───┼───┼───┼───┼───┤     │
│              │   │   │   │   │   │   │   │   │   │     │
│              ├───┼───┼───┼───┼───┼───┼───┼───┼───┤     │
│              │   │   │   │   │ ⊕ │   │   │   │   │  9×9│
│              ├───┼───┼───┼───┼───┼───┼───┼───┼───┤ GRID│
│              │   │   │   │   │   │   │   │   │   │     │
│              ├───┼───┼───┼───┼───┼───┼───┼───┼───┤     │
│              │   │   │   │   │   │   │   │   │   │     │
│              ├───┼───┼───┼───┼───┼───┼───┼───┼───┤     │
│              │   │   │   │   │   │   │   │   │   │     │
│              └───┴───┴───┴───┴───┴───┴───┴───┴───┘     │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────┐   │
│  │                     CHAT                         │   │
│  │  Any new UI loads through chat                   │   │
│  │  Any entity can be controlled via chat or grid   │   │
│  │  Anything can easily be branched                 │   │
│  └─────────────────────────────────────────────────┘   │
├─────────────────────────────────────────────────────────┤
│  ┌─────┐  [SCENE SELECTOR] [TETRAD OP]  ┌─────┐ FOOTER │
│  │ BTN │                                │ BTN │        │
│  └─────┘                                └─────┘        │
└─────────────────────────────────────────────────────────┘
```

### The Aha Moment

**URL**: [nexadoc-jar](https://hartswf0.github.io/nexadoc-jar/)

> The complexity of TILTH gave way to the simplicity of the **anecdote of the jar**.

**URL**: [epir.html](https://hartswf0.github.io/nexadoc-jar/epir.html)

Based on Wallace Stevens's ekphrastic poem "Anecdote of a Jar"—investigating ways of showing prompt/completion chains with ekphrasis.

### Core URLs

| Component | URL |
|-----------|-----|
| **Tetrad Pad** (early experiment) | [tetrad-pad.html](https://hartswf0.github.io/role-deck/tetrad-pad.html) |
| **Thousand Tetrad** (critical juncture) | [thousand-tetrad.html](https://hartswf0.github.io/1000-small-futures/thousand-tetrad.html) |
| **LEGOS Framework** | [LEGOS](https://hartswf0.github.io/LEGOS/) |

### The Tetrad Operator

> What if **obsolesce, retrieve, reverse, and enhance** were the D-pad on a speculative design game for Game Boy? How can McLuhan's tetrad be operationalized as a prompt controller?

```
              ENHANCE
                 ↑
                 │
    RETRIEVE ◀───┼───▶ OBSOLESCE
                 │
                 ↓
              REVERSE
```

### Constraints as Freedom

| Constraint | Purpose |
|------------|---------|
| **9×9 Grid** | Bounded spatial canvas for scenarios |
| **LEGOS Elements** | Location, Entities, Goals, Obstacles, Shifts/Solutions |
| **Tetrad Operators** | McLuhan's four laws as scene transformers |
| **Branching Mechanics** | Any state can fork into alternatives |
| **Open-ended Chat** | Natural language control layer |

### Trail Artifact

```
┌─────────────────────────────────────────────────────┐
│  THOUSAND-TETRAD: TRAIL LEVEL 2 — BACKBONE          │
│                                                     │
│  Artifacts: 100+ test scenes, grid layouts          │
│  Metadata: API costs, session logs, branch trees    │
│  Decisions: Tetrad operations, entity placements    │
│                                                     │
│  Pattern: INVARIANT_SUBSTRATE                       │
│  Same pattern scales across any world               │
└─────────────────────────────────────────────────────┘
```

---

## COLLABORATORS: The Testing Ground

### Shuruq Tramontini — A Thousand Lives

**Context**: Worked with one of the main simulation architects of the Thousand Lives spinoff of "Life After Bob."

**Goal**: Create a substrate enabling Shuruq's thousand-small-scale futures to be explored more easily.

**Approach**: Opposite of TILTH—**extremely bounded** experiments.

---

### Tehri Marttila — Portuguese Computational Humanities Researcher

**Collaboration Pattern**:
- Met weekly
- Tested thousand-tetrad extensively
- Pushed toward lower-cost/open-source LLMs

**Outcomes**:
- Built deeper collaborative project about forest/branching paths perspectives
- Thousand-tetrad was useful for pathfinding and grounding collaboration

**Challenges**:
| Issue | Description |
|-------|-------------|
| API bleeding | Testing only possible with my API key |
| Integration friction | Restructuring for different LLMs created problems |
| 1-of-1 experience | Sometimes too personal to generalize |
| Sunken cost | Total system overhaul would be costly |

**Key Realization**: System prompt could be used for free on any LLM, but missing affordance of grid and branching mechanic. Bigger issue: **how to export meaningfully**?

---

### Jordan Caldwell — Black Metal / Training Grounds

**Context**: Speculative worldbuilding for "Black Metal" physical book project.

**Approach**: Found my way through operators and operationalizing her speculative world.

**Learnings from TILTH and Thousand Lives**: Prepared me for a complex training ground.

**Workshop Outcome**:
- Too short to realize technical ambition
- System could not adequately absorb the variety of her world built so quickly
- World had primarily been built for physical book format

---

### Kayla Uleah Evans — Responsible AI Summit

**Context**: Met at Responsible AI Summit. Interested in ethical negotiation simulations/training for tech professionals.

**Collaboration Dynamics**:

> She had a sense of being creative director. I told her I could hardly keep the codebase together. Barely knew how it worked. I wouldn't be of much help to such a role.

**My Response**:
- Produced documents, essays, prompt guides
- Made it easier for her to engage hands-on
- Let her see the frictions and strains I was fighting
- Got out of the way to see the negotiation live
- **Not trying to act like I had a real platform**

---

## THE TECHNICAL CHALLENGES

### Uncanny Valley of Competence

> Not technical enough to engage with the computer scientists/engineering architecture people.

**Reference Points**:

| Person | Platform/Context |
|--------|------------------|
| **Shuruq** | Uses Unreal Engine |
| **Parag Mital** | [emergentic.ai](https://emergentic.ai) — presenting at NeurIPS |

### Parag Mital — The Garden in the Machine

> Multi-agent AI Authoring and Simulation Platform. Easily author, simulate, and deploy custom agents. Explore the potential for storytelling with agentic NPCs.

**Teaching Aspirations**:
- [UCLA Cultural Automation with Machine Learning](https://pkmital.com/home/teaching/ucla-cultural-automation-with-machine-learning/)
- [UCLA Course on Cultural Appropriation with Machine Learning](https://pkmital.com/home/teaching/ucla-course-on-cultural-appropriation-with-machine-learning/)

**NeurIPS 2025 Panel**: [Emergent Stories: AI Agents and New Narratives](https://neurips.cc/virtual/2025/loc/san-diego/panel/131735)

> So did not meet the threshold YET! But I learned a lot about software engineering and simulation architecture—but mostly about **context engineering**!

### Academic References

| Title | Authors | DOI/Link |
|-------|---------|----------|
| From linear story generation to branching story graphs | Mark Riedl, R. Michael Young | [10.1109/MCG.2006.56](https://www.researchgate.net/publication/7070973_From_linear_story_generation_to_branching_story_graphs) |
| Generative Agents: Interactive Simulacra of Human Behavior | Joon Sung Park et al. | [arXiv:2304.03442](https://arxiv.org/abs/2304.03442) |
| Audiovisual Scene Synthesis (Doctoral thesis) | Parag Kumar Mital | Goldsmiths, University of London, 2014 |

### Technical Pathologies

| Problem | Description |
|---------|-------------|
| **Context window degradation** | LLM performance degrades over time in session |
| **Scene graph complexity** | Building and maintaining scene state |
| **Ring buffer memory** | Managing what the system remembers |
| **Export problem** | How to share something generated with LLM collaboration that is not just a vibe-coded website or raw text |

---

## PHASE 2: HOLO-PROJECT — The Transition

**URL**: [holo-project.html](https://hartswf0.github.io/holo-project/holo-project.html)

### The 2D → 3D Pivot

**Motivations**:
- Technical problems with API
- Inability to share outputs meaningfully
- Both Jordan and Kayla's projects pushed toward novel 3D scenes more clearly representing scenarios

### What It Was

> A chance to explore the DIRTY DISCLOSURE project as a 9×9 grid space, embedding narrative camera movement into a prebaked format.

**Goal**: Make films/scenarios that can be **shared without LLM access but made by LLM**.

### Technical Shift

```
LEGOS-multi-channel scene graph
          │
          ▼
    disc-data.json format
          │
          ▼
   Prebaked 3D narratives
```

---

## PHASE 3: TRACTOR-DCE-GYO — The Synthesis

### The Decision

> How to embed more geometry/dimensionality while also making it easier to bridge the gap between:
> - Interest in AI applications
> - Unwillingness or inability to write API-level code

### The LDraw Pivot

Looking for ways to make 3D scenes:
- Easier to build
- More engaging
- More than a toy
- More specific

**Approach**: Shifting to LDraw / using real digital LEGO for scene construction.

### The Crucial Insight

> Using LLM to construct scene led to frustration with fine-grain controls. Assembly of the scene was the issue. This issue was resolved by seeing places where **LLMs got in the way**.

**The Shift**:

```
BEFORE                              AFTER
──────                              ─────
LLM manages the scene               LLM manages the VOID
LLM as constructor                  LLM as gatekeeper
Scene complexity → friction         Void → possibility space
```

### What ONYX STUDIO Aims to Address

The export problem—how to produce outputs that:
- Can be shared meaningfully
- Don't require LLM access to view
- Aren't just vibe-coded websites
- Represent the work done in collaboration with LLMs

---

## TRAIL EVOLUTION: Full Arc

```
LEVEL 0 ─────────────────────────────────────────────────────────────────────
  TILTH: TRAILS AS INVISIBLE EXHAUST
  
  • Speculative world that collapsed under complexity
  • Each addition made system harder to use
  • Trail data: lost in convoluted branches
  
LEVEL 1 ─────────────────────────────────────────────────────────────────────
  THOUSAND-TETRAD: TRAILS AS FEATURES
  
  • 9×9 grid as bounded canvas
  • Tetrad operators as transformers
  • 100+ test scenes
  • Trail data: session logs, API costs, branch trees
  • Collaborators could engage but export remained a problem
  
LEVEL 2 ─────────────────────────────────────────────────────────────────────
  TRACTOR-DCE-GYO: TRAILS AS BACKBONE (EMERGING)
  
  • LLM manages void, not scene
  • LDraw/LEGO as scene grammar
  • ONYX STUDIO for meaningful export
  • Trail data: becomes the product itself
```

---

## Key Learnings

### On Complexity

> As project context grew, ability to finish it got exponentially more challenging.

**Solution**: Invariant design patterns that scale without accumulating complexity.

### On Collaboration

> Not trying to act like I had a real platform.

**Solution**: Documents, prompt guides, hands-on friction exposure. Get out of the way.

### On Technical Thresholds

> Did not meet the threshold YET!

**Solution**: Keep building toward recognition as future collaborator. Learn context engineering.

### On LLMs in Creative Tools

> Assembly of the scene was the issue. LLMs got in the way of fine-grain control.

**Solution**: LLM as gatekeeper of void space, not constructor of scene.

### On Export

> Bigger issue is how to export something generated with LLM collaboration that is not just a vibe-coded website.

**Solution**: ONYX STUDIO, disc-data.json, prebaked narratives.

---

## Ontology Mapping: This Journey

### Objects Generated

| Symbol | Type | Instance in This Journey |
|--------|------|--------------------------|
| `C` | Creator | Watson Hartsoe |
| `T` | Trail | TILTH → THOUSAND-TETRAD → HOLO → TRACTOR |
| `A` | Artifact | 100+ test scenes, role decks, grid layouts |
| `M` | Metadata | API costs, collaboration logs, workshop notes |
| `D` | Decision | Pivot from 2D to 3D, LLM as void manager |
| `S` | Tool | Thousand-tetrad, HOLO-project |
| `S*` | Trail-Aware Tool | ONYX STUDIO (emerging) |
| `P` | Pattern | Invariant 9×9 substrate, complexity spiral |
| `I` | Intent | Enable collaborative speculation at scale |

### Morphisms Enacted

```
generates : Watson → {TILTH, THOUSAND-TETRAD, HOLO, TRACTOR}
    "Creator generates trail through iterative failure and pivot"

contains : Trail → {test scenes, API logs, collaboration notes}
    "Trail contains artifacts of each phase"

observes : ONYX STUDIO → Trail
    "Trail-aware tool observes the accumulated journey"

infers : ONYX × Trail → {INVARIANT_SUBSTRATE, COMPLEXITY_SPIRAL}
    "Tool infers patterns: what scales vs. what collapses"

adapts : ONYX × Patterns → ONYX'
    "Tool adapts: LLM manages void, not scene"

supports : ONYX' → Collaborative Speculation at Scale
    "Adapted tool supports intent without requiring API-level code"
```

---

## Collaborator Credits

| Name | Role | Project Connection |
|------|------|-------------------|
| **Shuruq Tramontini** | Thousand Lives simulation architect | 1000-small-futures, substrate inspiration |
| **Tehri Marttila** | Portuguese Computational Humanities researcher | Weekly testing, forest/branching collaboration |
| **Jordan Caldwell** | Black Metal worldbuilder | Training Grounds, 6-axis framework |
| **Kayla Uleah Evans** | Responsible AI Summit | Ethical negotiation simulations, the-fork |
| **Parag Mital** | emergentic.ai, Garden in the Machine | Technical threshold reference point |

---

## URLs Index

| Project | URL |
|---------|-----|
| TILTH Investigation | https://hartswf0.github.io/role-deck/tilth-investigation.html |
| Nexadoc Jar | https://hartswf0.github.io/nexadoc-jar/ |
| Ekphrasis (Anecdote of a Jar) | https://hartswf0.github.io/nexadoc-jar/epir.html |
| Tetrad Pad | https://hartswf0.github.io/role-deck/tetrad-pad.html |
| Thousand Tetrad | https://hartswf0.github.io/1000-small-futures/thousand-tetrad.html |
| LEGOS Framework | https://hartswf0.github.io/LEGOS/ |
| HOLO Project | https://hartswf0.github.io/holo-project/holo-project.html |
| emergentic.ai | https://emergentic.ai |
| NeurIPS Panel | https://neurips.cc/virtual/2025/loc/san-diego/panel/131735 |

---

## Academic Context

**Course**: LMC-6650 Project Studio: Creating Toolkits & Engagements with Social Values during the Design of Technology in Organizations (Fall 2025)

**Instructor**: Richmond Y. Wong, PhD

**Key Reading Connections**:
- Weeks 10–14: Project Workshopping → THOUSAND-TETRAD development
- Week 16: Final Presentations → TRACTOR-DCE-GYO synthesis

---

*This journey map documents the trail from speculative failure to invariant infrastructure—through the collaborators and pivots that shaped the path.*

**Credits**: Project Lead: Watson Hartsoe · Development: GPT-5, Claude, Gemini · Fall 2025
