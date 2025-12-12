# WAG Studio Pattern Glossary: Theoretical Groundings

> Recurring behaviors and design patterns across the WAG Studio Suite, grounded in HCI, CSCW, and computational narratology.

**Last updated:** December 2025 · 18 patterns · 8 ontology types · 6 morphisms

---

## Ontology Types (C-T-A-M-D-S-P-I)

These types form a genome schema for tracking creative provenance—who made what, when, why, and how. The structure draws from David Spivak's *Ontology Logs* (ologs), which provide "a rigorous system for knowledge representation using the language of category theory as a formal scaffold" (Spivak 2012). In Spivak's framework, an olog is not merely a diagram but a "functorial" mapping between categories—ensuring that relationships between concepts are *structure-preserving*. The WAG Genome (C-T-A-M-D-S-P-I) functions as an olog where each type represents an object and each morphism represents a structure-preserving arrow.

| Type | Name | Theoretical Grounding |
|------|------|----------------------|
| **C** | **Creator** | The human author whose decisions shape the trail. Draws on Geertz's concept of "author-function" and what Suchman (1987) calls the "accountable actor"—the situated agent whose decisions are visible in the artifact trail. |
| **T** | **Trail** | The evolving history of a creative work; a temporal sequence of artifacts and decisions. Grounded in Bush's (1945) *Memex* concept: "a device in which an individual stores all his books, records, and communications... and which may be consulted with exceeding speed and flexibility." The trail is Bush's "associative trail" made computational. |
| **A** | **Artifact** | Concrete outputs: MPD files, JSON manifests, GLB exports. What Hutchins (1995) calls "cognitive artifacts"—objects that "have been shaped by their participation in cultural practices" and that scaffold distributed cognition. |
| **M** | **Metadata** | Timestamps, file-learnings, birth dates. "Data about data"—the contextual envelope. Following Bowker & Star's (1999) work on *classification and infrastructure*, metadata is the "invisible" layer that enables coordination across contexts. |
| **D** | **Decision** | Architectural choices: "use stud_skeleton," "adopt Frank bus." Schön's (1983) "reflection-in-action"—the in-situ design decisions that leave traces in the system. Each decision is an intervention in Meadows' (1999) sense: a "leverage point" that shapes system behavior. |
| **S** | **Tool** | Software that transforms artifacts. Swiss, COURAGE, GOLD, MENTO. These are what Beaudouin-Lafon (2000) calls "instruments"—reified commands that become first-class manipulable objects. |
| **P** | **Pattern** | Recurring structure detected across artifacts. Following Alexander's (1977) *A Pattern Language*: "each pattern describes a problem which occurs over and over again in our environment, and then describes the core of the solution." |
| **I** | **Intent** | The creator's purpose. What Geertz (1973) calls "thick" meaning—the cultural and contextual significance that transforms a "twitch" into a "wink." Intent is the semantic layer that disambiguates action. |

---

## Morphisms (Structure-Preserving Relationships)

