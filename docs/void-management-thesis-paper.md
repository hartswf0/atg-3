# Void Management: A Design Pattern for LLM-Assisted Creative Systems

**Abstract**

Large Language Model (LLM)-assisted creative systems exhibit a characteristic failure mode: they function well for simple, bounded tasks but collapse under cumulative modification. This paper introduces the *void management* thesis, which argues that this collapse occurs because these systems attempt to manage unbounded state ("scenes") rather than operating within bounded possibility spaces ("voids") instantiated by human users. We ground this thesis in three domains: (1) empirical evidence from Context Degradation Syndrome and long-horizon task failure; (2) theoretical foundations in systems thinking and political philosophy; and (3) a fifteen-week design research project that iteratively discovered and validated the pattern. The thesis produces a falsifiable prediction: void-managed systems should sustain >20 cumulative modifications without coherence collapse, while scene-managed systems cannot. We propose a design pattern—the invariant grid with flexible instantiation—that operationalizes void management and report results from collaborative testing with four domain experts.

**Keywords:** human-AI collaboration, context engineering, possibility space, design patterns, creative systems

---

## 1. Introduction

### 1.1 The Problem

Anyone who has used ChatGPT for an extended creative project has experienced the phenomenon we call *complexity grey*: the gradual degradation where the system loses coherence, forgets constraints, contradicts earlier commitments, and eventually produces outputs where "broken" and "designed" become indistinguishable (Howard, 2024). The standard response—regenerate, start over, or accept inferior output—represents a fundamental failure of the human-AI collaboration paradigm.

This paper argues that complexity grey is not a bug to be engineered away but a *symptom of a category error* in how we design LLM-assisted creative systems. The error: treating LLMs as scene managers rather than void operators.

### 1.2 Core Distinction

We introduce a fundamental distinction:

**Scene Management:** The system maintains and modifies cumulative state. Each interaction builds upon all previous interactions. The AI must understand the whole to modify any part. Cost grows unboundedly with history.

**Void Management:** The system operates within a bounded possibility space with fixed dimensions and variable instantiations. The AI populates or transforms a pre-structured space. Cost remains constant regardless of history because the structure itself bounds complexity.

The thesis is simple: scene management fails because its cognitive cost grows unboundedly. Void management succeeds because bounded structures cannot accumulate unbounded context.

### 1.3 Contributions

This paper makes four contributions:

1. **Theoretical Framework:** A unified explanation for disparate LLM collaboration failures
2. **Design Pattern:** An invariant structure (9×9 grid + chat + operators) that operationalizes void management
3. **Empirical Grounding:** Case studies from a fifteen-week design research project with four collaborators
4. **Falsifiable Prediction:** A testable claim that distinguishes void-managed from scene-managed systems

---

## 2. Theoretical Foundations

### 2.1 Systems Thinking: Meadows on Leverage Points

Donella Meadows' "Thinking in Systems" (2008) provides the first theoretical scaffold. Meadows identifies twelve leverage points for intervention in complex systems, ranging from parameters (low leverage) to paradigms (high leverage).

The void management thesis argues that the shift from "AI creates content" to "AI prepares possibility spaces" represents a paradigm-level intervention—Meadows' highest leverage point. This shift changes not just *what* the system does but *how we conceptualize what the system is*.

In Meadows' terminology:
- **Scene management = reinforcing feedback loop:** Each modification adds context, which requires more processing, which increases error, which requires more modification. Runaway growth toward collapse.
- **Void management = balancing loop:** The bounded structure absorbs complexity into fixed positions. No matter how many instantiations occur, the structure remains constant.

### 2.2 Political Philosophy: Scott on Mētis vs. Techne

James C. Scott's "Seeing Like a State" (1998) distinguishes between *techne* (abstract, rule-based knowledge that can be systematized and transmitted) and *mētis* (practical, local, contextual knowledge that emerges from experience and cannot be fully codified).

Scene management represents pure techne: the ambition to systematically encode all relevant information into a state that the AI can manipulate algorithmically. This ambition fails for the same reason state-led high-modernist projects fail—it cannot accommodate the mētis of situated human judgment.

