# Citation Map: POML (Prompt Orchestration Markup Language)
## Placing 23 Sources on the Project Landscape

**Date:** December 10, 2025  
**Purpose:** Map POML literature to the project's **18 existing POML operators**

---

## THE BINDING THESIS

> "POML redefines the prompt as a hierarchical document, solving the 'context soup' problem of early LLM development."

This **IS** what the project's 18 POML files already do. The Microsoft POML paper (August 2025) provides academic validation for the pattern this project discovered through practice.

---

## PROJECT'S POML LIBRARY (Pre-existing Implementation)

| POML File | Size | Function | Maps to POML Concept |
|-----------|------|----------|---------------------|
| `sinter.poml` | 16,965 bytes | Compress multiple sources | `<task>` + `<document>` |
| `anneal.poml` | 15,230 bytes | Iterative refinement | Control flow (`<if>`, `<for>`) |
| `furnace.poml` | 15,017 bytes | High-heat transformation | `<role>` + intensive `<task>` |
| `forage.poml` | 14,453 bytes | Search and gather | `<document src="">` pattern |
| `forensic.poml` | 13,457 bytes | Deep artifact analysis | `<role>` as specialist |
| `forge.poml` | 13,892 bytes | Construct new artifacts | `<output-format>` |
| `guardian.poml` | 12,842 bytes | Protect invariants | `<stylesheet>` constraints |
| `upgrade.poml` | 11,777 bytes | Improve existing systems | `<example>` + diff output |
| `tactics.poml` | 10,191 bytes | Strategic sequencing | Control flow logic |
| `parody.poml` | 9,475 bytes | Humor as analysis | `<role>` persona shift |
| `citation-hunt.poml` | 22,426 bytes | Citation forensics | `<document>` + validation |
| `legos-cognitive-architect-v8.poml` | 6,300 bytes | LEGOS framework | Modular `<task>` composition |
| `prompt.poml` | 5,968 bytes | Basic operator | Core `<role>`/`<task>` |
| `mythos.poml` | 3,209 bytes | Narrative extraction | `<example>` story patterns |
| `parody-gen.poml` | 2,325 bytes | Parody generation | `<output-format>` |
| `recursive.poml` | 2,318 bytes | Self-referential analysis | Nested templates |
| `meta-prime.poml` | 2,020 bytes | Meta-prompt template | Base pattern |
| `inverse-essay.poml` | 1,377 bytes | Argument inversion | `<task>` transformation |

**Total: ~200KB of POML operators developed BEFORE the Microsoft paper.**

---

## CITATION → PROJECT MAPPING

### TIER 1: CORE POML SPECIFICATION

| # | Citation | Concept | Maps To | Project File |
|---|----------|---------|---------|--------------|
| 2, 11 | arXiv:2508.13948 | POML white paper, component taxonomy | **ALL 18 POML files** | `poml-library-pyramid.md` |
| 9 | microsoft/poml GitHub | Reference implementation | **Validation** | all `.poml` files |
| 3 | Emergent Mind | Semantic Componentization | `<role>`, `<task>`, `<example>` | decomposition |
| 16 | POML Docs — Components | Tag specifications | Implementation reference | technical |

**Key Quote to Place:**
> "By isolating the persona, the POML engine can treat this information differently during execution... ensuring the persona definition is 'sticky' and resists 'catastrophic forgetting'."

**Place in:** `poml-library-pyramid.md` → Mechanism section

---

### TIER 2: STYLESHEETS AND DECOUPLING (NSP Connection)

| # | Citation | Concept | Maps To | Project File |
|---|----------|---------|---------|--------------|
| 13 | POML Docs — Stylesheets | Content/Presentation decoupling | **Void Management** | thesis connection |
| 14 | Reddit — LocalLLaMA | "Markup Programming Language" | Hybrid paradigm | technical debate |
| 21 | Towards Data Science | Declarative vs Imperative | What vs How | design philosophy |

