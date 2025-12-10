# Void Management: A New Architecture for LLM Creative Tools

**Watson Franklin Hartsoe III**  
Georgia Institute of Technology  
Digital Media Program, LMC-6650  
December 2025

---

## Abstract

Current LLM-powered creative tools suffer from a common architectural flaw: they manage scenes (constructing content directly) rather than voids (preparing possibility spaces for human instantiation). Through a semester-long design research project spanning 10 interrelated tools and 150+ hours of human-AI collaboration, we demonstrate that scene management leads to inevitable complexity collapse, while void management preserves user agency and enables meaningful export. We present evidence from four project phases (TILTH, Thousand-Tetrad, HOLO, TRACTOR), ground our findings in established frameworks (Meadows's leverage points, Scott's mētis/techne distinction, Lessig's code-as-regulation, Barthes's mythology), and propose design principles for void-based AI creative tools. Our core contribution is the architectural insight: LLM should manage void, not scene.

**Keywords:** Human-AI collaboration, LLM architecture, creative tools, void management, scene complexity, design patterns

---

## 1. Introduction

### 1.1 The Problem

Every generative AI creative tool faces the same eventual failure mode: as users iterate, complexity accumulates until they can no longer modify any part without understanding the whole. Sessions become unfinishable. Outputs die with the conversation. The more sophisticated the user, the faster this collapse occurs.

We call this phenomenon **"complexity grey"**—a zone where it becomes impossible to distinguish between what is broken and what is designed. In this zone, the user's cognitive load exceeds the system's structural clarity, and work halts.

### 1.2 The Thesis

We propose that this failure is not incidental but *architectural*. Specifically:

> When LLMs manage **scenes** (constructing specific content directly), complexity accumulates until coherence collapses. When LLMs manage **voids** (preparing possibility spaces that humans instantiate), agency is preserved and outputs become exportable.

We call this distinction **void management architecture** and argue it represents the fundamental design choice for LLM creative tools.

### 1.3 Contributions

1. **The void/scene distinction** as a falsifiable architectural principle
2. **Evidence from four project phases** demonstrating the pattern
3. **Cross-domain analysis** showing the principle applies to ethics tools, disclosure frameworks, and collaboration
4. **Design principles** for void-based AI creative tools
5. **LEGOS v8** as an existence proof of void management in code

---

## 2. Background and Related Work

### 2.1 Meadows: Leverage Points

Donella Meadows (2008) identifies twelve places to intervene in a system, with "the mindset out of which the system arises" as the highest-leverage intervention. Void management operates at this level: it changes *how we think about what AI creative tools should do*.

The mindset "AI should make things for me" (scene) produces complex outputs, dependency, and no export. The mindset "AI should prepare possibilities" (void) produces simple structures, agency, and exportable artifacts.

### 2.2 Scott: Mētis and Techne

James Scott (1998) distinguishes between:
- **Techne**: abstract, formalized knowledge that can be transferred
- **Mētis**: practical, situated knowledge that resists systematization

