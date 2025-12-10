# Void Management: A Theoretical Framework for Context Engineering in LLM-Assisted Creative Systems

**Hart Schwartz**  
Georgia Institute of Technology  
LMC-6650: Computing, Ethics, & Society  
December 2025

---

## Abstract

Generative AI systems increasingly support iterative creative work, yet their collaboration patterns remain poorly theorized. We introduce *void management*, an architectural framework that distinguishes two paradigms: *scene management*, where LLMs construct cumulative content requiring full context to modify, and *void management*, where LLMs prepare bounded possibility spaces that users instantiate.

Our distinction emerges from a 45-year intellectual trajectory: from Suchman's critique of planning models (1987), through Scott's analysis of legibility (1998), to Lessig's architectural regulation (1999), and into contemporary context engineering practice (Karpathy, 2025). We ground the thesis in five theoretical traditions: complexity theory (Simon, Brooks), situated action (Suchman, Agre), cognitive science (Sweller, Cowan), human-centered AI (Shneiderman, Amershi), and infrastructure studies (Bowker, Star, Latour).

The thesis explains recent empirical discoveries: many-shot in-context learning works because it "terraforms" the void with examples; cognitive workspaces help because they prevent scene accumulation; seamful XAI succeeds because it makes the void visible. Through 150+ hours of design research, we developed POML (Prompt Orchestration Markup Language), a 1,300+ line prompt library embodying void principles. Evidence includes failure-success pairs: TILTH (scene management) collapsed; Thousand-Tetrad (void management) sustained 40+ iterations.

The thesis is falsifiable: scene-managed systems maintaining >20 modifications without coherence collapse would refute it. We contribute: (1) the void/scene distinction, (2) a mechanism explaining context degradation, (3) architectural principles for practice, and (4) exportable void structures as proof of concept.

**Keywords:** Context Engineering, Human-AI Collaboration, LLM, Bounded Rationality, Situated Action, HCAI, Prompt Architecture

---

## 1. Introduction

The transition from "prompt engineering" to "context engineering" marks a fundamental shift in human-computer interaction. It reframes the interaction with Large Language Models (LLMs) not as a series of queries, but as the architectural management of a high-dimensional, probabilistic material (Karpathy, 2025). This paper introduces *void management*—a theoretical framework that explains why certain context engineering strategies succeed and others fail.

### 1.1 The Problem

Contemporary LLM collaboration exhibits a puzzling pattern: short interactions often succeed while extended collaborations frequently collapse. A user can obtain excellent results from a single carefully-crafted prompt, yet find that iterating on those results through conversation leads to what Howard (2024) terms "Context Degradation Syndrome"—the gradual breakdown of coherence and utility.

This pattern resists explanation by brute-force scaling. Even with context windows exceeding 100K tokens, long conversations degrade. The limit appears to be human coherence, not model context. Why?

### 1.2 The Thesis

We propose that LLM collaboration succeeds when users manage **voids**—bounded possibility spaces with fixed dimensions and variable instantiations—and fails when users manage **scenes**—cumulative state requiring full context to modify any part.

**Scene management fails because complexity accumulates faster than coherence.** Each response adds context that subsequent responses must account for. The cognitive cost of tracking this accumulated state grows unbounded while human capacity remains fixed. Eventually, the user can no longer distinguish intentional design from accumulated error—a state we call "complexity grey."

**Void management succeeds because bounded possibility spaces cannot accumulate unbounded context.** The void's dimensions are fixed; only instantiation varies. Users navigate finite structure rather than accumulating infinite state.

### 1.3 Contributions

This paper makes four contributions:

1. **Conceptual:** The void/scene distinction as analytical vocabulary for LLM collaboration patterns
2. **Mechanistic:** An explanation of context degradation grounded in complexity theory and cognitive science
3. **Historical:** A 45-year genealogy connecting context engineering to situated action, legibility, and infrastructure studies
4. **Practical:** POML (1,300+ lines) and exportable void structures as proof of implementation

