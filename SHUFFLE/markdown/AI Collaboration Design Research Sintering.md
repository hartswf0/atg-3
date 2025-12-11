# Designing the Void: Agency, Context, and the Ontological Drift in Generative Systems

## 1. The Ontological Drift: From Tool Use to Void Management

The history of Human-Computer Interaction (HCI) is largely a history of specificities. From the rigid syntax of the command line to the pixel-perfect metaphors of the graphical user interface (GUI), the discipline has traditionally focused on narrowing the gap between a user's specific intent and the machine's precise execution. Donald Norman termed this the \"Gulf of Execution\" ^1^, a framework that presupposed a deterministic relationship between input and output. In this classical paradigm, the computer is a tool---a sophisticated chisel or a typewriter---that amplifies human capability through predictable mechanisms. However, the emergence of large-scale generative models in the 2020s has precipitated a fundamental \"ontological drift\" in this relationship. We are witnessing the dissolution of the tool metaphor and the emergence of a new, unstable category of technological existence: the \"Quasi-Creature\".^3^

This report posits that the central design challenge of the generative era is not the refinement of model accuracy or the expansion of context windows, but the management of the \"Void\"---a high-dimensional, probabilistic possibility space---and its counterpart, the \"Scene\"---the accumulated, situated context that constrains this space. By synthesizing classical design theory with contemporary research on large language models (LLMs) and generative interfaces from 2020--2025, we argue that the preservation of human agency requires a radical shift in interaction design. We must move from *output evaluation* to *process alignment*, designing interfaces that expose the \"seams\" of computation ^4^ rather than obscuring them behind a veil of magical seamlessness.

### 1.1 The Emergence of the Quasi-Creature

The interaction with contemporary generative systems is defined by a profound paradox: these entities exhibit superhuman fluency and creative capacity while simultaneously demonstrating baffling, often absurd, failures in common sense, consistency, and factual grounding.^3^ This paradox disrupts the established mental models of HCI. A calculator does not \"hallucinate\" math; a word processor does not \"forget\" the previous paragraph. When traditional software fails, it is a bug---a breakdown in logic that can be debugged. When a generative model fails, it is often a failure of *alignment* or *grounding*, perceived by the user not as a mechanical error but as a cognitive lapse.

Recent theoretical work identifies this new class of entity as the \"Quasi-Creature\"---an agent that simulates intelligent behavior with unprecedented sophistication but lacks the grounding of embodiment, environmental interaction, and genuine understanding.^3^ The Quasi-Creature occupies a new conceptual space termed the \"Uncanny Valley of Agency.\" Unlike Masahiro Mori's original Uncanny Valley, which mapped physical human-likeness to emotional response, this new valley maps *perceived autonomous agency* against user trust and cognitive comfort.

**Table 1: The Ontological Shift in Human-Machine Relations**

  ----------------------------------------------------------------------------------------------------------------------
  **Dimension**              **The Tool (Classical HCI)**           **The Quasi-Creature (Generative HCI)**
  -------------------------- -------------------------------------- ----------------------------------------------------
  **Interaction Paradigm**   Command-based (Explicit Instruction)   Intent-based (Negotiation of Probability)

  **Ontology**               Deterministic, Passive                 Probabilistic, Agentic, \"Alien\"

  **Failure Mode**           Error/Bug (Syntactic failure)          Hallucination/Drift (Semantic/Ontological failure)

  **User Role**              Operator/Pilot                         Curator/Manager/Sinterer

  **Design Goal**            Efficiency, Usability (Seamlessness)   Alignment, Legibility (Seamfulness)

  **Key Theorist**           Norman (Gulf of Execution) ^1^         Winograd & Flores (Breakdown) ^3^
  ----------------------------------------------------------------------------------------------------------------------

The Quasi-Creature represents a \"breakdown\" in the Heideggerian sense utilized by Winograd and Flores.^3^ In *Understanding Computers and Cognition*, Winograd and Flores argued that tools are \"ready-to-hand\"---invisible in use---until they break, at which point they become \"present-at-hand,\" objects of inquiry. The Quasi-Creature exists in a permanent state of oscillation between these two modes. It is ready-to-hand when it fluently writes code or drafts emails, but violently present-at-hand when it confabulates a legal precedent or ignores a safety constraint. This instability creates a \"paradigm stress\" ^3^, forcing users to constantly monitor the system\'s internal state, a task for which current \"seamless\" interfaces are woefully ill-equipped.

### 1.2 The Void as Possibility Space

To design for the Quasi-Creature, we must first understand the medium in which it operates. We term this medium the \"Void.\" In classical design theory, Herbert Simon described design as a search through a \"solution space\".^5^ For Simon, this space was vast but theoretically enumerable. In the context of Generative AI, the Void is the latent space of the model---the bounded but incomprehensibly vast set of all possible token sequences, pixel arrangements, or audio waveforms that the model can generate.^5^