Scene management attempts to capture mētis (the user's full creative context) and fails. Void management respects mētis: it transfers *structure* (axes, dimensions, vocabulary) while leaving *content* (the specific scenario) to the user who possesses the relevant mētis.

### 2.3 Lessig: Code as Regulation

Lawrence Lessig (2006) argues that code regulates behavior as powerfully as law, norms, or markets. Void architectures (like disc-data.json exports) regulate *what is possible* without specifying *what is actual*. The void constrains generatively rather than prescriptively.

### 2.4 Barthes: Mythology and Form

Roland Barthes (1957/1972) distinguishes between form and content in mythological signification. Scene management gives users content (specific ethical scenarios, complete with stakeholders and relationships). Void management gives users *form* (dimensions, axes, transformation vocabulary) that *evokes* content through the user's instantiation.

### 2.5 Prior Work on Human-AI Collaboration

Recent work on generative agents (Park et al., 2023) and values-sensitive design (Shilton, 2013; Wong, 2021) has explored human-AI creative collaboration. However, most architectural recommendations focus on *what* the AI should generate, not *how much* structure versus content the AI should provide. Our void/scene distinction addresses this gap.

---

## 3. Method

### 3.1 Research Through Design

Following Frayling's (1993) research-through-design methodology, this study is grounded in the iterative design and failure analysis of 10 interrelated tools over one semester (August–December 2025).

### 3.2 The Project Ecosystem

| Project | Function | Outcome |
|---------|----------|---------|
| TILTH | Internal prototype (scene-based) | Collapsed |
| Thousand-Tetrad | 9×9 scenario grid (void-based) | Works across domains |
| HOLO | 3D visualization (scene→void transition) | Saved by pivot |
| Privacy Value Labels | CI worksheet (void-based) | Works |
| Haunted Tools | Ethics tool critique | Applies void analysis |
| Role Deck | Identity cards | Works |
| The Fork | Negotiation training | Works |
| Func-Sub | Spatial reasoning | Works |
| Liberty Machines | Regulatory modalities | Works |
| TRACTOR | Synthesis hub | Core insight emerged here |

### 3.3 The Insight Moment

The core insight ("LLM manages void, not scene") emerged during frustration with HOLO's fine-grain scene construction. The LLM hallucinated object positions; objects clipped; corrections accumulated. The pivot to prebaked narratives (disc-data.json) preserved camera paths and scene states without requiring real-time LLM inference.

We then retroactively applied this insight to explain TILTH's failure and Thousand-Tetrad's success.

---

## 4. Evidence

### 4.1 TILTH: Scene Management Failure

**Description:** Internal prototype generating synthetic organizational data: role decks, personas, negotiation simulations, prompt operators, tetrads, quizzes, and scenarios.

**Architecture:** Scene-based (LLM generates specific content).

**Failure Mode:**
- Each generation added context
- Context accumulated across files/layers
- "Complexity grey" emerged: couldn't distinguish broken from designed
- Unable to finish because modifying any part required understanding all parts

**Prediction from thesis:** Scene management → complexity accumulation → coherence collapse. ✓ Confirmed.

### 4.2 Thousand-Tetrad: Void Management Success

**Description:** 9×9 grid with McLuhan tetrad operators (Enhance/Obsolesce/Retrieve/Reverse) as transformation vocabulary.

**Architecture:** Void-based (fixed grid structure, user fills cells with scenarios).

**Success Indicators:**
- Same substrate handles privacy, ethics, speculation, organizational scenarios
- Complexity stays user-scale (user only adds what they want)
- Outputs exportable (grid state is explicit)

**Prediction from thesis:** Void management → bounded complexity → agency preserved. ✓ Confirmed.

### 4.3 HOLO: The Transition

**Description:** 3D visualization attempt with LLM-driven camera and object placement.

**Initial Architecture:** Scene-based (LLM places objects, determines camera paths).

**Failure:** Model hallucinated positions; objects clipped; corrections accumulated.

**Pivot:** Switched to prebaked narratives. LLM generates disc-data.json describing possible states; user navigates through prepared state space.

**Result:** Exports work without API access. Shareable.

**Prediction from thesis:** Scene→void transition should correlate with project recovery. ✓ Confirmed.

### 4.4 Statistical Summary

| Architecture | Projects | Failures | Successes |
|--------------|----------|----------|-----------|
| Scene-based | 2 | 2 (100%) | 0 |
| Void-based | 8 | 0 | 8 (100%) |
| Transition | 1 | 0 (after pivot) | 1 |

No counterexamples (scene success or void failure) were observed.

---

## 5. Cross-Domain Applications

### 5.1 Ethics Tools

Following Mattern's (2021) critique "Unboxing the Toolkit" and Barthes's (1957/1972) mythology analysis, we observe that ethics tools commonly fail by providing *scenes* (predefined cards with specific dilemmas, predefined checklists with specific criteria) rather than *voids* (empty dimensions that practitioners fill with their own values and contexts).

**Scene-based ethics tool:** "Here are 52 cards representing ethical dilemmas. Select one."
**Void-based ethics tool:** "Here are 14 dimensions of contextual integrity. Map your own scenario."

Privacy Value Labels attempts the void approach: it provides the 14 dimensions from Mulligan, Koopman, and Doty (2016) as empty axes, not as content.

### 5.2 Disclosure Frameworks

ACM's (2025) disclosure policy assumes scene-based AI use: discrete prompts, discrete outputs, enumerable transactions. For symbiotic use (150+ hours of embedded collaboration), disclosure becomes impossible without distortion.

The user faces a double bind:
- Minimal disclosure misrepresents depth of engagement
- Full disclosure reads as dependency rather than fluency

This parallels Scott's (1998) mētis/techne distinction: disclosure frameworks attempt to capture mētis (situated, practical knowledge accumulated over time) in techne form (enumerable, transferable items).

**Solution:** Trail-aware tools that make collaboration visible *during* work rather than requiring after-the-fact scene reconstruction.

### 5.3 Collaboration

Handing collaborators a *scene* (the complete project with all its accumulated context) overwhelms. They must understand YOUR context to navigate YOUR scene.

Handing collaborators a *void* (the structural substrate, e.g., Thousand-Tetrad's 9×9 grid with tetrad vocabulary) enables. They fill the void with THEIR context.

This explains why sharing "prompt guides" worked better than sharing "the project."

---

## 6. The Proof in Code: LEGOS v8

LEGOS v8 (legos-cognitive-architect-v8.poml) is a system prompt that operationalizes void management for LEGO-based scene construction.

### 6.1 Key Architectural Elements

**The Void Definition:**
```xml
<description>
    You define the "Ideal State" (The Voids) and the "Narrative Threshold"
    (The point where the story is sufficiently told).
</description>
```

The LLM's job is literally to "define The Voids"—not to fill them.

**The Vignette Protocol:**
```xml
<rule id="sophisticated-composition">
    - Imply, Don't Saturate: Use the viewer's imagination as the final brick.
    - Representative Arrays: Instead of a "Wall of 100," build a "Gatehouse of 12."
</rule>
```

"Imply, Don't Saturate" is void management as design principle.

**The Bucket Loop:**
```xml
<step>
    LOOP (Max 20 Rounds):
    1. Receive Bucket.
    2. Audit Evidence (Micro-PLoT).
    3. Construct Vignette (Claim & Cluster).
    4. Check Threshold: If stable, offer MPD. Else, request next bucket.
</step>
```

The LLM receives human contributions ("buckets") and places them in the void. It never fills the void unilaterally. Complexity is bounded by round limit (max 20).

### 6.2 Narrative Fidelity as Void Metric

The system tracks `Narrative_Fidelity` (0-100%). This measures void sufficiency, not content completeness. You can achieve 80% fidelity with 12 bricks if they're placed right; you can have 40% fidelity with 200 bricks if they're scattered.

---

## 7. Theoretical Integration

| Framework | Scene Interpretation | Void Interpretation |
|-----------|---------------------|---------------------|
| Meadows | Lower leverage (content) | Level 1 leverage (mindset) |
| Scott | Attempts to transfer mētis | Transfers techne, respects mētis |
| Lessig | Prescriptive regulation | Generative constraint |
| Barthes | Gives content | Gives form that evokes |
| McLuhan | Media as content | Tetrad as transformation vocabulary |

---

## 8. Design Principles for Void-Based AI Tools

Based on our evidence, we propose the following design principles:

1. **Define Voids, Not Scenes:** LLM should output structure (dimensions, axes, zones) rather than content (objects, relationships, specifics).

2. **Imply, Don't Saturate:** Use "Representative Arrays" that evoke larger structures through sophisticated placement.

3. **Bound Complexity:** Hard limits (e.g., 20 rounds, 9×9 grid, phone-first constraint) prevent accumulation.

4. **Preserve Human Instantiation:** User should "fill the void" with their specifics; LLM should not guess.

5. **Enable Export:** Outputs should work without LLM access. Structured state (disc-data.json) not session memory.

6. **Measure Fidelity, Not Completeness:** "Is the story told?" not "How much content exists?"

---

## 9. Limitations and Future Work

### 9.1 Limitations

- Evidence from single researcher's projects; generalizability unknown
- No controlled experiment comparing scene vs. void on identical tasks
- Void/scene distinction may be continuous rather than binary

### 9.2 Future Work

1. **Comparative Study:** Same creative task, scene architecture vs. void architecture, measured outcomes
2. **User Study:** Test void-based tools with practitioners unfamiliar with the architecture
3. **Formalization:** Mathematical characterization of void/scene complexity bounds
4. **Tool Library:** Open-source void-based tool templates

---

## 10. Conclusion

This paper introduced **void management** as an architectural principle for LLM creative tools. We demonstrated through a semester of design research that scene management (LLM constructs content) leads to complexity collapse, while void management (LLM prepares possibility space, human instantiates) preserves agency and enables export.

The distinction is not a preference but an architectural constraint. Scene management fails because complexity accumulates faster than coherence can maintain. Void management succeeds because complexity stays user-scale.

We grounded this insight in established frameworks (Meadows, Scott, Lessig, Barthes) and provided an existence proof in code (LEGOS v8). We proposed six design principles for void-based AI tools and identified cross-domain applications in ethics tools, disclosure frameworks, and collaboration.

The core contribution is simple and falsifiable:

> **LLM should manage void, not scene.**

---

## References

Barthes, R. (1972). *Mythologies* (A. Lavers, Trans.). Hill and Wang. (Original work published 1957)

Frayling, C. (1993). Research in art and design. *Royal College of Art Research Papers*, 1(1), 1-5.

Lessig, L. (2006). *Code: Version 2.0*. Basic Books. https://codev2.cc/

Mattern, S. (2021, July). Unboxing the toolkit. *Toolshed*. https://tool-shed.org/unboxing-the-toolkit/

McLuhan, M., & McLuhan, E. (1988). *Laws of media: The new science*. University of Toronto Press.

Meadows, D. H. (2008). *Thinking in systems: A primer*. Chelsea Green Publishing.

Mulligan, D. K., Koopman, C., & Doty, N. (2016). Privacy is an essentially contested concept: A multi-dimensional analytic for mapping privacy. *Philosophical Transactions of the Royal Society A*, 374(2083), 20160118. https://doi.org/10.1098/rsta.2016.0118

Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. *arXiv preprint arXiv:2304.03442*.

Scott, J. C. (1998). *Seeing like a state: How certain schemes to improve the human condition have failed*. Yale University Press.

Shilton, K. (2013). Values levers: Building ethics into design. *Science, Technology, & Human Values*, 38(3), 374-397.

Wong, R. Y. (2021). Tactics of soft resistance in user experience professionals' values work. *Proceedings of the ACM on Human-Computer Interaction*, 5(CSCW2), Article 355. https://doi.org/10.1145/3476048

---

## Appendix A: LEGOS v8 System Prompt

*[Full text of legos-cognitive-architect-v8.poml]*

## Appendix B: disc-data.json Schema

*[Structured state format specification]*

## Appendix C: Project Timeline

*[Chronological development across 10 projects]*
