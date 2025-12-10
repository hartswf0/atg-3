# POML Prompt Library
## Prompt Object Markup Language — Layered Prompt Engineering

> **Core Thesis**: Writing prompts that write prompts is a valid mode of sophisticated AI collaboration. This library documents a semester's worth of meta-prompt development—prompts designed to generate other prompts, extract ideal types, and produce structured analytical outputs.

---

## What is POML?

**POML** (Prompt Object Markup Language) is an XML-based format for structuring complex prompts with:
- **Roles** — persona/voice specification
- **Tasks** — core instruction sets
- **Stylesheets** — syntax and formatting rules
- **Output Schemas** — JSON structure enforcement
- **Runtime Configuration** — model parameters

Unlike flat prompts, POML enables:
1. **Composability** — prompts can reference and embed other prompts
2. **Reusability** — extracted configurations can be applied to new domains
3. **Transparency** — the structure exposes what the prompt is actually doing
4. **Iteration** — refinement happens at the schema level, not just the text

---

## The Library

### 1. forensic.poml — Ethical Forensics Analyst

**Purpose**: Multi-ledger ethical diagnostic for any target system/product/event.

**Key Features**:
- 7 ethics lenses (deontological, consequentialist, virtue, care, capabilities, critical, environmental)
- 10 off-ledger persistence mechanisms (externalization, info asymmetry, regulatory capture, etc.)
- Stress tests (reductio, inversion, reversal, stakeholder audit)
- Repair proposals tagged by macro lever (Law/Market/Code/Norms)

**Output Structure**:
```
Calibration → Steelman → Assumption Map → Materiality Map → 
Logical Tensions → Paradox Table → Stress Tests → Foundational Counters → 
Audience Fit → Ethics Score & Stoplight → Repairs → Executive Verdict →
Self-Audit → Quote Locator → References
```

**Use Case**: Analyzing business models, policies, or media artifacts for hidden harms.

---

### 2. mythos.poml — Weberian-Bayesian Mythographer

**Purpose**: Extract ideal types, build comparative rulers, and model Bayesian updates with myth layer integration.

**Key Features**:
- Weber's ideal type extraction (3–6 accentuated features)
- Ruler construction (0–5 scale with anchor descriptors)
- PLoT (Probabilistic Language of Thought) for prior/posterior modeling
- Barthes myth integration (archetypes, micro-narratives)

**Output Structure**:
```
Ideal Type Statement → Ruler Table → Bayesian Update → Myth Layer → JSON Appendix
```

**Use Case**: Analyzing discourse about organizations, technologies, or movements.

---

### 3. tactics.poml — De Certeau Tactics Excavator

**Purpose**: Full concordance of tactics from *The Practice of Everyday Life*.

**Key Features**:
- Forensic mode with deep strictness
- Verbatim quote requirement (≤25 words per quote, max 120)
- Classification types (Exemplary/Definitional/Anecdote/Metaphor)
- Strategy–tactic interface mapping

**Output Structure**:
```
Calibration → Tactic Index (Full Concordance) → Meta-Theory → 
Clusters & Families → Strategy–Tactic Interface → Paradox Table → 
Critical Counters → Executive Index → References
```

**Use Case**: Close reading of theoretical texts with systematic extraction.

---

### 4. parody.poml — POML→POML Forge Engine

**Purpose**: Extract ideal types + parodic mechanics from source text, then **generate a new POML** for producing parody essays.

**Key Features**:
- Two-stage output: CONFIG_JSON extraction + INNER_POML generation
- Parodic mechanics (runner motif, incongruity beats, carnival inversion, escalation ladder)
- Satire register specification (voice, tone, required beats)
- Safety guardrails (systemic targets only, no doxxing)

**Output Structure**:
```
CONFIG_JSON (extracted ideal type + mechanics + myth layer + ruler + PLoT priors)
↓
INNER_POML (ready to run; generates 900–1300 word parody essay + analytic appendix)
```

**Use Case**: Generating satirical critiques of institutional discourse.

---

### 5. parody-gen.poml — Parody Prompt Generator

**Purpose**: Lighter version of parody.poml for rapid prompt forging.

**Key Features**:
- Ideal type extraction (3–6 features)
- Parodic mechanics identification
- NEW_PROMPT generation for essay production

**Output**: Natural-language prompt + JSON config.

---

### 6. inverse-essay.poml — Inverse Essay Prompt Generator

**Purpose**: Parse source text into ideal type + parodic mechanics + myth layer, then forge reusable prompt.

**Key Features**:
- Bi-textual frame analysis (Hutcheon)
- Carnival inversion (Bakhtin)
- Ambivalent laughter mechanics