Void management preserves mētis by design. The AI provides structure (techne), but humans provide instantiation (mētis). The farmer knows which corner of the field needs attention; the framework simply provides the coordinate system.

**Key insight:** The void is the jar. It doesn't fill the wilderness—it organizes it. Human agency is preserved because the human decides what goes where.

### 2.3 Semiotics: Barthes on Mythology

Roland Barthes' "Mythologies" (1957/1972) analyzes how cultural artifacts naturalize ideology by hiding labor. The mythology of AI follows this pattern: slick interfaces present AI as magical, hiding both the computational labor of inference and the human labor of prompting, correcting, and iterating.

Scene management reinforces this mythology because the growing state becomes opaque. The user cannot see why the system behaves as it does—the history has become too complex to inspect.

Void management demystifies by making structure visible. A 9×9 grid is inspectable. The user can see every cell, understand the operators, trace causality. Both human and machine labor become visible, breaking the mythology of autonomous AI creation.

---

## 3. Empirical Grounding

### 3.1 Context Degradation Syndrome

Howard (2024) documents "Context Degradation Syndrome" (CDS): the user-centric experience of LLM coherence loss during extended interactions. Key observations:

- Coherence reliably degrades after 15-20 significant exchanges
- Users develop compensatory strategies (summarization, explicit reminders)
- The experience is frustrating and undermines trust

CDS describes the *symptom*. The void management thesis provides the *mechanism*: each exchange adds to cumulative state, increasing the cognitive cost of maintaining coherence until that cost exceeds the benefit of any modification.

### 3.2 Long-Horizon Task Failure

Petersson et al. (2024) introduce the Vending-Bench benchmark, testing LLMs on multi-step tasks requiring sustained coherence. Key findings:

- Performance degrades significantly after ~10 sequential decisions
- "Meltdown loops" occur where errors compound
- High variance indicates unstable internal representations

These findings provide empirical evidence for scene collapse in controlled conditions. The 10-decision threshold aligns with Howard's 15-20 exchange observation, suggesting a consistent underlying limit.

### 3.3 The Slice Framework

Soshnin (2024) proposes "context purification"—deliberately limiting context to improve performance. This is, in effect, void management without the theoretical framework. The Slice Framework demonstrates that bounded context improves outcomes, validating the core claim that limits enable rather than constrain.

---

## 4. Design Research: From TILTH to Thousand-Tetrad

### 4.1 The Failure of TILTH

The void management thesis emerged from the failure of TILTH, a speculative design project attempting to build an interactive investigation of a speculative company.

**What TILTH Attempted:**
- A world inside a world (speculative investigation of speculative company)
- Multiple scenario tools interconnected
- Cumulative narrative building across sessions

**Why TILTH Failed:**
- Scenarios became convoluted quickly
- Impossible to show enough of the world for coherence
- Each addition made the whole harder to maintain
- Stuck in "trough of quality"—almost good enough to stand alone, but completion costs grew exponentially with context

TILTH exhibited the exact scene management failure the thesis describes. The project became its own complexity grey.

### 4.2 The Discovery: Nexadoc-Jar

The breakthrough came from an unexpected direction: investigating ekphrasis (verbal description of visual art) as a prompt engineering technique.

While building a tool to show prompt/completion chains, a simpler structure emerged. The complexity of TILTH gave way to the simplicity suggested by Wallace Stevens' "Anecdote of the Jar":

> I placed a jar in Tennessee,  
> And round it was, upon a hill.  
> It made the slovenly wilderness  
> Surround that hill.

The jar is the void. It doesn't fill the wilderness—it organizes it. This became the design principle: provide a bounded structure that makes the unbounded environment sensible.

### 4.3 The Thousand-Tetrad Pattern

From this insight emerged an invariant design pattern:

