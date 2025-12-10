# Flatness is Discipline: Void Management as Architectural Principle for LLM Collaboration

**Hart Schwartz**  
Georgia Institute of Technology  
LMC-6650: Creating Toolkits & Engagements with Social Values  
December 2025

---

## Abstract

This paper reports a practical discovery from 150+ hours of LLM collaboration: **don't ask the LLM to construct content (scene management); ask it to prepare structure you fill (void management).** The insight emerged from project failure—a speculative world called TILTH that collapsed under accumulated complexity—and crystallized into an invariant design pattern: 9×9 grid + tetrad operators + chat layer, now deployed across six toolkit components. I ground the discovery in course readings (Scott's legibility, Meadows's leverage points, Shilton's values levers, Wong's infrastructure inversion) and report validation through collaborator testing. The contribution is a design heuristic for LLM collaboration and a prompt infrastructure (POML, 1,300+ lines) that embodies it.

---

## 1. The Problem: Complexity Grey

TILTH was a speculative company I built with LLM assistance—role decks, personas, negotiation simulations, tetrads, prompt operators, quizzes, leaked documents. Each generation coherent in isolation. Collectively: **complexity grey**. I couldn't tell broken from designed. Each edit required understanding the accumulated whole. The project became unfinishable (cf. Brooks, 1987 on "essential vs. accidental complexity").

**Observation:** Complexity accumulated faster than coherence could maintain it.

---

## 2. The Discovery: Void vs. Scene

The pivot came from constraint: it had to work on a phone. What survived was an invariant substrate—**Thousand-Tetrad**:

| Component | Function |
|-----------|----------|
| 9×9 grid | Bounded canvas (81 cells) |
| Tetrad operators | Transformation vocabulary (Enhance/Obsolesce/Retrieve/Reverse) |
| Chat layer | Natural language control |
| Phone constraint | Forces flatness |

This worked where TILTH failed. The difference:

| Scene Management (TILTH) | Void Management (Thousand-Tetrad) |
|--------------------------|-----------------------------------|
| LLM generates content | LLM suggests dimensions |
| Each session accumulates | Each session fills empty cells |
| Cells interdependent | Cells independent |
| Heavy, session-bound | Light, exportable |

**The insight:** When LLMs manage scenes (content), complexity accumulates. When LLMs manage voids (structure), complexity stays with the user who owns it.

---

## 3. The Toolkit

The insight became architectural principle across six components:

| Tool | Void Structure | Course Connection |
|------|---------------|-------------------|
| **Thousand-Tetrad** | 9×9 grid + tetrad operators | McLuhan's tetrad as prompt controller |
| **Privacy Value Labels** | 14 CI dimensions (empty axes) | Mulligan/Koopman/Doty's privacy analytic |
| **Haunted Tools** | 7 archetypes × form/concept/twist | Mattern "Unboxing the Toolkit" + Barthes |
| **Role Deck** | 4 Bartle types × 3 risk patterns | Wong's practitioner archetypes |
| **The Fork** | Ethical frameworks as dialogic agents | Shilton's values levers |
| **Func-Sub** | 6-axis spatial reasoning substrate | Wong's infrastructure inversion |

All share the invariant pattern: **empty structure the user fills**, not populated content the user navigates.

### Export: disc-data.json

Scene outputs die with the session. Void outputs travel:

```json
{
  "void_structure": { "dimensions": 9, "operators": 4 },
  "instantiated_cells": [
    { "row": 3, "col": 5, "content": "USER_CHOICE" }
  ]
}
```

The file contains choices, not LLM memory. It works without API access.

---

## 4. Theoretical Grounding

### Meadows: Leverage Point Level 1

The void/scene distinction operates at Meadows's highest leverage—**the mindset out of which the system arises** (Meadows, 2008):

> "AI should make things for me" → Scene → Dependency  
> "AI should prepare possibilities" → Void → Agency

### Scott: Legibility Without Destroying Mētis

Scene management imposes the LLM's legibility grid, destroying local knowledge. Void management hands over structure while **preserving space for mētis**—the user's situated judgment (Scott, 1998).

### Shilton: Values Levers

Void structures **create openings for values discussions** by making ethical dimensions explicit (Shilton, 2013). Privacy Value Labels' 14 empty dimensions invite articulation; a scene of pre-filled privacy concerns forecloses it.

### Wong: Infrastructure Inversion

