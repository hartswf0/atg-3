# CONTEXT ENGINEERING GENEALOGY
## Intellectual History for Void Management Thesis

---

```
═══════════════════════════════════════════════════════════════════════════════
FROM THICK DESCRIPTION TO VOID ARCHITECTURE
A genealogy tracing context engineering from anthropology to LLM collaboration
═══════════════════════════════════════════════════════════════════════════════
```

---

## Part I: Conceptual Foundations

### 1.1 Thick Description (Geertz, 1973)

**SOURCE:** Geertz, C. (1973). *The Interpretation of Cultures*. Basic Books.

**KEY CONCEPT:** Thick description vs thin description
- Thin: "He winked"
- Thick: "He winked conspiratorially to signal irony about the authority figure"

**THESIS TRANSLATION:**
- Scene management = thin description (accumulate tokens without interpretive frame)
- Void management = thick description (structure that makes meaning possible)
- The void provides the interpretive frame; instantiation provides the particulars

**QUOTABLE:**
> "Culture is not a power, something to which social events, behaviors, institutions, or processes can be causally attributed; it is a context, something within which they can be intelligibly described." (p. 14)

---

### 1.2 Situated Action (Suchman, 1987)

**SOURCE:** Suchman, L. (1987). *Plans and Situated Actions*. Cambridge University Press.

**KEY CONCEPT:** Plans as resources, not determinants
- Traditional AI: plan specifies action sequence
- Situated action: plans are resources for improvisation
- Action emerges from circumstances, not from plan execution

**THESIS TRANSLATION:**
- Scene = the plan that tries to determine all subsequent action
- Void = the resource that enables situated response
- Scene management fails like planning fails: circumstances exceed specification

**QUOTABLE:**
> "However detailed a plan, action is never fully representable... The plan is inevitably incomplete with respect to essential details of situated action."

---

### 1.3 Material-Semiotic Analysis (Latour, 1980s-2000s)

**SOURCE:** Latour, B. (1987). *Science in Action*. Harvard University Press.
**SOURCE:** Latour, B. (2005). *Reassembling the Social*. Oxford University Press.

**KEY CONCEPTS:**
- Inscription: making durable traces
- Black-boxing: rendering technical content invisible
- Immutable mobiles: artifacts that travel without distortion

**THESIS TRANSLATION:**
- Scene = black-boxed AI contribution (labor hidden)
- Void = inscription device (makes structure visible and mobile)
- `disc-data.json` = immutable mobile (exports without local dependencies)

**QUOTABLE:**
> "Give me a laboratory and I will raise the world." (Latour, 1983)
> Translation: Give me a void architecture and I will export meaning.

---

### 1.4 Situated Knowledges (Haraway, 1988)

**SOURCE:** Haraway, D. (1988). Situated Knowledges: The Science Question in Feminism and the Privilege of Partial Perspective. *Feminist Studies, 14*(3), 575–599.

**KEY CONCEPT:** Vision is always embodied and positioned
- No "view from nowhere"
- Objectivity as partial, locatable perspective
- Accountability for where you stand

**THESIS TRANSLATION:**
- Scene management claims false neutrality (LLM generates "objectively")
- Void management makes position explicit (constraints are visible)
- The void names itself as a position, not a universal

**QUOTABLE:**
> "The moral is simple: only partial perspective promises objective vision." (p. 583)

---

### 1.5 Reflection-in-Action (Schön, 1983)

**SOURCE:** Schön, D. (1983). *The Reflective Practitioner*. Basic Books.

**KEY CONCEPT:** Professional practice as "conversation with the situation"
- Technical rationality fails for complex problems
- Practitioners reflect-in-action, not just apply rules
- Each situation reframes the problem

**THESIS TRANSLATION:**
- Scene management = technical rationality (apply rules to accumulated context)
- Void management = reflective practice (conversation with possibility space)
- Each instantiation is a reflection-in-action, not a rule application

**QUOTABLE:**
> "When someone reflects-in-action, he becomes a researcher in the practice context. He is not dependent on the categories of established theory and technique..."

---

### 1.6 Interpretation and Context (Dreyfus, 1972/1992)

**SOURCE:** Dreyfus, H. (1972/1992). *What Computers Can't Do* / *What Computers Still Can't Do*. MIT Press.

**KEY CONCEPT:** The frame problem
- AI systems can't determine what's relevant
- Context is unbounded; rules can't capture it
- Background understanding enables interpretation

**THESIS TRANSLATION:**
- Scene management suffers the frame problem (what context is relevant?)
- Void management solves it by bounding the frame explicitly
- The void's dimensions ARE the relevance criteria