The Void is not empty; it is dense with the statistical detritus of the internet. It contains not just information, but \"vibe,\" style, bias, and structural grammar. Christopher Alexander's concept of *A Pattern Language* provides a useful lens here. Alexander described the \"space of possible buildings\" as being governed by generative rules that allow for infinite variation within coherent structures. Similarly, the generative Void is structured by the high-dimensional geometry of the Transformer architecture.^3^ However, unlike Alexander's patterns, which were derived from human culture and biology, the patterns of the Void are derived from statistical co-occurrence. They are, as Agre might argue, \"captured\" representations of human activity, stripped of their original indexical context.^6^

The design challenge, therefore, shifts from *construction* (manually assembling artifacts) to *sintering*. Sintering is the process of compacting a granular material into a solid mass using heat or pressure without melting it to the point of liquefaction. In generative design, the user applies \"heat\" (prompts, constraints, context) to the granular dust of the Void to solidify it into a usable \"Scene.\" The \"possibility space\" described by Salen and Zimmerman in game design ^5^ becomes a \"probability space\" in AI. The user's agency lies in their ability to manipulate the probability distribution of this space, constraining the Void until the desired artifact emerges.

### 1.3 The Crisis of Agency and Control

The central tension in this new ontology is the preservation of human agency. Ben Shneiderman's framework for *Human-Centered AI* (HCAI) argues for systems that ensure high levels of human control alongside high levels of computer automation.^7^ However, the nature of the Void makes this difficult. If the user exerts too much control (specifying every pixel), the generative advantage is lost. If they exert too little, they surrender to the statistical mean of the training data---a phenomenon known as \"model collapse\" or \"homogenization\".^8^

This report explores how we can resolve this tension by moving beyond the binary of \"automation vs. control.\" We draw on Latour's Actor-Network Theory (ANT) to view the human and the AI not as separate entities but as a \"hybrid\" network.^9^ The goal is not to maintain total control over the *output*, but to maintain control over the *process* of sintering. This requires new forms of \"Process Alignment\" ^10^ and \"Seamful Design\" ^11^ that make the operations of the Void legible and manipulable.

## 2. The Void: Legibility, Hallucination, and the Bounds of Possibility

The Void is the raw material of the 21st century. It is a statistical commons, enclosed by the architecture of the model and mined by the prompt. However, exploring this space is fraught with epistemic risk. Because the Void is generated probabilistically, it lacks the ontological stability of a database. A database retrieves; the Void *confabulates*. Understanding the nature of this confabulation is critical for designing interfaces that support truthful and effective collaboration.

### 2.1 Hallucination as a Feature of the Void

The term \"hallucination\" is a misnomer that anthropomorphizes the machine. A more accurate term, derived from the work of Winograd and Flores on \"breakdowns\" ^3^, might be *ontological drift*. The model does not \"know\" facts; it knows probability distributions. When a user asks for a citation, the model generates a sequence of tokens that *looks like* a citation. This is a feature, not a bug, of the generative process. It is the same mechanism that allows the model to write poetry or generate novel code.

However, from the perspective of \"Legibility\"---a concept James C. Scott applied to the state's need to simplify society ^12^---this drift is a disaster. Scott argued that legibility requires simplification, standardization, and the elimination of local nuance. In the context of AI, the user needs the *model* to be legible. They need to know *why* a specific output was generated.

Recent research on \"Prover-Verifier Games\" ^14^ suggests a path forward. By training small \"verifier\" models to check the reasoning of larger \"prover\" models, we can incentivize the generation of \"legible\" outputs---outputs that come with a verifiable chain of reasoning. This aligns with the \"Seamful XAI\" approach ^4^, which argues for exposing the \"seams\" of the generation process. Instead of presenting a seamless, authoritative answer, the interface should present the answer alongside its \"confidence scalar\" ^15^, its \"alternative interpretations\" ^15^, and the \"evidence strength\".^15^

### 2.2 Many-Shot Learning: Warping the Possibility Space

One of the most powerful mechanisms for shaping the Void is \"Many-Shot In-Context Learning\" (ICL). Research by Anthropic and others ^16^ demonstrates that as the number of examples (shots) in the context window increases from a few dozen to several thousand, the model's performance improves dramatically. More importantly, Many-Shot ICL allows the user to *override* the model's pre-training biases.

This capability confirms Simon's view of design as a search.^5^ By populating the context window with hundreds of examples, the user essentially terraforms the solution space. They create a \"local geometry\" within the Void that biases the search towards a specific style, format, or logic. This is a profound shift in agency. The user is no longer just a \"prompter\"; they are a \"dataset curator.\" They design the Void by designing the examples that define it.

