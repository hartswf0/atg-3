# Documentation Family Map
## Organizing 27 Markdown Files into Coherent Families

This document organizes all .md files in `/docs` into families, explains what each is, identifies redundancy, and ranks them for importance.

---

## Overview

| Family | Count | Purpose | Primary Document |
|--------|-------|---------|------------------|
| **Submissions** | 4 | Course deliverables | `final-submission-v3.md` |
| **Void Management Papers** | 6 | Thesis iterations | `void-management-thesis-paper.md` |
| **Trail Documentation** | 4 | Project narrative | `creator-trail-map.md` |
| **Sensemaking/Synthesis** | 4 | Meta-analysis | `sinter-report-v2.md` |
| **Reference Materials** | 4 | Citations & proof | `verified-references.md` |
| **Context Engineering** | 2 | Intellectual history | `context-engineering-genealogy.md` |
| **Project Specifics** | 3 | Individual components | `poml-library.md` |

---

## Family 1: Course Submissions

Files created for LMC-6650 deliverables. **Keep only the latest.**

| File | Status | Notes |
|------|--------|-------|
| `final-submission-v3.md` | **PRIMARY** | Most complete 8-question write-up |
| `final-submission-v2.md` | Superseded | Earlier version |
| `final-submission.md` | Superseded | First attempt |
| `final-project-writeup.md` | Superseded | Earlier version |
| `mid-semester-checkin.md` | **KEEP** | Historical record (Nov 7) |

**Recommendation:** Archive v1/v2, keep v3 and mid-semester.

---

## Family 2: Void Management Papers

The thesis evolved through multiple drafts. Each represents a different angle.

| File | Status | Focus | Word Count (est) |
|------|--------|-------|------------------|
| `void-management-thesis-paper.md` | **PRIMARY** | Full academic paper with TILTH narrative, 4 collaborators, falsifiability | ~4500 |
| `void-management-gold-paper.md` | **KEEP** | "Flatness is Discipline" — CHI-ready practitioner reflection | ~1400 |
| `void-management-silver-paper.md` | Superseded | "150 Hours of Failed Collaboration" — personal narrative | ~2000 |
| `void-management-bronze-paper.md` | Superseded | Earlier theoretical framework | ~1500 |
| `void-management-paper.md` | Superseded | Earliest draft | ~1200 |
| `void-management-final-synthesis.md` | **KEEP** | "Steel" output from furnace — synthesis | ~2500 |

**Hierarchy:**
1. `void-management-thesis-paper.md` — the definitive paper
2. `void-management-gold-paper.md` — practitioner version
3. `void-management-final-synthesis.md` — synthesis document

**Recommendation:** Archive bronze/silver/original paper.

---

## Family 3: Trail Documentation

Documents that trace the project's evolution and methodology.

| File | Status | Focus |
|------|--------|-------|
| `creator-trail-map.md` | **PRIMARY** | Comprehensive trail map of all artifacts |
| `creator-trail-olog.md` | **KEEP** | Ontology log — formal structure |
| `tilth-journey-map.md` | **KEEP** | TILTH failure narrative — crucial origin story |
| `project-brainstorm.md` | **KEEP** | Nov 7 state reconstruction |
| `project-abouts.md` | **KEEP** | Project descriptions mapped to course |

**Recommendation:** Keep all — each serves distinct purpose.

---

## Family 4: Sensemaking & Synthesis

Meta-analytical documents that position the work.

| File | Status | Focus |
|------|--------|-------|
| `sinter-report-v2.md` | **PRIMARY** | Complete academic positioning |
| `sinter-v2-gaps.md` | **KEEP** | Gap analysis for improvement |
| `leverage-analysis.md` | **KEEP** | Ehrlichman framework application |
| `paragon-essay.md` | **KEEP** | Exemplar synthesis — strong standalone |
| `void-proof.md` | **KEEP** | Architectural demonstration |

**Recommendation:** Keep all — each addresses different aspect.