---

## 2. Related Work

### 2.1 Complexity and Bounded Rationality

The intellectual foundations of void management lie in Simon's complexity theory. Simon (1962) introduced "near-decomposable" systems—complex wholes amenable to hierarchical understanding. Brooks (1987) extended this to software, distinguishing *essential* complexity (inherent to the problem) from *accidental* complexity (introduced by solutions). Void management bounds accidental complexity; scene management accumulates it unboundedly.

Cognitive load theory provides the psychological mechanism. Sweller (1988) distinguished intrinsic load (problem difficulty), extraneous load (presentation overhead), and germane load (learning effort). Miller (1956) and Cowan (2001) established bounded working memory capacity. When extraneous load—the overhead of tracking accumulated context—exceeds capacity, users enter "complexity grey."

### 2.2 Situated Action and Representation

Suchman (1987) argued that plans are "resources for action, not its determinants." This anticipates scene management failure: a complete scene is a failed plan, overwhelmed by circumstances it cannot anticipate.

Agre (1997) distinguished *deictic* representations (absolute world models) from *indexical* representations (relative references). Deictic systems require complete state maintenance; indexical systems require only local context. This distinction IS the void/scene distinction: scenes are deictic (require full accumulated state); voids are indexical (require only dimensional navigation).

Winograd and Flores (1987) introduced the concept of *breakdown*—the moment tools become visible. Void management productively embraces breakdown: the void's dimensions are always visible as discrete structure. Dourish (2001) argued context is "achieved, not observed"—constructed through interaction. Scene management treats context as container; void management treats context as achievement.

### 2.3 Infrastructure and Legibility

Bowker and Star (1999) proposed *infrastructural inversion*: making background systems foreground. Scene management black-boxes AI contribution; void management exposes prompt architecture for examination.

Scott (1998) analyzed state "legibility" projects: simplifications that make complex realities tractable but destroy local knowledge (*mētis*). Scene management reproduces high-modernist failure; void management preserves mētis by bounding dimensions while leaving instantiation to human judgment.

Latour (1987, 2005) contributed *inscription* and *black-boxing*. The void is both inscription device (creating durable structures) and anti-black-box (keeping seams visible). Exported void structures are "immutable mobiles"—artifacts that travel without distortion.

### 2.4 Human-Centered AI

Horvitz (1999) established mixed-initiative principles. Amershi et al. (2019) validated 18 guidelines for human-AI interaction. Shneiderman (2022) proposed a two-dimensional framework where ideal systems achieve high control and high automation.

Our contribution is *architectural mechanism*. Guidelines describe WHAT (high control, transparency); void management provides HOW. The void's dimensions are explicit (transparency); instantiation is human (control); LLM prepares the void (automation).

### 2.5 Context Engineering

Karpathy (2025) coined "context engineering" to emphasize architectural curation of the context window. Empirical discoveries validate void management predictions.

Many-shot in-context learning (Anthropic, 2024) works by "terraforming" probability space with examples—populating the void with instantiation templates. Cognitive workspaces (2024-2025) prevent scene accumulation through active memory management. Process alignment (Terry et al., 2025) makes reasoning seams visible. Seamful XAI (Ehsan et al., 2024) advocates strategic exposure of AI limitations—void architecture made navigable.

Chain-of-thought prompting (Wei et al., 2022) and variants (zero-shot CoT, tree-of-thoughts) are proto-void management: constraining the reasoning process without specifying content. POML formalizes what these techniques discovered empirically.

---

## 3. The Void/Scene Distinction

### 3.1 Definitions

**Scene:** A cumulative representation where modifying any element requires understanding the whole. Each LLM response adds to the scene; subsequent responses must account for all prior content. The scene grows monotonically; accidental complexity accumulates without bound.

**Void:** A bounded possibility space with fixed dimensions and variable instantiations. The void defines WHAT CAN BE, not WHAT IS. Users navigate dimensions to instantiate particulars. The void's complexity is fixed by design; only instantiation varies.