**Key Quote to Place:**
> "The separation of content (Intent) from presentation (Style) allows for cross-model portability."

**This IS the bounded structure / variable content principle!**
- Fixed POML structure = bounded possibility space
- Variable model/parameters = flexible instantiation

---

### TIER 2.5: SOFT-TOKEN STRUCTURALISM ↔ WONG'S SOFT RESISTANCE

This is the critical theoretical bridge.

#### The Connection

| Concept | Source | Manifestation |
|---------|--------|---------------|
| **Soft-Token Tags** | POML/ICL Markup (Citation #15) | Structured tags reduce arbitrary decisions |
| **Soft Resistance** | Wong (2021) — already in verified refs | Subtle tactics to subvert organizational practices |
| **Narrative Structuralism** | DH literary theory | Text as system of functional components |

#### The Argument

Wong's "Tactics of Soft Resistance" identifies three strategies for ethics practitioners:
1. **Creating space** for UX expertise to address values
2. **Making values visible** to organizational stakeholders  
3. **Changing organizational processes** toward values

**POML operationalizes all three for DH scholars:**

| Wong Tactic | POML Implementation |
|-------------|---------------------|
| Creating space | Modular `<task>` imports create space for multiple perspectives |
| Making visible | XML structure makes analytical framework explicit and inspectable |
| Changing processes | Version control + reproducibility transforms "chatting" into systematic inquiry |

#### The Generalist-Specialist Architecture

```xml
<!-- ROOT: Generalist Historical Context -->
<poml>
  <role>
    You are a literary scholar specializing in 19th-century British novels.
    You understand the historical, economic, and social context of the Victorian era.
  </role>
  
  <!-- IMPORT: Specialist Task Modules -->
  <import src="perspectives/marxist.poml" />
  <import src="perspectives/feminist.poml" />
  <import src="perspectives/postcolonial.poml" />
  
  <task>
    Analyze the provided passage through EACH imported perspective.
    Maintain the Generalist context while applying Specialist lenses.
  </task>
  
  <document src="dickens_passage.txt" />
</poml>
```

**perspectives/marxist.poml:**
```xml
<poml>
  <role>Marxist literary critic following Eagleton and Jameson</role>
  <task>
    Identify class relations, labor conditions, commodity fetishism.
    Locate ideological contradictions in the text's representation of capital.
  </task>
  <example>
    <input>Scene of factory workers in Hard Times</input>
    <output>
      Dickens exposes the alienation of labor while simultaneously 
      naturalizing bourgeois philanthropy as the solution...
    </output>
  </example>
</poml>
```

**perspectives/feminist.poml:**
```xml
<poml>
  <role>Feminist literary critic following Gilbert, Gubar, and Spivak</role>
  <task>
    Analyze gender performance, domestic ideology, the "angel in the house."
    Identify moments of resistance or complicity in patriarchal structures.
  </task>
</poml>
```

#### Why This Matters for DH

| Before POML | After POML |
|-------------|------------|
| "Chat" with archive | **Query** archive with structured methodology |
| Ad-hoc prompting | **Reproducible** analytical framework |
| Individual interpretation | **Collaborative** perspective modules |
| Opaque reasoning | **Version-controlled** intellectual history |
| "Vibe-based" analysis | **Peer-reviewed** task definitions |

#### The Soft Resistance Connection

Wong's insight: practitioners resist through structure, not confrontation.

**POML enables scholarly soft resistance:**
- The XML structure **forces** methodological transparency
- Importing multiple perspectives **mandates** pluralism
- Version control **documents** interpretive evolution
- The format itself **embodies** the values of rigor and openness

> "These tactics are often subtle attempts to subvert or change existing practices and organizational structures towards more values-conscious ends." — Wong (2021)

POML is a **structural tactic** for subverting the "black box" of LLM-assisted literary analysis.

#### Key Quote to Add

From POML paper (Citation #15 - ICL Markup):
> "Research in 'ICL Markup' suggests that using 'soft-token tags' helps to compose prompt templates that reduce arbitrary decisions."

**This reduces arbitrary interpretive decisions by structuring them.**

---

### TIER 3: ECOSYSTEM AND TOOLING

| # | Citation | Concept | Maps To | Project File |
|---|----------|---------|---------|--------------|
| 17 | iberi22/POML-MCP | MCP server integration | **Agent orchestration** | future integration |
| 18 | GhennadiiMir/poml-ruby | Cross-language implementation | Portability validation | ecosystem |
| 10 | Socket.dev — pomljs | Security analysis (Shai-Hulud) | Risk awareness | security |
| 5 | HuggingFace Papers | LangChain critique ("heavy") | Why POML is simpler | positioning |

**Key Quote to Place:**
> "The poml-mcp server allows an AI agent to 'discover' POML templates as tools. An agent can query the server, find a 'Summarize' POML template, and execute it."

**Future integration:** Could expose project's 18 POML operators via MCP.

---

### TIER 4: THEORETICAL FOUNDATIONS

| # | Citation | Concept | Maps To | Project File |
|---|----------|---------|---------|--------------|
| 6-8 | Nan Chen papers | Content-Format Integration, VIDEE | HCI lineage | `context-engineering-pyramid.md` |
| 15 | HuggingFace — ICL Markup | Soft-token tags, Generalist-Specialist | Modular composition | `poml-library-pyramid.md` |
| 4 | Scribd — POML Revolution | Context organization | Attention management | `context-as-material-pyramid.md` |

**Key Quote to Place:**
> "There was no semantic way to tell the model that this block of text was a high-priority instruction while that block was low-priority background data."

**This is the "Lost in the Middle" problem** — POML solves via structure.

---

### TIER 5: CRITICAL RECEPTION

| # | Citation | Concept | Maps To | Project File |
|---|----------|---------|---------|--------------|
| 19-20 | Reddit / Hacker News | "Reinvention of XML" critique | Counter-argument | balanced view |
| 12 | Reddit — PromptEngineering | Community debate | Real-world reception | adoption |
| 23 | Sean Wu — Medium | Three ways to program LLMs | POML positioning | alternatives |

**Key Debate to Document:**
- **Minimalists:** "Why not just use Markdown?"
- **Structuralists:** "Markdown describes formatting, not semantics. For enterprise reliability, XML tags provide semantic precision."

---

## POML ↔ PROJECT EQUIVALENCE TABLE

| POML Concept | Paper Definition | Project Implementation |
|--------------|------------------|------------------------|
| `<role>` | Persona definition | Every `.poml` file header |
| `<task>` | Teleological goal | Primary operator function |
| `<example>` | Few-shot demonstration | Pattern matching in `mythos.poml` |
| `<document src="">` | External file reference | `forage.poml` gathering |
| `<table>` | Structured data | Analysis outputs |
| `<stylesheet>` | Format control | `guardian.poml` constraints |
| `<if>/<for>` | Control flow | `anneal.poml` iterative logic |
| `<output-format>` | Directorial note | `forge.poml` construction |

**The project's POML library IS a working implementation of the Microsoft POML specification, developed independently and earlier.**

---

## ACE ↔ POML CONNECTION

The Stanford/SambaNova ACE paper (already in `citation-map-context-material.md`) defines three roles:

| ACE Role | Function | Project POML Operator |
|----------|----------|----------------------|
| **Generator** | Attempts task, produces traces | `forge.poml`, `prompt.poml` |
| **Reflector** | Analyzes output, distills lessons | `forensic.poml`, `sinter.poml` |
| **Curator** | Edits playbook, manages context | `guardian.poml`, `upgrade.poml` |

**The 18 POML operators ARE the ACE architecture operationalized.**

---

## CITATIONS TO ADD TO verified-references.md

### Tier 1: PRIMARY SOURCES (Must Add)

```
Zhang, Y., Chen, N., Xu, J., & Yang, Y. (2025). Prompt Orchestration 
    Markup Language. arXiv:2508.13948.
https://arxiv.org/abs/2508.13948

Microsoft. (2025). POML [GitHub repository].
https://github.com/microsoft/poml

Microsoft. (2025). POML Documentation.
https://microsoft.github.io/poml/latest/
```

### Tier 2: ECOSYSTEM (Should Add)

```
Iberi22. (2025). POML-MCP: MCP server for POML templates.
https://github.com/iberi22/POML-MCP

Socket.dev. (2025). pomljs Security Analysis.
https://socket.dev/npm/package/pomljs
```

### Tier 3: THEORETICAL (Nice to Have)

```
Chen, N. (2024). Beyond Prompt Content: Enhancing LLM Performance 
    via Content-Format Integrated Prompt Optimization.
https://www.researchgate.net/publication/388792075

Declarative and Imperative Prompt Engineering for Generative AI.
    Towards Data Science.
https://towardsdatascience.com/declarative-and-imperative-prompt-engineering-for-generative-ai/
```

---

## THE POML ARCHITECTURE DIAGRAM

```
                    POML DOCUMENT
                         │
         ┌───────────────┼───────────────┐
         │               │               │
    INTENTION        DATA         PRESENTATION
         │               │               │
    ┌────┴────┐    ┌────┴────┐    ┌────┴────┐
    │ <role>  │    │<document>│    │<style> │
    │ <task>  │    │ <table>  │    │ sheet  │
    │<example>│    │  <img>   │    │        │
    └────┬────┘    └────┬────┘    └────┬────┘
         │               │               │
         └───────────────┼───────────────┘
                         │
                    TEMPLATING
                         │
                    ┌────┴────┐
                    │  <if>   │
                    │  <for>  │
                    │  <let>  │
                    └────┬────┘
                         │
                    RENDERED
                    PROMPT
```

---

## CONNECTION TO NSP THESIS

POML **IS** Negative Space Programming for prompts:

| NSP Concept | POML Manifestation |
|-------------|-------------------|
| **Invalid states unrepresentable** | Schema validation (invalid tags rejected) |
| **Types as constraints** | `<role>`, `<task>`, `<example>` = semantic types |
| **Correctness by construction** | Structured document → correct prompt |
| **Ghost evidence** | No "spaghetti prompting" (deleted) |
| **Bounded structure** | Fixed tag vocabulary |
| **Variable content** | Infinite instantiation within tags |

**POML eliminates the "context soup" failure mode by making it structurally impossible.**

---

## KNOWLEDGE GAPS IDENTIFIED

### Critical (Research Needed)

1. **POML → project POML mapping** — Formal conversion of `.poml` files to Microsoft POML spec
2. **MCP server for project operators** — Expose 18 operators as discoverable tools
3. **Benchmark comparison** — Test project operators against POML examples

### Moderate (Nice to Have)

4. **Security audit** — Review project `.poml` files for injection risks
5. **Cross-model testing** — Validate operators across GPT-4, Claude, Gemini
6. **Stylesheet extraction** — Formalize implicit formatting as explicit stylesheets

---

## ACTION ITEMS

### Immediate
- [ ] Add Microsoft POML paper to `verified-references.md`
- [ ] Update `poml-library-pyramid.md` with POML literature validation
- [ ] Cross-reference ACE (Generator/Reflector/Curator) with specific operators

### Short-term
- [ ] Create formal mapping: project operator → POML tag
- [ ] Explore MCP integration for operator discoverability

### Long-term
- [ ] Propose project operators as contributions to POML ecosystem
- [ ] Develop `poml.html` visualization of operator library

---

*This document validates the project's 18 POML operators against the academic literature. The project discovered the pattern through practice; the Microsoft paper provides theoretical legitimacy.*
