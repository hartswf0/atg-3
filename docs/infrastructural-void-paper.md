# Towards Creating Infrastructures for Validity in the Production of Generative AI Systems

**A Genealogical Analysis of Constraint-Based Design**

---

## Abstract

The emergence of generative AI has precipitated what Winograd and Flores \cite{winograd1987understanding} call a "breakdown"—a moment when taken-for-granted practices become visible and questionable. The dominant HCI response—building "prompt engineering tools," "guardrails," and "alignment features"—reproduces what Suchman \cite{suchman1987plans} identified as the central error of classical AI: treating plans as programs rather than resources for action. Drawing on Star and Bowker's \cite{bowker1999sorting} concept of "infrastructural inversion" and Wong's \cite{wong2021soft} tactics of "soft resistance," we argue that the fundamental challenge of generative systems is not **tool design** but **infrastructure creation**: redesigning the organizational processes, social positions, invisible labor practices, and policy structures that produce AI systems. Through a genealogical analysis tracing constraint-based design from Dijkstra \cite{dijkstra1968goto} and Hoare \cite{hoare2009null} through Modulex \cite{minibricks2011saving} to contemporary context engineering \cite{karpathy2025context}, we demonstrate how the concept of "Void Management"—constraining the latent space rather than expanding it—offers an infrastructural intervention that shifts focus from product to process. We conclude with tactical recommendations grounded in Meadows' \cite{meadows1999leverage} leverage points framework for designers working within what Scott \cite{scott1998seeing} calls "hostile infrastructures."

---

## 1. Introduction: A Breakdown and a Vignette

### 1.1 The Theoretical Ground

Winograd and Flores \cite{winograd1987understanding} argue that all effective design begins with a "breakdown"—a disruption of the smooth functioning that makes invisible infrastructure suddenly visible:

> "It is in the moments of breakdown that we encounter the world as real, as 'there,' as demanding our attention." \cite[p. 77]{winograd1987understanding}

The arrival of generative AI constitutes such a breakdown. The taken-for-granted relationship between human intent and computational output has been irrevocably disrupted. As Miller \cite{miller1956magical} established in his foundational work on cognitive capacity, human working memory is fundamentally bounded:

> "The span of absolute judgment and the span of immediate memory impose severe limitations on the amount of information that we are able to receive, process, and remember." \cite[p. 95]{miller1956magical}

This limit—what Miller famously called "the magical number seven, plus or minus two"—grounds our argument. If human cognition is bounded, and generative systems produce outputs from an effectively unbounded latent space (the "Void"), then the fundamental design challenge is not expansion but **constraint**.

### 1.2 The Vignette: Mara's Collapse

Mara is a UX researcher at a mid-sized AI company. She has spent three years building what she calls a "Responsible Prompting Toolkit"—documentation, templates, guardrails. The toolkit is well-designed. It follows Amershi et al.'s \cite{amershi2019guidelines} guidelines for human-AI interaction. It incorporates Shneiderman's \cite{shneiderman2022human} principles of human-centered AI.

Six months after launch, the toolkit is deprecated. Not officially—just routed around. Following Wong \cite{wong2021soft}, we can identify the specific tactics of organizational resistance:

1. **Power users discovered workarounds**: Guardrails slowed output velocity
2. **Sales made enterprise promises**: "Full access to model capabilities"
3. **Sprint velocity dominated**: No OKR for "prompt safety"

Mara's colleague explains: "The toolkit was great, but it wasn't in the incentive structure."

### 1.3 The Diagnosis: Tool-Solutionism

This is what Agre \cite{agre1997computation} calls the "capture" problem—the belief that rationalized systems can encode and enforce values:

> "Technical representations are constructed so as to capture actions, objects, and situations... The world is rendered as an object of computation." \cite[p. 74]{agre1997computation}

Mara's toolkit **captured** the problem correctly. It **represented** the ethical concerns accurately. But representation is not power. As Suchman \cite{suchman1987plans} demonstrated:

> "Plans are resources for action, not its structure. The plan is just a representation; the situated action is the reality." \cite[p. 178]{suchman1987plans}

The toolkit was a plan. The organizational infrastructure was the action. They were misaligned.

---

## 2. The Infrastructural Argument

### 2.1 Infrastructural Inversion

