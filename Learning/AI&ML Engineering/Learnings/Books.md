Great question — and you've identified the right pain point. **Evals (evaluation) is genuinely the hardest part** of agent development. Here's a structured reading path using your O'Reilly subscription:

---

## 📚 Recommended Learning Path

### Phase 1 — Foundation (Start Here)

|Resource|Why|
|---|---|
|**Hands-On Large Language Models** — Jay Alammar (O'Reilly, 2024)|Visual, intuitive approach — builds the mental model of how LLMs behave under different conditions, which matters when designing agents that need to reason, plan, and use tools consistently.|
|**AI Engineering** — Chip Huyen (O'Reilly, 2025)|Rated 4.7 on Amazon — covers building applications with foundation models end-to-end, the most practical applied ML work from one of the clearest voices in the field.|

### Phase 2 — Agent-Specific

|Resource|Why|
|---|---|
|**AI Agents in Action** — Micheal Lanham (Manning/O'Reilly, 2025)|Focused entirely on agentic patterns — tool use, memory, orchestration|
|**LLMOps** (O'Reilly)|Covers monitoring LLM performance when traditional metrics don't tell the whole story, plus setting up evaluations, governance, and security audits that actually matter for GenAI.|

### Phase 3 — Evals (Your Key Gap)

|Resource|Why|
|---|---|
|**Evals for AI Engineers** (O'Reilly, upcoming)|Purpose-built for this — covers error analysis, synthetic data generation, automated LLM-as-a-judge systems, production monitoring, and cost optimization. Designed for engineers building real AI products.|

---

## 🎯 On Evals Specifically

The core trap is "vibe-check development" — the agent appears to work well, but the moment it's modified, you can't establish that it's still working correctly. The right mental model: use **code-based evals for deterministic failures**, and an **LLM-as-a-judge for subjective cases**.

The two main approaches:

- **Code assertions** — did the agent call the right tool? did it return valid JSON? did it complete in N steps?
- **LLM-as-judge** — did the response sound correct, grounded, on-tone?

---

## 🔀 Alternate Approach (non-O'Reilly)

- **[Jurafsky & Martin — Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3)** — Free online, updated through 2025–2026 with new chapters specifically on agents, evaluation, and safety. Great complement to O'Reilly content.
- **Hamel Husain's course — "AI Evals For Engineers & PMs"** — Taught by a former ML engineer from Airbnb and GitHub, specifically structured around practical eval workflows.

---

**My suggested order for you specifically** (given your background integrating into apps):

1. _AI Engineering_ (Chip Huyen) — big picture
2. _Hands-On LLMs_ (Alammar) — intuition building
3. _LLMOps_ — operationalizing agents
4. _Evals for AI Engineers_ — your stated gap