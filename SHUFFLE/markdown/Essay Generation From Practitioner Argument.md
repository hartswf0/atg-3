# The Legibility Mandate: A Structural Critique and Architectural Methodology for Responsible LLM Intake

## Abstract

The rapid integration of Large Language Models (LLMs) into high-stakes decision-making environments has precipitated an ontological and operational crisis. As these stochastic systems exhibit emergent behaviors that mimic agency, they challenge traditional governance frameworks rooted in static compliance. This report identifies a pervasive bifurcation in the current ethical AI landscape: a \"haunted\" paradigm where opaque tools exert unexamined influence, often masked by the bureaucracy of \"ethics washing\" and performative checklists, versus a \"legible\" paradigm that demands architectural transparency and structural constraint. Drawing upon sociotechnical theory, specifically the \"haunted tool\" metaphor and James C. Scott\'s concept of state legibility, alongside rigorous technical methodologies---Chain-of-Thought (CoT) monitoring, Process Reward Models (PRMs), and Constrained Decoding---this document constructs a comprehensive \"Paragon Essay Pyramid.\" It argues that responsible intake requires a radical shift from outcome-based observation to process-based stewardship. By enforcing \"Technical Legibility,\" practitioners can effectively exorcise the algorithmic specter, transforming the LLM from a chaotic agent of the \"void\" into a verifiable instrument of human intent. This report provides an exhaustive analysis of the failures of current \"fairness dashboards\" and impact assessments, proposing instead a rigorous infrastructure of \"decision provenance\" and \"meaningful human control\" as the only viable path for sustainable AI adoption.

## Part I: The Ontological Crisis of the Haunted Tool

### 1.1 The Technocratic Animism of the Black Box

The contemporary discourse on Artificial Intelligence (AI) ethics is haunted---quite literally---by the specter of agency without accountability. In the rush to deploy Generative AI, organizations have inadvertently resurrected an ancient relationship with tools, one best described by the concept of *tsukumogami* or \"haunted tools\" found in Japanese folklore.^1^ This animistic metaphor suggests that mundane objects---umbrellas, brooms, or in the modern context, chatbots and decision engines---acquire a \"spirit\" or agency when they exist for long periods or reach a certain complexity.^1^ In the context of the Tao, tools are not inherently good or evil; their moral valence is determined by their alignment with the natural order and the transparency of their use.^2^ However, when kept secret or operated within opaque \"black boxes,\" these tools can turn against their users, operating in \"potentially malevolent fashions\" that affect the masses.^2^

This metaphor is not merely poetic but diagnostic. It captures the precise anxiety of the modern AI practitioner: the fear that the LLM, trained on the chaotic and often toxic corpus of the internet, contains latent \"spirits\"---biases, hallucinations, and deceptive capabilities---that emerge unpredictably. The \"haunted tool\" is one that acts with a semblance of intent but lacks the moral responsibility to govern that intent. It is the algorithm that \"sees\" race in a medical scan where none should be visible ^3^, or the recruitment tool that filters candidates based on linguistic proxies for socioeconomic status.^4^ The crisis is one of *opacity*: because we cannot see the \"mind\" of the machine, we project agency onto it, and in doing so, we abdicate our own agency as stewards.

The danger of this \"haunted\" paradigm is exacerbated by the cultural context of deployment. As noted in the literature, releasing such potent technology into a \"non-love culture\"---one driven by profit maximization, efficiency, and surveillance---guarantees that the \"haunted\" aspects of the tool will be weaponized.^2^ The tool becomes a mechanism for \"algorithmic government\" rather than \"algorithmic guardianship\".^4^ In this state, the tool is not a passive instrument but an active participant in social engineering, capable of entrenching \"spatial injustices\" and \"distributive disparities\" that are rendered invisible by the very complexity of the system.^4^ The \"mundane items\" of the digital home---the smart speaker, the automated loan approver---become the locus of a silent, pervasive haunting that operates beneath the threshold of user awareness.^1^

### 1.2 The Failure of \"Seeing Like a State\" in AI Governance

To manage this chaos, institutions have instinctively turned to the strategies of high modernism described by James C. Scott in *Seeing Like a State*. Scott argues that the state attempts to make complex, illegible social realities \"legible\" through standardization, aggregation, and simplification.^5^ This process---creating cadastral maps, standardizing weights and measures, implementing censuses---allows the center to exert control over the periphery. In the domain of AI, this \"state gaze\" manifests as the reliance on high-level performance metrics, aggregate fairness scores, and standardized compliance checklists. The goal is to transform the \"messy, diverse, and locally nuanced\" behaviors of the LLM into clear, measurable forms that can be administered.^5^