**Output**:
```
CONFIG_JSON → NEW_PROMPT template
```

---

### 7. prompt.poml — Prompt → POML Transformer

**Purpose**: Convert any natural-language prompt into valid POML structure.

**Key Features**:
- Mode selection (minimal/balanced/maximal)
- Automatic schema generation (light/strict)
- Tool detection and definition
- Special character escaping

**Use Case**: Migrating existing prompts into POML format for reuse.

---

### 8. recursive.poml — Recursive Prompt Generator

**Purpose**: Prompts that generate prompts that generate prompts.

**Key Features**:
- Level-1 base prompts (law, bias, apparatus, counterfactual, signals)
- Level-2 combinators (fuse multiple dimensions)
- Level-3 child POML template
- Grammar rules ("Frame X; test Y; falsify Z")

**Philosophy**: Every prompt must spawn at least 3 further prompts.

---

### 9. meta-prime.poml — Meta-Prompt Engine

**Purpose**: For any given author text, extract their implicit "prompt logic."

**Key Features**:
- Operating system extraction (how does this thinker frame problems?)
- Prompt family generation (3–7 meta-prompts in author's style)
- Generalized template output

**Example Prompt Logic**:
- **Ong**: "Where is memory stored: in sound, or in inscription?"
- **Schafer**: "Is this environment hi-fi or lo-fi? What are its soundmarks?"
- **Sterne**: "What apparatus crystallizes listening?"

---

## Typology of POML Usage

| Type | Description | Examples |
|------|-------------|----------|
| **Analytical** | Extract structured findings from text | forensic.poml, tactics.poml |
| **Generative** | Produce new text in defined genre | parody.poml, inverse-essay.poml |
| **Transformative** | Convert between formats | prompt.poml |
| **Recursive** | Generate prompts from prompts | recursive.poml, meta-prime.poml |
| **Compositional** | Embed one POML inside another | parody.poml (INNER_POML output) |

---

## Why This Matters for Disclosure

The ACM policy on generative AI disclosure assumes **transactional** prompt use:
> "Which content/section(s) were created by generative AI? What tool version? The text of your input prompts?"

But POML represents **infrastructural** prompt use:
- Prompts are designed to be reused, not consumed
- Prompts generate other prompts in recursive chains
- The "input prompt" is itself a structured artifact with its own development history

**The paradox**: The more sophisticated the prompt engineering, the harder it becomes to itemize discrete "prompts" for disclosure. A single POML file represents dozens of iterations, refinements, and test runs—none of which map cleanly onto "I used ChatGPT with this prompt."

This is mētis in action: practical knowledge accumulated through sustained engagement, resistant to the legibility that disclosure frameworks require.

---

## Future Work

1. **POML Compiler**: Validate and execute POML files directly without copy-paste
2. **POML Inheritance**: Child POMLs that extend parent configurations
3. **POML Registry**: Shareable library of validated prompt patterns
4. **POML→Code**: Generate executable code from POML schemas
5. **POML Versioning**: Track iterative refinements with semantic versioning

---

## Connection to Course Themes

| POML | Course Connection |
|------|-------------------|
| forensic.poml | Lessig's regulatory modes (Law/Market/Code/Norms) as repair levers |
| mythos.poml | Weber's ideal types as analytical infrastructure |
| tactics.poml | De Certeau's mētis—practical knowledge encoded as prompt logic |
| parody.poml | Barthes' mythology analysis operationalized |
| meta-prime.poml | Shilton's values levers—extracting implicit operating systems |

---

## Files

| File | Lines | Purpose |
|------|-------|---------|
| `forensic.poml` | 351 | Ethical forensics with 7 lenses + stress tests |
| `mythos.poml` | 93 | Weberian ideal type + Bayesian + myth |
| `tactics.poml` | 239 | De Certeau concordance extraction |
| `parody.poml` | 280 | POML→POML forge for parody essays |
| `parody-gen.poml` | 62 | Light parody prompt generator |
| `inverse-essay.poml` | 47 | Essay reversal + myth layer |
| `prompt.poml` | 184 | Natural language → POML transformer |
| `recursive.poml` | 72 | Recursive prompt generation engine |
| `meta-prime.poml` | 46 | Author OS → prompt logic extractor |

**Total**: 1,374 lines of structured prompt infrastructure.

---

*This library represents one mode of sophisticated AI collaboration: building prompts that generate prompts, extracting reusable patterns, and creating infrastructures for future work.*

**Credits**: Watson Hartsoe · LMC-6650 Project Studio · Fall 2025
