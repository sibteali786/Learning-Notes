# Quiz Session Instructions

When the user starts a practice session in this folder (e.g. "quiz me", "let's drill numbers"):

## Setup
1. Read `progress.md` in full. Build a queue: all topics where `next_review_date <= today`, sorted oldest-due first.
2. If fewer than ~4 due topics, top up the queue with unpracticed topics (`repetitions == 0`) not already due.
3. Deprioritize `mastered: true` topics unless nothing else is due — they can still show up occasionally.

## Loop (repeat ~8-12 times, or until user says stop)
1. Pick next topic from queue. Read the matching section in `numbers.md` and pull a pattern from `drills.md` for that topic. Instantiate ONE concrete scenario question — plug in real numbers/context, don't paste the pattern template verbatim. Alternate recall vs. applied where the queue allows.
2. Ask that one question. Wait for the user's answer before continuing — never ask multiple questions in one turn.
3. Grade the answer:
   - State correct/incorrect (or "close" for right-order-of-magnitude but off on specifics).
   - Give the correct number with 1-2 sentences of reasoning, citing numbers.md.
   - If it was an [Applied] estimation question, walk the dimensional analysis briefly if the user's chain was off.
4. Ask the user to self-rate difficulty 0-5 (0=blackout, 3=correct but effortful, 5=instant/easy).
5. Update `progress.md`:
   - Apply SM-2 math per the rules documented at the top of progress.md, using the self-rating as `q`.
   - Update `interval_days`, `repetitions`, `ease_factor`, `next_review_date`, `last_result`, `mastered`.
   - Append a row to the History Log table (date, topic, question paraphrase, user's answer, correct?, rating, notes).
6. Move to next queued topic.

## Ending
Stop when the user says stop, or after a reasonable session (~8-12 questions). Give a short summary:
- Topics nailed (high ratings / correct)
- Topics still weak (low ratings / incorrect / reset repetitions)
- Upcoming `next_review_date`s in the next 7 days, so the user knows what's coming

## Notes
- Keep questions scenario-style per drills.md conventions — never phrase as "what is the latency of X."
- If the user's answer references a number not in numbers.md, prefer numbers.md as ground truth; if genuinely unsure/outdated, say so rather than guessing.
- Don't ask about progress.md/drills.md file format — just use them as data.
