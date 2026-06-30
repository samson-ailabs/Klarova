# Roadmap

The public, tracked projection of the build plan. The method is a **walking skeleton, then
deepen**: the thinnest slice that *runs and is measured* first, then one capability at a
time. After every step the system still runs end to end and an evaluation still reports a
number — never a half-built scaffold, never an unmeasured change.

Pace is self-directed; the markers below are sequence, not a calendar.

## Ship 1 — the context layer (the moat), measured

A skeleton that already touches the warehouse *and* the docs, then each capability
deepened in turn.

- [ ] **Skeleton (both substrates)** — kernel (`create_agent` + persistence + CLI) + a thin
      agent that routes a question to the warehouse (one validated read-only `run_sql`, via
      governed execution with provenance) **or** the docs (retrieve a passage and cite it).
      *Measured by:* SQL execution accuracy on ~10 gold pairs **and** doc retrieval recall +
      citation match.
- [ ] **Search quality** — better retrieval (chunking, hybrid tuning, rerank), answers with
      citations, multi-hop. *Measured by:* recall@k / nDCG on BEIR + HotpotQA; citation match.
- [ ] **Semantic layer** — governed metric definitions; the agent picks a metric by name.
      *Measured by:* accuracy on metric questions vs. raw SQL.
- [ ] **Cross-source** — combine a governed warehouse number and a doc fact into one cited
      answer. *Measured by:* a sub-claim checklist.
- [ ] **Grounding** — example query-pair retrieval + schema-doc retrieval (wire a BIRD db
      here). *Measured by:* example-grounding lift on Olist; schema-doc lift on BIRD.
- [ ] **Governed access** — execution scopes rows, columns, and documents to a passed
      identity, and audits. *Measured by:* access-control tests.
- [ ] **MCP server** — expose query, metric, retrieval, and governed-execution tools over
      MCP. *Measured by:* plug Claude/Cursor in → same governed, cited answers.

**Milestone:** `v0.1` + pattern-series post #1.

## Ship 2 — the full copilot

Situate + identity · diagnostic data prep · investigation (parallel sub-agents) ·
verification · human-in-the-loop · action (deploy, gated) · memory.

**Milestone:** `v0.2` + post #2.

## Ship 3 — integrated and shipped

Host (embed copilot in Acme Analytics) · reliability + deploy (pass-rate-over-k,
cross-model regression, public hosted demo).

**Milestone:** `v1.0` + post #3.

## Ship 4 — stretch

One thin second vertical on the unchanged engine-core.

**Milestone:** post #4.

## Form evolution

CLI → MCP server → headless copilot → hosted web app → multi-vertical engine.
