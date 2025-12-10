# Flatness is Discipline: What 150 Hours of Failed LLM Collaboration Taught Me About Managing Generative AI

**Hart Schwartz**  
Georgia Institute of Technology  
LMC-6650: Computing, Ethics, & Society  
December 2025

---

## Abstract

After 150 hours of collaborative work with large language models, I discovered a practical distinction that changed everything: don't ask the LLM to build the thing (scene management); ask it to prepare the space where you build (void management). 

This paper reports on a semester-long design research project that collapsed, pivoted, and eventually crystallized around this insight. The evidence is experiential, not experimental: one practitioner's journey from generative sprawl to exportable structures. The theoretical connections—to Suchman's situated action, Scott's legibility, contemporary context engineering—are offered as resonances, not claims to extension. The contribution is modest but potent: a heuristic for LLM collaboration that explains why long conversations degrade and suggests what to do about it.

**Keywords:** Context Engineering, Human-AI Collaboration, Prompt Engineering, Design Research, Practitioner Reflection

---

## 1. The Failure That Taught Me

TILTH was supposed to be brilliant. A speculative company called Agronica—an AI-powered agricultural platform—with every artifact you'd find in a real organization. Role decks mapping employee archetypes. Personas with documented biases. Negotiation simulations for ethics training. Tetrads structuring scenario logic. Prompt operators functioning as neurosymbolic controllers. Quizzes, intro videos, leaked fake documents providing narrative depth.

I used Claude and GPT to generate all of it. Layer upon layer. Each generation coherent in isolation. Session after session, the world grew richer.

Then it collapsed.

Not dramatically—gradually. I entered what I now call **complexity grey**: a zone where brokenness and design pathways become indistinguishable. Was the inconsistency in Role Deck 3 a bug or a feature? Did the leaked memo contradict the persona document, or was that intentional unreliable narration? I couldn't tell. The system's liability exceeded its asset value. Every edit required holding the entire accumulated world in mind. TILTH sprawled across index files and nested hyperlinks until finishing it became impossible.

This is the experience that grounded the insight. Not a theoretical derivation—a felt collapse.

---

## 2. The Discovery: Complexity Accumulates Faster Than Coherence

Looking back at TILTH's failure, the pattern was clear:

**Each LLM response added content.** A new persona meant checking against existing personas. A new scenario meant ensuring consistency with established lore. A new prompt operator meant verifying it didn't break existing ones.

**Complexity grew exponentially; coherence grew linearly at best.** The accumulated context demanded more cognitive work to maintain than new content was worth. Eventually, adding anything made the whole harder, not richer.

**There was no clean state to return to.** Unlike version control for code, there was no way to "revert" the generative sprawl. The LLM's outputs had become my constraints.

This is the first half of the insight: **Scene management fails because complexity accumulates faster than coherence can maintain.**

I was asking the LLM to construct a world. The LLM obliged. I drowned in the world it built.

---

## 3. The Pivot: Empty Structures That Stay Fixed

The solution emerged from constraint. I needed a tool that worked on a phone—no desktop sprawl, no nested menus, no accumulated complexity. That constraint alone eliminated most of what TILTH had become.

What survived was a substrate: a 9×9 grid. Fixed dimensions. Empty cells. Tetrad operators (Enhance, Obsolesce, Retrieve, Reverse) as transformation vocabulary. A chat layer for interaction. Nothing more.

I called it **Thousand-Tetrad**. And it worked.

| TILTH (Failed) | Thousand-Tetrad (Worked) |
|----------------|--------------------------|
| LLM generated content | LLM suggested dimensions |
| Each session added to accumulated world | Each session filled empty cells |
| Context required to modify anything | Cells independent of each other |
| Heavy, slow, unmaintainable | Light, fast, exportable |
| Could only work with this specific content | Works with any content poured in |

The difference wasn't technical sophistication. Thousand-Tetrad is *simpler* than TILTH. The difference was what the LLM was asked to do.