Following category theory (cf. Spivak's *Category Theory for the Sciences*, 2014), these are structure-preserving maps between types. In the WAG Ontology, morphisms are not merely labels—they are *functors* that guarantee "what is true in one category remains true when reflected in another" (Spivak 2014).

### `generates : C → T`
A Creator generates a Trail through sustained practice.

> **Thick Description:** Watson Hartsoe generates the DCE-GYO trail over months, producing 200+ HTML artifacts from `wag-brave.html` to `homer-studio.html`. This is what Lave & Wenger (1991) call "legitimate peripheral participation"—learning through doing, leaving traces of practice.

### `contains : T → {A, M, D}`
A Trail contains Artifacts, Metadata, and Decisions.

> **Thick Description:** The Trail is a "sedimentary" structure in Dourish's (2001) sense—context that accumulates layer by layer, each decision and artifact becoming part of the interpretive backdrop for future actions.

### `transforms : S × A → A'`
A Tool transforms an Artifact into a new Artifact.

> **Thick Description:** GOLD transforms an MPD file by editing a brick line. COURAGE transforms MPD into GLB for export. This is Beaudouin-Lafon's (2000) "instrumental interaction"—the tool "reifies" an abstract operation into a concrete manipulation.

### `syncs : Frank × {S₁, S₂, ...} → coherence`
Frank bus synchronizes multiple Tools into coherent state.

> **Thick Description:** What Star & Ruhleder (1996) call "infrastructure"—the invisible backbone that enables coordination. Frank routes selection events from COURAGE to GOLD: when you click a brick, the entire ecosystem knows.

### `derives : A → stud_skeleton`
An MPD Artifact derives a stud_skeleton ownership map.

> **Thick Description:** This is "analytical provenance"—Hill et al.'s (1992) concept of "edit wear," where "the history of use becomes visible in the artifact itself."

### `supports : S → I`
A Tool supports the Creator's Intent.

> **Thick Description:** TIMBER supports the intent "debug skeleton issues" by docking WERE and MASTER alongside COURAGE. Following Norman (1988): a tool's *affordances* are the action possibilities it provides; when affordances match intent, the tool becomes "ready-to-hand" (Winograd & Flores 1986).

---

## Design Patterns

### `anti-tool`
*A design philosophy where the interface minimizes administrative overhead (menus, toolbars) to allow the user's spatial thinking to dominate.*

**Theoretical Grounding:**

This pattern embodies Heidegger's concept of *Zuhandenheit* (ready-to-hand) as operationalized by Winograd & Flores (1986). Tools are "ready-to-hand" when functioning smoothly—*invisible* in use—but become "present-at-hand" (visible objects of study) when they fail or "break down."

> "The tool should be ready-to-hand, visible only when it breaks down." (Context Engineering Genealogy)

The anti-tool philosophy also aligns with Beaudouin-Lafon's (2000) model of **Instrumental Interaction**, where "reification turns commands into manipulable objects." By removing menus and toolbars, the grid itself becomes the cognitive scaffold—what Norman (1988) calls "knowledge in the world" rather than "knowledge in the head."

**In DCE-GYO:** COURAGE viewer, BRICK Grid, single-file HTML tools.

---

### `stud-skeleton`
*A data structure that maps "stud at position X belongs to part line Y." This is how selections and edits stay coherent across tools.*

**Theoretical Grounding:**

The stud-skeleton embodies Hill et al.'s (1992) theory of **"Edit Wear and Read Wear"**—systems where "the history of use becomes visible in the artifact itself." Each stud-ownership mapping is a form of *provenance tracking*, answering the question: "who made this, and how?"

From a CSCW perspective, the skeleton is what Hutchins (1995) calls a **"cognitive artifact"**—an external representation that participates in distributed cognition. The skeleton map makes implicit relationships (which brick owns which stud) *explicit* at the data level, enabling coordination across surfaces.

**Freshness Convention:** Skeletons carry `source_hash`, `built_at`, and `tool_version` to signal staleness—a form of Bateson's (1972) "difference that makes a difference."

---

### `mpd-truth`
*"One Truth, Many Views." The MPD file is the canonical artifact. Everything else (renders, skeletons, exports) must be regenerable from MPD + manifests.*

**Theoretical Grounding:**

This is the **Single Source of Truth** pattern, grounded in database theory's normalization principles and software architecture's DRY (Don't Repeat Yourself) axiom. But it also reflects Spivak's (2012) olog-theoretic insight: the MPD is the *terminal object* in the category of WAG artifacts—all other representations factor through it.

From a context engineering perspective (Karpathy 2025), this is the principle of **reversibility**: "one can always retrieve the full content from the wilderness using the reference in the jar, but one cannot fit the wilderness in the jar." The MPD is the "jar"—the bounded, canonical container.

**Implication:** If it can't be regenerated from MPD, it's user-facing state and must be explicit (saved, versioned, diffable).

---

### `frank-bus`
*Message bus pattern using `window.postMessage` for cross-tool synchronization without tight coupling.*

**Theoretical Grounding:**

Frank implements what Chalmers & Galani (2004) call **"Seamful Design"**—systems that deliberately expose the "seams" (boundaries, handoffs) of infrastructure rather than hiding them. Unlike seamless integration, Frank's explicit messaging channels make coordination *visible* and debuggable.

The publish/subscribe pattern also echoes Actor-Network Theory (Latour 2005): each WAG surface is an "actor" in a sociotechnical network, and Frank is the "intermediary" that translates between them. The guarantee—"Edit in GOLD updates selection/render in COURAGE"—is what Star & Ruhleder (1996) call "infrastructural reliability."

**Channels:** `selection`, `file-open`, `line-edit`, `camera`

**Failure Mode:** Nothing syncs → use TIMBER/HOMER shell (pre-wired)

---

### `progressive-disclosure`
*"Less is more." Beginners see 10% of the interface. Experts can expand to see 100%. Complexity is earned, not imposed.*

**Theoretical Grounding:**

Grounded in Sweller's (1988) **Cognitive Load Theory**:

> "Extraneous cognitive load reduces capacity for essential problem-solving."

Progressive disclosure minimizes extraneous load for novices while providing expert pathways. It operationalizes what your SHUFFLE papers call "Jobs-ification"—"show the promise, not the plumbing."

This also aligns with Vygotsky's (1978) **Zone of Proximal Development (ZPD)**: the interface scaffolds the user from what they can do alone to what they can do with help. As the user's expertise grows, the scaffolding retracts.

**In DCE-GYO:** Project Genome page, tutorial sections, glossary disclosures, collapsible "Learn more" toggles.

---

### `shell-wiring`
*Pre-wired shells (TIMBER, HOMER) that embed multiple tools in iframes with Frank bus already connected.*

**Theoretical Grounding:**

Shells are what Star & Ruhleder (1996) call **"installed base"**—infrastructure that has been pre-configured by experts so that novices don't need to understand the plumbing. This eliminates the "nothing syncs" failure mode for beginners.

From an Activity Theory perspective (Leontiev 1978), shells convert what would be an "action" (consciously connecting tools) into an "operation" (automatic, unconscious). The cognitive effort is front-loaded by the shell designer, not the end user.

**Trade-off:** Less flexibility than manual multi-tab setup.

**Pattern:** If multi-tab sync breaks, route users into pre-wired shell automatically.

---

### `scene-snapshot`
*Capturing complete application state as a serializable JSON object to enable persistence, sharing, and "time travel."*

**Theoretical Grounding:**

This pattern implements the **Memento Pattern** from software architecture (Gamma et al. 1994)—architectural support for undo/restore without violating encapsulation.

From a provenance perspective, snapshots align with the **W3C PROV model**—capturing the history of *actions*, not just final state. Hill et al. (1992) call this "deep provenance"—"the investigator's own 'trail' of exploration."

**Files:** `gold-*.json`, `wag-gold-scene.json`

---

### `ldraw-composition`
*Using the LDraw MPD (Multi-Part Document) format for multi-part composition. The brick as text, not mesh.*

**1. The Definition:**

LDraw composition is the practice of treating the LEGO brick not as a *proprietary mesh* but as **code**—a line of plain text defining vector geometry. An MPD (Multi-Part Document) is a scene graph encoded as a recursive tree of submodels referencing each other. This enables:

- **Infinite composability:** Any submodel can reference any other submodel
- **Semantic transparency:** A human can read and edit an LDraw file in a text editor
- **Mathematical perfection:** The LDraw Unit (LDU) coordinate system ensures parts from different authors interlock seamlessly

**2. The Theorist (STS/Media Studies Angle):**

> **Source:** [Digital LEGO History Research Architecture](file:///Users/gaia/ATG%203.0/SHUFFLE/markdown/Digital%20LEGO%20History%20Research%20Architecture.md)

The SHUFFLE corpus identifies a **"Dual-Core" history** of the digital brick:

| Dimension | Corporate Brick (Darwin/LDD) | Community Brick (LDraw) |
|-----------|------------------------------|-------------------------|
| **Ontology** | Brick as physics-constrained asset | Brick as linguistic construct |
| **Access** | Closed, proprietary mesh | Open, plain-text coordinates |
| **Epistemology** | "Black box" encrypted geometry | "White box" inspectable code |
| **Flexibility** | Click-and-snap constraints prevent "illegal" connections | Parts can intersect, float—prioritizing freedom |

James Jessiman's contribution (1995) was not just software but a **linguistic definition** of the brick. He established `stud.dat`—a single primitive file referenced by thousands of parts. If you improve `stud.dat`, you improve the entire library instantly. This is what the SHUFFLE papers call **"Void Management" avant la lettre**—optimizing memory long before GPUs were powerful.

> "Jessiman's untimely death in 1997 created a 'martyrdom effect' that solidified the community's resolve to maintain the standard... turning part authoring into a democratic, peer-reviewed process."

**Philip Agre's Critique:** The line-type protocol (Type 0 = meta, Type 1 = part reference, Type 2-5 = geometry primitives) is a form of what Agre (1994) calls **"captured grammar"**—human activity formalized into machine-readable instructions. But unlike Agre's critique of surveillance, the LDraw capture was *voluntary*—a community gift economy that liberated the brick from corporate scarcity.

**Parnas's Modularity:** LDraw embodies Parnas's (1972) principles of **modular decomposition**: a scene is a tree of submodels referencing each other. This is what Alexander (1977) calls "hierarchical pattern language"—each level of the hierarchy is self-contained yet composable.

**3. The SHUFFLE Application (Why It Matters):**

LDraw provides the foundational metaphor for the **LEGO-AI Entanglement thesis**:

> "Effective interaction with probabilistic models is not merely about string construction but about the entanglement of modular, deterministic cognitive blocks (the LEGOs: tools, vector retrievals, constrained interfaces) with the stochastic, fluid nature of the model's latent space (the AI)."

The MPD file *is* the context window: a plain-text, hierarchical, human-readable structure that constrains the infinite wilderness of possible bricks into a coherent scene. The same principle applies to prompt architecture: we compose prompts from modular primitives (role, task, examples) that reference each other.

**Gender/Media Studies Note:** The SHUFFLE research also identifies how "the technical language of LDraw—with its emphasis on coordinates, 'primitive substitution,' and CAD-like interfaces—historically codified the digital ecosystem as a male-dominated engineering domain." The "Pink Brick Problem" (Friends palette segregation in UIs) reveals how even open standards can encode bias.

**Mechanism:** MPD files contain multiple submodels; reference via `1 color x y z ... submodel.ldr`. Parse recursively to build scene graph.

---

## Works Cited

| Citation | Concept | DCE-GYO Application |
|----------|---------|---------------------|
| Agre, P. (1994). Surveillance and Capture | Captured grammar | Frank protocol, LDraw line types |
| Alexander, C. (1977). A Pattern Language | Pattern = problem + solution | Pattern glossary structure |
| Bateson, G. (1972). Steps to an Ecology of Mind | Difference that makes a difference | Skeleton freshness signals |
| Beaudouin-Lafon, M. (2000). Instrumental Interaction | Reification of commands | Tools as instruments |
| Bowker, G.C. & Star, S.L. (1999). Sorting Things Out | Classification as infrastructure | Metadata type (M) |
| Bush, V. (1945). As We May Think | Associative trails | Trail type (T) |
| Chalmers, M. & Galani, A. (2004). Seamful Interweaving | Seamful design | Frank bus visibility |
| Dourish, P. (2001). Where the Action Is | Embodied interaction | Context as sediment |
| Geertz, C. (1973). Thick Description | Thick vs thin meaning | Intent type (I) |
| Hill, W.C. et al. (1992). Edit Wear and Read Wear | History visible in artifact | stud-skeleton provenance |
| Hutchins, E. (1995). Cognition in the Wild | Distributed cognition | Cognitive artifacts |
| Karpathy, A. (2025). Context Engineering | Jar and wilderness | MPD as canonical "jar" |
| Latour, B. (2005). Reassembling the Social | Actor-Network Theory | Frank as intermediary |
| Lave, J. & Wenger, E. (1991). Situated Learning | Legitimate peripheral participation | Trail generation |
| Leontiev, A.N. (1978). Activity, Consciousness, Personality | Activity/Action/Operation | Shell pre-wiring |
| Meadows, D. (1999). Leverage Points | System intervention | Decision type (D) |
| Norman, D. (1988). Design of Everyday Things | Affordances, constraints | Anti-tool transparency |
| Parnas, D. (1972). On the Criteria for Decomposing Systems | Modular decomposition | LDraw composition |
| Schön, D. (1983). The Reflective Practitioner | Reflection-in-action | Decision traces |
| Spivak, D. (2012). Ologs | Structure-preserving maps | Genome morphisms |
| Star, S.L. & Ruhleder, K. (1996). Steps Toward an Ecology of Infrastructure | Infrastructure as installed base | Shell-wiring, Frank |
| Suchman, L. (1987). Plans and Situated Actions | Situated action | Plans as resources |
| Sweller, J. (1988). Cognitive Load Theory | Extraneous vs germane load | Progressive disclosure |
| Vygotsky, L. (1978). Mind in Society | Zone of Proximal Development | Progressive scaffolding |
| Winograd, T. & Flores, F. (1986). Understanding Computers and Cognition | Ready-to-hand, breakdown | Anti-tool philosophy |

---

## Pattern Synthesis: The Thesis

> "The 'Void Management' thesis adopts Norman's view: the wilderness is full of false affordances (irrelevant data); the engineered context must *constrain* the model to the path of success. Meaning emerges from these constraints."
>
> — Context Engineering Genealogy (SHUFFLE)

The WAG Pattern Glossary is not merely a list of design decisions—it is a **theoretical scaffold** that connects implementation to epistemology. Each pattern answers a genealogical question:

| Question | Pattern | Theorist |
|----------|---------|----------|
| How do constraints enable meaning? | anti-tool | Norman, Winograd |
| How does history become visible? | stud-skeleton | Hill et al. |
| What is the canonical source of truth? | mpd-truth | Spivak, Karpathy |
| How do distributed tools coordinate? | frank-bus | Star, Latour |
| How do we manage cognitive load? | progressive-disclosure | Sweller, Vygotsky |
| How do we pre-wire expertise? | shell-wiring | Leontiev, Star |
| How do we support time travel? | scene-snapshot | PROV model, Gamma |
| How do we compose complex structures? | ldraw-composition | Parnas, Alexander |

---

## Additional Patterns (Gap Analysis Additions)

### `worlding`
*Creating a self-contained, rule-based universe that serves as a testing ground for philosophical inquiry. AI as "infinite game" rather than finite tool.*

**Theoretical Grounding:**

Derived from artist Ian Cheng's *Emissaries* trilogy and his book *WORLDING: A Guide for Creators in Changing Times*. Cheng defines a world as a "gated garden with laws and borders"—the imposition of a **Grid** upon the "Wilderness" of generative possibility: "Through meaningful constraints comes infinite possibilities."

> **Source:** [Synthesizing AI Ontologies: A Frankenstein](file:///Users/gaia/ATG%203.0/SHUFFLE/markdown/Synthesizing%20AI%20Ontologies_%20A%20Frankenstein.md)

The Hybrid Frankenstein is designed to *co-inhabit* the institution. It takes over the "metabolic" burden of routine management, allowing human operators to focus on high-level "Worlding."

**Four Personas of Worlding:** Architect (builds structure), Narrator (generates story), Caretaker (maintains coherence), Player (introduces chaos).

---

### `metabolism`
*An AI's "drive to resolve stress"—the internal motivation that compels action when the model's state diverges from reality.*

**Theoretical Grounding:**

Cheng's concept of **metabolism** gives agents a nervous system: "The Nervous System (Worlding): A 'Bag of Beliefs' engine that continuously models the state of the world. It experiences 'Stress' when the model diverges from reality, driving it to 'act.'"

> **Source:** [Synthesizing AI Ontologies: A Frankenstein](file:///Users/gaia/ATG%203.0/SHUFFLE/markdown/Synthesizing%20AI%20Ontologies_%20A%20Frankenstein.md)

This is what distinguishes an *agent* from a *tool*: the agent has internal state that creates urgency.

---

### `void-management`
*The central design challenge of the generative era: managing the high-dimensional, probabilistic possibility space ("Void") and its counterpart, the accumulated context ("Scene").*

**Theoretical Grounding:**

The Void is the latent space of the model—"the bounded but incomprehensibly vast set of all possible token sequences that the model can generate." It is not empty but "dense with the statistical detritus of the internet."

> **Source:** [AI Collaboration Design Research Sintering](file:///Users/gaia/ATG%203.0/SHUFFLE/markdown/AI%20Collaboration%20Design%20Research%20Sintering.md)

The design challenge shifts from *construction* to **sintering**: "The user applies 'heat' (prompts, constraints, context) to the granular dust of the Void to solidify it into a usable 'Scene.'"

---

### `sintering`
*The process of compacting granular material (tokens, probabilities) into a solid mass using heat/pressure (prompts, constraints) without melting it completely.*

**Theoretical Grounding:**

A metallurgical metaphor for context engineering:

- **The Material:** The granular, probabilistic dust of the Void (tokens, pixels)
- **The Energy:** The "heat" of the user's intent (prompts, context, constraints)
- **The Process:** Applying pressure to fuse the material into solid form without melting it completely (preserving generative spark while imposing structure)

> **Source:** [Context Engineering as Material Science](file:///Users/gaia/ATG%203.0/SHUFFLE/markdown/Context%20Engineering%20as%20Material%20Science.md)

---

### `context-rot`
*The degradation of model performance as irrelevant information accumulates in the context window—a form of entropy.*

**Theoretical Grounding:**

Context Rot suggests that LLMs have an **"Attention Budget."** Every token introduced consumes a fraction of this budget. When flooded with irrelevant data ("context pollution"), the signal-to-noise ratio drops, leading to hallucinations or reversion to training priors.

> **Source:** [Context Engineering as Material Science](file:///Users/gaia/ATG%203.0/SHUFFLE/markdown/Context%20Engineering%20as%20Material%20Science.md)

The **Second Law of Context Dynamics:** In a closed context window, the ratio of useful to useless information tends to decrease over time. Without active curation, the system devolves to maximum entropy.

---

### `intra-action`
*Entities do not precede their interaction; they emerge THROUGH their entanglement. Knowledge is intra-actively produced at the moment of inference.*

**Theoretical Grounding:**

Karen Barad's concept from *Meeting the Universe Halfway* (2007). Applied to LLMs: "The 'knowledge' of the model is not a static retrieval from a database. It is intra-actively produced at the moment of inference by the entanglement of the model's weights (past) and the context window (present)."

> **Source:** [Context Engineering: From Anthropology to AI](file:///Users/gaia/ATG%203.0/SHUFFLE/markdown/Context%20Engineering_%20From%20Anthropology%20to%20AI.md)

The engineer, by defining the **"agential cut"** (what is included/excluded from context), literally constructs the reality in which the agent exists.

---

### `agential-cut`
*The boundary that defines what is included or excluded from context—a performative act that constructs reality.*

**Theoretical Grounding:**

From Barad's material-semiotics: "The 'agential cut' defines the boundary between the observer and the observed, or in our case, the prompt and the completion." In practical terms: the *format* of the context (JSON vs XML vs Markdown) is not neutral—it is a material constraint that alters the "semiotic flows" of the model.

> **Source:** [Context Engineering: From Anthropology to AI](file:///Users/gaia/ATG%203.0/SHUFFLE/markdown/Context%20Engineering_%20From%20Anthropology%20to%20AI.md)

---

### `entanglement`
*The thesis that effective interaction with probabilistic models is about the entanglement of modular, deterministic blocks (LEGOs) with the stochastic, fluid nature of the model's latent space (AI).*

**Theoretical Grounding:**

The "LEGO-AI Entanglement" framework: "This framework posits that effective interaction with probabilistic models is not merely about string construction but about the entanglement of modular, deterministic cognitive blocks (the LEGOs: tools, vector retrievals, constrained interfaces) with the stochastic, fluid nature of the model's latent space (the AI)."

> **Source:** [Researching LEGO-AI Entanglement Gaps](file:///Users/gaia/ATG%203.0/SHUFFLE/markdown/Researching%20LEGO-AI%20Entanglement%20Gaps.md)

**The Entanglement is Cultural:** "The effectiveness of a context structure is deeply entangled with the cultural data it was trained on. There is no 'Universal Prompt'; there are only culturally specific keys that unlock specific latent clusters."

---

### `quasi-creature`
*An entity that exhibits superhuman fluency and creative capacity while demonstrating baffling failures in common sense—occupying the "Uncanny Valley of Agency."*

**Theoretical Grounding:**

The Quasi-Creature "exists in a permanent state of oscillation" between Heidegger's ready-to-hand and present-at-hand. It is ready-to-hand when fluently writing code, but violently present-at-hand when it confabulates a legal precedent. This creates **"paradigm stress"**—forcing users to constantly monitor the system's internal state.

> **Source:** [AI Collaboration Design Research Sintering](file:///Users/gaia/ATG%203.0/SHUFFLE/markdown/AI%20Collaboration%20Design%20Research%20Sintering.md)

---

### `situated-action`
*Intelligence is not abstract processing inside "the skull" (or weights) but emerges from improvised interaction between agent and environment.*

**Theoretical Grounding:**

Lucy Suchman's *Plans and Situated Actions* (1987): "Plans are merely resources for action, but the action itself is 'situated'—it emerges from the immediate, improvised interaction between the actor and their environment."

> **Source:** [Context Engineering: From Anthropology to AI](file:///Users/gaia/ATG%203.0/SHUFFLE/markdown/Context%20Engineering_%20From%20Anthropology%20to%20AI.md)

If the agent relies solely on the static plan (system prompt), it fails to adapt to contingencies. This theory underpins **Dynamic Cheatsheets** and **Agentic Context Engineering (ACE)**.

---

### `linguistic-dark-matter`
*Non-Anglocentric context architectures that remain invisible to Western researchers yet dominate Asian functional ecosystems.*

**Theoretical Grounding:**

The Japanese "Negative Prompt" system for image generation—lists of hundreds of "banned" tags to sculpt the negative space—acknowledges that "one cannot simply ask for 'beauty' without explicitly negating the specific types of 'ugliness' or 'blandness' that the model defaults to."

> **Source:** [Researching LEGO-AI Entanglement Gaps](file:///Users/gaia/ATG%203.0/SHUFFLE/markdown/Researching%20LEGO-AI%20Entanglement%20Gaps.md)

Chinese LLMs outperform Western models on Traditional Chinese Medicine queries (78.4% vs 35.9%) because Western models lack the "Linguistic Dark Matter" of TCM concepts (Qi, Meridians) in their vector space.

---

### `vibe-coding`
*Programming through intent and persona rather than explicit logic—the "Narrative Orchestrator" who defines constraints that shape the material of generation.*

**Theoretical Grounding:**

Andrej Karpathy's concept from "Software 3.0": "In Software 3.0, the prompt *is* the code. However, this code is 'soft' and probabilistic." Vibe Coding requires "Emotional Precision"—the ability to articulate the 'vibe' of the desired output so clearly that the model generates correct code or content.

> **Source:** [Context Engineering: From Anthropology to AI](file:///Users/gaia/ATG%203.0/SHUFFLE/markdown/Context%20Engineering_%20From%20Anthropology%20to%20AI.md)

---

## Extended Works Cited

| Citation | Concept | Source Paper |
|----------|---------|--------------|
| Barad, K. (2007). Meeting the Universe Halfway | Intra-action, agential cut | Context Engineering: From Anthropology to AI |
| Cheng, I. (2018). WORLDING | Metabolism, Bag of Beliefs | Synthesizing AI Ontologies: A Frankenstein |
| Karpathy, A. (2024). Software 3.0 | Vibe coding, context as RAM | Context Engineering as Material Science |
| Liu et al. (2023). Lost in the Middle | U-shaped retrieval curve | Context Engineering as Material Science |
| Suchman, L. (1987). Plans and Situated Actions | Situated action, plans as resources | Context Engineering: From Anthropology to AI |
| Chroma Research (2025). Context Rot | Entropy in context windows | AI Collaboration Design Research Sintering |

---

*Part of the DCE-GYO Project Genome knowledge infrastructure.*

*Patterns verified against source code December 2025.*

*Gap analysis completed December 2025.*
