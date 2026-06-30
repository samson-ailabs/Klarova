# Architecture

This document is updated per module as the build proceeds (a quality gate: a step isn't
done until its `ARCHITECTURE.md` section is updated). It records *what is built*; the
build *order* lives in [`ROADMAP.md`](ROADMAP.md), and decision-level rationale lives in
[`decisions/`](decisions/).

## The two sides

Keeping these cleanly separate is the whole design.

### The context layer — the moat (passive, reusable, MCP-exposed)

Does no reasoning and writes no SQL of its own. Three responsibilities:

- **Semantic model** — the governed *meaning* of the business: metric definitions,
  entities, relationships. Declarative; the single source of truth for what the numbers
  mean.
- **Grounding & memory** — retrieval that gives an agent the context to ask accurately
  (relevant schema, example query pairs, the document corpus) plus a memory of corrected
  definitions and queries that worked.
- **Governed execution** — takes what an agent produced (a named metric, or one validated
  read-only SQL statement, or a document request), enforces the asker's access, executes
  it, returns rows or passages **with provenance / citation**, and **audits** the access.

Exposed as an **MCP server**. The only model it uses is an embedder for retrieval —
otherwise deterministic by design.

### The agent — the copilot (where the reasoning lives)

Turns a question into an answer by *consuming* the context layer: understand → recall →
plan → generate → execute → investigate → verify → synthesize → act → write-back.
Deliberately thin in machinery; the intelligence it leans on lives in the layer beneath.

## Engine-core vs. ports vs. the agent

- **Engine-core** — reusable, domain-agnostic agent machinery (kernel, middleware seam,
  sub-agent isolation, verification, HITL mechanism, memory, eval runner) + the
  MCP-server scaffold.
- **Ports** — the context layer's substrate-specific seams: `DataSource`,
  `SemanticContext`, `Grounding`, `ActionSurface`, `Identity/Governance`, `Oracle`.
- **The agent** — the reasoning that consumes the ports through the engine-core.

Seams now (dependency injection, small stable surfaces, boundary tests); shared
abstractions only at the third real use.

## Code structure (target)

```
src/klarova/
  core/          # engine-core: build_agent, config, model, context, sub-agent, registry
  middleware/    # the composition seam: situation, verification, HITL, summarization
  tools/         # thin LLM-facing tool definitions the agent calls
  warehouse/     # context layer · DataSource: governed execution + SQL guard + provenance
  semantic/      # context layer · SemanticContext: governed metric definitions + compiler
  retrieval/     # context layer · Grounding: corpus loader + hybrid index + doc citations
  mcp/           # engine-core: the context layer served as an MCP server
  storage/       # context layer: memory store + recall
  connectors/    # agent: MCP integration for host actions
  eval/          # engine-core + oracles: per-capability tests + cross-model regression
  cli.py         # development REPL
apps/acme-analytics/   # the host app (FastAPI + a small UI)
data/                  # warehouse, doc corpus, indexes, eval sets (git-ignored)
```

> Directories are created as the build reaches the module that needs them — not stubbed
> ahead of use.

## Modules

Filled in as each lands.

- **M1 Foundation** (engine-core) — _pending: skeleton._
