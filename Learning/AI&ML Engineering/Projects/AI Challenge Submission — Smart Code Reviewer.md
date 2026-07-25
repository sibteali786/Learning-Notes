
## Repository

Public GitHub repo: https://github.com/sibteali786/go-code-reviewer.git

---

## Why This Approach

The challenge explicitly allows lightweight tools, ChatGPT, Colab, Streamlit and
expects roughly 30-60 minutes. I chose to build a real Go CLI instead, for a few
deliberate reasons:

1. **Go is this team's stack.** The JD is explicit that Golang is the primary language
   for this role. A prompt in ChatGPT shows I can write a prompt; a working Go CLI shows
   I can write Go, structure a project, and make an abstraction decision (the `Provider`
   interface) that would actually hold up if this were a real internal tool, not just a
   one-off demo.
2. **A code reviewer is a natural fit for a small backend tool, not just a prompt.**
   The task is inherently about structure — reading a file, calling a model, parsing its
   output into something a reviewer can act on. That's a CLI's job, not a chat
   transcript's job.
3. **I scoped it down on purpose, not by accident.** I started from a much larger plan
   (two LLM providers, `git diff` mode, CI, Docker, GoReleaser, a GitHub Action
   wrapper) and deliberately cut it to what one person can build and demo end-to-end in
   a single sitting — documenting what I cut and why, rather than either over-building
   past a reasonable time box or quietly shipping something half-finished. For a role
   that includes on-call and production reliability, I think that scoping judgment is
   worth showing alongside the code itself.

I did use AI heavily to build this, pairing with Claude Code to scaffold the project,
catch real bugs as I typed each file myself (a struct/interface mixup, a broken ANSI
escape sequence, a missing import, a Go-specific assumption baked into the prompt that
didn't belong there), and to push back on scope before I started coding. That process is
itself an answer to "how do you think with AI": not asking it to write the whole thing
unsupervised, but using it as a reviewer and sounding board while I did the actual coding myself.

---

**Screenshot:**
![[Pasted image 20260714215620.png]]
![[Pasted image 20260714215710.png]]
**Output:**

```markdown
➜  go-code-reviewer git:(main) ✗ ./bin/reviewer --file testdata/bad_sample.go --format markdown
Reviewing with ollama/qwen3:8b... done.
# Code Review Report

## Readability

- **Line 14**: Nested conditionals can be hard to follow
  - *Suggestion*: Refactor into separate functions for each mode

## Structure

- **Line 21**: Error handling is missing for os.Open
  - *Suggestion*: Check if f is nil before using it
- **Line 30**: The data slice is modified but not used elsewhere
  - *Suggestion*: Consider removing or using the data slice appropriately

## Maintainability

- **Line 25**: Hardcoded buffer size may not be suitable for all cases
  - *Suggestion*: Use a more flexible buffer size or reader

## Strengths

- Clear variable names
- Simple logic flow
```

---

## Summary

I built a Go CLI that reviews code for readability, structure, and maintainability
using a local LLM (Ollama/qwen3:8b), chosen because Go is your team's primary stack plus building such tools with Python or Typescript where Ollama already has SDK available is not so challenging. The core design decision is a `Provider` interface with a name→constructor registry,so swapping or adding LLM backends (hosted APIs, other local models) requires no changes to the CLI, prompt, or output rendering, just one new file. The prompt is language agnostic by design, since the challenge didn't specify a language. Output renders as terminal or
markdown, always ending with a strengths section. Built and demoed end-to-end in a
timeboxed session.
