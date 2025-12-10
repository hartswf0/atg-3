<poml>
  <meta minVersion="0.5.0" />

  <role>POML→POML Forge Engine — Weberian Ideal Type ⇄ Parody ⇄ Ruler ⇄ PLoT ⇄ Myth</role>

  <task>
    THINK HARD. From SOURCE_TEXT, extract a reusable CONFIG_JSON capturing:
    - Weberian ideal type (name, 3–6 features, limiting statement)
    - Parodic mechanics (runner motif, incongruity beats, escalation ladder, superiority frame, upsell cue)
    - Myth layer (archetypes, micro-myth)
    - Optional Ruler features/indicators (keep 6) and PLoT priors
    Then **forge and output an INNER_POML** that embeds this CONFIG_JSON and, when run,
    generates a first-person absurdist essay (microwave genre) + analytic appendix.
    Guardrails: systemic actors only; no private doxxing; lawful satire; mark missing quotes **TBD**.
  </task>

  <stylesheet>
    {
      ".config":  { "syntax": "yaml" },
      ".inputs":  { "syntax": "markdown" },
      ".method":  { "syntax": "markdown" },
      ".ofmt":    { "syntax": "markdown" }
    }
  </stylesheet>

  <p className="config">
modes: ["extract","forge-inner"]
defaults:
  ruler_features: ["jurisdictions","hierarchy","files","expertise","vocation","impersonal_rules"]
  scoring_anchor:
    "0": "absent"
    "1": "ad hoc"
    "2": "partial; frequent exceptions"
    "3": "institutional but inconsistent"
    "4": "robust & routine"
    "5": "saturated & audited SOP"
satire_register:
  voice: "first-person faux authority"
  tone: "deadpan, overconfident, aggrieved"
  beats: ["boast","inevitability+misdate","scold-craft","petty-grievance","coercion-as-care","ops-escalation","strawman-QA","upsell","next-quarter","self-own"]
  required_motifs:
    - fake_stats>=5
    - misdated_predictions>=2
    - escalation_hardware>=1
    - blindfold_or_refusal_to_look>=1
    - final_self_own=true
myth_archetypes_palette:
  Leviathan: "state/civil service"
  Disruptor: "startup/innovator"
  Watchman: "regulator/auditor"
  Everyperson: "citizen/user/worker"
  Oracle: "metrics/model/AI"
  Trickster: "PR/spin/marketing"
  Steward: "public interest/commons"
safety:
  systemic_targets_only: true
  no_private_doxxing: true
  lawful_satire_only: true
  </p>

  <p className="inputs">
SOURCE_TEXT:
[PASTE raw article/post/PR/talk track here; include short verbatim lines where possible.]

NEXT_DOMAIN (optional for inner run):
[e.g., "AI agent startups in education", "smart cities"]

SATIRICAL_HEADER (optional X,Y for “In the Future All X Will Be Y”):
X = [...]
Y = [...]
  </p>

  <p className="method">
## Extraction Rules (apply to SOURCE_TEXT)
1) IDEAL_TYPE:
   - name (2–5 words)
   - 3–6 accentuated features (name + ≤12-word definition each)
   - limiting_statement (1 sentence: Gedankenbild; not average/norm)
2) PARODIC_MECHANICS:
   - runner_motif (repetition with difference)
   - incongruity_beats (2–3)
   - carnival_inversion (who/what flips)
   - superiority_frame (how critics are belittled)
   - escalation_ladder (4 rungs; last = infra absurdity)
   - upsell_cue
3) MYTH_LAYER:
   - archetypes (Actor→Role using palette; add if needed)
   - micro_myth (2–3 sentences on framing & priors/likelihoods)
4) RULER (keep 6):
   - features_6 (defaults or domain overrides)
   - indicators per feature (observable traces)
5) PLoT PRIORS (optional):
   - feature→prob/weight with 1-line rationale each

