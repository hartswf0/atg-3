# Norman Heuristics for Studio Atlas

## The Interface as Constraint Infrastructure

> "The wilderness is full of false affordances (irrelevant data); the engineered context must *constrain* the model to the path of success."
> — Context Engineering Genealogy

Donald Norman's *The Design of Everyday Things* (1988/2013) provides the theoretical scaffold for Studio Atlas's interface architecture. Where classical HCI focused on bridging the "Gulf of Execution"—the gap between user intent and system action—Studio Atlas operates in a fundamentally different regime: the *Void*, where generative systems produce unbounded output requiring active constraint.

This section translates Norman's core principles into concrete implementation rules for Studio Atlas (DCE-GYO), treating **constraints as infrastructure** rather than limitation.

---

## 1. Make State Visible

**Norman's Principle:** The user should always be able to determine the current state of the system through easily perceived cues.

**The Void Problem:** In a multi-surface ecosystem (Swiss → COURAGE → GOLD → MASTER → MENTO), state becomes distributed. Users lose track of what's loaded, connected, or authoritative.

**Implementation:**
```
┌─────────────────────────────────────────────────────────────┐
│ STATUS HUD (persistent across all surfaces)                 │
│ MPD ✅ | Parts ✅/❌ | Bus ✅/OFF | Skeleton fresh/stale      │
│ Camera = 368/369/373 | Export ready ✅/❌                    │
└─────────────────────────────────────────────────────────────┘
```

**Test:** Can a new user answer the 6 state questions in 5 seconds without reading documentation?

---

## 2. Immediate Feedback for Every Action

**Norman's Principle:** Every action must show an effect *somewhere visible* within ~200ms or acknowledge work in progress.

**The Void Problem:** Generative systems have unpredictable latency. Users cannot distinguish "working" from "broken."

**Implementation:**
- GOLD edit → highlights changed line + flashes affected brick in COURAGE
- Bus message sent → "SYNC" pulse animation + last message type displayed
- If feedback delayed >200ms → show "pending" spinner explicitly

**Norman's Terminology:** This addresses the *Gulf of Evaluation*—helping users understand "what happened?"

---

## 3. Strong Signifiers (Not Discoverability by Lore)

**Norman's Principle:** Affordances are action possibilities; *signifiers* are the perceptible indicators that communicate those possibilities.

**The Void Problem:** Power users accumulate "tribal knowledge" about which elements are interactive. New users see a wall of text.

**Implementation:**
- Grid cells show hover affordances + label the action ("Open Viewer", "Copy MPD")
- Labs marked with **hazard tape** visuals + "Experimental" chip
- Interactive elements have consistent visual vocabulary (blue = action, gray = display)

**Test:** Users can correctly predict what's clickable 90% of the time without training.

---

## 4. Natural Mappings (Controls Match Effects)

**Norman's Principle:** The relationship between controls and their effects should follow from physical analogy, cultural standards, or logical order.

**The Void Problem:** The LEGO-to-GLB pipeline is abstract. "Where does my edit go?" has no physical analogy.

**Implementation:** Default shell layout mirrors the conceptual pipeline:

```
LOAD (Swiss) → VIEW (COURAGE) → EDIT (GOLD/Grace) → VALIDATE (MASTER) → CAPTURE (MENTO) → EXPORT (GLB)
     ↓              ↓                ↓                   ↓                  ↓              ↓
  [Left]    [Center-Left]     [Center]          [Center-Right]        [Right]        [Far Right]
```

**Test:** If you hide labels, can users still infer which panel does what from position alone?

---

## 5. Constraints That Prevent Mistakes (Not Just Warnings)

**Norman's Principle:** Prefer "can't do wrong" over "told you it's wrong." Physical constraints make errors impossible; logical constraints make them clearly illegitimate.

**The Void Problem:** Generative systems produce plausible nonsense. Users don't know they've made an error until export fails.

**Implementation:**
- If Parts library missing → **disable** "Export GLB" button + provide one-click fix path
- If skeleton stale → show "Rebuild Skeleton" button next to selection tools
- Invalid MPD syntax → prevent save, not just warn after

**Norman's Key Insight:**
> "Constraints are as important as affordances. Constraints limit behavior to prevent error."

**Test:** Most common failures become **impossible**, not merely documented.

---

## 6. Good Conceptual Model (One Sentence That Stays True)

**Norman's Principle:** Users build mental models of how systems work. Design must ensure the model matches reality.

**The Void Problem:** Calling Studio Atlas an "OS" suggests monolithic integration that doesn't exist.

**Correct Model:**
> "A set of browser tools that share an MPD and optionally sync via a bus."

**Test:** No feature should contradict that sentence. If a tool doesn't share the MPD, it doesn't belong in the ecosystem.

---

## 7. Knowledge in the World, Not in the Head

**Norman's Principle:** Don't force users to remember—embed information in the environment itself.

**The Void Problem:** Users must remember "which MENTO is stable" or "how Frank wiring works." Tribal knowledge accumulates.

**Implementation:**
- Swiss routes by **capability chips** (capture/keyframes/animation) not version numbers
- Always show **Copy Pack** links next to each workflow step
- Contract Cards (`?`) embedded in every surface, in the same position