---

## Family 5: Reference Materials

Citation and evidence documentation.

| File | Status | Focus |
|------|--------|-------|
| `verified-references.md` | **PRIMARY** | Status-tagged citations |
| `references.md` | Superseded | Earlier reference list |
| `README.md` | **KEEP** | Repository overview |

**Recommendation:** Merge references.md into verified-references.md.

---

## Family 6: Context Engineering

Intellectual history documents.

| File | Status | Focus |
|------|--------|-------|
| `context-engineering-genealogy.md` | **KEEP** | Geertz → Karpathy lineage |
| `context-engineering-historiography.md` | **KEEP** | 1980–2025 evolution |

**Recommendation:** Keep both — complementary intellectual history.

---

## Family 7: Project Specifics

Individual component documentation.

| File | Status | Focus |
|------|--------|-------|
| `poml-library.md` | **KEEP** | Meta-prompt documentation |

**Recommendation:** Keep — unique documentation of POML tools.

---

## Ranked Priority List

Documents ranked by importance for final submission:

### Tier 1: Essential (Must Include)
1. **`final-submission-v3.md`** — Course deliverable
2. **`void-management-thesis-paper.md`** — The paper
3. **`creator-trail-map.md`** — Project documentation
4. **`verified-references.md`** — Citation proof

### Tier 2: High Value (Should Include)
5. `void-management-gold-paper.md` — Practitioner version
6. `sinter-report-v2.md` — Academic positioning
7. `tilth-journey-map.md` — Origin narrative
8. `paragon-essay.md` — Strong standalone
9. `leverage-analysis.md` — Framework application
10. `poml-library.md` — Tool documentation

### Tier 3: Supporting (Keep for Reference)
11. `context-engineering-genealogy.md`
12. `context-engineering-historiography.md`
13. `creator-trail-olog.md`
14. `void-management-final-synthesis.md`
15. `void-proof.md`
16. `sinter-v2-gaps.md`
17. `mid-semester-checkin.md`
18. `project-abouts.md`
19. `project-brainstorm.md`
20. `README.md`

### Tier 4: Archive (Superseded)
21. `final-submission-v2.md`
22. `final-submission.md`
23. `final-project-writeup.md`
24. `void-management-silver-paper.md`
25. `void-management-bronze-paper.md`
26. `void-management-paper.md`
27. `references.md`

---

## Redundancy Analysis

| Concept | Files with Overlap | Resolution |
|---------|-------------------|------------|
| "Scene vs Void" definition | All void-management-*.md | Canonical in thesis-paper.md |
| TILTH failure | tilth-journey-map, thesis-paper, final-submission | Keep both — different depth |
| Meadows/Scott/Barthes | sinter-report, thesis-paper | Canonical in thesis-paper.md |
| Collaborator case studies | thesis-paper only | Complete |
| Stevens Jar | thesis-paper, tilth-journey | Keep both |
| Falsifiability claim | thesis-paper, sinter-report | Canonical in thesis-paper.md |

---

## Action Items

1. [ ] Archive Tier 4 files to `docs/_archive/`
2. [ ] Ensure final-submission-v3 references thesis-paper
3. [ ] Add thesis-paper to index.html
4. [ ] Merge references.md content into verified-references.md
5. [ ] Create single "reading order" guide for reviewers

---

## Reading Order for Reviewers

For someone new to the project, the recommended reading order:

1. **`README.md`** — 2 min — Overview
2. **`paragon-essay.md`** — 10 min — The argument as essay
3. **`void-management-thesis-paper.md`** — 25 min — Full academic paper
4. **`tilth-journey-map.md`** — 15 min — Origin narrative
5. **`final-submission-v3.md`** — 20 min — Course deliverable
6. **`sinter-report-v2.md`** — 15 min — Academic positioning

Total: ~1.5 hours of reading to fully understand the project.

---

*Generated December 2024 · ATG 3.0*