### 3.2 The Failure Mechanism

Scene management fails through three stages:

1. **Accumulation:** Each response adds context (successful outputs, corrections, clarifications, examples)
2. **Degradation:** Tracking accumulated context exceeds cognitive capacity; user loses ability to verify coherence
3. **Collapse:** Modifications produce unintended cascading effects; "complexity grey" emerges where broken and designed become indistinguishable

The mechanism is asymptotic: complexity grows faster than coherence, approaching a ceiling where further iteration produces only noise.

### 3.3 The Success Mechanism

Void management succeeds by inverting all three failure modes:

1. **Bounding:** Dimensions are fixed at design time; the void cannot accumulate unbounded structure
2. **Navigation:** Users navigate finite dimensions rather than tracking accumulated state; cognitive load remains bounded
3. **Instantiation:** Each modification fills a void slot without affecting other slots; near-decomposability is preserved by design

### 3.4 Evidence from Practice

Through 150+ hours of design research, we observed consistent patterns:

| Project | Approach | Modifications | Outcome |
|---------|----------|---------------|---------|
| **TILTH** | Scene | 8 | Collapsed—couldn't modify without cascading errors |
| **Thousand-Tetrad** | Void (9×9 grid) | 40+ | Sustained—each cell independent |
| **HOLO Agents** | Void (agent roles) | 25+ | Sustained—role boundaries preserved independence |
| **DCE-GYO Scenarios** | Void (scenario slots) | 30+ | Sustained—scenarios modifiable without interference |

The pattern holds across creative fiction, ethics frameworks, game design, and technical systems.

---

## 4. Theoretical Integration

### 4.1 The Genealogical Arc

Context engineering is not a new invention. It is the modern realization of intellectual projects spanning 45 years:

| Era | Theorist | Contribution | Void Translation |
|-----|----------|-------------|------------------|
| 1973 | Geertz | Thick description | Void = interpretive frame |
| 1983 | Schön | Reflection-in-action | Void enables reflection |
| 1987 | Suchman | Plans as resources | Void = resource for action |
| 1987 | Winograd/Flores | Breakdown | Void makes breakdown visible |
| 1988 | Haraway | Situated knowledges | Void makes position explicit |
| 1997 | Agre | Indexical vs deictic | Void = indexical representation |
| 1998 | Scott | Legibility / mētis | Void preserves mētis |
| 1999 | Bowker/Star | Infrastructural inversion | Void reveals infrastructure |
| 2001 | Dourish | Context as achievement | Void enables achievement |
| 2025 | Karpathy | Context engineering | Practice-level naming |

### 4.2 Five Theoretical Pillars

The thesis is grounded by five independent traditions:

1. **Complexity Theory** (Simon, Brooks): Scene produces non-decomposable systems; void enforces near-decomposability
2. **Situated Action** (Suchman, Agre): Scene = failed plan; void = resource for situated action
3. **Cognitive Science** (Sweller, Cowan): Scene exceeds capacity; void respects bounds
4. **Human-Centered AI** (Shneiderman, Amershi): Void implements HCAI (high control + high automation)
5. **Infrastructure Studies** (Bowker, Star, Latour): Void makes infrastructure visible; scene black-boxes

If ANY of these traditions is correct, the thesis gains support. All five converge on the same conclusion: bounded structures scale; unbounded accumulation collapses.

---

## 5. POML: Void Architecture in Practice

### 5.1 Design Principles

POML (Prompt Orchestration Markup Language) embodies five void management principles:

1. **Define dimensions, not content:** `<role>`, `<task>`, `<rules>` specify structure, not outputs
2. **Bound the possibility space:** Explicit constraints, finite options, enumerated choices
3. **Let users instantiate:** LLM prepares void; human fills slots
4. **Make constraints explicit (seamful):** Visible seams enable navigation
5. **Enable export:** Void structures serialize independently of conversation

### 5.2 Architecture