**Table 2: The Impact of Many-Shot Context on the Void**

  -------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Feature**           **Few-Shot (Classical Prompting)**   **Many-Shot (Void Terraforming)**         **Design Implication**
  --------------------- ------------------------------------ ----------------------------------------- --------------------------------------------------------
  **Context Size**      \< 10 examples                       100s--1,000s of examples                  Need for tools to manage/curate large example sets.

  **Bias Mitigation**   Limited; relies on pre-training.     High; can override pre-training priors.   User agency shifts to *example selection* (curation).

  **Performance**       Plateauing accuracy.                 Linear/Log-linear scaling.^16^            \"More data\" becomes a design strategy for end-users.

  **Reasoning**         Fragile; prone to drift.             Robust; learns complex functions.         Enables \"Inverse Design\" (teaching by showing).
  -------------------------------------------------------------------------------------------------------------------------------------------------------------

### 2.3 The Legibility of Capture

Philip Agre's critique of \"capture\" ^6^ is highly relevant here. Agre argued that computers do not interact with the world; they interact with a \"grammar of action\" that has been captured and formalized. In Generative AI, this capture is total. The training data *is* the captured world. When we interact with the Void, we are interacting with a captured, tokenized, and statistical shadow of human activity.

This creates a \"Legibility Gap.\" The model's internal representation of a concept (e.g., \"fairness\" or \"style\") is a high-dimensional vector. The user's representation is semantic and cultural. Interfaces like **PromptCanvas** ^18^ attempt to bridge this gap by converting these vectors into \"Dynamic Widgets.\" By allowing users to manipulate sliders for \"Tone,\" \"Creativity,\" or \"Length,\" the interface makes the dimensions of the Void legible and manipulable. This is an act of *translation*, converting the alien geometry of latent space into the familiar affordances of a GUI.

## 3. The Scene: Accumulated Context and Cognitive Overload

If the Void is the space of potentiality, the \"Scene\" is the space of actuality. It is the accumulated context---the chat history, uploaded documents, system instructions, and user memories---that anchors the generative process. As context windows expand to millions of tokens ^20^, the Scene theoretically becomes infinite. However, this technological capability collides with the hard limits of human cognition.

### 3.1 The Infinite Context Fallacy

The promise of \"infinite context\" is often framed as the solution to AI memory. If the model can \"remember\" everything, surely it can understand the user perfectly? This view, however, ignores the user\'s role in the \"Human-AI Assemblage\".^22^ While the machine can retrieve specific tokens from a million-token window, the human user is bound by what Miller famously identified as the \"magical number seven\" ^20^---the limit of working memory.

Recent research on the **CoThinker** architecture ^23^ highlights this \"Cognitive Overload.\" The study found that as the complexity of the accumulated context increases, single-agent systems degrade in performance, mirroring human failure modes. The Scene becomes a chaotic pile of information rather than a structured workspace. The user loses track of what they have told the AI, what the AI has hallucinated, and what constraints are currently active.

This leads to a \"double-bind\" of context:

1.  **Too little context:** The Void is unconstrained; the model drifts.

2.  **Too much context:** The Scene is unmanageable; the user loses agency.

### 3.2 Context as Interactional Achievement

Paul Dourish's theory of \"Embodied Interaction\" offers a critical corrective to the \"container\" view of context.^25^ Dourish argues that context is not a static container of information; it is an *interactional achievement*. Context is what we *make* relevant in the moment of action. It is dynamic, situated, and constantly negotiated.

Current Chat UIs fail to support this dynamic. They treat context as a \"sedimentary\" layer ^27^---a linear log of everything that has happened. This obscures the *active* context. Users need tools to manage the Scene---to explicitly \"pin\" certain constraints, \"archive\" irrelevant history, and \"fork\" the conversation into new directions. The **Cognitive Workspace** ^20^ proposes an architecture for \"Active Memory Management,\" where the system (or user) actively curates the Scene, deciding what to keep in \"working memory\" and what to relegate to long-term storage.

### 3.3 Longitudinal Drift and Identity Negotiation

The management of the Scene is not just a cognitive task; it is an identity task. Longitudinal studies of artists and creative professionals using Generative AI ^25^ reveal a complex \"Identity and Value Negotiation\" that occurs over time.

Initially, users may view the AI as a \"tool\" (low agency, low threat). However, as the Scene accumulates---as the AI \"learns\" the user\'s style, preferences, and quirks---the relationship shifts. The AI begins to act as a \"collaborator\" or even a \"competitor.\" If the Scene is designed well---allowing the user to imprint their values and identity onto the system---this leads to a sense of \"co-creation.\" If the Scene is opaque, the user feels \"de-skilled\" and alienated.

