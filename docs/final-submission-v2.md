# LMC-6650 Final Project Submission
## Watson Franklin Hartsoe III
## December 9, 2025

---

# Part 1: Toolkit

**Primary Toolkit Interface:**  
https://hartswf0.github.io/tractor-dce-gyo/

**Project Genome (Integrated Documentation):**  
https://hartswf0.github.io/tractor-field-notes/project-genome.html

**Tractor Field (Single-Scroll Visualization):**  
https://hartswf0.github.io/tractor-field-notes/tractor-field.html

**Component Projects:**
- [Thousand-Tetrad](https://hartswf0.github.io/1000-small-futures/thousand-tetrad.html) — 9×9 scenario grid with McLuhan tetrad operators
- [Privacy Value Labels](https://hartswf0.github.io/privacy-value-labels/) — Contextual Integrity worksheet (14 dimensions)
- [Haunted Tools](https://hartswf0.github.io/haunted-tools/) — Barthesian mythology catalog (7 tool archetypes)
- [Role Deck](https://hartswf0.github.io/role-deck/HUB.html) — Ethical Identity Cards (Bartle taxonomy)
- [The Fork](https://hartswf0.github.io/the-fork/) — Ethical negotiation simulations
- [Func-Sub (Training Grounds)](https://hartswf0.github.io/func-sub/func-index.html) — 6-axis spatial reasoning substrate
- [Liberty Machines](https://hartswf0.github.io/liberty-machines/) — Lessig's four regulatory modalities

---

# Part 2: Write-Up

## 1. Describe Your Tool/Toolkit

**WAG: Words Assemble Geometries** is a fortified documentation ecosystem that treats every design decision as a LEGO brick—visible, repositionable, and structurally load-bearing. Rather than a monolithic application, it is a suite of single-file HTML artifacts interconnected through an invariant design pattern.

The project emerged from a methodological commitment I call **negative space programming**: the constraint comes first; content is generated until it snaps into the constraint's shape. This inverts conventional development where structure follows content. Here, structure is the independent variable—better constraints produce better content, while good content without constraints produces sprawl.

**The Invariant Pattern:**
- **9×9 grid interface** — bounded canvas for any scenario
- **Tetrad operators** — McLuhan's Enhance/Obsolesce/Retrieve/Reverse as transformation controllers (McLuhan & McLuhan, 1988)
- **Chat layer** — natural language control without leaving the substrate
- **Branching mechanics** — any state can fork into alternatives
- **Phone-first constraint** — must work on mobile; eliminates accumulated complexity

This pattern survived the failure of TILTH (Phase 0), an internal prototype that used AI to generate synthetic data exhaust of a fictional organization: role decks, personas, negotiation simulations, prompt operators, tetrads, quizzes, and scenario documents. Layer upon layer produced what I call **complexity grey**—a zone where brokenness and design pathways became indistinguishable. TILTH sprawled across countless index files and nested hyperlinks until its liability exceeded its asset value.

The pivot extracted the tetrad controller mechanics and built Thousand-Tetrad: a system that stays **fixed and empty** while supporting diverse scenarios.

**Component Architecture:**

| Tool | Function | Course Reading Connection |
|------|----------|---------------------------|
| **Privacy Value Labels** | Mobile-first CI worksheet | Mulligan, Koopman, & Doty (2016) — 14 privacy dimensions |
| **Haunted Tools** | Mythology catalog | Mattern (2021); Barthes (1957/1972) |
| **Thousand-Tetrad** | Scenario substrate | McLuhan & McLuhan (1988) |
| **Role Deck** | Identity mapping | Wong (2021); Bartle (1996) |
| **The Fork** | Negotiation training | Ethical frameworks as dialogic agents |
| **Func-Sub** | 6-axis substrate | Collaborator-developed speculative framework |
| **Liberty Machines** | Regulatory modalities | Lessig (2006) — Code 2.0 |

---

## 2. What Issues Does the Toolkit Address?

The toolkit addresses five interconnected problems identified through course readings and documented failures:

### The Complexity Spiral
TILTH demonstrated the pathology: as project context grew, ability to finish it got exponentially more challenging. Worlds accumulate context faster than coherence can maintain. The invariant 9×9 substrate addresses this by providing **bounded complexity** that scales without accumulating. Flatness is not poverty—flatness is discipline.

### The Export Problem
Most generative AI tools produce ephemeral outputs that cannot be meaningfully shared, versioned, or built upon. LLM sessions vanish. The shift to **"LLM manages void, not scene"** resolves this: the LLM prepares possibility spaces; the user selects and instantiates; outputs export as structured data files (disc-data.json) that persist beyond the session and work without API access.

### The Toolkit Mythology
Following Mattern's (2021) critique "Unboxing the Toolkit" and Barthes's (1957/1972) semiotic method in *Mythologies*, **Haunted Tools** exposes instruments that perform ethics work without transferring real resources. Seven archetypes catalogued:
- **The Deck** — transfers design time, not budget/risk
- **The Audit** — captures liability, not harm reduction  
- **The Forum** — performs listening without committing to action
- **The Dashboard** — shows what's measured, not what matters
- **The Pledge** — transfers reputation risk, not operational change
- **The Lab** — contains disruption safely away from core business
- **The Chief** — individual hero absorbs structural responsibility

Each operates through Barthes's form/concept/signification structure: the form (card deck, checklist, dashboard) appears identical to the concept (deliberation, accountability, transparency), occluding the twist (no resource transfer).

### The Disclosure Theatre
Week 1's dirty-disclosure project exposed the double bind: ACM's disclosure frameworks assume transactional AI use (prompt→output), not symbiotic collaboration (embedded thought partner over 150+ hours). This asymmetry parallels what Scott (1998) calls the gap between **mētis** (practical, situated knowledge) and **techne** (abstract, systematizable knowledge) in *Seeing Like a State*. The sophisticated user faces a paradox—minimal disclosure misrepresents depth; full disclosure reads as dependency. The solution: **trail visibility**. If collaboration were observable *during* work (like pair programming metrics), disclosure would be observation, not confession.

### The API Dependency
Current LLM-powered creative tools require active API connections, creating barriers for designers without infrastructure or budget. The toolkit's **single-file HTML philosophy** enables exploration without dependencies. Every component can be opened directly in a browser, forked on GitHub, or modified locally.

---

## 3. Who Are the Audiences?

**Primary: UX Researchers and Designers**  
Working within organizational constraints, needing lightweight tools for values articulation that work on mobile phones, in meetings, during client consultations. Privacy Value Labels specifically targets this use case—14 dimensions of contextual integrity (Mulligan, Koopman, & Doty, 2016) accessible in pocket.

**Secondary: Ethics Practitioners**  
Navigating organizational power structures, mapped through Role Deck's Bartle taxonomy (Bartle, 1996) adaptation:
- **Achievers** — metrics-driven, compliance-focused; risk: optimization without reflection
- **Explorers** — research-oriented, boundary-testing; risk: perpetual research, no deployment
- **Socializers** — relation-building, consensus-seeking; risk: captured by powerful voices
- **Killers** — adversarial, red-teaming; risk: marginalization as "difficult"

These are Wong's (2021) "soft resisters"—practitioners who engage in "tactics of soft resistance" within organizational constraints. Gray, Chivukula, et al. (2023) further identified ethics-focused practitioner roles through co-design workshops.

**Tertiary: Computational Humanities Researchers**  
Interested in scenario-building substrates. Collaborations with:
- **Terhi Marttila** (Interactive Technologies Institute, Portugal) — weekly testing, pushed toward open-source LLMs
- **Jordan Caldwell** (co-author, *Black Metal* book with Afrotectopia) — speculative philosophy frameworks
- **Kayla Evans** (Georgia Tech, Responsible AI Summit) — power dynamics and ethical negotiation
- **Shuruq Tramontini** (Lead Unity Artist, *Life After Bob*) — multi-agent narrative inspiration

**Aspirational: Multi-Agent Narrative Systems Researchers**  
Future collaborators on platforms like emergentic.ai and similar multi-agent simulation environments. Did not yet reach the technical threshold—but learned enormously about context engineering, ring buffer memory systems, and scene graph architecture.

---

## 4. Context of Use

**During Design Processes:**  
Privacy Value Labels maps information flows during UX research using Nissenbaum's (2009) contextual integrity framework operationalized as 14 dimensions. The LEGOS framework (Location, Entities, Goals, Obstacles, Shifts/Solutions) provides vocabulary for scenario articulation. Mobile-first design means it's available *in the meeting*, not after.

**During Organizational Navigation:**  
Role Deck helps practitioners identify their position within organizational games. "We need more Socializers on this committee" becomes a legitimate coalition-building move. Identity is tactical.

**During Collaborative Speculation:**  
Thousand-Tetrad supports real-time scenario forking during workshops. Enables rapid branching through alternative futures using McLuhan's tetrad operators. Any state can fork; the substrate stays invariant.

**During Post-Session Sharing:**  
The shift from live LLM scene construction to prebaked narratives (disc-data.json format) enables outputs to be shared, critiqued, and built upon without requiring API access. Export is the real problem; the structured output format addresses it.

---

## 5. Levers, Leverage Points, and Regulatory Modes

### Shilton's Values Levers
Following Shilton's (2013) framework on how values become embedded in design processes, the toolkit creates openings for values discussions by:
- **Making information flows visible** — Privacy Value Labels surfaces 14 CI dimensions
- **Making ethical identities explorable** — Role Deck maps practitioner archetypes
- **Making toolkit mythologies explicit** — Haunted Tools provides form/concept/twist vocabulary

### Meadows's Leverage Points
Following Meadows's (2008) *Thinking in Systems* hierarchy, the toolkit operates at multiple levels:

| Level | Type | Intervention | Tool |
|-------|------|--------------|------|
| 4 | Infrastructure | disc-data.json export format | Structured export |
| 3 | Information Flows | Trail visibility; scenario exploration logs | Tractor Field |
| 2 | Organizing Principles | 9×9 invariant grid; transfer audit requirement | All components |
| 1 | Mindsets | **LLM manages void, not scene** | TRACTOR synthesis |

The highest-leverage insight: reframing AI creative tool design from "LLM constructs" to "LLM prepares, user instantiates." This preserves agency, reduces API dependency, and enables meaningful export.

### Lessig's Regulatory Modes
**Liberty Machines** explicitly maps Lessig's (2006) four regulatory modalities from *Code: Version 2.0*—Law, Norms, Market, and Architecture—as interactive forces:
- **Case study**: Cigarette pack as "freedom theatre"
- **Application**: Platform API terms shape behavior as powerfully as legislation
- **Architecture/code** is equally powerful regulatory force as law—often more powerful because invisible

### Paradigm Shift
The toolkit's most significant intervention: treating **trail data as first-class design material** rather than invisible exhaust. Trail Level 0 (exhaust) → Level 1 (feature) → Level 2 (backbone). At Level 2, architecture is built around trail visibility from the start.

---

## 6. Design/Creation Process

### Phase 0: TILTH — The Failure
Built an internal prototype to explore through generative accumulation. Used AI to generate synthetic data exhaust: role decks, personas, negotiation simulations, prompt operators, tetrads, quizzes, and scenario documents.

**Why it failed:**
- Convoluted speculation: world inside a world
- Coherency collapse: couldn't show enough for coherence
- Exponential context growth: additions made system harder, not richer
- Polish bottleneck: final editing/coding/integration blocked

**What it taught:** Negative space programming—build the key first, constrain dimensionality, be parasitic off existing worlds rather than building new ones.

### Phase 1: Thousand-Tetrad — The Discovery
Recognized that better speculative worlds already existed (Ted Chiang's fiction, "Life After Bob" animation). Extracted the tetrad controller mechanics and built an invariant substrate:
- 9×9 grid — bounded canvas
- Tetrad operators — McLuhan's four laws as transformation vocabulary (McLuhan & McLuhan, 1988)
- Chat layer — natural language control
- Phone constraint — forces bounded complexity

### Phase 2: Transition to 3D
Technical problems with API and inability to share outputs meaningfully pushed toward 2D→3D pivot. Collaborators' projects required novel 3D scenes. Embedded narrative camera movement into prebaked formats.

**Goal:** Make films/scenarios that can be shared without LLM access but made with LLM assistance.

### Phase 3: TRACTOR — The Synthesis
Synthesized all components. Crucial insight: frustration with fine-grain LLM scene construction resolved by seeing **where LLMs got in the way**.

**Before:** LLM manages the scene → scene complexity → friction  
**After:** LLM manages the VOID → possibility space → user selects → agency preserved

---

## 7. Learnings and Reflections

### On Negative Space Programming
The shape of the key determines what the generation produces. Build the key first. Generative abundance must be disciplined by structural scarcity. Better constraints > better content.

### On Technical Thresholds
I am not yet technical enough to engage with computer scientists working on multi-agent systems. But I learned enormously about:
- Context engineering: structuring prompts, managing context windows
- Ring buffer memory systems: bounded persistent state
- Scene graph complexity: managing what the system remembers
- Linear algebra for 3D transformations

### On Collaboration Without a Platform
Working with collaborators taught me: "Not trying to act like I had a real platform." The better approach:
- Produce documents, prompt guides, essays
- Enable hands-on friction exposure
- Get out of the way to observe
- Let collaborators experience the system's limitations directly

### On Invariant Patterns
Design patterns that stay invariant across scenario-building scale better than patterns that accumulate context. The 9×9 grid + chat + tetrad + footer structure works for:
- Privacy scenarios (Privacy Value Labels)
- Ethical negotiations (The Fork)
- Speculative worldbuilding (Thousand-Tetrad)
- Self-alignment (Func-Sub)

### On Export as the Real Problem
The bigger issue than generation is export—how to produce artifacts from LLM collaboration that others can meaningfully engage with. Structured output formats attempt to address this.

---

## 8. Future Directions

1. **LDraw/LEGO integration:** Using real digital LEGO for scene construction; make 3D outputs more specific and engaging than abstract geometries

2. **Open-source LLM adaptation:** Restructure system prompts to work without proprietary API dependency entirely

3. **Multi-agent architectures:** Moving toward generative agents model (Park et al., 2023) with persistent agent memory and social dynamics

4. **Physical artifacts:** Printed Haunted Tools and Role Deck cards for workshop contexts

5. **Collaboration with simulation platforms:** Reaching the technical threshold to contribute to multi-agent simulation projects

6. **POML development:** Expanding the prompt library into formal infrastructure for prompt composition, inheritance, and versioning; community registry

7. **Trail-aware tool ecosystem:** Position paper on observation vs. confession in AI disclosure

---

# Appendix: POML Prompt Library

## The Library (9 Files, ~1,365 Lines)

| File | Lines | Purpose | Course Connection |
|------|-------|---------|-------------------|
| `forensic.poml` | 350 | Multi-ledger ethical diagnostic | Lessig's regulatory modes as repair levers |
| `parody.poml` | 279 | POML→POML forge for parody essays | Barthes' mythology analysis operationalized |
| `tactics.poml` | 238 | De Certeau concordance extraction | Mētis—practical knowledge as prompt logic |
| `prompt.poml` | 183 | Natural language → POML transformer | Infrastructure for prompt migration |
| `mythos.poml` | 92 | Weberian ideal type extraction | Weber's ideal types as analytical infrastructure |
| `recursive.poml` | 71 | Recursive prompt generation engine | "Prompts that write prompts" |
| `parody-gen.poml` | 61 | Light parody prompt generator | Reusable satire scaffolding |
| `inverse-essay.poml` | 46 | Essay reversal + myth extraction | Hutcheon's bi-textual frame analysis |
| `meta-prime.poml` | 45 | Author OS → prompt logic extractor | Shilton's values levers |

## Why This Matters

The POML library exemplifies **layered, sophisticated AI usage** that defies simple disclosure:

- **Compositional:** Prompts embed and reference other prompts
- **Recursive:** Each prompt designed to spawn further prompts
- **Reusable:** Extracted configurations transfer across domains
- **Transparent:** Structure exposes what the prompt does

This is **infrastructural** prompt work, not transactional. The POML files are artifacts of mētis (Scott, 1998)—practical knowledge accumulated through sustained engagement that cannot be itemized into discrete "prompts I used."

---

# Generative AI Statement

## Disclosure

I used ChatGPT-4o, Claude (3.5 Sonnet, Opus), and Gemini as **embedded thought partners** across approximately 150+ hours of work this semester. The AI was not a tool I picked up and put down; it was a persistent interlocutor—present in every design decision, every code iteration, every conceptual refinement.

## Nature of Collaboration

- **Multi-turn conversations:** some extending 50+ exchanges
- **System prompt development:** 9 POML files refined through iteration
- **Code generation with debugging:** AI generated code that I then debugged, restructured, often rewrote
- **Conceptual exploration:** AI proposed interpretations of readings that I contested, refined, or built upon
- **Scenario generation:** Direct API integration in Thousand-Tetrad (100+ test scenes)
- **Document structuring:** AI organized scattered notes into coherent form

To answer "which sections were created by AI" is like asking which parts of a conversation were created by the other speaker. The ideas emerged *between* us.

## The Double Bind

This creates what I examined in my Disclosure Theatre project—a structure where:
- **Minimal disclosure** performs compliance but misrepresents depth of engagement
- **Full disclosure** produces volumes that read as dependency rather than fluency

The ACM guidelines reward **tidy, transactional use**: "I used ChatGPT to rephrase paragraph 2." They penalize—or fail to accommodate—**symbiotic use**: sustained collaboration where human and AI cognition become difficult to disentangle.

This asymmetry favors **techne** (abstract, systematizable knowledge) over **mētis** (context-dependent, experiential knowledge). Someone who uses AI clumsily can report cleanly. Someone who develops fluency finds the reporting framework inadequate.

## Specific Prompts

The POML library (9 files, ~1,365 lines) contains the structured prompt infrastructure developed this semester. Rather than listing ephemeral prompts, I provide the prompt *infrastructure*—reusable, versionable, composable.

## Learning from the AI

- Ring buffer memory system architecture
- Scene graph management approaches
- Linear algebra for 3D transformations
- Context window management strategies
- The concept of "LLM managing void, not scene"

## Trail Visibility as Solution

The antidote to disclosure theatre is **trail-aware tools**: architectures that treat trail data as first-class design material rather than invisible exhaust. If collaboration were observable *during* work (like pair programming metrics), disclosure would be observation, not confession.

This statement follows the ACM disclosure policy while acknowledging its limitations for capturing symbiotic AI collaboration.

---

# References

Association for Computing Machinery. (2025). *ACM Policy on Authorship* (updated Sept. 16, 2025). https://www.acm.org/publications/policies/new-acm-policy-on-authorship

Bartle, R. (1996). Hearts, clubs, diamonds, spades: Players who suit MUDs. *Journal of MUD Research*, 1(1). http://mud.co.uk/richard/hcds.htm

Barthes, R. (1972). *Mythologies* (A. Lavers, Trans.). Hill and Wang. (Original work published 1957)

Goñi, J. I., Rodrigues, E., Parga, M. J., Illanes, M., & Millán, M. J. (2024). Tooling with ethics in technology: A scoping review of responsible research and innovation tools. *Journal of Responsible Innovation*, 11(1), Article 2360228. https://doi.org/10.1080/23299460.2024.2360228

Gray, C. M., Obi, I., Chivukula, S. S., Li, Z., Carlock, T., Will, M., et al. (2023). Practitioner trajectories of engagement with ethics-focused method creation. *arXiv preprint arXiv:2210.03002*. https://arxiv.org/abs/2210.03002

Lessig, L. (2006). *Code: Version 2.0*. Basic Books. https://codev2.cc/

Mattern, S. (2021, July). Unboxing the toolkit. *Toolshed*. https://tool-shed.org/unboxing-the-toolkit/

McLuhan, M., & McLuhan, E. (1988). *Laws of media: The new science*. University of Toronto Press.

Meadows, D. H. (2008). *Thinking in systems: A primer*. Chelsea Green Publishing.

Mulligan, D. K., Koopman, C., & Doty, N. (2016). Privacy is an essentially contested concept: A multi-dimensional analytic for mapping privacy. *Philosophical Transactions of the Royal Society A*, 374(2083), 20160118. https://doi.org/10.1098/rsta.2016.0118

Nissenbaum, H. (2009). *Privacy in context: Technology, policy, and the integrity of social life*. Stanford University Press.

Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). Generative agents: Interactive simulacra of human behavior. *arXiv preprint arXiv:2304.03442*.

Scott, J. C. (1998). *Seeing like a state: How certain schemes to improve the human condition have failed*. Yale University Press.

Shilton, K. (2013). Values levers: Building ethics into design. *Science, Technology, & Human Values*, 38(3), 374-397.

Wong, R. Y. (2021). Tactics of soft resistance in user experience professionals' values work. *Proceedings of the ACM on Human-Computer Interaction*, 5(CSCW2), Article 355. https://doi.org/10.1145/3476048

---

**Full documentation:** `docs/` directory  
**Source code:** https://github.com/hartswf0/tractor-field-notes  
**License:** MIT

*Fall 2025 · LMC-6650 · Georgia Institute of Technology*
