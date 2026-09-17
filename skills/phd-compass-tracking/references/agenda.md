# Agenda

What is overdue, due soon, and missing, across the whole search.

## 1. Collect every dated item
- Run `compass.py agenda <save> --days <N> --today <date>` (N = 30 unless the owner asks otherwise). It covers target next actions and deadlines, scholarship deadlines, calls and standalone actions.
- Add the Markdown-only items the script cannot see:
  - **Outreach:** `sent` emails whose follow-up date has arrived with no reply.
  - **Referees:** letters requested but not confirmed as submitted, with the deadline they serve.
  - **Submissions:** applications with a stated decision date that has passed without news.
  - **Interviews:** upcoming interviews and pending thank-you notes.

Done when every dated item in the data block and in those four sections is classed as overdue, inside the window, or later.

## 2. Flag gaps
- Overdue items.
- Active targets with a deadline but no next action, or a next action with no date.
- `standing` or `upcoming` positions and programmes not checked in the last 4 weeks (look at the latest access date in their links).
- Open ads whose closing dates have all passed (the script flags these).
- Materials checklist rows not `ready` that a deadline inside the window needs.
- Eligibility checks still `check` on a target with a deadline inside the window.

## 3. Fix what can be fixed now
Update stale `pos` values (`open` → `past`), add missing next actions with the owner's agreement, and set statuses the owner confirms. Run `sync`.

## 4. Report
A short agenda:
- **Overdue**
- **This week**
- **Later in the window**
- **Gaps** (from step 2)
- **The three most important actions**, each with a date and why it comes first (a hard deadline beats a soft follow-up; a referee needs lead time).