Table 3: Stages of Identity Negotiation in the Scene ^25^

  --------------------------------------------------------------------------------------------------------------------------------------------
  **Stage**                  **User Perception**     **Role of the Scene**    **Key Friction**
  -------------------------- ----------------------- ------------------------ ----------------------------------------------------------------
  **Initial Encounter**      AI as Novelty/Toy       Minimal Context          \"It doesn\'t understand me.\"

  **Exploration**            AI as Tool/Apprentice   Context Accumulation     \"I need to teach it my style.\"

  **Integration**            AI as Partner/Engine    Deep Context (Persona)   \"Who is the author?\"

  **Resistance/Rejection**   AI as Threat/Replacer   Context Saturation       \"It\'s copying me too well\" or \"It\'s ignoring my nuance.\"
  --------------------------------------------------------------------------------------------------------------------------------------------

The design of the Scene must therefore support *identity preservation*. This means allowing users to explicitly define their \"persona\" within the system, to view and edit the \"memories\" the AI has formed about them, and to reject outputs that violate their professional values.

## 4. Agency and Alignment: From Output to Process

The central problem of \"Human-Centered AI\" (HCAI), as articulated by Shneiderman ^7^, is the preservation of human control. In the generative era, this control has largely been limited to \"Evaluation Alignment\"---the ability to accept, reject, or edit the final output. This is a shallow form of agency. To maintain genuine control over the Quasi-Creature, we must achieve \"Process Alignment\".^10^

### 4.1 The Three Dimensions of Alignment

Terry et al. ^10^ introduce a tripartite framework for interactive alignment that is essential for understanding the design space of generative tools:

1.  **Specification Alignment:** Aligning on *what* to do. This is the domain of Prompt Engineering. The user tries to articulate their intent in natural language. The friction here is the \"Gulf of Evaluation\" ^1^---did the model understand the prompt?

2.  **Process Alignment:** Aligning on *how* to do it. This is the missing link in current interfaces. The user has no visibility into the model\'s \"chain of thought,\" its search strategy, or its intermediate decisions.

3.  **Evaluation Alignment:** Aligning on the *quality* of the result. This is the domain of RLHF (Reinforcement Learning from Human Feedback) and output editing.

The current \"Chat\" paradigm collapses these three dimensions into a single turn-taking mechanic. The user specifies (1), the model does (2) invisibly, and the user evaluates (3). If the result is wrong, the user has no way to debug the process; they can only refine the specification. This \"black-boxing\" ^4^ disempowers the user.

### 4.2 Seamful XAI: Revealing the Machinery

To achieve Process Alignment, we must embrace \"Seamful Design\".^4^ Unlike seamless design, which seeks to hide the complexity of the system, seamful design deliberately exposes the \"seams\"---the boundaries, uncertainties, and decision points.

In the context of Generative AI, Seamful XAI might involve:

- **Visualizing Uncertainty:** Using color-coding or heatmaps to show which parts of a generated text the model is unsure about.^15^

- **Exposing Branching Paths:** Allowing the user to see alternative \"drafts\" or \"thoughts\" that the model discarded.

- **Intervention Points:** allowing the user to pause the generation process, edit the intermediate state (e.g., the plan), and then resume.

This approach transforms the interaction from a \"transaction\" (input -\> output) to a \"collaboration\" (input -\> process -\> intervention -\> output). It aligns with Suchman's view of situated action ^28^: plans (prompts) are just resources for action. The real work happens in the situated navigation of the task. By making the process visible, the user can \"situate\" themselves within the AI\'s reasoning.

### 4.3 AsyncVoice Agent and Process Fidelity

A concrete example of Process Alignment is the **AsyncVoice Agent**.^29^ This system decouples the model\'s \"reasoning\" stream from its \"voice\" stream. Instead of waiting for the model to finish thinking, the agent \"narrates\" its thought process in real-time.

Crucially, the authors introduce the metric of **Process Fidelity**.^29^ This measures the degree to which the agent\'s verbal explanation matches its actual internal reasoning steps. High Process Fidelity is essential for trust. If the agent says \"I am searching for the file\" but is actually hallucinating, trust is broken.

The AsyncVoice Agent allows for \"barge-in\"---the user can interrupt the agent mid-thought to correct a misunderstanding or steer the direction. This is a profound shift in agency. The user is no longer a passive recipient of the output; they are an active director of the process. They are \"sintering\" the thought process in real-time, applying constraints (interruptions) to shape the Void as it crystallizes into the Scene.

**Table 4: Evaluation of Alignment Strategies**

  ----------------------------------------------------------------------------------------------------------------------------
  **Strategy**                    **Focus**         **Agency Mechanism**    **Limitation**
  ------------------------------- ----------------- ----------------------- --------------------------------------------------
  **Prompt Engineering**          Specification     Linguistic Precision    Ambiguity; requires \"vibe coding\" skills.

  **RLHF / Editing**              Evaluation        Post-hoc Selection      High effort; \"fixing\" is harder than creating.

  **Seamful XAI**                 Process           Visibility of Seams     Cognitive load; requires user expertise.

  **AsyncVoice / Interruption**   Process           Real-time Steering      Latency constraints; conversational overhead.

  **DeckFlow / Canvas**           Structure         Spatial Decomposition   Friction of setup; breaks flow.
  ----------------------------------------------------------------------------------------------------------------------------

