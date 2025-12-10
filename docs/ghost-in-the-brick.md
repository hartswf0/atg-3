# The Ghost in the Brick

**On LDraw, Modulex, and the Infrastructure We Stand On**

---

In 1995, a programmer named James Jessiman did something that would outlast him by twenty-seven years and counting. He wrote down, in plain text, how to describe a LEGO brick in three-dimensional space. The file format he created—LDraw—uses no proprietary encoding, no encrypted geometry, no compiled binaries. It is, at its core, a language. Line Type 1 says: "reference another file." Line Type 3 says: "draw a triangle here." A stud is fifty-two lines of code. A 2x4 brick is a reference to four studs, arranged. An entire model is a reference to a thousand bricks, each a reference to the primitives that compose it.

Jessiman died in 1997. He was in his twenties. The community he left behind—hobbyists, engineers, obsessives—organized within weeks. They established committees. They codified review processes. They built, over the next three decades, a library of 18,000 parts, modeled to tolerances that exceed LEGO's own promotional renders. The file format he wrote in a text editor became the invisible infrastructure that supports every major digital LEGO tool today: BrickLink Studio, Mecabricks, the third-party renderers that compete with the corporation's own.

This is the first story.

---

The second story begins in 1960, in Billund, Denmark. Godtfred Kirk Christiansen—son of the founder, heir to the toy empire—is building a scale model of his new house. He uses the bricks his company manufactures. They do not work.

The problem is geometric. A standard LEGO brick is 8mm wide and 9.6mm tall—an aspect ratio of 5:6. This means you cannot scale uniformly in all three dimensions. A wall twenty studs long is not proportional to a wall twenty bricks high. For a child's imagination, this is irrelevant. For an architect, it is catastrophic.

Christiansen's solution was to commission a new brick. The Modulex brick is a perfect 5mm cube: 1:1:1 aspect ratio. One brick equals ten centimeters at 1:20 scale—a standard European module. The geometry is rational. Uniform scaling becomes possible. The architectural model of a building can now match the building's actual proportions.

Modulex launched in 1963. By 1966, it had failed as an architecture tool—too expensive, too rigid for the organic forms coming into fashion. The company pivoted to industrial planning: wall-mounted boards where factory managers could move colored tiles to schedule production. By the 1970s, they pivoted again to signage. By 2015, when a family member tried to revive the original brick system, LEGO's legal arm acquired the project and shut it down. The molds were transferred to corporate control. The test parts that escaped are now among the rarest artifacts in plastic collecting.

---

These two histories appear unrelated. One is about software; the other is about plastic. One is open-source; the other is proprietary. One succeeded; the other failed.

But look closer.

In both cases, the intervention was the same: **make the constraint explicit**.

Jessiman wrote the brick's geometry as text. This made the brick *readable*—and therefore debuggable, shareable, improvable. The corporate alternative, LEGO Digital Designer, hid its geometry in encrypted assets. When LEGO discontinued the software in 2022, users discovered they could not even extract their own models. The proprietary brick was a black box; the community brick was a language. The language survived.

Christiansen redesigned the brick's dimensions. This made architectural scaling *possible*—not through training or discipline, but through geometry. You could not build a disproportionate model in Modulex. The constraint was in the material. When the aspect ratio was 1:1:1, scaling errors became structurally impossible.

---

Here is the difference that makes the difference:

**LDraw is text.**

This sounds trivial. It is not. The entire history of the digital LEGO ecosystem is a history of text versus binary, open versus closed, language versus image. LEGO's internal tools—the Panter system (1986), the L3D database (1996), the Darwin project with its SGI supercomputers—were all attempts to create proprietary representations of the brick. They ran on specialized hardware. They required corporate infrastructure to maintain. When the projects ended, the knowledge died with them. No one outside LEGO knows what the Panter source code looked like. The L3D database is "linguistic dark matter"—we know it existed, but we cannot read it.

LDraw, by contrast, is human-readable. A child with a text editor can open a .dat file and understand, roughly, what it does. This property—*legibility*—is what allowed the community to maintain the format for thirty years without corporate sponsorship. It is what allows new contributors to author parts, submit them for review, and integrate them into the official library within weeks of LEGO releasing new molds. It is what makes the format *infrastructure* rather than product.

**Modulex is a cube.**

This also sounds trivial. It is also not. The 5:6 aspect ratio of the standard LEGO brick is a *representable invalid state*. It permits proportional errors. It allows the builder to construct something geometrically inconsistent. The 1:1:1 aspect ratio of Modulex *removes the possibility of that error*. It does not catch the mistake; it makes the mistake unthinkable.

This is the principle we have named *Negative Space Programming*: the reliability of a system is inversely proportional to the size of its representable invalid states. Dijkstra eliminated `goto` from the language; the programmer could no longer write spaghetti code. Hoare regretted inventing `null`; the program could crash at runtime. Algebraic data types close the null-shaped hole; the compiler catches the error before execution. Modulex closed the scaling error; the geometry enforced correctness.

---

Our project stands on both histories.

We use LDraw-compatible tools to visualize our models. The infrastructure we did not build—the 18,000 parts, the decades of community labor—is the foundation on which our work rests. We could not do what we do if Jessiman had not written those file format specifications in 1995, or if the community had not maintained them through his death and the years that followed.

We draw on the Modulex principle when we design POML operators. Each operator is a constraint. It closes a region of the possibility space. It does not tell the user what to do; it eliminates certain classes of error by making them unrepresentable. A `<forbidden>` block in POML is not a warning; it is a grammatical exclusion. The prompt that would produce the forbidden output cannot be written within the structure.

When we write about "Void Management," we are writing about this:

The Void is all possible outputs of a generative system. It is boundless. To dwell in the Void is to be overwhelmed. The response is not to expand context (feed the model more information, as if that would help) but to *constrain the Void*—to sinter the granular material into a usable shape.

LDraw is a sintered format. It does not try to represent every possible 3D form; it represents only the forms that compose from primitives. This is its power. The constraint is the feature.

Modulex is a sintered geometry. It does not try to support every possible aspect ratio; it supports only the 1:1:1 cube. This was its limitation for architects who wanted curves. But it was its salvation for architects who wanted accuracy.

---

Wong's Infrastructural Turn asks: How do we redesign the organization to make ethics work survivable?

We ask: How do we redesign the artifact so that infrastructure is less necessary?

The LDraw ecosystem answers: Make the format open. Make it text. Make it modular, referenceable, reviewable. The community will maintain what the corporation will not.

The Modulex history answers: Make the constraint geometric. Make the error impossible. But know that this is not enough—power will acquire and suppress what threatens its control.

Both answers are partial. Both are necessary.

Jessiman died young. His format outlived him because it was *written down as text*. Christiansen's grandchild tried to revive Modulex. LEGO's lawyers bought and buried it because the corporation controls the molds.

The ghost in the brick is the file format. It is the invisible syntax that determines what can be built. It is the infrastructure we depend on and rarely see.

And the question for the generative era is: What is the LDraw of large language models? What file format, what constraint structure, what open standard will outlive any of us?

POML is an attempt. The pyramids are documentation. The thesis is this:

**You cannot own the Void. But you can write down the constraints.**

And if you write them as text—human-readable, community-maintainable, modular, referenceable—they might just survive.

---

*For James Jessiman (1969–1997), whose twenty-seven-year-old file format is the foundation we stand on.*