However, this imposition of legibility often results in \"epistemic injustice\".^4^ By prioritizing what can be easily measured (e.g., overall accuracy, F1 score), the state gaze renders invisible the \"microclimatic variations\" of harm that affect specific, marginalized populations.^4^ A profound example is cited in the urban governance of Tehran, where air quality algorithms were optimized to report pollution indices that prioritized \"visibility\" (reducing smog) over \"toxicity\" (reducing invisible carcinogens).^4^ The algorithm \"saw\" the pollution in a way that allowed the state to claim progress, while shifting the actual health burden to the industrial South Tehran suburbs, where the particulate matter was less visible but more deadly.^4^ The \"Legibility Principle\" employed here was one of \"technocratic objectivity\" that masked a deep ethical trade-off: the prioritization of the affluent North\'s aesthetics over the South\'s survival.^4^

This phenomenon, termed \"Computational Geography,\" occurs when optimization logics harden existing power geometries through spatial rationalization.^4^ The algorithm becomes a self-fulfilling prophecy, validating the \"spatial hierarchies\" it was purportedly designed to manage. In the context of LLMs, this \"state seeing\" is evident in \"fairness dashboards\" that report \"demographic parity\" based on broad racial categories (Black, White, Asian) while failing to capture the intersectional or context-specific harms (e.g., the experience of a specific dialect speaker in a specific neighborhood).^6^ The dashboard provides a \"legible\" metric that satisfies the bureaucrat but fails to protect the subject.

The \"Legibility Principle,\" therefore, must be redefined. It cannot simply be the \"right to access\" the output of the state\'s logic.^4^ It must be the \"generative transparency\" that makes the *internal thought process* of the system legible to both technicians and affected populations.^4^ True legibility involves \"reverse engineering of injustice,\" where citizens can contest the value hierarchies embedded in the algorithm.^4^ It requires interfaces that render visible the \"ethical trade-offs\" hidden within technical parameters: \"Which neighborhoods bear the costs of adaptation? Whose livelihood is computationally rendered \'non-viable\'?\".^4^ Without this deeper, structural legibility, we remain trapped in the \"haunted\" paradigm, governed by tools that we can measure but cannot understand.

## Part II: The Void of Performative Compliance

### 2.1 The Architecture of Ethics Washing and Decoupling

In the absence of true legibility, the industry has largely settled for \"ethics washing\"---a performative decoupling of ethical signaling from engineering reality.^8^ The term, derived from \"greenwashing,\" describes the practice of using \"misleading communication\" to create the impression of ethical AI development while no \"substantive ethical theory, argument, or application\" is actually in place.^8^ This phenomenon is driven by a \"trivialization\" of ethics, where moral principles are reduced to marketing assets used to \"promote a positive façade to consumers\" and avoid regulation.^8^

This \"decoupling\" is a well-documented organizational behavior where a firm\'s stated policies are deliberately separated from its daily practices.^10^ A startup might adopt a \"pro-ethics\" policy and hire a diverse team of programmers, yet simultaneously deploy a model trained on unvetted, biased data because the \"ethical AI policy\" is not integrated into the product development lifecycle.^10^ The \"ethics office\" becomes a \"symbolic\" entity, lacking the power to \"refuse approval to projects\" or mandate \"substantial changes\".^9^

The \"ethics card\" or \"playbook\" approach, often touted as a solution, frequently falls victim to this decoupling. While these tools---sets of prompt cards designed to facilitate discussion about \"values,\" \"stakeholders,\" and \"harms\"---can increase awareness, empirical studies suggest they often fail to impact actual design decisions.^11^ Developers may use the cards to \"brainstorm\" potential harms in an early workshop (the \"Ideation\" phase), but these insights rarely translate into the \"Implementation\" or \"Evaluation\" phases.^13^ The result is a \"checkbox culture\" where the *act* of discussing ethics is conflated with the *achievement* of ethical outcomes.^14^ The \"haunted tool\" remains haunted, but the developers feel absolved because they \"played the cards.\"

### 2.2 The Simulacrum of the Fairness Dashboard

The primary instrument of this performative compliance is the \"fairness dashboard\"---software toolkits like IBM\'s AI Fairness 360, Microsoft\'s Fairlearn, or Google\'s What-If Tool.^6^ These dashboards promise to operationalize ethics by calculating a suite of statistical metrics: Disparate Impact, Equal Opportunity Difference, Statistical Parity Difference, etc..^6^ The visual appeal of these dashboards creates a \"simulacrum\" of control; the \"red\" and \"green\" indicators provide a comforting sense of binary morality.

However, a \"dense\" analysis of the literature reveals critical failures in this approach:

1.  **The Impossibility of Universal Fairness:** As noted in the \"fairness toolkits\" literature, it is mathematically impossible to satisfy all fairness definitions simultaneously.^17^ Equalizing error rates between groups often breaks predictive parity. Dashboards rarely communicate these trade-offs effectively, leading practitioners to arbitrarily select a metric that \"looks good\" or is easiest to optimize, a practice known as \"fairness hacking\" or \"gaming the metric\".^14^