## 5. Interface Paradigms: Canvases, Decompositions, and Spatiality

If the Chat UI is the \"Command Line\" of the Generative era---linear, text-based, opaque---what is the \"GUI\"? The research points toward **Infinite Canvases** and **Structured Decomposition** as the native interfaces for Void Management.

### 5.1 The Failure of Linearity

The dominance of the linear chat interface (e.g., ChatGPT, Claude) is a historical accident, a skeuomorph of human-to-human messaging. However, creative work is rarely linear. It involves branching, merging, backtracking, and parallel exploration. As noted in the **DeckFlow** research ^32^, the linear chat forces users to serialize their non-linear thoughts, creating friction and \"context collapse.\"

Furthermore, linearity exacerbates the \"Gulf of Evaluation.\" In a long chat thread, it is difficult to see which parts of the context are currently active. The Scene becomes a \"scroll\" rather than a \"map.\"

### 5.2 DeckFlow: Spatializing the Void

**DeckFlow** ^32^ proposes an alternative: an \"infinite canvas\" where users can spatially organize their interaction with the Void. DeckFlow introduces the concept of **Task Decomposition** via \"Cards.\"

- **Goal Cards** define the high-level intent.

- **Action Cards** break that intent into sub-tasks (e.g., \"Generate Image,\" \"Write Text\").

- **Cluster Cards** group related outputs for comparison.

This spatial arrangement serves two functions:

1.  **Externalizing Cognitive Load:** By placing the steps on a canvas, the user offloads the need to remember the \"state\" of the project.^24^ The canvas *is* the state.

2.  **Visualizing the Void:** DeckFlow allows for \"Generative Space Exploration\" ^32^ by generating multiple variations for each card and displaying them in a grid. This allows the user to \"see\" the possibility space and make informed choices (sintering) rather than accepting the first result.

### 5.3 PromptCanvas: Dynamic Widgets and Affordances

**PromptCanvas** ^18^ takes the spatial concept further by introducing \"Dynamic Widgets.\" Instead of relying solely on natural language (which has infinite \"negative affordance\"---you can type anything, but don\'t know what will work), PromptCanvas allows users to create custom GUI elements for their prompts.

For example, a user writing a story might create a \"Tone\" slider, a \"Character List\" dropdown, and a \"Plot Twist\" button. These widgets act as **Affordances** ^1^ for the Void. They constrain the possibility space to a manageable set of dimensions.

This aligns with Norman's principles of **Constraints**.^2^ A text box is unconstrained. A widget is constrained. By allowing the user to *build* their own widgets, PromptCanvas empowers the user to define the *parameters* of their own agency. They are not just using a tool; they are building the control panel for the Quasi-Creature.

### 5.4 The \"Uncanny\" and the Interface

The interface must also manage the \"Uncanny Valley of Agency\".^3^ If the interface looks too much like a human chat (e.g., using \"I\" statements, simulating emotion), it risks deepening the uncanny effect when the system fails.

Spatial interfaces like DeckFlow and PromptCanvas mitigate this by re-framing the AI as a \"material\" or a \"engine\" rather than a \"person.\" The spatial layout emphasizes *structure* and *process* over *personality*. This \"de-anthropomorphizes\" the interaction, helping the user to maintain a clear mental model of the system as a probabilistic machine rather than a social agent.

## 6. Synthesis: Sintering the Future of Human-AI Collaboration

The transition from \"tool use\" to \"Void management\" requires a fundamental rethinking of design principles. We are moving from a world of *deterministic execution* to a world of *probabilistic negotiation*. In this new world, the designer's role is to provide the scaffolding---the \"seams,\" the \"canvases,\" and the \"widgets\"---that allow users to sinter the chaotic potential of the Void into meaningful, human-aligned Scenes.

### 6.1 Sintering as a Design Metaphor

We propose **Sintering** as the defining metaphor for Human-AI interaction in the generative age. Sintering captures the essence of the user\'s task:

- **The Material:** The granular, probabilistic dust of the Void (tokens, pixels).

- **The Energy:** The \"heat\" of the user\'s intent (prompts, context, constraints).

- **The Process:** Applying pressure to fuse the material into a solid form without melting it completely (preserving the generative spark while imposing structure).

Tools like DeckFlow and AsyncVoice Agent are \"Sintering Engines.\" They allow the user to apply precise, localized heat (context) and pressure (constraints) to specific parts of the Void.

### 6.2 The Politics of the Void

We must also confront the political implications of this shift. As Agre warned ^6^, the \"capture\" of human activity into machine-readable grammars (tokens) is a form of power. The Void is not neutral; it is shaped by the training data, which in turn is shaped by the power structures of the internet.

When we design interfaces that make the Void \"legible\" ^12^, we are also making the user \"legible\" to the machine. The decomposition of a creative task into \"Action Cards\" ^32^ is a form of disciplining the user---forcing them to think in the modular logic of the machine. We must remain vigilant against the risk of \"de-skilling\" ^25^, where the user becomes a mere operator of the sintering engine, losing the ability to create from scratch.

### 6.3 Future Directions

The future of HCI lies in the exploration of:

1.  **Ontological Interfaces:** Tools that map the high-dimensional geometry of the Void into human-understandable spatial metaphors (beyond 2D canvases).

2.  **Seamful Agents:** Agents that narrate their uncertainty and invite human \"barge-in\" as a core mechanic.

3.  **Active Scene Management:** Systems that help users curate, prune, and visualize the accumulated context of long-term collaborations.

4.  **Legibility Training:** Algorithms that optimize models not just for correctness, but for the human verifiability of their reasoning.^14^

The Quasi-Creature is here. It is too powerful to be ignored, and too alien to be trusted blindly. Our task as design researchers is to build the interfaces that will allow us to live with it---not by hiding its strangeness, but by making its strangeness legible, manipulable, and ultimately, aligned with the human condition.

### Key Concepts & Definitions

- **The Void**: The latent possibility space of a generative model; the set of all potential outputs.

- **The Scene**: The accumulated context (tokens, history, examples) that constrains the Void.

- **Sintering**: The process of applying constraints (pressure) to the Void to solidify it into a specific output.

- **Quasi-Creature**: An entity (AI) that exhibits high agency and intelligence but lacks embodiment and consistent reliability.^3^

- **Uncanny Valley of Agency**: The dip in user trust caused by systems that are too agentic to be tools but too unreliable to be partners.^3^

- **Process Fidelity**: The degree to which an AI\'s explained reasoning matches its actual computational process.^29^

- **Seamful Design**: Interfaces that deliberately expose system limits and uncertainties to enhance user agency.^4^

- **Process Alignment**: Aligning the human and machine on *how* a task is performed, not just the output.^10^

### References Integration

This report integrates insights from:

- **Classical HCI/Design**: Simon ^5^, Alexander, Suchman ^28^, Winograd & Flores ^3^, Agre ^6^, Norman ^1^, Dourish ^25^, Latour.^9^

- **Contemporary AI Research (2020-2025)**: CoThinker ^23^, AsyncVoice Agent ^29^, DeckFlow ^32^, PromptCanvas ^18^, Anthropic Many-Shot ^16^, Seamful XAI ^4^, Prover-Verifier Games.^14^

*End of Report*

#### Works cited

1.  User interface - Grokipedia, accessed December 9, 2025, [[https://grokipedia.com/page/User_interface]{.underline}](https://grokipedia.com/page/User_interface)

2.  Chapter 4: "Knowing What to do: Constraints, Discoverability, and Feedback" - Medium, accessed December 9, 2025, [[http://medium.com/design-bootcamp/chapter-4-knowing-what-to-do-constraints-discoverability-and-feedback-df4ea21fd5d8]{.underline}](http://medium.com/design-bootcamp/chapter-4-knowing-what-to-do-constraints-discoverability-and-feedback-df4ea21fd5d8)

3.  The Quasi-Creature and the Uncanny Valley of Agency: A \... - arXiv, accessed December 9, 2025, [[https://arxiv.org/pdf/2508.18563]{.underline}](https://arxiv.org/pdf/2508.18563)

4.  Seamful XAI: Operationalizing Seamful Design in Explainable AI - ResearchGate, accessed December 9, 2025, [[https://www.researchgate.net/publication/380202521_Seamful_XAI_Operationalizing_Seamful_Design_in_Explainable_AI]{.underline}](https://www.researchgate.net/publication/380202521_Seamful_XAI_Operationalizing_Seamful_Design_in_Explainable_AI)

5.  Planet Raku, accessed December 9, 2025, [[https://planet.raku.org/]{.underline}](https://planet.raku.org/)

6.  Surface Reading LLMs: Synthetic Text and Its Styles - arXiv, accessed December 9, 2025, [[https://www.arxiv.org/pdf/2510.22162]{.underline}](https://www.arxiv.org/pdf/2510.22162)

7.  Human-Centered AI; A Multidisciplinary Perspective for Policy-Makers, Auditors, and Users - OAPEN Library, accessed December 9, 2025, [[https://library.oapen.org/bitstream/handle/20.500.12657/100309/9781003860792.pdf?sequence=1&isAllowed=y]{.underline}](https://library.oapen.org/bitstream/handle/20.500.12657/100309/9781003860792.pdf?sequence=1&isAllowed=y)

8.  Personalized AI Scaffolds Synergistic Multi-Turn Collaboration in Creative Work, accessed December 9, 2025, [[https://www.researchgate.net/publication/397188389_Personalized_AI_Scaffolds_Synergistic_Multi-Turn_Collaboration_in_Creative_Work]{.underline}](https://www.researchgate.net/publication/397188389_Personalized_AI_Scaffolds_Synergistic_Multi-Turn_Collaboration_in_Creative_Work)

9.  The World is Not Enough: Growing Waste in HPC-enabled Academic Practice, accessed December 9, 2025, [[https://nora.nerc.ac.uk/id/eprint/539056/1/chi25-831.pdf]{.underline}](https://nora.nerc.ac.uk/id/eprint/539056/1/chi25-831.pdf)

10. Interactive AI Alignment: Specification, Process, and Evaluation Alignment - arXiv, accessed December 9, 2025, [[https://arxiv.org/pdf/2311.00710]{.underline}](https://arxiv.org/pdf/2311.00710)

11. Seamful XAI: Operationalizing Seamful Design in Explainable AI - arXiv, accessed December 9, 2025, [[https://arxiv.org/pdf/2211.06753]{.underline}](https://arxiv.org/pdf/2211.06753)

12. (PDF) From Privacy to Social Legibility - ResearchGate, accessed December 9, 2025, [[https://www.researchgate.net/publication/363301710_From_Privacy_to_Social_Legibility]{.underline}](https://www.researchgate.net/publication/363301710_From_Privacy_to_Social_Legibility)

13. Legibility and the Legacy of Racialized Dispossession in Digital Agriculture - NSF PAR, accessed December 9, 2025, [[https://par.nsf.gov/servlets/purl/10309323]{.underline}](https://par.nsf.gov/servlets/purl/10309323)

14. Prover-Verifier Games improve legibility of LLM outputs \| Request PDF - ResearchGate, accessed December 9, 2025, [[https://www.researchgate.net/publication/382363274_Prover-Verifier_Games_improve_legibility_of_LLM_outputs]{.underline}](https://www.researchgate.net/publication/382363274_Prover-Verifier_Games_improve_legibility_of_LLM_outputs)

15. A Multi-faceted Analysis of Cognitive Abilities: Evaluating Prompt Methods with Large Language Models on the CONSORT Checklist I - arXiv, accessed December 9, 2025, [[https://arxiv.org/pdf/2510.19139?]{.underline}](https://arxiv.org/pdf/2510.19139)

16. Many-Shot In-Context Learning - OpenReview, accessed December 9, 2025, [[https://openreview.net/forum?id=AB6XpMzvqH&referrer=%5Bthe%20profile%20of%20Azade%20Nova%5D(%2Fprofile%3Fid%3D\~Azade_Nova1)]{.underline}](https://openreview.net/forum?id=AB6XpMzvqH&referrer=%5Bthe+profile+of+Azade+Nova%5D(/profile?id%3D~Azade_Nova1))

17. Many-Shot In-Context Learning - arXiv, accessed December 9, 2025, [[https://arxiv.org/html/2404.11018v3]{.underline}](https://arxiv.org/html/2404.11018v3)

18. PromptCanvas: Composable Prompting Workspaces Using Dynamic Widgets for Exploration and Iteration in Creative Writing - arXiv, accessed December 9, 2025, [[https://arxiv.org/html/2506.03741v1]{.underline}](https://arxiv.org/html/2506.03741v1)

19. PromptCanvas: Composable Prompting Workspaces Using Dynamic Widgets for Exploration and Iteration in Creative Writing \| Request PDF - ResearchGate, accessed December 9, 2025, [[https://www.researchgate.net/publication/392406689_PromptCanvas_Composable_Prompting_Workspaces_Using_Dynamic_Widgets_for_Exploration_and_Iteration_in_Creative_Writing]{.underline}](https://www.researchgate.net/publication/392406689_PromptCanvas_Composable_Prompting_Workspaces_Using_Dynamic_Widgets_for_Exploration_and_Iteration_in_Creative_Writing)

20. (PDF) Cognitive Workspace: Active Memory Management for LLMs \-- An Empirical Study of Functional Infinite Context - ResearchGate, accessed December 9, 2025, [[https://www.researchgate.net/publication/394687800_Cognitive_Workspace_Active_Memory_Management_for_LLMs\_\--\_An_Empirical_Study_of_Functional_Infinite_Context]{.underline}](https://www.researchgate.net/publication/394687800_Cognitive_Workspace_Active_Memory_Management_for_LLMs_--_An_Empirical_Study_of_Functional_Infinite_Context)

21. Cognitive Workspace: Active Memory Management for LLMs An Empirical Study of Functional Infinite Context - arXiv, accessed December 9, 2025, [[https://arxiv.org/html/2508.13171v1]{.underline}](https://arxiv.org/html/2508.13171v1)

22. Explainable AI Reloaded: Challenging the XAI Status Quo in the Era of Large Language Models, accessed December 9, 2025, [[https://par.nsf.gov/servlets/purl/10613092]{.underline}](https://par.nsf.gov/servlets/purl/10613092)

23. UNITED MINDS OR ISOLATED AGENTS? EXPLORING COORDINATION OF LLMS UNDER COGNITIVE LOAD THEORY - OpenReview, accessed December 9, 2025, [[https://openreview.net/pdf/e95274f5c5daec085546434cabe5d882de30d5f9.pdf]{.underline}](https://openreview.net/pdf/e95274f5c5daec085546434cabe5d882de30d5f9.pdf)

24. (PDF) United Minds or Isolated Agents? Exploring Coordination of LLMs under Cognitive Load Theory - ResearchGate, accessed December 9, 2025, [[https://www.researchgate.net/publication/392530283_United_Minds_or_Isolated_Agents_Exploring_Coordination_of_LLMs_under_Cognitive_Load_Theory]{.underline}](https://www.researchgate.net/publication/392530283_United_Minds_or_Isolated_Agents_Exploring_Coordination_of_LLMs_under_Cognitive_Load_Theory)

25. Tracing Generative AI in Digital Art: A Longitudinal Study of Chinese Painters\' Attitudes, Practices, and Identity Negotiation - arXiv, accessed December 9, 2025, [[https://arxiv.org/html/2511.03117v1]{.underline}](https://arxiv.org/html/2511.03117v1)

26. What We Talk About When We Talk About Context (Draft) - ResearchGate, accessed December 9, 2025, [[https://www.researchgate.net/publication/2527939_What_We_Talk_About_When_We_Talk_About_Context_Draft]{.underline}](https://www.researchgate.net/publication/2527939_What_We_Talk_About_When_We_Talk_About_Context_Draft)

27. Reclaiming the Computer through LLM-Mediated Computing - ACM Interactions, accessed December 9, 2025, [[https://interactions.acm.org/archive/view/september-october-2025/reclaiming-the-computer-through-llm-mediated-computing]{.underline}](https://interactions.acm.org/archive/view/september-october-2025/reclaiming-the-computer-through-llm-mediated-computing)

28. (PDF) Situated Cognition in Theoretical and Practical Context - ResearchGate, accessed December 9, 2025, [[https://www.researchgate.net/publication/239062816_Situated_Cognition_in_Theoretical_and_Practical_Context]{.underline}](https://www.researchgate.net/publication/239062816_Situated_Cognition_in_Theoretical_and_Practical_Context)

29. (PDF) AsyncVoice Agent: Real-Time Explanation for LLM Planning and Reasoning, accessed December 9, 2025, [[https://www.researchgate.net/publication/396714915_AsyncVoice_Agent_Real-Time_Explanation_for_LLM_Planning_and_Reasoning]{.underline}](https://www.researchgate.net/publication/396714915_AsyncVoice_Agent_Real-Time_Explanation_for_LLM_Planning_and_Reasoning)

30. AsyncVoice Agent: Real-Time Explanation for LLM Planning and Reasoning - arXiv, accessed December 9, 2025, [[https://arxiv.org/html/2510.16156v1]{.underline}](https://arxiv.org/html/2510.16156v1)

31. AsyncVoice Agent: Real-Time Explanation for LLM Planning and Reasoning - ChatPaper, accessed December 9, 2025, [[https://chatpaper.com/paper/201360]{.underline}](https://chatpaper.com/paper/201360)

32. DeckFlow: Iterative Specification on a Multimodal Generative Canvas - arXiv, accessed December 9, 2025, [[https://arxiv.org/html/2506.15873v1]{.underline}](https://arxiv.org/html/2506.15873v1)

33. DeckFlow: Specification Decomposition on a Multimodal Generative Canvas - John Joon Young Chung, accessed December 9, 2025, [[https://johnr0.github.io/assets/publications/VLHCC2022-DeckFlow.pdf]{.underline}](https://johnr0.github.io/assets/publications/VLHCC2022-DeckFlow.pdf)

34. Composable Prompting Workspaces for Creative Writing: Exploration and Iteration Using Dynamic Widgets, accessed December 9, 2025, [[https://www.medien.ifi.lmu.de/pubdb/publications/pub/amin2025chi/amin2025chi.pdf]{.underline}](https://www.medien.ifi.lmu.de/pubdb/publications/pub/amin2025chi/amin2025chi.pdf)

35. Prover-verifier games improve legibility of llm outputs - arXiv, accessed December 9, 2025, [[https://arxiv.org/html/2407.13692v1]{.underline}](https://arxiv.org/html/2407.13692v1)