The export format (disc-data.json) performs Wong's **infrastructural inversion**—making the prompt architecture visible rather than black-boxed (Wong, 2021). The void is the infrastructure made examinable.

---

## 5. Evidence

### Failure-Success Pairs

| Project | Approach | Modifications | Outcome |
|---------|----------|---------------|---------|
| TILTH | Scene | 8 | Collapsed—complexity grey |
| Thousand-Tetrad | Void | 40+ | Sustained—cells independent |
| HOLO (early) | Scene (live 3D) | 12 | Frustrated—hallucinated positions |
| HOLO (pivoted) | Void (disc-data.json) | 30+ | Exported—shareable without API |

### Collaborator Testing

| Collaborator | Context | Finding |
|--------------|---------|---------|
| Tehri Marttila | Computational humanities (Portugal) | Pushed toward open-source LLMs; substrate transferred |
| Jordan Caldwell | Black Metal philosophy | 6-axis Func-Sub framework adopted |
| Kayla Uleah Evans | Responsible AI Summit | The Fork scenarios used in training |

Sharing **prompt guides** (void) worked. Sharing **full project exports** (scene) overwhelmed.

---

## 6. POML: Prompt Infrastructure

The insight became infrastructure through POML (Prompt Orchestration Markup Language)—1,374 lines across 9 files:

| POML File | Function | Lines |
|-----------|----------|-------|
| forensic.poml | Multi-lens ethical diagnostic | 351 |
| parody.poml | meta-prompt generator | 280 |
| tactics.poml | De Certeau concordance | 239 |
| prompt.poml | Natural language → POML | 184 |

These are **prompts that generate prompts**—infrastructural, not transactional. They embody void management: each defines structure (lenses, axes, transformation rules) without specifying content.

---

## 7. Design Implications

### For LLM Practitioners

**Before starting:** Ask, "Am I requesting content or structure?"

**When stuck:** Extract dimensions from accumulated scene. Keep axes; discard points.

**When sharing:** Give collaborators voids (templates, guides), not scenes (completed outputs).

### For Toolkit Builders

**Design empty.** The most powerful toolkit is the one users fill, not the one pre-filled.

**Constrain dimensions.** The 9×9 grid works because it forces flatness. Complexity lives in user choices, not system accumulation.

**Enable export.** Scene outputs require your context to understand. Void outputs carry their structure with them.

### For Disclosure Frameworks

Current policies assume scene-based AI use (discrete prompts → discrete outputs). Void-based use—structure prepared, instances chosen over time—doesn't itemize. Trail visibility (cf. Wong's infrastructure inversion) would work better than prompt inventories.

---

## 8. Limitations

This is practitioner reflection, not controlled study. The evidence is: TILTH failed, Thousand-Tetrad works, three collaborators found the substrate useful. I haven't tested across domains, practitioners, or LLM architectures. The heuristic is offered, not proven.

---

## 9. Conclusion

> **Flatness is not poverty. Flatness is discipline.**

TILTH failed because it sprawled. Thousand-Tetrad works because it stays flat. The difference is what the LLM manages: scene (content that accumulates) or void (structure that bounds).

The toolkit, the POML library, the export format—all embody one principle: **let the LLM prepare the void; let the user fill it.** Agency is preserved not by limiting AI but by relocating AI work to structure rather than content.

---

## Generative AI Statement

This project used ChatGPT-4o, GPT-5, Claude, and Gemini as embedded collaborators across 150+ hours. The AI participated in the failures and successes I describe. Judgment—what mattered, what to pursue, what to abandon—remained human. The POML library (1,374 lines) documents the prompt infrastructure developed.

---

## References

Brooks, F. P. (1987). No silver bullet. *Computer*, 20(4), 10–19.

Meadows, D. H. (2008). *Thinking in Systems*. Chelsea Green.

Mulligan, D., Koopman, C., & Doty, N. (2016). Privacy is an essentially contested concept. *Philosophical Transactions A*, 374.

Scott, J. C. (1998). *Seeing Like a State*. Yale.

Shilton, K. (2013). Values levers. *Science, Technology, & Human Values*, 38(3), 374–397.

Suchman, L. (1987). *Plans and Situated Actions*. Cambridge.

Wong, R. Y. (2021). Tactics of soft resistance. *PACM HCI*, 5(CSCW2).

---

*Word count: ~1,400. Practitioner reflection for LMC-6650.*