Bowker and Star \cite{bowker1999sorting} propose a method they call "infrastructural inversion":

> "Study an information system and neglect its standards, wires, and settings, and you miss equally essential aspects of aesthetics, justice, and change." \cite[p. 33]{bowker1999sorting}

Applied to generative AI, this means: **Don't study the model. Study the organizational infrastructure that produces, deploys, and maintains it.**

Latour \cite{latour2005reassembling} offers a complementary framework:

> "What we call 'society' is the result of countless associations between human and non-human actors... The task is to trace these associations, not to explain them away." \cite[p. 108]{latour2005reassembling}

The "society" of generative AI includes:
- The sprint cycle that ships prompts without review
- The OKR structure that rewards velocity over safety
- The outsourced data annotation that is invisible in the product
- The legal department that disclaims liability

### 2.2 The Genealogy of Constraint

Our argument gains force from a genealogical analysis showing that **constraint-based design is not new**—it is the hidden infrastructure of all reliable systems.

#### 2.2.1 Dijkstra and the Elimination of Goto

Dijkstra \cite{dijkstra1968goto} did not merely critique the `goto` statement. He identified it as a representable invalid state:

> "The go to statement as it stands is just too primitive; it is too much an invitation to make a mess of one's program." \cite[p. 147]{dijkstra1968goto}

The solution was infrastructural: change the **language** to make `goto` unrepresentable. Structured programming did not add a feature. It **removed a possibility**.

#### 2.2.2 Hoare and the Billion-Dollar Mistake

Hoare \cite{hoare2009null} later reflected on his 1965 invention of the null reference:

> "I call it my billion-dollar mistake. It was the invention of the null reference in 1965... I couldn't resist the temptation to put in a null reference, simply because it was so easy to implement. This has led to innumerable errors, vulnerabilities, and system crashes."

Null is a **representable invalid state**. The solution—Option types, Result types, algebraic data types—follows the same infrastructural logic: change the type system to make null unrepresentable \cite{functionalarch2020illegal}.

#### 2.2.3 Modulex and Physical Negative Space Programming

The most striking precedent comes from physical design. In 1963, Godtfred Kirk Christiansen encountered a geometric constraint when attempting to build an architectural model with standard LEGO bricks \cite{minibricks2011saving}:

> "GKC attempted to build a scale model of a new house using standard LEGO bricks. He immediately encountered a geometric limit: the standard LEGO brick has a width-to-height ratio of 5:6, making uniform scaling impossible."

The solution was not a tool—it was a **new physical infrastructure**: the Modulex brick, with a perfect 1:1:1 cube ratio (5mm × 5mm × 5mm). Scaling errors became structurally impossible.

This is **Physical Negative Space Programming**: the same principle that Dijkstra and Hoare applied to software, applied to plastic.

### 2.3 The Applicability to Generative AI

The generative AI context presents the same structural problem. The "Void"—the latent space of all possible outputs—is analogous to:
- **Goto**: An unbounded jump space
- **Null**: A representable invalid state
- **5:6 Aspect Ratio**: A geometric constraint that produces systematic errors

Current approaches (guardrails, RLHF, Constitutional AI) attempt to **filter outputs**. This is analogous to adding runtime checks for null—it catches errors after they're representable, not before.

The infrastructural solution is to **constrain the Void at the input level**—what we call "Sintering," following the metallurgical metaphor: applying heat (constraints) to consolidate granular material (context) without melting it (losing fidelity).

---

## 3. Tactics for Infrastructural Intervention

Following Meadows \cite{meadows1999leverage}, we identify interventions at multiple leverage points:

> "Leverage points are places within a complex system where a small shift in one thing can produce big changes in everything... The higher the leverage point, the more the system will resist changing it." \cite{meadows1999leverage}

### 3.1 Designing Process: The Sintering Review

**Meadows Leverage Point**: #8 — Rules of the System

**Current State**: Prompts are shipped in sprints. There is no organizational ritual for reviewing context accumulation over time.

**Intervention**: Create a quarterly "Sintering Review"—a cross-functional meeting where teams examine:
1. What context has accumulated in long-running systems?
2. What should be archived, discarded, or consolidated?
3. Where has "context rot" \cite{anthropic2025agents} degraded performance?

This follows Terry et al.'s \cite{terry2023alignment} framework of "Process Alignment":

