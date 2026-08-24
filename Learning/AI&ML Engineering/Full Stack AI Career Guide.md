
## TL;DR

- **Your fastest path is "AI Engineer" (the applied-LLM builder), not "ML Engineer."** The highest-demand, highest-ROI skills are, in order: LLM API integration, RAG (retrieval-augmented generation) with embeddings + vector DBs, agentic workflows/tool-calling, and evaluation/observability. Your existing Next.js/Node/NestJS/PostgreSQL/AWS stack is a genuine advantage — pgvector on your existing Postgres and the Vercel AI SDK in TypeScript let you ship credible AI apps without leaving your ecosystem.
- **DeepLearning.AI is best used as a concept primer, not a credential.** Only ONE of its short courses is JavaScript-native ("JavaScript RAG Web Apps with LlamaIndex"); nearly all others are Python-first. Take a focused sequence of ~8 short courses for concepts, but pair each with a hands-on build in your own stack.
- **The single most important deliverable is 2–3 deployed, well-documented projects** that show production instincts — not another "ChatGPT wrapper." AI-skilled roles command a meaningful salary premium (PwC's 2025 Global AI Jobs Barometer put it at 56%, up from 25% the prior year; Levels.fyi shows ~12% at mid-level within the same company).

## Key Findings

### The market is hiring "AI Engineers" who build on top of pretrained models

The role you want is the applied AI engineer: someone who integrates LLMs via API, ships RAG pipelines, writes evals, manages cost and latency, and owns agentic flows end-to-end — not the research-heavy ML engineer track requiring deep math, PyTorch, and model training.

Per Lightcast/Stanford AI Index 2025: "In 2024, more than 66,000 postings specifically mentioned generative AI as a skill, up from 16,000 in 2023." Community sentiment on Blind and Reddit confirms SWEs are already transitioning, and the role is "mostly building applications around LLMs using RAG, fine tuning models, creating platforms and tooling around LLMs."

### The recurring tech stack in job postings

- **Languages:** Python or TypeScript. A hybrid TS-product-layer + Python-AI-layer profile is the most versatile.
- **LLM SDKs:** OpenAI, Anthropic, Google Gemini, Cohere.
- **Frameworks:** LangChain, LangGraph, LlamaIndex; Vercel AI SDK for TypeScript.
- **Vector DBs:** Pinecone, pgvector, Weaviate, Qdrant, Chroma, FAISS, Milvus.
- **Embeddings:** OpenAI text-embedding-3, Cohere, sentence-transformers; hybrid search + re-ranking.
- **Evaluation/observability:** LangSmith, Ragas, DeepEval, Langfuse, Arize Phoenix, Braintrust, Helicone.
- **Agentic/MCP:** LangGraph, AutoGen, CrewAI; Model Context Protocol (MCP).
- **Deployment:** FastAPI or Node/Next API routes, Docker, AWS/GCP/Vercel, cost/latency monitoring.

Strong resume bullet example: "Built a RAG chatbot over 380K internal support docs using pgvector + OpenAI text-embedding-3-large; retrieval precision at k=5 reached 87% after hybrid search + re-ranking."

### MCP and agentic workflows are the fastest-rising skills

MCP was open-sourced by Anthropic on November 25, 2024, adopted by OpenAI, Google, and Microsoft within months, and donated to the Agentic AI Foundation under the Linux Foundation on December 9, 2025. Per Anthropic's December 2025 announcement: "over 10,000 public MCP servers are now active," with 97 million monthly SDK downloads.

### RAG vs. fine-tuning

**RAG is the priority skill, not fine-tuning.** RAG is cheaper to start, more inspectable, handles dynamic data. "Prompt Engineering + RAG is the sweet spot"; fine-tune only when you truly need expert-level specialization.

### DeepLearning.AI: strengths, limits, and the JS caveat

Short courses (1–2 hrs each) are good concept primers but passive — one developer completed 8 courses and "couldn't build a simple RAG pipeline from scratch." Only ONE JS-native course exists: "JavaScript RAG Web Apps with LlamaIndex" (Laurie Voss). Everything else is Python-first; rebuild concepts in your own stack afterward.

### Salary/demand signal

- **PwC 2025 Global AI Jobs Barometer:** 56% wage premium for AI skills (up from 25% prior year); 2026 Barometer updated to 62%.
- **Lightcast "Beyond the Buzz" (2025):** AI-skill postings offer 28% higher salaries (~$18,000/year more); 43% premium with 2+ AI skills.
- **Levels.fyi Q3 2025:** ~12% premium at mid-level, ~19% at Staff+, within same company.
- **Pay is volatile:** median US AI engineer total pay swung from $295K (Mar 2024) to $228,500 (Jan 2025) to $277K (Mar 2025) per Levels.fyi. ZipRecruiter reports a lower ~$101,752/year average. Treat top-end numbers cautiously.

## Details: The Prioritized Roadmap

### Guiding principle

Rank topics by hiring demand × your leverage from existing skills. Weight toward the JS/TS-native AI stack, with just enough Python to be credible.

### DeepLearning.AI Courses → Projects Mapping

| Order    | Course                                            | Instructor(s)                          | Maps to Project                       |
| -------- | ------------------------------------------------- | -------------------------------------- | ------------------------------------- |
| 1        | ChatGPT Prompt Engineering for Developers         | Isa Fulford + Andrew Ng                | Foundation — needed before A          |
| 2        | Building Systems with the ChatGPT API             | Isa Fulford + Andrew Ng                | Foundation — needed before A          |
| 3        | LangChain: Chat with Your Data                    | Harrison Chase                         | **Project A** (RAG)                   |
| 4        | Building and Evaluating Advanced RAG Applications | Jerry Liu + Anupam Datta               | **Project A** (RAG + evals)           |
| 5        | Building Applications with Vector Databases       | Pinecone (DeepLearning.AI partnership) | **Project A** (vector DB concepts)    |
| 6        | JavaScript RAG Web Apps with LlamaIndex           | Laurie Voss                            | **Project A** (only JS-native course) |
| 7        | Functions, Tools and Agents with LangChain        | Harrison Chase                         | **Project B** (tool-calling)          |
| 8        | AI Agents in LangGraph                            | Harrison Chase + Rotem Weiss           | **Project B** (orchestration)         |
| 9        | Agentic AI                                        | Andrew Ng                              | **Project B** (planning/multi-agent)  |
| 10       | Evaluating AI Agents                              | Arize AI (Gilhuly + Khan)              | **Project C** (evals microservice)    |
| 11       | Evaluating and Debugging Generative AI            | Weights & Biases                       | **Project C** (evals microservice)    |
| 12       | MCP: Build Rich-Context AI Apps with Anthropic    | Elie Schoppik (Anthropic)              | **Project D** (MCP server)            |
| 13       | Serverless LLM Apps with Amazon Bedrock           | Mike Chambers (AWS)                    | Deployment — any project              |
| Optional | Finetuning Large Language Models                  | Sharon Zhou (Lamini)                   | Conceptual only                       |
| Optional | AI Python for Beginners                           | Andrew Ng                              | Only if Python is rusty               |

**How to use it:** take each course (concepts only, 1-2 hrs), then immediately rebuild the concept in the matching project. Courses 1-6 → Project A. 7-9 → Project B. 10-11 → Project C. 12 → Project D. Course language doesn't matter — the project's target stack is what you actually build in.

### Tier 1 — Core, do first (highest demand, immediate leverage)

**1. LLM API fundamentals + prompt engineering.** (Courses 1-2.) Build: a Next.js route streaming responses via the **Vercel AI SDK** with OpenAI/Anthropic providers.

**2. RAG + embeddings + vector databases.** (Courses 3-6.) Build: RAG over your own documents using **pgvector on PostgreSQL** — your biggest unfair advantage. Add chunking, hybrid search, re-ranking. Reference: Vercel's `ai-sdk-rag` template.

**3. Tool-calling / function-calling and structured outputs.** (Course 7.) Build: an AI chat feature calling real tools/DB queries, returning typed JSON.

### Tier 2 — Differentiators (rising fast, strong signal)

**4. Agentic workflows / orchestration.** (Courses 8-9.) Build: a multi-step agent with persistence, human-in-the-loop, failure recovery.

**5. Evaluation & observability.** (Courses 10-11.) Instrument with **LangSmith**/Langfuse, run **Ragas**/DeepEval, track cost/p95 latency. Put trace screenshots and eval scores in your README.

**6. MCP (Model Context Protocol).** (Course 12.) Build: a small MCP server (Node/TS SDK) exposing one of your APIs; connect to Claude Desktop or an agent.

### Tier 3 — Round out / conceptual

**7. Fine-tuning vs RAG (mostly conceptual).** Learn when NOT to fine-tune.

**8. Just-enough Python + serverless AI deployment.** (Course 13 — pairs with your AWS background.)

### Suggested sequence (calendar)

- **Weeks 1–3:** Prompt eng + RAG concepts. Ship Project A (RAG SaaS) in TS.
- **Weeks 4–6:** Tools + agents. Ship Project B (agentic app).
- **Weeks 7–9:** Evals/observability + MCP. Retrofit evals into A/B; build Project C and D.
- **Weeks 10–12:** Fine-tuning concepts, Bedrock/serverless, polish, deploy, write up. Start applying once 2–3 projects are live — don't wait for "AI-complete."

## Portfolio Projects (leverage your existing stack)

Build 2–3 deeply rather than many shallow ones. Deploy each, document decisions, add evals, handle errors, track cost/latency.

**Stack split:** 3 of 4 projects stay TS-first (fastest to ship, strongest differentiator). One project deliberately uses Python — because evals/embeddings tooling (Ragas, DeepEval) is genuinely more mature there.

**Project A — RAG-powered SaaS over PostgreSQL/pgvector — TS (flagship).** Multi-tenant "chat with your knowledge base": Next.js + Vercel AI SDK frontend with streaming, NestJS/Node API, embeddings in **pgvector**. Chunking, hybrid search + re-ranking, citation tracking. Signal: "multi-document RAG with citation tracking, hybrid search, and evaluation metrics" separates strong candidates from wrapper demos.

**Project B — AI agent with tool-calling and orchestration — TS.** LangGraph.js or Vercel AI SDK agent primitives on Node/NestJS. Multi-step planning, real tool/API calls, persisted state, human-in-the-loop, failure recovery.

**Project C — Evals/embeddings microservice — Python (the one Python-touch project).** Small FastAPI service doing embedding generation + Ragas/DeepEval eval runs, called internally by Projects A/B (A sends chunks+queries, C returns groundedness/precision@k). Realistic polyglot-microservice pattern; gives genuine Python eval fluency. Tradeoff: two deployments + inter-service auth vs. embedding evals directly in A.

**Project D — MCP server + client integration — TS.** Node/TypeScript MCP SDK exposing one of your services, wired into an agent or Claude Desktop.

## Recommendations

1. **Commit to the AI Engineer track for near-term employability.** Save deep ML/math for Phase 2 (below).
2. **Learn the JS/TS-native AI stack first**, add just-enough Python via Project C.
3. **Treat DeepLearning.AI courses as concept primers, then immediately rebuild in your stack.**
4. **Ship Project A within ~3 weeks and deploy it publicly.** A deployed, evaluated project beats a dozen tutorials.
5. **Speak the production vocabulary in interviews:** retrieval precision@k, groundedness, p95 latency, cost per 1,000 queries.
6. **Consider the internal-transfer path** — proposing an AI feature at your current employer.

### Benchmarks that would change the plan

- Targeting frontier labs/ML-heavy roles → add real ML foundations, expect a longer runway.
- Target postings emphasize Python/FastAPI heavily → front-load Python, build Project A's backend in FastAPI.
- Target job ads repeatedly mention a specific vector DB → swap pgvector for that in one project.

## Caveats

- Salary figures vary widely (~$101K avg to ~$277K median total comp) and may be inflated; some pay volatility suggests a partial bubble.
- "AI Engineer" means at least five different jobs depending on the company — read each JD carefully.
- Course content ages fast; cross-check current docs.
- Certificates are weak signals; projects matter far more.
- Some sources are vendor/marketing blogs; salary specifics should be validated against live postings in your market.

---

## Phase 2 — Post-Hire / Long-Term: The Open-Weights Production System Project

_Start this once Phase 1 (Projects A-D) has landed you a role, or run it slowly alongside the ML Specialization once you're no longer under job-hunt time pressure. This is ML Infrastructure / Model Serving depth — a different skill axis than Phase 1's applied AI engineering, and it's a multi-month build, not a sprint._

**Source:** roadmap shared by a Senior AI Engineer (core ML background), community-sourced.

**Why it's Phase 2, not Phase 1:** Steps 1-3 and 10-13 require self-hosted GPU inference, quantization, distributed serving — skills most "AI Full Stack" job postings don't test for (they use hosted APIs). It also takes months by the author's own account, which conflicts with near-term employability.

**Progress note:** You've started the ML Specialization (Andrew Ng) and completed Course 1 — this project pairs naturally once you're past Course 2-3, since you'll have the math/model foundations to understand _why_ KV cache and quantization work, not just follow steps.

**The roadmap:**

1. Take a pretrained open-weights model, understand its inference path (what compute happens per generated token).
2. Build an inference server — serve via **vLLM** or **SGLang**, expose an API, support multiple users.
3. Understand inference performance — batching, KV cache, quantization, GPU memory, scheduling, speed/cost/quality tradeoffs.
4. Build the backend — users, auth, chat history, DB, caching, rate limits, error handling, security.
5. Build a chat product frontend — streaming responses, conversation + history management.
6. Add RAG — load documents, retrieve, pass context to the model.
7. Add tool-calling and an agent loop.
8. Add evaluation and monitoring — answer/retrieval quality, latency, errors, token usage, GPU usage, cost.
9. Add reliability/safety — auth, retries, timeouts, failure handling, data isolation, prompt injection defense, safe tool use.
10. Deploy — cloud GPU, containerized, understand inter-service communication in production.
11. Load-test — find bottlenecks, improve throughput/latency/GPU utilization/cost.
12. Scale — multiple model servers, multi-GPU, distributed inference.
13. Automate the lifecycle — testing, model versioning, pre-deploy eval, auto-deploy, monitoring, rollback.
14. Iterate by hypothesis, not tutorial — diagnose bottlenecks yourself before searching for help.

**Overlap note:** Steps 4-9 substantially overlap with Phase 1 Projects A/B/C — that work isn't wasted, it transfers directly.