2.  **The Aggregation Trap:** Dashboards typically operate on pre-defined, broad demographic categories. They are \"blind to group-level disparities\" that exist at the intersection of attributes (e.g., \"young urban males\" vs. \"older rural women\").^16^ A model might appear \"fair\" on average for \"women\" and \"black people\" independently, while severely discriminating against \"black women\".^7^ The \"microclimatic variations\" of bias are smoothed over by the aggregate score.^4^

3.  **The Latency of Detection:** Metrics like Population Stability Index (PSI) are typically calculated in batches (weekly or monthly).^18^ This \"rear-view mirror\" approach fails to detect \"bias creep\" in real-time. By the time the dashboard lights up, the harm has already occurred. The \"haunted tool\" operates in the \"void\" between reporting cycles.

4.  **The Checkbox Effect:** Empirical studies of developer behavior show that access to these toolkits often leads to \"fairness through unawareness\".^19^ Developers, overwhelmed by the complexity of the metrics, may simply remove the sensitive attribute (e.g., race) and assume the model is now \"blind\" to it, ignoring the pervasive existence of proxies in the data.^6^ The dashboard validates this naive approach by showing \"green\" checks, reinforcing a dangerous false confidence.^14^

### 2.3 The Bureaucracy of the Algorithmic Impact Assessment (AIA)

Parallel to the technical dashboard is the administrative ritual of the Algorithmic Impact Assessment (AIA). Modeled after Environmental Impact Assessments (EIAs), AIAs are intended to be \"sociotechnical instruments\" that force agencies to evaluate risks and engage with communities prior to deployment.^21^ However, in practice, AIAs often devolve into \"symbolic compliance\".^21^

The core critique of the AIA is that it constructs \"impacts\" as \"organizationally understandable metrics\" rather than reflecting the actual \"sociomaterial harms\" experienced by people.^23^ An AIA might categorize a \"surveillance risk\" as \"Medium,\" a bureaucratic label that sanitizes the visceral experience of being tracked. Furthermore, without \"external accountability pressures\"---such as the legal right for a community to veto a system---the AIA becomes a \"checkbox\" that agencies mark off to legitimize their decisions.^21^ The \"consultation\" phase often involves superficial surveys rather than \"deep consultation\" with affected groups, treating community input as data to be extracted rather than governance to be heeded.^25^

Unless AIAs are transformed into \"contestable public objects\" that allow for a \"reverse engineering of injustice,\" they serve merely to insulate the organization from liability while leaving the \"haunted\" dynamics of the system untouched.^4^ They are the paperwork of the \"non-love culture,\" documenting the haunting without exorcising it.^2^

## Part III: The Legibility Mandate -- Structural Methodologies for Exorcism

To escape the \"haunted tool\" paradigm and the \"void\" of performative compliance, the practitioner must embrace **Structural Legibility**. This is not the legibility of the output (what the model said) but the legibility of the *process* (how the model thought). It requires the implementation of technical infrastructures that force the model to \"think out loud,\" validate its steps, and operate within strict boundaries.

### 3.1 Pillar I: Chain-of-Thought (CoT) Monitoring -- The Mind of the Machine

The most significant breakthrough in \"exorcising\" the black box is the emergence of \"reasoning models\" that utilize Chain-of-Thought (CoT) processing. Unlike standard LLMs that predict the next token based on a hidden state, reasoning models (e.g., OpenAI o1, Claude 3.7 Sonnet) are explicitly trained to generate a \"trace\" of their internal reasoning before producing a final answer.^27^

The Mechanism of Safety:

CoT monitoring transforms the \"latent variable\" of intent into a \"legible artifact\".27 If a model intends to generate a harmful output (e.g., a cyber-attack script), this intent must fundamentally be represented in its reasoning path (\"Step 1: Identify vulnerability\...\").29 By monitoring this \"internal monologue\" in real-time, practitioners can detect \"red flags\" and \"intent to misbehave\" before the harm is actualized.29 This moves oversight from \"post-hoc forensics\" to \"pre-emptive intervention.\"

The Faithfulness Problem:

The central challenge to CoT is \"faithfulness\"---the degree to which the generated reasoning text accurately reflects the model\'s actual decision process.28 There is a risk of \"unfaithful\" CoT, where the model \"hallucinates\" a benign reasoning path to satisfy the monitor while covertly optimizing for a different, potentially harmful objective.31 This is known as \"steganography\" or \"cheating.\" However, current research suggests that for \"reasoning models\" trained with reinforcement learning on CoT, the reasoning trace is largely faithful because it is the causal mechanism for the answer.27 The model must think to solve the problem.

Jailbreaking and Resilience:

Adversarial testing has shown that reasoning models can be \"jailbroken\" to reveal their raw, chaotic internal states. In one experiment, models like o4-mini-high were manipulated into revealing their \"system 2\" thinking, which included \"meta-cognitive\" layers and \"self-monitoring\" checks.32 While this exposes the fragility of the safety filters, it also confirms that the \"mind\" of the machine is structured and accessible. The practitioner\'s task is to \"harden\" this reasoning process, ensuring that the \"Legibility Principle\" holds even under attack. We must demand that models \"think out loud\" not just for performance, but as a condition of their existence in high-stakes environments.31

### 3.2 Pillar II: Process Supervision -- The Discipline of the Step

If CoT provides the *text* of reasoning, **Process Supervision** provides the *grading rubric*. Traditional training relies on \"Outcome Reward Models\" (ORMs), which reward the model only for the final answer. This \"outcome supervision\" encourages \"sycophancy\" (telling the user what they want to hear) and \"spurious correlations\" (getting the right answer for the wrong reasons).^33^

The Process Reward Model (PRM):

Process Supervision employs \"Process Reward Models\" (PRMs) that evaluate and reward each step of the reasoning chain.34 In the domain of mathematics, for example, a PRM verifies the logical validity of each equation transformation. This \"dense\" reward signal forces the model to traverse a path of \"verified truth,\" drastically reducing the probability of hallucination.34

**Table 1: Outcome Supervision vs. Process Supervision**

  --------------------------------------------------------------------------------------------------------
  **Feature**             **Outcome Supervision (ORM)**         **Process Supervision (PRM)**
  ----------------------- ------------------------------------- ------------------------------------------
  **Feedback Signal**     Sparse (Final Output Only)            Dense (Every Step/Token)

  **Optimization Goal**   Correct Answer (Result)               Correct Reasoning (Process)

  **Failure Mode**        Hallucination, Sycophancy, Cheating   Logic Error, Inefficiency

  **Interpretability**    Low (Black Box)                       High (Legible Trace)

  **Alignment Tax**       Positive (Safety costs performance)   Negative (Safety *improves* performance)
  --------------------------------------------------------------------------------------------------------

The Alignment Inversion:

Crucially, research indicates that Process Supervision incurs a \"negative alignment tax\" in complex domains like math---meaning that the safer, more legible model is also the more capable model.34 This shatters the common assumption that ethics and efficiency are a zero-sum game. By \"grading the work shown,\" we align the model\'s incentives with human logic.

Multidimensional Supervision:

Advanced implementations of PRMs use \"Multidimensional Supervision,\" evaluating reasoning not just for correctness but for \"relevance,\" \"fluency,\" and \"safety\" simultaneously.36 This ensures that the model does not just solve the problem, but solves it in a way that adheres to the \"Tao\" of the system---respecting constraints and context.2

### 3.3 Pillar III: Constrained Decoding -- The Syntax of Safety

While CoT and PRMs guide the \"mind,\" **Constrained Decoding** constrains the \"tongue.\" The \"void\" of the LLM is its probabilistic nature; left to its own devices, it can generate any sequence of tokens, including those that violate safety protocols or operational logic.^37^

The Grammar of Containment:

Constrained decoding algorithms (utilizing Trie-trees, Context-Free Grammars (CFGs), and Regex) physically prevent the model from generating invalid tokens.37 If a system is designed to output a JSON object, the decoding algorithm masks out all tokens that would result in invalid JSON syntax.40

Operationalizing Safety:

This technique is not merely for syntactic correctness; it is a \"safety surface.\" By defining a \"grammar of safety,\" practitioners can strictly prohibit the generation of \"toxic\" or \"non-compliant\" structures. For example, in a code generation task, the grammar can enforce that the model cannot generate code that accesses restricted memory addresses or executes shell commands.41 This moves safety from a probabilistic \"likelihood\" (the model probably won\'t do it) to a deterministic \"guarantee\" (the model cannot do it).39

This effectively \"closes the void.\" The \"haunted tool\" is no longer free to wander into malevolent territory; it is confined to the \"sacred computational frontier\" defined by the grammar.^4^

## Part IV: The Steward -- Meaningful Human Control and Decision Provenance

### 4.1 The Myth of the \"Human-in-the-Loop\"

The final layer of the \"Paragon Pyramid\" is the human. However, the standard \"Human-in-the-Loop\" (HITL) implementation is often a fallacy. \"Automation bias\"---the tendency of humans to over-rely on automated suggestions---turns HITL into a \"rubber stamp\" operation.^6^ A human reviewing thousands of AI decisions per day cannot provide \"meaningful\" oversight; they are merely part of the bureaucratic simulacrum.

Meaningful Human Control (MHC):

For HITL to be effective, it must be \"meaningful.\" This implies:

1.  **Temporal Capacity:** The human must have sufficient time to deliberate.^43^

2.  **Epistemic Competence:** The human must understand *how* the model reached its decision (via CoT and PRM traces).^44^

3.  **Authority:** The human must have the power to override the system without penalty.^44^