**QUOTABLE:**
> "The problem of relevance... is not being solved; it is being swept under the rug."

---

## Part II: Architectural Metaphors

### 2.1 Cognitive Mapping (Lynch, 1960)

**SOURCE:** Lynch, K. (1960). *The Image of the City*. MIT Press.

**KEY ELEMENTS:**
1. Paths — channels of movement
2. Edges — boundaries between regions
3. Districts — areas with common character
4. Nodes — strategic foci
5. Landmarks — external reference points

**THESIS TRANSLATION:**
The 9×9 void grid implements Lynch's five elements:
- Paths = morphisms connecting entities
- Edges = zone boundaries (inner ring, outer ring)
- Districts = zones with semantic character
- Nodes = entities at strategic positions
- Landmarks = anchor objects that orient

**DESIGN PRINCIPLE:**
Voids are cognitively mappable. Scenes become cognitively unmappable as they accumulate.

---

### 2.2 Pattern Language (Alexander, 1977)

**SOURCE:** Alexander, C. (1977). *A Pattern Language*. Oxford University Press.

**KEY CONCEPT:** Generative grammar for design
- Patterns = reusable solutions to recurring problems
- Patterns compose into languages
- Languages generate infinite buildings from finite patterns

**THESIS TRANSLATION:**
- Pattern = named void with activation conditions
- Pattern language = system of composable voids
- The void IS a pattern: it solves the problem "how to enable action without specifying content"

**QUOTABLE:**
> "Each pattern describes a problem which occurs over and over again... and then describes the core of the solution to that problem, in such a way that you can use this solution a million times over." (p. x)

---

### 2.3 Information Architecture (Rosenfeld & Morville, 1998)

**SOURCE:** Rosenfeld, L. & Morville, P. (1998). *Information Architecture for the World Wide Web*. O'Reilly.

**KEY FRAMEWORK:**
- Organization systems (how we categorize)
- Labeling systems (how we name)
- Navigation systems (how we browse)
- Search systems (how we query)

**THESIS TRANSLATION:**
POML implements information architecture for prompts:
- Organization: `<role>`, `<task>`, `<rules>` structure
- Labeling: semantic markup tags
- Navigation: call hierarchy and includes
- Search: targeted sub-prompts

Void management = information architecture for AI collaboration

---

## Part III: Contemporary Context Engineering

### 3.1 Karpathy's Reframing (2025)

**SOURCE:** Karpathy, A. (2025, February 2). X post on context engineering.

**KEY CLAIM:**
> "The hottest new programming language is English... and the art of programming in English is 'context engineering.' I think this is a better term than 'prompt engineering.'"

**THESIS TRANSLATION:**
- Prompt engineering = crafting individual queries (scene-first)
- Context engineering = designing the context window (void-first)
- Void management is a specific theory of context engineering

---

### 3.2 Simon Willison's Elaboration (2025)

**SOURCE:** Willison, S. (2025). Context Engineering. *simonwillison.net*.

**KEY FRAMEWORK:**
> "Context engineering is about creating the optimal context—the input—for the model to succeed at performing a given task."

Components:
- System prompts
- Retrieved content (RAG)
- Conversation history
- Tool outputs
- Structured data

**THESIS TRANSLATION:**
Willison describes WHAT (context components). 
Thesis provides HOW (void management architecture).
All Willison's components are void-definable.

---

### 3.3 Anthropic's Context Patterns (2025)

**SOURCE:** Anthropic. (2025). *Building effective agents*. docs.anthropic.com

**KEY PATTERNS:**
1. **Context rot** — accumulated context degrades performance
2. **Context compaction** — summarize history to maintain relevance
3. **Structured note-taking** — agents maintain scratchpads

**THESIS TRANSLATION:**
- Context rot = scene management failure (thesis predicted this)
- Context compaction = implicit void management (reduce to structure)
- Scratchpads = externalized void (bounded possibility space)

**QUOTABLE:**
> "Even 'perfect memory' models experience a phenomenon called 'distraction'—too much irrelevant context degrades performance."

---

### 3.4 Model Context Protocol (2024)

**SOURCE:** Anthropic. (2024). *Model Context Protocol*. modelcontextprotocol.io

**KEY CONCEPT:** Standardized protocol for context integration
- Resources: external data sources
- Tools: executable capabilities
- Prompts: reusable templates

**THESIS TRANSLATION:**
MCP is plumbing for void management:
- Resources = potential void content
- Tools = instantiation capabilities
- Prompts = void specifications
The protocol enables voids to receive external input.

---

### 3.5 Survey of Context Engineering (Mei et al., 2025)