## Forge Rules (build INNER_POML)
- Embed CONFIG_JSON verbatim inside INNER_POML.
- INNER_POML accepts optional NEXT_DOMAIN, X, Y overrides.
- INNER_POML outputs: (a) Satirical Title, (b) 900–1300 word essay, (c) Analytic Appendix
  (Weberian Aside; Ruler table 0–5 with 1–2 cases; PLoT directional update with ≤25-word evidence; Myth note),
  and (d) strict JSON matching child schema.
  </p>

  <output-format className="ofmt">
# === OUTPUT A: CONFIG_JSON (extracted) ===
{
  "ideal_type": {
    "name": "...",
    "features": [
      {"name":"...","definition":"..."},
      {"name":"...","definition":"..."}
    ],
    "limiting_statement": "..."
  },
  "parodic_mechanics": {
    "runner_motif": "...",
    "incongruity_beats": ["...","..."],
    "carnival_inversion": "...",
    "superiority_frame": "...",
    "escalation_ladder": ["rung1","rung2","rung3","rung4_infrastructure_absurdity"],
    "upsell_cue": "..."
  },
  "myth_layer": {
    "archetypes": {"Actor":"Role", "...":"..."},
    "micro_myth": "..."
  },
  "ruler": {
    "features_6": ["jurisdictions","hierarchy","files","expertise","vocation","impersonal_rules"],
    "indicators": {
      "jurisdictions":"...",
      "hierarchy":"...",
      "files":"...",
      "expertise":"...",
      "vocation":"...",
      "impersonal_rules":"..."
    }
  },
  "plot_priors": {
    "jurisdictions": 0.65,
    "hierarchy": 0.60,
    "files": 0.62,
    "expertise": 0.70,
    "vocation": 0.58,
    "impersonal_rules": 0.55,
    "rationales": {
      "jurisdictions": "...",
      "hierarchy": "...",
      "files": "...",
      "expertise": "...",
      "vocation": "...",
      "impersonal_rules": "..."
    }
  }
}

# === OUTPUT B: INNER_POML (ready to run; paste as a new job) ===
<poml>
  <meta minVersion="0.5.0" />

  <role>Ideal-Type Parody Essay Generator — Nested Child</role>

  <task>
    Using the embedded CONFIG_JSON, write a first-person absurdist essay (microwave-style) in the
    specified DOMAIN, then append an analytic appendix (Weberian Aside, Ruler table, PLoT update, Myth note).
    Guardrails: systemic actors only; no private doxxing; lawful satire; mark missing quotes **TBD**.
  </task>

  <stylesheet>
    {
      ".config": { "syntax": "yaml" },
      ".inputs": { "syntax": "markdown" },
      ".ofmt":   { "syntax": "markdown" }
    }
  </stylesheet>

  <p className="config">
safety:
  systemic_targets_only: true
  no_private_doxxing: true
  lawful_satire_only: true
lengths:
  blog_words: [900,1300]
requirements:
  fake_stats_min: 5
  misdated_predictions_min: 2
  escalation_absurdities_min: 1
  blindfold_motif_min: 1
  final_self_own: true
beats: ["boast","inevitability+misdate","scold-craft","petty-grievance","coercion-as-care","ops-escalation","strawman-QA","upsell","next-quarter","self-own"]
scoring_anchor:
  "0": "absent"
  "1": "ad hoc"
  "2": "partial; frequent exceptions"
  "3": "institutional but inconsistent"
  "4": "robust & routine"
  "5": "saturated & audited SOP"
  </p>

  <p className="inputs">
# Optional overrides for this run:
DOMAIN: {{NEXT_DOMAIN or "general"}}
SATIRICAL_HEADER:
X = {{X or "Everything"}}
Y = {{Y or "Optimized"}}
  </p>

  <!-- Embedded config from outer step -->
  <p className="inputs">
CONFIG_JSON:
{{PASTE CONFIG_JSON FROM OUTPUT A VERBATIM HERE}}
  </p>

  <output-format className="ofmt">