> "Process Alignment asks whether the human agrees with HOW the AI arrived at its output, not just WHAT the output is."

The Sintering Review operationalizes Process Alignment as an organizational ritual.

**Grounding Citations**:
- Process design: \cite{terry2023alignment}
- Context rot: \cite{anthropic2025agents}
- Cognitive workspace: \cite{cogworkspace2025}

### 3.2 Building Community: The Prompt Engineering Guild

**Meadows Leverage Point**: #10 — Goal of the System

**Current State**: Prompt engineers are isolated within product teams. There is no professional community, no shared ethics, no collective bargaining.

**Intervention**: Create a cross-organizational "Prompt Engineering Guild" following Wong's \cite{wong2021soft} tactics of "soft resistance":

> "UX professionals create space for ethics by... building communities of practice that legitimate values work as 'knowledge sharing' rather than 'activism.'" \cite{wong2021soft}

The Guild provides:
- Failure story sharing (learning from Mara's collapse)
- Template libraries (shared constraint patterns)
- Collective voice (policy input on AI regulation)

This follows Freire's \cite{freire1970pedagogy} concept of "conscientização"—critical consciousness through collective reflection:

> "Conscientização refers to learning to perceive social, political, and economic contradictions, and to take action against the oppressive elements of reality."

**Grounding Citations**:
- Soft resistance: \cite{wong2021soft}
- Critical pedagogy: \cite{freire1970pedagogy}
- Constructionism: \cite{papert1980mindstorms}
- Commons-based design: \cite{sanchez2019architecture}

### 3.3 Supporting Invisible Labor: The Context Curation Role

**Meadows Leverage Point**: #11 — Paradigm (What is valued)

**Current State**: Context curation is invisible labor. Someone decides what goes in the system prompt. Someone cleans training data. This work is outsourced, undercompensated, and unrecognized.

**Intervention**: Create a named, visible, compensated role: **Context Curator**.

This follows Jackson's \cite{jackson2014rethinking} argument for "rethinking repair":

> "Repair and maintenance... constitute the main ways by which the infrastructures of modernity are sustained over time."

And Haraway's \cite{haraway1988situated} concept of "situated knowledges":

> "Feminist objectivity means quite simply situated knowledges... The only way to find a larger vision is to be somewhere in particular."

The Context Curator is **somewhere in particular**—responsible for the partial, situated decisions that shape the Void.

**Grounding Citations**:
- Repair: \cite{jackson2014rethinking}
- Situated knowledge: \cite{haraway1988situated}
- Classification labor: \cite{bowker1999sorting}
- Invisible work: \cite{latour1987science}

### 3.4 Policy as Design: Piggybacking on Regulation

**Meadows Leverage Point**: #8 — Rules of the System

**Current State**: AI ethics is voluntary. Guardrails are "best practices." There is no compliance mechanism.

**Intervention**: Translate Void Management principles into regulatory language that piggybacks on existing law.

Following Lessig \cite{lessig2006code}:

> "Code is law... The architectures of cyberspace regulate behavior as effectively as law."

| Regulation | Void Management Translation |
|------------|------------------------------|
| GDPR Art. 22 (Automated Decisions) | Require "Seamful XAI" \cite{seamfulxai2022}—expose uncertainty |
| NIST AI RMF | Require "Context Audits"—document what context is used |
| EU AI Act (High-Risk) | Require "Sintering Reviews"—quarterly context curation |

**Grounding Citations**:
- Code as law: \cite{lessig2006code}
- Legibility: \cite{scott1998seeing}
- Seamful XAI: \cite{seamfulxai2022}
- Value Sensitive Design: \cite{friedman2019value}

---

## 4. Discussion: Navigating Hostile Infrastructures

### 4.1 The Tempered Radical

Scott \cite{scott1998seeing} describes how states simplify local knowledge to make it "legible":

> "Certain forms of knowledge and control require a narrowing of vision. The great advantage of such tunnel vision is that it brings into sharp focus certain limited aspects of an otherwise far more complex and unwieldy reality."

The AI industry has its own legibility projects: OKRs, velocity metrics, model benchmarks. These simplifications render values work invisible—it doesn't fit the metrics.

Wong \cite{wong2021soft} identifies the "tempered radical" as a survival strategy:

> "Tempered radicals work within existing structures while pushing for gradual change... They use the language and tools of the organization against its own worst tendencies."

### 4.2 The Genealogical Warrant

Our genealogical analysis demonstrates that this struggle is not new. Every generation has faced what Winograd and Flores \cite{winograd1987understanding} call the tension between "breakdown" and "ready-to-hand":

| Era | Breakdown | Infrastructural Response |
|-----|-----------|--------------------------|
| 1960s | Spaghetti code | Structured programming standards \cite{dijkstra1968goto} |
| 1970s | Null pointer exceptions | Algebraic data types \cite{hoare2009null} |
| 1980s | Plans fail in practice | Situated action theory \cite{suchman1987plans} |
| 1990s | State simplification erases metis | Critical theory \cite{scott1998seeing} |
| 2010s | Platform extraction | Commons-based design \cite{sanchez2019architecture} |
| 2020s | Generative Void | **Void Management** |

### 4.3 The Serious Toy

Eames \cite{eames1958toys} offers a final grounding:

> "Toys are not as innocent as they look... Toys and games are the preludes to serious ideas."

This project—Thousand-Tetrad, POML, the bibliography scenes—is a **serious toy**. It uses the constraint-based logic of LEGO to make serious ideas about infrastructure visible and manipulable.

Papert \cite{papert1980mindstorms} called this "constructionism":

> "Learning happens 'felicitously' when the learner is engaged in constructing a public entity."

The paper is the public entity. The LEGOS scenes are the construction.

---

## 5. Conclusion

We have argued that the dominant HCI response to generative AI—building tools, features, and products—is insufficient because it addresses symptoms rather than causes. Drawing on Suchman's \cite{suchman1987plans} situated action, Star and Bowker's \cite{bowker1999sorting} infrastructural inversion, Wong's \cite{wong2021soft} soft resistance, and a genealogy from Dijkstra \cite{dijkstra1968goto} to Modulex \cite{minibricks2011saving}, we propose four infrastructural interventions:

1. **The Sintering Review** — Process alignment as organizational ritual
2. **The Prompt Engineering Guild** — Solidarity as resistance
3. **The Context Curation Role** — Making invisible labor visible
4. **Regulatory Piggybacking** — Policy as design leverage

The thesis is simple: **The Void cannot be managed by a toolkit. It must be constrained by infrastructure.**

Or, in the language of Meadows \cite{meadows1999leverage}:

> "People who manage to intervene in systems at the level of paradigm hit a leverage point that totally transforms systems."

---

## References

```bibtex
% The following citations are used in this paper.
% Full entries in docs/references.bib

\cite{miller1956magical}       % Cognitive limits
\cite{ashby1956introduction}   % Requisite variety
\cite{simon1969sciences}       % Bounded rationality
\cite{dijkstra1968goto}        % Structured programming
\cite{hoare2009null}           % Billion dollar mistake
\cite{suchman1987plans}        % Situated action
\cite{winograd1987understanding} % Breakdown
\cite{agre1997computation}     % Capture
\cite{dourish2001action}       % Embodied interaction
\cite{bowker1999sorting}       % Infrastructure studies
\cite{latour2005reassembling}  % ANT
\cite{latour1987science}       % Inscription
\cite{scott1998seeing}         % Legibility
\cite{geertz1973interpretation} % Thick description
\cite{haraway1988situated}     % Situated knowledge
\cite{meadows1999leverage}     % Leverage points
\cite{meadows2008thinking}     % Systems thinking
\cite{freire1970pedagogy}      % Critical pedagogy
\cite{papert1980mindstorms}    % Constructionism
\cite{eames1958toys}           % Serious toys
\cite{sanchez2019architecture} % Commons
\cite{wong2021soft}            % Soft resistance
\cite{amershi2019guidelines}   % HAI guidelines
\cite{shneiderman2022human}    % HCAI
\cite{lessig2006code}          % Code as law
\cite{friedman2019value}       % VSD
\cite{karpathy2025context}     % Context engineering
\cite{anthropic2025agents}     % Agentic patterns
\cite{terry2023alignment}      % Process alignment
\cite{seamfulxai2022}          % Seamful XAI
\cite{functionalarch2020illegal} % ADTs
\cite{minibricks2011saving}    % Modulex
\cite{jackson2014rethinking}   % Repair
\cite{cogworkspace2025}        % Context management
```