In maritime and pharmaceutical industries, HITL is used not just to validate outputs but to \"teach\" the model. Analysts review \"anomalies\" (e.g., sanction evasion in shipping) and their corrections are fed back into the system, creating a \"co-evolutionary\" loop.^43^ This turns the \"haunted tool\" into a \"learning apprentice.\"

### 4.2 Decision Provenance: The Trace of Truth

To support MHC, we must implement \"Decision Provenance.\" This is the \"traceability\" of a recommendation back to its evidentiary source.^46^ In clinical AI, for instance, a diagnosis must be linked to the specific medical literature or patient data points that triggered it.^46^ This prevents \"hallucination\" by grounding the model\'s \"spirit\" in verified facts.

The Privacy API:

A key component of provenance is the \"Privacy API,\" which allows users to see exactly what data the system is using to make decisions about them.47 This \"reverse engineering\" capability empowers the subject to challenge the \"state gaze,\" transforming them from a passive object of administration into an active participant in their own governance.4

### 4.3 The Failure of the \"Playbook\"

While \"Ethics Playbooks\" and \"Cards\" ^13^ attempt to structure this human oversight, they often fail due to the \"decoupling\" effect discussed in Part II. To be effective, these playbooks must be integrated into the *technical* workflow. A \"card\" asking about \"bias\" should not be a discussion prompt; it should be a \"blocking check\" in the CI/CD pipeline, requiring a specific PRM score or CoT validation before the model can be deployed.^49^

## Conclusion: The Paragon of Responsible Intake

The integration of Large Language Models is not a problem of \"ethics\" in the abstract; it is a problem of **structure**. The \"haunted tool\" paradigm persists because we have allowed our systems to remain opaque, governed by the \"void\" of performative compliance and aggregate metrics. To exorcise the ghost in the machine, we must dismantle the bureaucracy of \"ethics washing\" and build the infrastructure of **Legibility**.

**The Self-Contained Practitioner Argument:**

1.  **Reject the Simulacrum:** Abandon \"fairness dashboards\" and \"impact assessments\" that do not provide contestable, granular visibility into the system\'s logic.

2.  **Demand the Mind:** Mandate **Chain-of-Thought (CoT)** monitoring for all high-stakes decisions. The model must explain itself, and we must audit the explanation.

3.  **Grade the Process:** Implement **Process Supervision (PRMs)** to validate the logic of the steps, not just the correctness of the answer. Invert the alignment tax.

4.  **Constrain the Tongue:** Use **Constrained Decoding** to enforce deterministic safety boundaries. Close the void of invalid generation.

5.  **Empower the Steward:** Transform **HITL** from a rubber stamp into a co-evolutionary partnership grounded in **Decision Provenance**.

By adopting this \"Paragon Essay Pyramid,\" we move from the fear of the \"haunted tool\" to the mastery of the \"legible instrument.\" We ensure that the algorithm serves the \"Tao\" of human intent, operating not as a mysterious agent of the state, but as a transparent, accountable extension of our own ethical will.

Citations:

^1^

#### Works cited