```xml
<poml>
  <meta minVersion="0.5.0" />
  <role>The Architect</role>
  <task>
    Define a 9×9 semantic grid where:
    - Rows represent narrative functions
    - Columns represent ethical dimensions
    - Cells are VOIDS awaiting user instantiation
  </task>
  <rules>
    - Each cell is independent (near-decomposable)
    - Modifying cell (3,5) does not affect cell (7,2)
    - Grid dimensions are fixed; cell contents vary
  </rules>
  <output-format>
    JSON structure with 81 void slots, each containing:
    - function: the narrative role
    - dimension: the ethical axis
    - instantiation: [USER_INPUT or null]
  </output-format>
</poml>
```

### 5.3 Evidence

The POML library comprises 17+ prompt files totaling 1,300+ lines:

| POML File | Function | Void Architecture |
|-----------|----------|-------------------|
| `legos-cognitive-architect.poml` | Story grid construction | 9×9 dimensional grid |
| `forensic.poml` | Ethical forensics | 6 analytical lenses |
| `mythos.poml` | Mythographic analysis | Weberian ideal types |
| `tactics.poml` | De Certeau extraction | 12 tactical patterns |
| `anneal.poml` | Thesis hardening | 5-cycle refinement |
| `sinter.poml` | Academic positioning | Citation network |
| `furnace.poml` | Deep synthesis | Multi-stream melt |

Each file encodes structure (void) rather than content (scene).

---

## 6. Implications and Applications

### 6.1 For Practitioners

**Design Heuristic:** When beginning LLM collaboration, ask: "Am I accumulating a scene or defining a void?" If you're accumulating (each response adds to a growing whole), expect degradation. If you're defining (responses fill slots in bounded structure), expect sustainability.

**Intervention Point:** When collaboration degrades, don't add more context—reduce to void. Summarize accumulated state into dimensional structure. Convert scene to void.

### 6.2 For Researchers

**Falsification Condition:** The thesis predicts scene-managed systems cannot sustain >20 iterative modifications without coherence collapse. Counterexamples would refute the claim.

**Measurement:** "Coherence collapse" = modifying element X causes unintended changes to >3 elements. This operationalizes the thesis for empirical testing.

### 6.3 For Tool Builders

**Interface Design:** Chat interfaces encourage scene accumulation. Alternatives—infinite canvases (DeckFlow, PromptCanvas), structured editors, dimensional navigators—encourage void management.

**Architecture:** Systems should support void export. Conversation histories die with sessions; void structures (JSON schemas, POML files, dimensional templates) travel independently.

---

## 7. Limitations and Future Work

### 7.1 Limitations

- **Domain:** Evidence comes primarily from creative/design work. Technical, analytical, and administrative domains need investigation.
- **Scale:** Observations involve one practitioner (the author). Multi-user studies needed.
- **Operationalization:** "Coherence collapse" needs refined measurement instruments.

### 7.2 Future Work

- **Empirical Studies:** Controlled comparisons of void vs scene management across domains
- **Cognitive Load Measurement:** Physiological studies (pupillometry, NASA-TLX) of void vs scene conditions
- **Tool Development:** Void-first interfaces that make dimensional structure primary
- **Formalization:** Category-theoretic treatment of void composition and instantiation

---

## 8. Conclusion

This paper introduced void management—a theoretical framework for context engineering in LLM-assisted systems. The core claim is mechanistic: scene management fails because complexity accumulates faster than coherence; void management succeeds because bounded spaces cannot accumulate unbounded context.

The thesis is not speculative philosophy. It is design research grounded in 150+ hours of practice, validated by failure-success pairs, and falsifiable by counterexample. It connects contemporary context engineering to a 45-year intellectual trajectory spanning complexity theory, situated action, cognitive science, human-centered AI, and infrastructure studies.

> **Pragmatic Context Engineering is the modern realization of Suchman's situated action and Scott's legibility projects. It is the discipline of constructing "habitable" information environments within the alien topology of the generative void.**