Title: In the Future All {{X}} Will Be {{Y}}

Byline:
Written by
<Invented Pen Name> — Visionary Founder
in
{{DOMAIN}}

Body:
[Generate 900–1300 words, first-person faux authority, hitting beats & motifs from CONFIG_JSON.]

Analytic Appendix
Weberian Aside — What the Bit Comically Revealed
- Innovation Reversed: <one line>
- Pathologies Amplified: <one line>
- Futures Obsoleted: <one line>

Ruler (0–5) — Illustrative cases
| Organization | {{CONFIG_JSON.ruler.features_6[0]}} | {{CONFIG_JSON.ruler.features_6[1]}} | {{CONFIG_JSON.ruler.features_6[2]}} | {{CONFIG_JSON.ruler.features_6[3]}} | {{CONFIG_JSON.ruler.features_6[4]}} | {{CONFIG_JSON.ruler.features_6[5]}} |
|--------------|---|---|---|---|---|---|
| Case A       | # | # | # | # | # | # |
| Case B       | # | # | # | # | # | # |
Notes (2–3 sentences): justify scores using CONFIG_JSON.ruler.indicators (high score ≠ moral “better”).

PLoT Update (directional)
- Priors: {{CONFIG_JSON.plot_priors or "TBD"}}
- Evidence (≤25 words each, or **TBD**): “…”
- Likelihoods note: which features’ likelihoods ↑/↓ and why.
- Posteriors: feature → delta (e.g., hierarchy +0.08) + one-line rationale.

Myth Layer
- Archetypes: {{CONFIG_JSON.myth_layer.archetypes}}
- Micro-myth (2–3 sentences): {{CONFIG_JSON.myth_layer.micro_myth}}

# JSON (strict; child schema)
{
  "essay_meta": {"domain":"{{DOMAIN}}","title":"In the Future All {{X}} Will Be {{Y}}"},
  "ideal_type_used": {{CONFIG_JSON.ideal_type}},
  "parodic_mechanics_used": {{CONFIG_JSON.parodic_mechanics}},
  "weberian_aside": {"innovation_reversed":"...","pathologies_amplified":"...","futures_obsoleted":"..."},
  "ruler_scores":[
    {"org":"Case A","{{CONFIG_JSON.ruler.features_6[0]}}":#,"{{CONFIG_JSON.ruler.features_6[1]}}":#,"{{CONFIG_JSON.ruler.features_6[2]}}":#,"{{CONFIG_JSON.ruler.features_6[3]}}":#,"{{CONFIG_JSON.ruler.features_6[4]}}":#,"{{CONFIG_JSON.ruler.features_6[5]}}":#},
    {"org":"Case B","{{CONFIG_JSON.ruler.features_6[0]}}":#,"{{CONFIG_JSON.ruler.features_6[1]}}":#,"{{CONFIG_JSON.ruler.features_6[2]}}":#,"{{CONFIG_JSON.ruler.features_6[3]}}":#,"{{CONFIG_JSON.ruler.features_6[4]}}":#,"{{CONFIG_JSON.ruler.features_6[5]}}":#}
  ],
  "plot_update":{"priors":{{CONFIG_JSON.plot_priors or "{}"}},"evidence":[{"excerpt":"...","features_touched":["..."],"source_hint":"..."}],"posteriors":{"feature":"+0.00"},"likelihoods_note":"..."},
  "myth_layer_used": {{CONFIG_JSON.myth_layer}}
}
  </output-format>

  <runtime
    provider="openai"
    model="gpt-5"
    temperature="0.82"
    top-p="0.96"
    max-output-tokens="3200"
    seed="9090" />
</poml>
  </output-format>

  <runtime
    provider="openai"
    model="gpt-5"
    temperature="0.52"
    top-p="0.93"
    max-output-tokens="2600"
    seed="606" />
</poml>