In TILTH, the LLM managed the **scene**: constructing specific content, positions, relationships, embedded assumptions. In Thousand-Tetrad, the LLM managed the **void**: preparing empty structure with defined dimensions, transformation options, no content until I added it.

This is the second half of the insight: **Void management works because complexity stays with the user who owns it.**

---

## 4. What I Mean by "Void" and "Scene"

These aren't theoretical constructs. They're descriptions of what I experienced.

**Scene:** A cumulative representation where everything is entangled. Modifying persona X requires checking relationships with personas Y and Z. Adding scenario 7 requires verifying consistency with scenarios 1-6. The LLM constructed this; I'm now trapped inside it.

**Void:** A bounded possibility space with fixed dimensions and empty slots. The 9×9 grid has 81 cells. Each cell is independent. Filling cell (3,5) doesn't require understanding cell (7,2). The LLM prepared this; I navigate freely within it.

The metaphor that helped me: 

> **Scene is furniture arrangement.** The LLM placed everything; I live in the room it designed.
> 
> **Void is blueprint.** The LLM drew the walls and marked the outlets; I furnish it myself.

---

## 5. Evidence from Practice (Not Experiment)

I want to be honest about what kind of evidence I have.

### What I Have

**One practitioner's experience** across 150+ hours. TILTH failed. Thousand-Tetrad worked. The transition correlated with the shift from scene to void. This is genuine evidence, but it's not controlled.

**Cross-project observation.** The pattern held when applied elsewhere:
- Privacy Value Labels (14 dimensions = void, user fills with specific flows)
- Role Deck (Bartle taxonomy = void, user maps their organization)
- Func-Sub collaborations worked better when I shared prompt guides (void) instead of full projects (scene)

**Failure-success pairs.** HOLO started as scene management (real-time LLM 3D construction) and failed. It pivoted to void management (prebaked disc-data.json) and worked. The transition tracks the insight.

### What I Don't Have

**Controlled experiments.** I didn't randomly assign tasks to scene vs. void conditions.

**Multiple practitioners.** This is my experience, not a study of others.

**Falsification testing.** I haven't systematically sought counterexamples.

The claim is practitioner-grade, not science-grade. It's useful if you're doing LLM collaboration; whether it's *true* in some deeper sense remains open.

---

## 6. Resonances (Not Extensions)

The insight connects to existing theoretical work. I want to name these connections honestly—as resonances, not as claims that I'm extending or grounding these theories.

### Suchman's Situated Action

Lucy Suchman argued that plans don't determine action—they're resources for action. You don't execute a plan; you improvise with it.

**Resonance:** Scene management is like assuming the plan will execute. Void management treats the structure as a resource for improvisation.

I'm not claiming to extend Suchman. I'm noticing that her 1987 insight about plans and action maps onto something I experienced with LLMs in 2025.

### Scott's Legibility

James Scott analyzed "high modernist" failures: states imposing abstract grids onto local realities, destroying the practical knowledge (mētis) that made places work.

**Resonance:** Scene management imposes the LLM's abstractions. Void management preserves space for my situated judgment.

Again—resonance, not extension. TILTH failed like a high-modernist scheme, but I'm not claiming to theorize state formation.

### Context Engineering

Andrej Karpathy recently popularized "context engineering" to describe the architectural management of what enters an LLM's context window.

**Resonance:** Void management is one strategy for context engineering. Keep the structure; manage what content enters the structure.

This is the most direct connection. What I discovered experientially, practitioners are beginning to name.

---

## 7. The Practical Heuristic

If the theory is uncertain, the practice is simple:

### When Starting LLM Collaboration, Ask

> "Am I asking the LLM to construct content for me to navigate? Or am I asking the LLM to prepare structure for me to fill?"

If the former, expect degradation over long conversations. If the latter, expect sustainability.

### When Collaboration Degrades, Try