**Test:** Users complete core tasks without memorizing tool trivia.

---

## 8. Clear, Recoverable Errors (Blame the System)

**Norman's Principle:** When errors occur, help users understand what happened, why, and how to recover. Never blame the user.

**The Void Problem:** Generative failures ("hallucination") have no clear cause. "It didn't work" is the only feedback.

**Implementation:** Standard error format everywhere:
```
┌─────────────────────────────────────────────────┐
│ SYMPTOM: GLB export failed                      │
│ CAUSE:   Parts library not loaded               │
│ FIX:     Click "Load Parts" in Swiss panel      │
│ VERIFY:  [Verify Fix ✓]                         │
└─────────────────────────────────────────────────┘
```

**Test:** Every error has a one-click "Verify fix" action.

---

## 9. Design for Repair (Undo, Revert, Diff)

**Norman's Principle:** Make actions reversible. Let users explore without fear of irreversible damage.

**The Void Problem:** Generative edits compound. "Undo" across surfaces is undefined.

**Implementation:**
- MPD timeline snapshots + diff viewer
- "Revert last edit" works across surfaces (event log tracks cross-surface mutations)
- Every destructive action requires confirmation

**Test:** Can users recover from a wrong edit in under 15 seconds?

---

## 10. Discoverability Through Progressive Disclosure

**Norman's Principle:** Show only what's needed now; reveal depth on demand.

**The Void Problem:** The full ecosystem is overwhelming. New users see 12 surfaces and flee.

**Implementation:**
- **Beginner mode:** Swiss + COURAGE + GOLD + "Export" button
- **Advanced mode:** Skeleton labs, manifolds, taxonomies (toggle to reveal)
- Labs quarantined behind explicit "Show Labs" toggle

**Test:** New users aren't forced to learn manifolds to place a brick.

---

## 11. Consistency (Names, Shortcuts, Contracts)

**Norman's Principle:** Similar things should behave similarly. Consistency reduces learning burden.

**The Void Problem:** Each surface was built independently. Shortcuts, terminology, and UI patterns drift.

**Implementation:**
- Same shortcut for "Copy MPD," "Save Snapshot," "Open Inspector" across all shells
- Every surface has a Contract Card (`?`) in the same position (top-right)
- Terminology locked: "MPD" not "file," "Surface" not "tool," "Bus" not "sync"

**Test:** Switching surfaces doesn't reset the user's muscle memory.

---

## 12. Make the Right Thing the Easiest Thing

**Norman's Principle:** Defaults should be safe, stable, and canonical. The path of least resistance should be the correct path.

**The Void Problem:** Labs are seductive. Users wander into experimental surfaces and get confused.

**Implementation:**
- MENTO default = 368 (basic, stable)
- Labs quarantined behind a toggle
- Copy Pack always first-class in UI hierarchy
- "Hello World" example always one click away

**Test:** The shortest path is also the most reliable path.

---

## The Copy Bar: Knowledge in the World

A concrete implementation that embodies multiple Norman principles:

```
┌─────────────────────────────────────────────────────────────┐
│ COPY BAR (pinned in every shell)                            │
│ [Copy MPD] [Copy Minimal Example] [Copy Bus Session]        │
│ [Copy Validation Report]                                    │
└─────────────────────────────────────────────────────────────┘
```

This turns "examples at hand" into **knowledge-in-the-world** + **repairability**:
- **Copy MPD:** Current project state
- **Copy Minimal Example:** Canonical hello scene (works every time)
- **Copy Bus Session:** Last 50 messages (for debugging)
- **Copy Validation Report:** Parts missing / skeleton stale / transforms invalid

---

## The Norman Gate: A Shipping Checklist

Before any new surface or feature ships, it must pass the Norman Gate:

| Criterion | Question | Pass/Fail |
|-----------|----------|-----------|
| **State Visibility** | Can user determine current state in 5s? | ○ |
| **Feedback** | Does every action show effect in <200ms? | ○ |
| **Signifiers** | Are interactive elements visually distinct? | ○ |
| **Mapping** | Does layout match conceptual pipeline? | ○ |
| **Constraints** | Are common errors impossible (not just warned)? | ○ |
| **Repair** | Can user undo in <15s? | ○ |

---

## Theoretical Grounding

This framework synthesizes Norman with the broader "Void Management" thesis:

| Theorist | Concept | Studio Atlas Application |
|----------|---------|--------------------------|
| Norman (1988) | Affordances | MPD structure *affords* certain edits |
| Norman (1988) | Constraints | UI *constrains* to valid operations |
| Norman (2013) | Signifiers | Visual vocabulary for interactivity |
| Winograd & Flores (1986) | Breakdown | Design for graceful failure states |
| Dourish (2001) | Embodiment | Pipeline layout embodies conceptual model |

> "The 'Void Management' thesis adopts Norman's view: the wilderness is full of false affordances (irrelevant data); the engineered context must *constrain* the model to the path of success. Meaning emerges from these constraints."

---

*Section prepared for DCE-GYO / Studio Atlas Technical Documentation*
*December 2025*
