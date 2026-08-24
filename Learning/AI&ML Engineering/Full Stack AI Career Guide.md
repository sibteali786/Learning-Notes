# AI Full-Stack Engineer Roadmap: A Prioritized Curriculum for a TypeScript/React/Node Developer

## TL;DR
- **Your fastest path is "AI Engineer" (the applied-LLM builder), not "ML Engineer."** The highest-demand, highest-ROI skills are, in order: LLM API integration, RAG (retrieval-augmented generation) with embeddings + vector DBs, agentic workflows/tool-calling, and evaluation/observability. Your existing Next.js/Node/NestJS/PostgreSQL/AWS stack is a genuine advantage — pgvector on your existing Postgres and the Vercel AI SDK in TypeScript let you ship credible AI apps without leaving your ecosystem.
- **DeepLearning.AI is best used as a concept primer, not a credential.** Only ONE of its short courses is JavaScript-native ("JavaScript RAG Web Apps with LlamaIndex"); nearly all others are Python-first. Take a focused sequence of ~8 short courses for concepts, but pair each with a hands-on build in your own stack, because interviewers weigh a deployed project far more than a completion certificate.
- **The single most important deliverable is 2–3 deployed, well-documented projects** that show production instincts (retrieval quality, evals, error handling, cost/latency tracking) — not another "ChatGPT wrapper." AI-skilled roles command a meaningful salary premium (PwC's 2025 Global AI Jobs Barometer put it at 56%, up from 25% the prior year; Levels.fyi shows ~12% at mid-level within the same company), so the effort pays off.

## Key Findings

### The market is hiring "AI Engineers" who build on top of pretrained models
The role you want is the applied AI engineer: someone who integrates LLMs via API, ships RAG pipelines, writes evals, manages cost and latency, and owns agentic flows end-to-end. This is explicitly the largest and most overloaded AI job category, and it is the natural destination for a full-stack developer — not the research-heavy ML engineer track that requires deep math, PyTorch, and model training.

Demand is real and growing. Per the Lightcast/Stanford AI Index 2025: "In 2024, more than 66,000 postings specifically mentioned generative AI as a skill, up from 16,000 in 2023. Mentions of large language modeling grew from 5,000 to 20,000, while demand for prompt engineering rose from 1,400 to nearly 6,300 postings." Community sentiment on Blind and Reddit confirms that SWEs who "problem solve and communicate well with customers are already making that transition," and that the role is "mostly building applications around LLMs using RAG, fine tuning models, creating platforms and tooling around LLMs."

### The recurring tech stack in job postings (what to actually learn)
Across job postings (ZipRecruiter, Lemon.io, itjobswatch, agentic job boards) and resume analyses, the same stack recurs:
- **Languages:** Python or TypeScript. TypeScript is fully viable when "AI is one feature inside a full-stack product and your team already works in Node." A hybrid TS-product-layer + Python-AI-layer profile is the most versatile.
- **LLM SDKs:** OpenAI, Anthropic, Google Gemini, Cohere.
- **Frameworks:** LangChain, LangGraph, LlamaIndex (Python and JS/TS versions exist); Vercel AI SDK for TypeScript.
- **Vector DBs:** Pinecone, pgvector, Weaviate, Qdrant, Chroma, FAISS, Milvus.
- **Embeddings:** OpenAI text-embedding-3, Cohere, sentence-transformers; plus hybrid search + re-ranking.
- **Evaluation/observability:** LangSmith, Ragas, DeepEval, Langfuse, Arize Phoenix, Braintrust, Helicone.
- **Agentic/MCP:** LangGraph, AutoGen, CrewAI; Model Context Protocol (MCP).
- **Deployment:** FastAPI (Python) or Node/Next API routes, Docker, AWS/GCP/Vercel, plus cost/latency monitoring.

A representative strong junior AI engineer resume bullet from a 2026 ATS analysis: "Built a RAG chatbot over 380K internal support docs using pgvector + OpenAI text-embedding-3-large; retrieval precision at k=5 reached 87% after hybrid search + re-ranking." That's the level of specificity that gets callbacks.

### MCP and agentic workflows are the fastest-rising skills
Model Context Protocol (MCP) was introduced and open-sourced by Anthropic on November 25, 2024 (created by Anthropic engineers David Soria Parra and Justin Spahr-Summers). It was adopted by OpenAI, Google, and Microsoft within months and donated to the newly-formed Agentic AI Foundation (AAIF) under the Linux Foundation on December 9, 2025 — with platinum members AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, and OpenAI. Adoption is striking: per Anthropic's December 2025 announcement, "over 10,000 public MCP servers are now active," with 97 million monthly SDK downloads across Python and TypeScript, and Anthropic CPO Mike Krieger calling it "the industry standard for connecting AI systems to data and tools."

"Agent orchestration, MCP integration, eval design, prompt engineering, vector DB/RAG, cost optimization, safety/guardrails, computer-use deployment, production observability, and frontier-model fluency" are cited as the 2026 must-have screen — the plain "LangChain + Pinecone resume no longer signals production readiness."

### RAG vs. fine-tuning: what to emphasize
For a full-stack engineer, **RAG is the priority skill, not fine-tuning.** The consensus across IBM, practitioner blogs, and Reddit/Dev.to: RAG is cheaper to start, more inspectable, handles dynamic/changing data, and is the "first foray" for most LLM apps. Fine-tuning is for fixed domains, consistent style/format, and lower inference cost at high upfront cost. For most applications, "Prompt Engineering + RAG is the sweet spot"; use fine-tuning only when you truly need expert-level specialization. Learn RAG deeply; understand fine-tuning conceptually and be able to articulate the tradeoff in an interview.

### DeepLearning.AI: strengths, limits, and the JS caveat
DeepLearning.AI short courses are genuinely high-quality concept primers (1–2 hours each, free to access; graded assignments and certificates require the paid Pro tier). But two important caveats:
1. **They are passive.** You watch pre-built Jupyter notebooks run. One reviewer documented a developer who completed 8 short courses, then "couldn't build a simple RAG pipeline from scratch." The fix: rebuild every concept in your own stack.
2. **They are almost all Python.** Only ONE JavaScript-native course exists: "JavaScript RAG Web Apps with LlamaIndex" (Laurie Voss, LlamaIndex/npm co-founder), which builds a full-stack JS app with a backend API + React frontend and streaming chat. Everything else — LangChain, LangGraph, MCP, RAG, agents, fine-tuning — is Python-first. This is fine for learning concepts, but for hands-on JS/TS you'll supplement with the Vercel AI SDK docs/templates and LangChain.js/LlamaIndex.TS.

Also note some courses reference 2022–2023 model names and the pre-late-2023 OpenAI SDK, so cross-reference current docs when coding.

### Salary/demand signal
- **PwC's 2025 Global AI Jobs Barometer** (*The Fearless Future*, released June 3, 2025, analyzing ~1 billion job ads across 24 countries): "Workers with AI skills like prompt engineering command a 56% wage premium (up from 25% last year)." PwC's 2026 Barometer later updated this to 62%.
- **Lightcast "Beyond the Buzz"** (July 23, 2025, 1.3 billion postings): "job postings including AI skills offer 28% higher salaries—nearly $18,000 more per year." Postings listing two or more AI skills carried a 43% premium.
- **Levels.fyi Q3 2025** (within-company, same-level comparison): AI premium of ~6% entry, ~12% at Engineer/L4, ~14% at Senior/L5, ~19% at Staff/L6+.
- **Absolute pay varies hugely by source.** Levels.fyi's Q3 2025 trend report shows median US AI engineer total pay "peaked at $295K in March 2024, fell 22% to $228,500 by January 2025, then rebounded to $277K by March 2025" — evidence the premium is real but volatile. At the low end, ZipRecruiter (Dec 2025) reports a US average of ~$101,752/year, with $116,500 at the 75th percentile. Frontier labs pay far more (equity-driven). Treat top-end numbers cautiously — commentators openly debate a partial bubble.

## Details: The Prioritized Roadmap

### Guiding principle
Rank topics by **hiring demand × your leverage from existing skills.** You already have TypeScript, React, Next.js, Node, NestJS, PostgreSQL, MongoDB, and AWS — so weight the roadmap toward the JS/TS-native AI stack and layer in just enough Python to be credible.

### Tier 1 — Core, do first (highest demand, immediate leverage)
**1. LLM API fundamentals + prompt engineering.** Structured outputs, system prompts, function/tool calling, streaming, retries, token/cost awareness.
- DeepLearning.AI: **ChatGPT Prompt Engineering for Developers** (Isa Fulford + Andrew Ng, ~1.5h) → **Building Systems with the ChatGPT API** (Isa Fulford + Andrew Ng).
- Build in your stack: a Next.js route that streams responses via the **Vercel AI SDK** with the OpenAI and Anthropic providers (the AI SDK is TypeScript-native and integrates directly with Next.js/Node — your home turf).

**2. RAG + embeddings + vector databases** (the single most in-demand skill).
- DeepLearning.AI: **LangChain: Chat with Your Data** (Harrison Chase) → **Building and Evaluating Advanced RAG Applications** (Jerry Liu + Anupam Datta) → **Building Applications with Vector Databases** (Pinecone partnership).
- JS-native option: **JavaScript RAG Web Apps with LlamaIndex** (Laurie Voss) — the one course fully in your language.
- Build in your stack: RAG over your own documents using **pgvector on PostgreSQL** (you already know Postgres — this is your biggest unfair advantage). Add chunking strategy, hybrid search, and re-ranking. Vercel's official `ai-sdk-rag` template (Next.js + AI SDK + Drizzle + Postgres) is a strong starting reference.

**3. Tool-calling / function-calling and structured outputs.**
- DeepLearning.AI: **Functions, Tools and Agents with LangChain** (Harrison Chase).
- Build: an AI chat feature that calls real tools (DB queries, external APIs) and returns typed/structured JSON.

### Tier 2 — Differentiators (rising fast, strong signal)
**4. Agentic workflows / orchestration.**
- DeepLearning.AI: **AI Agents in LangGraph** (Harrison Chase + Rotem Weiss); plus Andrew Ng's newer **Agentic AI** course (Reflection, Tool Use, Planning, Multi-Agent patterns).
- Build: a multi-step agent with persistence, human-in-the-loop, and failure recovery.

**5. Evaluation & observability** (what separates "shipped a demo" from "production engineer").
- DeepLearning.AI: **Evaluating AI Agents** (Arize AI — John Gilhuly & Aman Khan); **Evaluating and Debugging Generative AI** (Weights & Biases).
- Tools: instrument with **LangSmith** (or Langfuse), run **Ragas**/DeepEval on a test set, track token cost and p95 latency. Put a LangSmith trace screenshot and Ragas scores in your project README — practitioners explicitly recommend this as an interview signal.

**6. MCP (Model Context Protocol).**
- DeepLearning.AI: **MCP: Build Rich-Context AI Apps with Anthropic** (Elie Schoppik, Anthropic — Python-based).
- Build: a small MCP server exposing one of your existing APIs/tools; connect it to Claude Desktop or an agent. (Note the TypeScript MCP SDK exists, so you can build the server in Node.)

### Tier 3 — Round out / conceptual (know the tradeoffs; go deep only if targeting these)
**7. Fine-tuning vs RAG (mostly conceptual for you).**
- DeepLearning.AI: **Finetuning Large Language Models** (Sharon Zhou, Lamini). Learn when NOT to fine-tune.

**8. Just-enough Python + serverless AI deployment.**
- DeepLearning.AI: **AI Python for Beginners** (Andrew Ng) if your Python is rusty; **Serverless LLM apps with Amazon Bedrock** (Mike Chambers, AWS) — pairs directly with your AWS experience.

### Suggested sequence (calendar)
- **Weeks 1–3:** Tier 1.1–1.2 (prompt eng + RAG). Ship Project A (RAG SaaS) in TS.
- **Weeks 4–6:** Tier 1.3 + Tier 2.4 (tools + agents). Ship Project B (agentic app).
- **Weeks 7–9:** Tier 2.5–2.6 (evals/observability + MCP). Retrofit evals + tracing into Projects A/B; build an MCP server.
- **Weeks 10–12:** Tier 3 (fine-tuning concepts, Bedrock/serverless) + polish, deploy, write up. Start applying once 2–3 projects are live.

## Portfolio Projects (leverage your existing stack)
Build 2–3 of these deeply rather than many shallow ones. For each: deploy it, document architecture decisions, add evals, handle errors gracefully, and track cost/latency.

**Stack split:** 3 of 4 projects stay TS-first (your strongest differentiator, fastest to ship). One project deliberately uses Python — not for its own sake, but because evals/embeddings tooling (Ragas, DeepEval) is genuinely more mature there, which is exactly the kind of judgment call interviewers want to see.

**Project A — RAG-powered SaaS over PostgreSQL/pgvector — TS (highest priority, flagship).**
A multi-tenant "chat with your knowledge base" app: Next.js + Vercel AI SDK frontend with streaming, NestJS/Node API, embeddings stored in **pgvector** on your existing Postgres. Add document chunking, hybrid search + re-ranking, citation tracking. This directly maps to the most-requested skill and shows off your Postgres depth. Signal: "multi-document RAG with citation tracking, hybrid search, and evaluation metrics" is explicitly what recruiters say separates strong candidates from API-wrapper demos.

**Project B — AI agent with tool-calling and orchestration — TS.**
LangGraph.js or Vercel AI SDK agent primitives on a Node/NestJS backend. Plans multi-step tasks, calls your real tools/APIs, persists state, supports human-in-the-loop, and recovers from failures. Hiring-manager signal: "builds agents that recover from failures and maintain state. Not a one-shot demo."

**Project C — Evals/embeddings microservice — Python (the one Python-touch project).**
A small, deliberately-scoped **FastAPI** service that does embedding generation and runs **Ragas/DeepEval** evaluation suites, exposed as an internal API that Projects A and B call (e.g., A sends retrieved chunks + queries, C returns groundedness/precision@k scores). This is a realistic polyglot-microservice pattern, not Python-for-its-own-sake — it gives you genuine fluency in the Python eval ecosystem to speak to in interviews, while keeping the app layer in TS. Tradeoff: adds integration work (auth between services, two deployments) vs. embedding evals directly into A, but it's a cleaner, more production-like story.

**Project D — MCP server + client integration — TS.**
Expose one of your services as an MCP server using the **Node/TypeScript MCP SDK** and wire it into an agent or Claude Desktop. The TS SDK is first-class here, so this stays in your primary stack and is a differentiator most candidates don't have yet.

## Recommendations
1. **Commit to the AI Engineer track, not ML research.** Don't burn months on the Deep Learning Specialization / heavy math unless targeting research roles. Your leverage is shipping production LLM apps.
2. **Learn the JS/TS-native AI stack first** (Vercel AI SDK, LangChain.js/LlamaIndex.TS, pgvector) so you can build fast in your own ecosystem, and add **just-enough Python** (AI Python for Beginners + one FastAPI exercise) so you're not filtered out of Python-first postings.
3. **Treat DeepLearning.AI courses as ~90-minute concept primers, then immediately rebuild each concept from a blank file in your stack.** Do not stack certificates hoping they signal skill — they don't, on their own.
4. **Ship Project A (RAG on pgvector) within ~3 weeks and deploy it publicly.** Then add evals/observability before moving on. A deployed, evaluated, documented project beats a dozen tutorials.
5. **Instrument everything and speak the production language in interviews:** retrieval precision@k, groundedness, p95 latency, cost per 1,000 queries, failure modes. This is the exact vocabulary hiring managers screen for.
6. **Consider the internal-transfer path.** Multiple experienced engineers note the easiest transition is proposing/building an AI feature at your current employer — lower interview barrier, real production experience.

### Benchmarks that would change the plan
- If you target **frontier labs or ML-heavy roles**, add real ML foundations (Deep Learning Specialization, PyTorch) — but expect a longer runway and heavier math.
- If your target postings emphasize **Python/FastAPI** heavily, front-load Python and build Project A's backend in FastAPI instead of Node.
- If you see repeated mentions of a specific vector DB (e.g., Pinecone or Weaviate) in your target job ads, swap pgvector for that in one project to match keywords.

## Caveats
- **Salary figures vary widely and may be inflated.** Sources range from ~$101K average (ZipRecruiter) to ~$277K median total comp (Levels.fyi, which skews toward Big Tech). The AI premium is real but some commentators flag a possible bubble given the pay volatility (a 22% swing in under a year) and $1B+ outlier offers. Treat top-end numbers as aspirational, not typical.
- **"AI Engineer" means at least five different jobs** depending on the company (applied LLM dev, ML infra, LLMOps, forward-deployed engineer, etc.). Read each JD carefully; the roadmap above targets the applied-LLM-dev flavor, which best fits your background.
- **The field moves fast and course content ages.** DeepLearning.AI courses may reference outdated SDKs/models; always cross-check current official docs.
- **Certificates are weak signals.** Interviewers at AI-forward companies know the DeepLearning.AI format; projects and the ability to explain decisions matter far more.
- **Some sources cited are vendor/marketing blogs** (course aggregators, recruiting firms, tool vendors). I've prioritized primary sources (deeplearning.ai, Lightcast, Levels.fyi, PwC, Anthropic, official docs) where possible, but demand/salary specifics should be validated against live job postings in your target market.

#### DeepLearning.AI Courses → Projects Mapping

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

**How to use it:** take each course (concepts only, 1-2 hrs), then immediately rebuild the concept in the matching project. Courses 1-6 → Project A. 7-9 → Project B. 10-11 → Project C. 12 → Project D. Course language doesn't matter — the project's target stack (TS or Python, per the split above) is what you actually build in.