> "Can I extract the structure from what's been built and discard the specific content? Can I convert accumulated scene to empty void?"

This often works. Summarize the dimensions of the world, not the world itself. Keep the axes; throw away the points.

### When Sharing with Collaborators

> "Am I handing them my scene (overwhelming) or a void (they fill with their context)?"

Prompt guides shared better than project exports. Template structures shared better than completed outputs.

---

## 8. The Export Problem

There's a practical consequence I didn't anticipate: export.

Scene-managed outputs **die with the session**. TILTH's world couldn't be meaningfully shared. It required my accumulated context to navigate. Without that context, it was an incoherent pile of documents.

Void-managed outputs **travel independently**. The 9×9 grid, the disc-data.json format, the POML prompt templates—these are structures that other people can fill. They don't require my context; they provide context for you.

> **Scene is session-bound. Void is exportable.**

This matters for collaboration. If I want others to use my work, I need to give them voids, not scenes.

---

## 9. Limitations and Honest Uncertainty

### What I Don't Know

**Is this generalizable?** My work was creative/design-oriented. Does the distinction hold for code generation, analysis, writing, other domains?

**Is there a middle?** I've described scene and void as binary. Maybe there's a useful hybrid I haven't discovered.

**Are there successful scene managers?** Maybe some practitioners can maintain coherence through accumulated complexity in ways I couldn't. My failure might be my limited capacity, not a universal constraint.

**Would this replicate?** I don't know if other practitioners would have the same experience.

### What I'm Confident About

**The heuristic is useful.** Even if the theory is wrong, asking "scene or void?" before starting LLM collaboration has practical value.

**TILTH failed and Thousand-Tetrad worked.** That's observed, not speculated.

**The transition mattered.** Something changed when I shifted from "build me a world" to "give me a grid to fill."

---

## 10. Conclusion: Flatness is Discipline

TILTH failed because it sprawled. Thousand-Tetrad works because it stays flat.

This is not a preference for simplicity over sophistication. It's an observation about where complexity should live. In scene management, complexity lives in the LLM's outputs—and I drown. In void management, complexity lives in my choices to fill the void—and I swim.

> **Flatness is not poverty. Flatness is discipline.**

The 9×9 grid is richer than TILTH because it can support any content. TILTH was poorer despite its accumulation because it could only support its specific content.

The practical takeaway: when working with LLMs, prefer structures to contents. Prefer dimensions to instances. Prefer empty grids to populated worlds.

Let the LLM manage the void. Let yourself fill it.

---

## Generative AI Disclosure

This paper was developed through sustained collaboration with Claude and Gemini across 150+ hours. The AI did not write this paper; it participated in the experiences I describe. The failure of TILTH was a failure with AI. The success of Thousand-Tetrad was a success with AI.

The relationship resists itemization. I cannot list "which sections were AI-generated" because the distinction between human and AI contribution dissolved over extended collaboration. What I can say: the judgment—what mattered, what to pursue, what to abandon—remained mine. The AI prepared possibilities; I made choices.

This disclosure performs what I critique: the ACM framework assumes scene-based AI use (discrete, enumerable transactions). My use was void-based (structure prepared, instances chosen over time). The framework cannot capture this without distortion.

The POML library (1,300+ lines of structured prompts) documents the prompt infrastructure developed this semester. These are not "prompts I used" but infrastructure I built—a different category that disclosure frameworks don't accommodate.

---

## References

Karpathy, A. (2025). Context engineering. X post.

Scott, J. C. (1998). *Seeing Like a State: How Certain Schemes to Improve the Human Condition Have Failed*. Yale University Press.

Suchman, L. A. (1987). *Plans and Situated Actions: The Problem of Human-Machine Communication*. Cambridge University Press.

---

*Paper submitted December 2025. Word count: ~2,400.*
*This is practitioner reflection, not empirical study.*
*The heuristic is offered; the theory is tentative.*
