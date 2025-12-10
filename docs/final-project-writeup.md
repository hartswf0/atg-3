# LMC-6650 Final Project Submission
## Watson Franklin Hartsoe III
## December 9, 2025

---

# Part 1: Toolkit

**Primary Toolkit Interface:**
https://hartswf0.github.io/tractor-dce-gyo/

**Project Genome (Integrated Documentation):**
https://hartswf0.github.io/tractor-field-notes/project-genome.html

**Component Projects:**
- [Thousand-Tetrad](https://hartswf0.github.io/1000-small-futures/thousand-tetrad.html) — 9×9 scenario grid with McLuhan tetrad operators
- [Privacy Value Labels](https://hartswf0.github.io/privacy-value-labels/) — Contextual Integrity worksheet
- [Haunted Tools](https://hartswf0.github.io/haunted-tools/) — Barthesian mythology catalog
- [Role Deck](https://hartswf0.github.io/role-deck/HUB.html) — Ethical Identity Cards
- [The Fork](https://hartswf0.github.io/the-fork/) — Ethical negotiation simulations
- [Func-Sub (Training Grounds)](https://hartswf0.github.io/func-sub/func-index.html) — 6-axis spatial reasoning substrate

---

# Part 2: Write-Up

## 1. Describe Your Tool/Toolkit

**WAG: Words Assemble Geometries** is a suite of single-file HTML artifacts designed to support values and ethics work in technology design contexts. Rather than a single toolkit, it is an ecosystem of interconnected tools—each responding to specific course readings and addressing distinct aspects of the toolkit critique we explored throughout the semester.

The central innovation is an **invariant design pattern**: a 9×9 grid interface with tetrad operators (Enhance/Obsolesce/Retrieve/Reverse), a chat layer for natural language control, and branching mechanics that allow any scenario state to fork into alternatives. This pattern emerged from the failure of an earlier project called TILTH, which collapsed under its own speculative complexity. The solution was to create infrastructures that get richer the more you use them, rather than harder to maintain.

The toolkit includes:
- **Privacy Value Labels**: A mobile-first Contextual Integrity interface operationalizing Mulligan, Koopman, and Doty's multi-dimensional privacy analytic
- **Haunted Tools**: A Barthesian mythology catalog exposing forms that look like ethics work but avoid transfers of budget, time, rights, or risk
- **Thousand-Tetrad**: A scenario-building substrate using McLuhan's tetrad as prompt controllers
- **ONYX Studio**: An operative workbench that produces shareable artifacts without requiring LLM API access

Each tool is designed as a **single HTML file** that can be opened directly in a browser, forked on GitHub, or modified without dependencies—embodying an anti-tool philosophy that exposes operations rather than hiding them.

## 2. What Issues Does the Toolkit Address?

The toolkit addresses several interconnected problems identified in our course readings:

**The Export Problem**: How do you share something generated through LLM collaboration that is not just a "vibe-coded website" or raw text output? Most generative AI tools produce ephemeral outputs that cannot be meaningfully shared, versioned, or built upon. The toolkit produces structured data files (disc-data.json, LEGOS scene graphs) that persist beyond the session.

**The Complexity Spiral**: As Wong (2021) documented, values work often happens through "soft resistance"—but the tools themselves can create cognitive overhead that makes sustained engagement difficult. TILTH demonstrated this failure mode firsthand. The invariant 9×9 substrate addresses this by providing bounded complexity that scales without accumulating.

**The Toolkit Mythology**: Following Mattern's (2021) "Unboxing the Toolkit" and Petterson et al.'s (2023) critique of power tools, Haunted Tools examines forms that perform ethics work without transferring real resources or shifting real power.

**The API Dependency**: Current LLM-powered creative tools require active API connections, creating barriers for designers who want to explore values-sensitive scenarios but lack technical infrastructure or budget. The shift to "LLM manages void, not scene" means the system prepares possibility spaces that can be explored without live AI.

## 3. Who Are the Audiences?

The toolkit addresses multiple audiences at different levels of technical engagement:

**Primary**: UX researchers and designers working within organizational constraints, who need lightweight tools for values articulation that work on mobile phones, in meetings, or during client consultations. The Privacy Value Labels app specifically targets this use case.

**Secondary**: Ethics practitioners navigating organizational power structures, as mapped in the Role Deck. These are the "soft resisters" Wong describes—people who need to understand their own tactical positions within systems.

**Tertiary**: Computational humanities researchers and simulation architects interested in scenario-building substrates. Collaborations with Tehri Marttila (computational humanities), Jordan Caldwell (speculative worldbuilding), and Kayla Uleah Evans (ethical negotiation training) tested these boundaries.

**Aspirational**: Future collaborators on multi-agent narrative systems like those presented at the NeurIPS 2025 Emergent Stories panel. The toolkit represents an attempt to reach a technical threshold for recognition in that community.

## 4. Context of Use

The toolkit operates across several contexts:

**During design processes**: Privacy Value Labels can be used to map information flows during UX research. The LEGOS framework (Location, Entities, Goals, Obstacles, Shifts) provides vocabulary for scenario articulation.

**During organizational navigation**: Role Deck helps practitioners identify their position within Bartle-taxonomy-style typologies of ethical work—understanding whether they're operating as Achievers, Explorers, Socializers, or Killers within their organizational game.

**During collaborative speculation**: Thousand-Tetrad supports real-time scenario forking during workshops. Tested extensively with collaborators, it enables rapid branching through alternative futures.

**During post-session sharing**: The shift from live LLM scene construction to prebaked narratives (disc-data.json format) enables outputs to be shared, critiqued, and built upon without requiring API access.

## 5. Levers, Leverage Points, and Regulatory Modes

Following **Shilton's (2013) values levers** framework, the toolkit creates openings for values discussions by:
- Making information flows visible (Privacy Value Labels)
- Making ethical identities explorable (Role Deck)
- Making toolkit mythologies explicit (Haunted Tools)

Following **Meadows's leverage points** (via Ehrlichman), the toolkit operates at:
- **Information flows** (making values work visible)
- **Rules of the system** (the 9×9 grid as invariant substrate constrains what can be built)
- **Goals of the system** (shifting from "LLM constructs scene" to "LLM manages void")

Following **Lessig's (2006) regulatory modes**, Liberty Machines explicitly maps Law, Norms, Market, and Code as interactive forces—using the cigarette pack as case study in "freedom theatre."

The toolkit's most significant intervention is at the level of **paradigm shift**: treating trail data (what creators leave behind as they work) as first-class design material rather than invisible exhaust.

## 6. Design/Creation Process

The process followed the arc documented in the TILTH Journey Map:

**Phase 0 (TILTH)**: Built a speculative company (Agronica) to explore through role decks and scenario builders. Failed due to convoluted complexity—a world inside a world that couldn't maintain coherency.

**Phase 1 (Thousand-Tetrad)**: Recognized that better speculative worlds already existed (Ted Chiang, Life After Bob). Built an invariant substrate (9×9 grid + tetrad operators + branching) that could be parasitic off any world rather than constructing its own.

**Phase 2 (HOLO)**: Transitioned from 2D to 3D to make outputs more shareable. Embedded narrative camera movement into prebaked formats.

**Phase 3 (TRACTOR)**: Synthesized components. Crucial insight: LLM frustration with fine-grain scene construction was resolved by having the LLM manage a void (possibility space) rather than the scene itself.

## 7. Learnings and Reflections

**On technical thresholds**: I learned I am not yet technical enough to engage with computer scientists working on multi-agent systems (emergentic.ai, NeurIPS panelists). But I learned enormously about context engineering—how to structure prompts, manage context windows, and build ring buffer memory systems.

**On collaboration without a platform**: Working with Kayla, Jordan, and Tehri taught me to "not try to act like I had a real platform." The better approach was producing documents, prompt guides, and hands-on friction exposure—then getting out of the way to observe.

**On invariant patterns**: The key learning was that design patterns which stay invariant across any scenario-building scale better than patterns that accumulate context. The 9×9 grid + chat + tetrad + footer structure works for privacy scenarios, ethical negotiations, and speculative worldbuilding alike.

**On export as the real problem**: The bigger issue than generation is export—how to produce artifacts from LLM collaboration that others can meaningfully engage with. ONYX Studio's focus on structured output formats attempts to address this.

## 8. Future Directions

If continuing this work, I would pursue:

1. **LDraw/LEGO integration**: Using real digital LEGO for scene construction to make 3D outputs more specific and engaging
2. **Open-source LLM adaptation**: Following Tehri's push toward lower-cost models, restructuring the system prompts to work without API dependency
3. **Multi-agent architectures**: Moving toward the Generative Agents model (Park et al., 2023) with persistent agent memory and social dynamics
4. **Physical artifacts**: Producing printed versions of Haunted Tools and Role Deck cards for workshop contexts
5. **Collaboration with simulation platforms**: Reaching the technical threshold to contribute to projects like emergentic.ai
6. **POML development**: Expanding the prompt library into a formal infrastructure for prompt composition, inheritance, and versioning

---

# Appendix: POML Prompt Library

One artifact of sophisticated AI collaboration is the development of **POML** (Prompt Object Markup Language)—a structured format for prompts that generate other prompts. This library represents 1,374 lines of meta-prompt infrastructure developed through the semester.

## The Library (9 Files)

| File | Purpose | Course Connection |
|------|---------|-------------------|
| `forensic.poml` | Multi-ledger ethical diagnostic (7 lenses + stress tests) | Lessig's regulatory modes as repair levers |
| `mythos.poml` | Weberian ideal type + Bayesian + myth layer | Weber's ideal types as analytical infrastructure |
| `tactics.poml` | De Certeau concordance extraction | Mētis—practical knowledge encoded as prompt logic |
| `parody.poml` | POML→POML forge for parody essay generation | Barthes' mythology analysis operationalized |
| `parody-gen.poml` | Light parody prompt generator | Reusable satire scaffolding |
| `inverse-essay.poml` | Essay reversal + myth layer extraction | Hutcheon's bi-textual frame analysis |
| `prompt.poml` | Natural language → POML transformer | Infrastructure for prompt migration |
| `recursive.poml` | Recursive prompt generation engine | "Prompts that write prompts that write prompts" |
| `meta-prime.poml` | Author OS → prompt logic extractor | Shilton's values levers—implicit operating systems |

## Why This Matters

The POML library exemplifies **layered, sophisticated AI usage** that defies simple disclosure:

1. **Compositional**: Prompts embed and reference other prompts (parody.poml generates an INNER_POML)
2. **Recursive**: Each prompt is designed to spawn further prompts (recursive.poml requires every prompt to generate 3+ children)
3. **Reusable**: Extracted configurations (ideal types, parodic mechanics) transfer across domains
4. **Transparent**: The structure exposes what the prompt is doing, unlike flat natural language

This is **infrastructural** prompt work, not transactional. The POML files are artifacts of mētis—practical knowledge accumulated through sustained engagement that cannot be itemized into discrete "prompts I used."

**Full documentation**: `docs/poml-library.md`

---

# Generative AI Statement

## The Disclosure Theatre Problem

This statement is itself an artifact of what my Week 1 project called **disclosure theatre**: the performance of transparency within a framework that cannot capture the nature of what is being disclosed.

The ACM policy asks me to specify "which content/section(s) were created by generative AI" and provide "the text of input prompts." This assumes a model of AI use where a human writes a prompt, receives output, and decides to keep or edit it—a discrete, transactional relationship that can be itemized.

My use of generative AI this semester does not fit this model. It is closer to what James Scott, in *Seeing Like a State*, calls **mētis**: practical, situated knowledge developed through sustained engagement with a complex environment. Mētis resists the legibility that state-like institutions require. The ACM framework, like Scott's high-modernist planners, demands that tacit knowledge be translated into explicit, auditable form. But the translation destroys the thing being translated.

## What I Actually Did

I used ChatGPT-4o, GPT-5, Claude (Opus, Sonnet, 3.5), and Gemini as **embedded thought partners** across approximately 150+ hours of work this semester. The AI was not a tool I picked up and put down; it was a persistent interlocutor—present in every design decision, every code iteration, every conceptual refinement.

To answer "which sections were created by AI" is like asking which parts of a conversation were created by the other speaker. The ideas emerged *between* us. I could not extract my contribution and label it "human-created" without falsifying the record.

## The Sword of Damocles

This creates a double bind—the very structure I examined in [Disclosure Theatre](https://hartswf0.github.io/dirty-disclosure/disclosure-theatre-01.html):

- **If I disclose minimally**, I perform compliance but misrepresent the depth of engagement
- **If I disclose fully**, the sheer volume and entanglement becomes "suspicious"—evidence not of sophisticated use but of dependency

The ACM guidelines implicitly reward **tidy, transactional use**: "I used ChatGPT to rephrase paragraph 2." They penalize—or fail to accommodate—what might be called **symbiotic use**: sustained collaboration where human and AI cognition become difficult to disentangle.

This asymmetry maps onto Scott's critique: legibility requirements favor **techne** (abstract, systematizable knowledge) over **mētis** (context-dependent, experiential knowledge). Someone who uses AI clumsily, for discrete tasks, can report cleanly. Someone who develops fluency—learning to prompt effectively, to iterate, to build on previous outputs, to structure multi-turn conversations—finds the reporting framework inadequate.

## What the Framework Misses

The ACM policy focuses on **answerism**: the concern that AI will "do the assignment" instead of the student. This is a real concern, but it misunderstands what sophisticated AI use looks like.

In my case, the AI never "did the assignment." The assignment—creating toolkits that address social values in technology design—was not something that could be delegated. Instead:

- The AI helped me think through McLuhan's tetrad as a prompt controller
- The AI generated code that I then debugged, restructured, and often rewrote
- The AI offered interpretations of readings that I contested, refined, or built upon
- The AI produced outputs (100+ test scenes in Thousand-Tetrad) that *I then evaluated* for their implications

The work of judgment—deciding what mattered, what to pursue, what to abandon—remained human. But the ACM framework has no category for "AI as cognitive scaffold" or "AI as externalized working memory."

## An Honest Disclosure

In the spirit of mētis—practical knowledge that resists but doesn't refuse legibility—here is what I can say:

**Tools Used**: ChatGPT-4o, GPT-5, Claude Opus, Claude Sonnet, Claude 3.5, Gemini Pro, Gemini 1.5

**Nature of Use**: 
- Persistent, multi-turn conversations (some extending 50+ exchanges)
- Code generation with extensive human debugging and modification
- Conceptual exploration where AI proposed interpretations I then tested against readings
- Scenario generation within the Thousand-Tetrad engine (direct API integration)
- Document structuring where AI organized my notes into coherent form
- Prompt engineering where I developed system prompts through iterative refinement

**What I Learned From the AI**:
- How to structure ring buffer memory systems
- Approaches to scene graph management
- Linear algebra for 3D transformations (GLB manipulation)
- The concept of "LLM managing void, not scene"

**What the AI Learned From Me**:
- The specific readings and their implications for toolkit design
- The constraints of the course context
- My aesthetic preferences and design vocabulary
- The accumulated context of previous sessions (through explicit context-setting)

**Editing and Post-Generation Work**:
Every AI output was reviewed, and most were substantially modified. But "editing" understates the relationship—it was more like "continuing a conversation" or "following up an experiment."

## The Real Question

The implicit question behind disclosure requirements is: *Did you do the work?*

I did the work. The AI did not take the class. The AI did not attend workshops with Jordan, Kayla, Tehri. The AI did not experience the frustration of TILTH's failure or the insight when the 9×9 grid finally cohered. The AI did not make the decision to pivot from scene construction to void management.

But the AI was present—as interlocutor, as scaffold, as tool, as collaborator—in ways the ACM framework cannot capture without flattening into something unrecognizable.

This statement is itself an act of disclosure theatre. The honest version would be: "I developed mētis with these tools, and mētis, by definition, cannot be fully disclosed."

---

**A Note on Dirty Disclosure**

My very first project this semester—[dirty-disclosure](https://hartswf0.github.io/dirty-disclosure/)—explored this double bind. The Disclosure Theatre interface demonstrated that LLM detectors could be gamed, that filters systematically penalized layered usage, and that the demand for transparency often produces performances of transparency rather than actual insight into use.

This final disclosure statement is the semester coming full circle: the anxiety that has hung over every assignment, the sword of Damocles that made it hard to fully engage, finally articulated as the intellectual problem it always was.

---

**Credits:**
Project Lead: Watson Hartsoe
Instructor: Richmond Y. Wong, PhD
Collaborators: Jordan Caldwell, Kayla Uleah Evans, Shuruq Tramontini, Tehri Marttila
Thought Partners: GPT-5, Claude, Gemini

LMC-6650 Project Studio: Creating Toolkits & Engagements with Social Values
Fall 2025, Georgia Institute of Technology