```
┌──────────────────────────────────────────────────────┐
│  [Corner]     HEADER / OPERATORS        [Corner]     │
└──────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────┐
│                                                      │
│                    9 × 9  G R I D                    │
│                                                      │
│     Any entity can be controlled via grid or chat   │
│              Anything can be branched               │
│                                                      │
└──────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────┐
│                      C H A T                         │
│          Any new UI loads through here              │
└──────────────────────────────────────────────────────┘
┌──────────────────────────────────────────────────────┐
│  [Corner]  Scene Selector │ Tetrad Op  [Corner]     │
└──────────────────────────────────────────────────────┘
```

**Invariant Elements:**
- 9×9 grid (81 bounded positions)
- Chat interface (all new UI loads through it)
- Four corner buttons (persistent controls)
- Scene selector + Tetrad operators (McLuhan's Enhance/Obsolesce/Retrieve/Reverse)

**Variable Elements:**
- What occupies each grid cell
- The scenario being explored
- The operators applied
- The branches taken

This pattern scales across any scenario while remaining inspectable at any moment.

### 4.4 Collaborative Testing

The pattern was tested with four collaborators:

**Tehri Marttila (Computational Humanities)**
- Weekly testing sessions over 3 months
- Pushed toward open-source LLM integration
- Built collaborative forest/branching paths project
- *Friction Point:* System prompt portable, but grid affordances not

**Jordan Caldwell (Speculative Design)**
- "Black Metal" training ground scenarios
- Complex world previously built for physical book
- *Friction Point:* System couldn't absorb world variety quickly enough

**Kayla Evans (Responsible AI)**
- Ethical negotiation training scenarios
- Tested creative director workflow
- *Friction Point:* Codebase fragility limited delegation

**Shuruq Tramontini (Narrative AI)**
- 1000 Lives scenarios
- Extremely bounded futures (opposite of TILTH)
- *Friction Point:* API cost in testing phase

**Cumulative Insight:** The void pattern enabled productive collaboration even when technical execution was fragile. The structure provided shared ground that the implementations couldn't always support.

---

## 5. The Design Pattern

### 5.1 Components

The void management design pattern consists of:

1. **Bounded Grid:** Fixed dimensional structure (9×9 = 81 positions). Every entity has a location. Every location is addressable.

2. **Chat Interface:** All AI interaction flows through a single channel. No modal switching. The chat both queries and modifies the grid.

3. **Operators:** McLuhan's tetrad (Enhance, Obsolesce, Retrieve, Reverse) as transformation functions. Any cell can be operated upon.

4. **Branching:** Any state can be forked. History becomes a tree, not a line. Returns are always possible.

5. **Scene Selector:** Predefined scenarios (67 across 12 categories) that instantiate the grid with specific content.

### 5.2 Why It Works

The pattern succeeds because:

1. **Bounded Complexity:** 81 positions is the maximum. No matter how many modifications, the space doesn't grow.

2. **Inspectable State:** The grid is visible. Users can always see everything that exists.

3. **Addressable Elements:** "Cell 4,7" is unambiguous. Natural language doesn't accumulate ambiguity.

4. **Reversible Modifications:** Branching means no modification is permanent. Exploration is safe.

5. **Separated Concerns:** Structure (grid) vs. content (instantiation) remain distinct.

### 5.3 Comparison to Scene Management

| Dimension | Scene Management | Void Management |
|-----------|-----------------|-----------------|
| State growth | Unbounded | Fixed at 81 |
| Modification cost | Increasing | Constant |
| Inspectability | Decreasing | Constant |
| Reversibility | Difficult | Built-in |
| Coherence | Degrades | Maintains |
| Agency | Erodes | Preserved |

---

## 6. Falsifiability

### 6.1 The Prediction

A properly designed void-managed system should sustain **>20 cumulative modifications** without coherence collapse.

A scene-managed system will exhibit measurable coherence loss within **10-15 modifications** (per Howard 2024, Petersson et al. 2024).

### 6.2 Operationalizing Coherence

Coherence collapse is operationalized as:
- Contradiction of established constraints
- Forgetting of previously specified elements
- Outputs that are "neither broken nor designed" (complexity grey)
- User need to restart or manually intervene

### 6.3 Testing Protocol

1. Create matched pairs: same creative task, one scene-managed (free chat), one void-managed (9×9 grid)
2. Apply identical sequence of 25 modifications
3. Measure coherence at modifications 5, 10, 15, 20, 25
4. Coherence metrics: constraint satisfaction, element recall, user-rated quality

If void-managed systems show significantly better coherence retention at high modification counts, the thesis is supported. If no difference or scene-managed systems perform better, the thesis is falsified.

---

## 7. Opposition Engagement

### 7.1 Engineered Autonomy

**Claim:** Better engineering (larger context windows, improved memory architectures) will solve scene management problems.

**Response:** Engineering improvements are actually implementations of void management. Retrieval-Augmented Generation (RAG) imposes bounded structures on what would otherwise be unbounded context. Memory hierarchies create bounded retrieval spaces. These solutions work *because* they bound complexity, not despite it.

### 7.2 External State Management

**Claim:** Vector databases and external memory solve the cumulative state problem.

**Response:** External memory doesn't create a true scene—it creates a distributed void. The act of retrieval is the act of creating a bounded possibility space. The "scene" never actually exists; only bounded slices are ever present.

### 7.3 User Preference for Completion

**Claim:** Users prefer complete AI outputs. Void management is more work.

**Response:** Distinguish short-term comfort from long-term satisfaction. Complete outputs feel good initially but lead to complexity grey and loss of ownership. Void management requires more initial investment but preserves agency and enables sustained creative control.

---

## 8. Implications and Extensions

### 8.1 Domain Extensions

The void management pattern should extend to:

- **Programming:** IDEs with bounded refactoring possibilities
- **Music Composition:** Tools with modular musical elements in fixed arrangements
- **Narrative Writing:** Character/plot spaces with addressable elements
- **Data Analysis:** Dashboard structures with variable data instantiation

### 8.2 Scale Extensions

- **Multi-Agent:** Coordination through role-based bounded spaces
- **Organizational:** Workflow design with fixed process structures
- **Educational:** Learning environments with bounded problem spaces

### 8.3 Formalization

Future work should formalize:
- **Type Theory:** Void as bounded type, Scene as unbounded
- **Information Theory:** Complexity bounds as entropy measures
- **Category Theory:** Abstract structure of transformation operators

---

## 9. Conclusion

The void management thesis provides a unified framework for understanding why LLM-assisted creative systems fail and how to design systems that succeed. The core insight is simple: bound the space, and complexity cannot grow unboundedly. The jar organizes the wilderness.

This is not a call for less powerful AI but for more thoughtful architecture. The question is not "how much can AI do?" but "what should AI prepare?" When we shift from scene management to void management, we preserve human agency while gaining machine assistance.

The 9×9 grid is not the only possible void. But it demonstrates that voids work—that bounded structures enable sustained creative collaboration where unbounded approaches collapse. Future work should explore other void architectures, test the falsifiable predictions rigorously, and extend the pattern to new domains.

The jar was round. The wilderness surrounded it. And for the first time, the wilderness made sense.

---

## References

Barthes, R. (1957/1972). *Mythologies*. Hill and Wang.

Howard, J. (2024). Context degradation syndrome in extended LLM interactions. *Proceedings of CHI 2024*.

Meadows, D. H. (2008). *Thinking in Systems: A Primer*. Chelsea Green Publishing.

Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. *arXiv:2304.03442*.

Petersson, K., et al. (2024). Vending-Bench: A benchmark for long-horizon decision making in LLMs.

Riedl, M., & Young, R. M. (2006). From linear story generation to branching story graphs. *IEEE Computer Graphics and Applications*, 26(3), 23-31.

Salen, K., & Zimmerman, E. (2004). *Rules of Play: Game Design Fundamentals*. MIT Press.

Scott, J. C. (1998). *Seeing Like a State: How Certain Schemes to Improve the Human Condition Have Failed*. Yale University Press.

Soshnin, A. (2024). The Slice Framework: Context purification for improved LLM performance.

Stevens, W. (1919). "Anecdote of the Jar." *Poetry*.

Yang, W., et al. (2025). Evaluating very long-term conversational memory of LLM agents.

---

*LMC-6650 Values in Design · Georgia Institute of Technology · December 2024*