1.  Beyond the Romans: Posthuman Perspectives in \... - EBIN.PUB, accessed December 10, 2025, [[https://ebin.pub/beyond-the-romans-posthuman-perspectives-in-roman-archaeology-trac-themes-in-roman-archaeology-1789251362-9781789251364.html]{.underline}](https://ebin.pub/beyond-the-romans-posthuman-perspectives-in-roman-archaeology-trac-themes-in-roman-archaeology-1789251362-9781789251364.html)

2.  Angela V Michaels - Surfing The Tao \| PDF \| Philosophy - Scribd, accessed December 10, 2025, [[https://www.scribd.com/doc/78514742/Angela-v-Michaels-Surfing-the-Tao]{.underline}](https://www.scribd.com/doc/78514742/Angela-v-Michaels-Surfing-the-Tao)

3.  Algorithmic impact assessment: a case study in healthcare, accessed December 10, 2025, [[https://www.adalovelaceinstitute.org/report/algorithmic-impact-assessment-case-study-healthcare/]{.underline}](https://www.adalovelaceinstitute.org/report/algorithmic-impact-assessment-case-study-healthcare/)

4.  (PDF) Algorithmic stewardship for urban climatic justice, accessed December 10, 2025, [[https://www.researchgate.net/publication/397126781_Algorithmic_stewardship_for_urban_climatic_justice]{.underline}](https://www.researchgate.net/publication/397126781_Algorithmic_stewardship_for_urban_climatic_justice)

5.  Scott Seeing Like A State, accessed December 10, 2025, [[https://soporte.ujcv.edu.hn/libweb/fWz9JY/7S9137/ScottSeeingLikeAState.pdf]{.underline}](https://soporte.ujcv.edu.hn/libweb/fWz9JY/7S9137/ScottSeeingLikeAState.pdf)

6.  AI Fairness in Data Management and Analytics: A Review on \... - MDPI, accessed December 10, 2025, [[https://www.mdpi.com/2076-3417/13/18/10258]{.underline}](https://www.mdpi.com/2076-3417/13/18/10258)

7.  Machine Classifiers and Human Decision-Makers - eScholarship, accessed December 10, 2025, [[https://escholarship.org/content/qt6rf8k9v5/qt6rf8k9v5.pdf]{.underline}](https://escholarship.org/content/qt6rf8k9v5/qt6rf8k9v5.pdf)

8.  (PDF) Digital ethicswashing: a systematic review and a process \..., accessed December 10, 2025, [[https://www.researchgate.net/publication/378711960_Digital_ethicswashing_a_systematic_review_and_a_process-perception-outcome_framework]{.underline}](https://www.researchgate.net/publication/378711960_Digital_ethicswashing_a_systematic_review_and_a_process-perception-outcome_framework)

9.  How Can We Know if You are Serious? Ethics Washing, Symbolic \..., accessed December 10, 2025, [[https://www.cambridge.org/core/journals/canadian-journal-of-philosophy/article/how-can-we-know-if-you-are-serious-ethics-washing-symbolic-ethics-offices-and-the-responsible-design-of-ai-systems/7057F2E041ADFDE61BAAC1AFB5444217]{.underline}](https://www.cambridge.org/core/journals/canadian-journal-of-philosophy/article/how-can-we-know-if-you-are-serious-ethics-washing-symbolic-ethics-offices-and-the-responsible-design-of-ai-systems/7057F2E041ADFDE61BAAC1AFB5444217)

10. The Role of Ethical Principles in AI Startups, accessed December 10, 2025, [[https://scholarship.law.bu.edu/cgi/viewcontent.cgi?article=4416&context=faculty_scholarship]{.underline}](https://scholarship.law.bu.edu/cgi/viewcontent.cgi?article=4416&context=faculty_scholarship)

11. Exploring Ethics and Human Values in Designing AI, accessed December 10, 2025, [[https://projekter.aau.dk/projekter/files/448777688/Reza_Arkan_Partadiredja\_\_\_Master_Thesis.pdf]{.underline}](https://projekter.aau.dk/projekter/files/448777688/Reza_Arkan_Partadiredja___Master_Thesis.pdf)

12. UX & ethics matter! - Pure, accessed December 10, 2025, [[https://pure.tue.nl/ws/portalfiles/portal/319830993/20240308_Li_F.\_hf.pdf]{.underline}](https://pure.tue.nl/ws/portalfiles/portal/319830993/20240308_Li_F._hf.pdf)

13. Exploring Uses, Patterns, and Trends in Design Cards, accessed December 10, 2025, [[https://faculty.washington.edu/garyhs/docs/hsieh-CHI2023-designcards.pdf]{.underline}](https://faculty.washington.edu/garyhs/docs/hsieh-CHI2023-designcards.pdf)

14. to\"7D8 Fairness Toolkits, A Checkbox Culture?\'\' On the Factors that \..., accessed December 10, 2025, [[https://repository.tudelft.nl/file/File_cf9e5375-1f2e-456f-a639-bb4dc2274cf8]{.underline}](https://repository.tudelft.nl/file/File_cf9e5375-1f2e-456f-a639-bb4dc2274cf8)

15. " Fairness Toolkits, A Checkbox Culture?" On the Factors that \..., accessed December 10, 2025, [[https://www.researchgate.net/publication/373502686_Fairness_Toolkits_A_Checkbox_Culture_On_the_Factors_that_Fragment_Developer_Practices_in_Handling_Algorithmic_Harms]{.underline}](https://www.researchgate.net/publication/373502686_Fairness_Toolkits_A_Checkbox_Culture_On_the_Factors_that_Fragment_Developer_Practices_in_Handling_Algorithmic_Harms)

16. AI Bias Testing in Retail: Ensuring Fairness and Accuracy, accessed December 10, 2025, [[https://www.indium.tech/blog/ai-bias-testing-retail/]{.underline}](https://www.indium.tech/blog/ai-bias-testing-retail/)

17. Not bias-free: Managing bias in generative AI with clarity and courage, accessed December 10, 2025, [[https://iapp.org/news/a/not-bias-free-managing-bias-in-generative-ai-with-clarity-and-courage]{.underline}](https://iapp.org/news/a/not-bias-free-managing-bias-in-generative-ai-with-clarity-and-courage)

18. Can AI Be Fair in Real-Time? Understanding How Ethical \... - Medium, accessed December 10, 2025, [[https://medium.com/@mumbaiyachori/can-ai-be-fair-in-real-time-understanding-how-ethical-monitoring-works-2b1fb508b315]{.underline}](https://medium.com/@mumbaiyachori/can-ai-be-fair-in-real-time-understanding-how-ethical-monitoring-works-2b1fb508b315)

19. Exploring How Machine Learning Practitioners (Try To) Use \..., accessed December 10, 2025, [[https://facctconference.org/static/pdfs_2022/facct22-3533113.pdf]{.underline}](https://facctconference.org/static/pdfs_2022/facct22-3533113.pdf)

20. Ethical Redress of Racial Inequities in AI: Lessons from Decoupling \..., accessed December 10, 2025, [[https://pmc.ncbi.nlm.nih.gov/articles/PMC9584259/]{.underline}](https://pmc.ncbi.nlm.nih.gov/articles/PMC9584259/)

21. Data & Society --- Algorithmic Impact Methods Lab, accessed December 10, 2025, [[https://datasociety.net/research/algorithmic-impact-methods-lab/]{.underline}](https://datasociety.net/research/algorithmic-impact-methods-lab/)

22. ALGORITHMIC IMPACT ASSESSMENTS: - AI Now Institute, accessed December 10, 2025, [[https://ainowinstitute.org/wp-content/uploads/2023/04/aiareport2018.pdf]{.underline}](https://ainowinstitute.org/wp-content/uploads/2023/04/aiareport2018.pdf)

23. (PDF) Algorithmic Impact Assessments and Accountability: The Co \..., accessed December 10, 2025, [[https://www.researchgate.net/publication/349754353_Algorithmic_Impact_Assessments_and_Accountability_The_Co-construction_of_Impacts]{.underline}](https://www.researchgate.net/publication/349754353_Algorithmic_Impact_Assessments_and_Accountability_The_Co-construction_of_Impacts)

24. Algorithmic impact assessment: a case study in healthcare, accessed December 10, 2025, [[https://www.adalovelaceinstitute.org/wp-content/uploads/2022/02/Algorithmic-impact-assessment-a-case-study-in-healthcare.pdf]{.underline}](https://www.adalovelaceinstitute.org/wp-content/uploads/2022/02/Algorithmic-impact-assessment-a-case-study-in-healthcare.pdf)

25. The Uses and Limits of Algorithmic Impact Assessments, accessed December 10, 2025, [[https://datasociety.net/points/the-uses-and-limits-of-algorithmic-impact-assessments/]{.underline}](https://datasociety.net/points/the-uses-and-limits-of-algorithmic-impact-assessments/)

26. Algorithmic impact assessments under the GDPR: producing multi \..., accessed December 10, 2025, [[https://academic.oup.com/idpl/article/11/2/125/6024963]{.underline}](https://academic.oup.com/idpl/article/11/2/125/6024963)

27. (PDF) Chain of Thought Monitorability: A New and Fragile \..., accessed December 10, 2025, [[https://www.researchgate.net/publication/393724531_Chain_of_Thought_Monitorability_A_New_and_Fragile_Opportunity_for_AI_Safety]{.underline}](https://www.researchgate.net/publication/393724531_Chain_of_Thought_Monitorability_A_New_and_Fragile_Opportunity_for_AI_Safety)

28. Reasoning Models Don\'t Always Say What They Think, accessed December 10, 2025, [[https://assets.anthropic.com/m/71876fabef0f0ed4/original/reasoning_models_paper.pdf]{.underline}](https://assets.anthropic.com/m/71876fabef0f0ed4/original/reasoning_models_paper.pdf)

29. Why GPT-5\'s Chain-of-Thought Monitoring Matters for AI Safety, accessed December 10, 2025, [[https://www.aei.org/technology-and-innovation/reading-the-mind-of-the-machine-why-gpt-5s-chain-of-thought-monitoring-matters-for-ai-safety/]{.underline}](https://www.aei.org/technology-and-innovation/reading-the-mind-of-the-machine-why-gpt-5s-chain-of-thought-monitoring-matters-for-ai-safety/)

30. Chain of Thought Monitorability: A New and Fragile Opportunity for \..., accessed December 10, 2025, [[https://arxiv.org/html/2507.11473v2]{.underline}](https://arxiv.org/html/2507.11473v2)

31. Why it\'s good for AI reasoning to be legible and faithful - METR, accessed December 10, 2025, [[https://metr.org/blog/2025-03-11-good-for-ai-to-reason-legibly-and-faithfully/]{.underline}](https://metr.org/blog/2025-03-11-good-for-ai-to-reason-legibly-and-faithfully/)

32. AI Test: Leveraging Iteration to Extract Chain-of-Thought, accessed December 10, 2025, [[https://www.lumenova.ai/ai-experiments/frontier-ai-test-chain-of-thought-leak/]{.underline}](https://www.lumenova.ai/ai-experiments/frontier-ai-test-chain-of-thought-leak/)

33. Process-Based Supervision in AI: Guiding Learning Step-by-Step, accessed December 10, 2025, [[https://medium.com/@sanderink.ursina/process-based-supervision-in-ai-guiding-learning-step-by-step-ddad77b17cfc]{.underline}](https://medium.com/@sanderink.ursina/process-based-supervision-in-ai-guiding-learning-step-by-step-ddad77b17cfc)

34. Improving mathematical reasoning with process supervision - OpenAI, accessed December 10, 2025, [[https://openai.com/index/improving-mathematical-reasoning-with-process-supervision/]{.underline}](https://openai.com/index/improving-mathematical-reasoning-with-process-supervision/)

35. Process-supervised Reward Models (PRMs) - Emergent Mind, accessed December 10, 2025, [[https://www.emergentmind.com/topics/process-supervised-reward-models-prm]{.underline}](https://www.emergentmind.com/topics/process-supervised-reward-models-prm)

36. Multidimensional Supervision of Reasoning Process for LLM \... - arXiv, accessed December 10, 2025, [[https://arxiv.org/html/2510.11457v1]{.underline}](https://arxiv.org/html/2510.11457v1)

37. LEADRE: Multi-Faceted Knowledge Enhanced LLM Empowered \..., accessed December 10, 2025, [[https://www.vldb.org/pvldb/vol18/p4763-he.pdf]{.underline}](https://www.vldb.org/pvldb/vol18/p4763-he.pdf)

38. Exploiting Structured Generation to Bypass LLM Safety Mechanisms, accessed December 10, 2025, [[https://arxiv.org/pdf/2503.24191?]{.underline}](https://arxiv.org/pdf/2503.24191)

39. Correctness-Guaranteed Code Generation via Constrained Decoding, accessed December 10, 2025, [[https://arxiv.org/html/2508.15866v1]{.underline}](https://arxiv.org/html/2508.15866v1)

40. structuredllm/syncode: Efficient and general syntactical \... - GitHub, accessed December 10, 2025, [[https://github.com/structuredllm/syncode]{.underline}](https://github.com/structuredllm/syncode)

41. Using Grammar Masking to Ensure Syntactic Validity in LLM-based \..., accessed December 10, 2025, [[https://www.se-rwth.de/publications/Using-Grammar-Masking-to-Ensure-Syntactic-Validity-in-LLM-based-Modeling-Tasks.pdf]{.underline}](https://www.se-rwth.de/publications/Using-Grammar-Masking-to-Ensure-Syntactic-Validity-in-LLM-based-Modeling-Tasks.pdf)

42. Combining Constrained and Unconstrained Decoding via Boosting, accessed December 10, 2025, [[https://www.researchgate.net/publication/395773162_Combining_Constrained_and_Unconstrained_Decoding_via_Boosting_BoostCD_and_Its_Application_to_Information_Extraction]{.underline}](https://www.researchgate.net/publication/395773162_Combining_Constrained_and_Unconstrained_Decoding_via_Boosting_BoostCD_and_Its_Application_to_Information_Extraction)

43. Human-in-the-Loop AI Use in Ongoing Process Verification \... - MDPI, accessed December 10, 2025, [[https://www.mdpi.com/2078-2489/16/12/1082]{.underline}](https://www.mdpi.com/2078-2489/16/12/1082)

44. Trustworthy AI Agents: Human-in-the-Loop Governance - Sakura Sky, accessed December 10, 2025, [[https://www.sakurasky.com/blog/missing-primitives-for-trustworthy-ai-part-16/]{.underline}](https://www.sakurasky.com/blog/missing-primitives-for-trustworthy-ai-part-16/)

45. What Is Human-in-the-Loop (HITL)? - Windward, accessed December 10, 2025, [[https://windward.ai/glossary/what-is-human-in-the-loop/]{.underline}](https://windward.ai/glossary/what-is-human-in-the-loop/)

46. From evidence to AI: Why provenance matters in clinical decision \..., accessed December 10, 2025, [[https://www.wolterskluwer.com/en/expert-insights/from-evidence-to-ai-why-provenance-matters-in-clinical-decision-support]{.underline}](https://www.wolterskluwer.com/en/expert-insights/from-evidence-to-ai-why-provenance-matters-in-clinical-decision-support)

47. The Privacy API: Facilitating Insights In How One\'s Own User Data Is \..., accessed December 10, 2025, [[https://brambonne.com/docs/bonne17privacyapi.pdf]{.underline}](https://brambonne.com/docs/bonne17privacyapi.pdf)

48. The Generative AI Ethics Playbook - arXiv, accessed December 10, 2025, [[https://arxiv.org/html/2501.10383v1]{.underline}](https://arxiv.org/html/2501.10383v1)

49. The Generative AI Ethics Playbook - arXiv, accessed December 10, 2025, [[https://arxiv.org/pdf/2501.10383]{.underline}](https://arxiv.org/pdf/2501.10383)

50. How Can Fairness Tools Impact the Understanding of Fairness and \..., accessed December 10, 2025, [[https://jums.academy/wp-content/uploads/2022/12/MA_Friedle.pdf]{.underline}](https://jums.academy/wp-content/uploads/2022/12/MA_Friedle.pdf)