**SOURCE:** Mei, K., et al. (2025). Context Engineering for AI Agents. arXiv.

**KEY TAXONOMY:**
1. Writing context (system prompts, task instructions)
2. Selecting context (memory retrieval, RAG)
3. Compressing context (summarization, pruning)
4. Isolating context (sandboxing, modular agents)
5. Updating context (tool output integration)

**THESIS TRANSLATION:**
| Mei et al. Category | Void Management Equivalent |
|---------------------|---------------------------|
| Writing context | Void specification (POML) |
| Selecting context | Void instantiation triggers |
| Compressing context | Scene → void reduction |
| Isolating context | Void boundaries |
| Updating context | Void state transitions |

---

## Part IV: Integration with Void Management

### 4.1 The Synthesis

Context engineering is the practice. Void management is a specific theory within that practice.

| Level | Contribution | Source |
|-------|--------------|--------|
| **Epistemology** | Context as interpretive frame | Geertz |
| **Ontology** | Context is material, not just information | Latour |
| **Agency** | Plans as resources, not determinants | Suchman |
| **Architecture** | Bounded possibility spaces | Alexander |
| **Implementation** | Context window curation | Karpathy, Willison |
| **Mechanism** | Void/scene distinction | *This thesis* |

### 4.2 What Void Management Adds

Prior work describes WHAT (engineer context) and WHY (context matters).
Void management provides:
1. **MECHANISM:** Why scene fails, why void works
2. **FALSIFIABILITY:** Testable predictions
3. **ARCHITECTURE:** Specific void patterns
4. **EXPORT:** Void structures serialize

### 4.3 The Steel (Reforged)

> Context engineering tells us to curate the context window.
> Void management tells us HOW: bound the possibility space, let users instantiate.
> The void is context architecture; the scene is context accumulation.
> Architecture scales; accumulation collapses.

---

## Part V: Additional Citations

### 5.1 Complementary Readings

| Author | Work | Contribution |
|--------|------|--------------|
| **Garfinkel** (1967) | *Studies in Ethnomethodology* | Practical accomplishment of order |
| **Lave & Wenger** (1991) | *Situated Learning* | Learning as participation |
| **Hutchins** (1995) | *Cognition in the Wild* | Distributed cognition |
| **Bowker & Star** (1999) | *Sorting Things Out* | Infrastructure visibility |
| **Jackson** (2014) | "Rethinking Repair" | Maintenance as knowledge work |

### 5.2 Contemporary Prompt Research

| Author | Work | Contribution |
|--------|------|--------------|
| **Zhou et al.** (2023) | LEAST-TO-MOST Prompting | Hierarchical decomposition |
| **Beurer-Kellner** (2024) | LMQL | Programmatic prompt construction |
| **Khattab et al.** (2023) | DSPy | Compiling prompts |
| **Zhu et al.** (2023) | PromptBench | Prompt robustness evaluation |

---

## Appendix: Full Bibliography

### Classical

1. Alexander, C. (1977). *A Pattern Language*. Oxford University Press.
2. Dreyfus, H. (1992). *What Computers Still Can't Do*. MIT Press.
3. Garfinkel, H. (1967). *Studies in Ethnomethodology*. Prentice-Hall.
4. Geertz, C. (1973). *The Interpretation of Cultures*. Basic Books.
5. Haraway, D. (1988). Situated Knowledges. *Feminist Studies*, 14(3).
6. Latour, B. (1987). *Science in Action*. Harvard University Press.
7. Latour, B. (2005). *Reassembling the Social*. Oxford University Press.
8. Lynch, K. (1960). *The Image of the City*. MIT Press.
9. Schön, D. (1983). *The Reflective Practitioner*. Basic Books.
10. Suchman, L. (1987). *Plans and Situated Actions*. Cambridge University Press.

### Contemporary Context Engineering

11. Anthropic. (2024). Model Context Protocol. modelcontextprotocol.io
12. Anthropic. (2025). Building effective agents. docs.anthropic.com
13. Karpathy, A. (2025, February 2). X post on context engineering.
14. Mei, K., et al. (2025). Context Engineering for AI Agents. arXiv.
15. Willison, S. (2025). Context Engineering. simonwillison.net

### Prompt Engineering

16. Beurer-Kellner, L. (2024). LMQL: Declarative LLM Queries.
17. Khattab, O., et al. (2023). DSPy: Compiling Declarative Language Programs. arXiv.
18. Zhou, D., et al. (2023). Least-to-Most Prompting. ICLR 2023.
19. Zhu, K., et al. (2023). PromptBench. arXiv.

---

*Genealogy compiled December 2025.*