The void management thesis provides the mechanism for this practice. Scene management is the digital heir of high-modernist planning; void management is the recovery of mētis for the age of LLMs.

---

## Generative AI Disclosure

This paper was developed through extensive collaboration with Large Language Models, principally Claude (Anthropic) and Gemini (Google DeepMind). The collaboration itself constitutes evidence for the thesis: early attempts at scene management (asking LLMs to iteratively draft sections) produced cascading incoherence; later void management (defining dimensional structure, then instantiating) produced the coherent document you are reading.

The author accepts full responsibility for all claims, arguments, and errors. The LLMs were tools for thought, not autonomous authors. This disclosure is itself a test of the thesis: can a paper about void management be produced through void management? The answer appears to be yes.

Specific POML files used: `anneal.poml` (thesis hardening), `sinter.poml` (academic positioning), `furnace.poml` (deep synthesis), `forage.poml` (evidence verification).

---

## References

Agre, P. E. (1997). *Computation and Human Experience*. Cambridge University Press.

Amershi, S., et al. (2019). Guidelines for human-AI interaction. *Proceedings of CHI '19*, 1–13.

Anthropic. (2024). Many-shot in-context learning. https://www.anthropic.com/research/

Anthropic. (2024). Model Context Protocol. https://modelcontextprotocol.io/

Bowker, G. C., & Star, S. L. (1999). *Sorting Things Out: Classification and Its Consequences*. MIT Press.

Brooks, F. P. (1987). No silver bullet: Essence and accidents of software engineering. *Computer*, 20(4), 10–19.

Brown, T., et al. (2020). Language models are few-shot learners. *NeurIPS 2020*, 1877–1901.

Cowan, N. (2001). The magical number 4 in short-term memory. *Behavioral and Brain Sciences*, 24(1), 87–114.

Dourish, P. (2001). *Where the Action Is: The Foundations of Embodied Interaction*. MIT Press.

Ehsan, U., et al. (2024). Seamful XAI: Operationalizing gaps as opportunities. *Proceedings of CHI '24*.

Geertz, C. (1973). *The Interpretation of Cultures*. Basic Books.

Haraway, D. (1988). Situated knowledges. *Feminist Studies*, 14(3), 575–599.

Horvitz, E. (1999). Principles of mixed-initiative user interfaces. *Proceedings of CHI '99*, 159–166.

Howard, J. (2024). Context degradation syndrome. https://jameshoward.us/

Karpathy, A. (2025). Context engineering. X post.

Kojima, T., et al. (2022). Large language models are zero-shot reasoners. *NeurIPS 2022*.

Latour, B. (1987). *Science in Action*. Harvard University Press.

Latour, B. (2005). *Reassembling the Social*. Oxford University Press.

Lessig, L. (2006). *Code: Version 2.0*. Basic Books.

Meadows, D. H. (2008). *Thinking in Systems: A Primer*. Chelsea Green.

Miller, G. A. (1956). The magical number seven. *Psychological Review*, 63(2), 81–97.

Schön, D. A. (1983). *The Reflective Practitioner*. Basic Books.

Scott, J. C. (1998). *Seeing Like a State*. Yale University Press.

Shneiderman, B. (2022). *Human-Centered AI*. Oxford University Press.

Simon, H. A. (1962). The architecture of complexity. *Proceedings of the American Philosophical Society*, 106(6), 467–482.

Suchman, L. A. (1987). *Plans and Situated Actions*. Cambridge University Press.

Sweller, J. (1988). Cognitive load during problem solving. *Cognitive Science*, 12(2), 257–285.

Terry, M., et al. (2025). Process alignment. *Proceedings of CHI '25*.

Wei, J., et al. (2022). Chain-of-thought prompting elicits reasoning in large language models. *NeurIPS 2022*.

Winograd, T., & Flores, F. (1987). *Understanding Computers and Cognition*. Addison-Wesley.

---

*Paper submitted December 2025. Word count: ~4,500.*
