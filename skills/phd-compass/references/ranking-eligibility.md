# Triage, priority and eligibility

One consistent standard for every candidate, so priorities mean the same across scans.

## Class
- **keep**: passes every rule below.
- **maybe**: passes except for one open question; name it (`question` field). Example: "start date not stated", "funding after the current grant".
- **drop**: fails a rule; record the reason in the Scan log's dropped list.

## Rules
1. **Scope.** The main work matches one of the owner's ranked areas. Record the best-matching area as `area` and others as `tags`.
2. **Type of work.** Compare with the owner's preferred work type: `work` = `yes` (matches), `partly`, or `no`. A `no` caps the priority at C unless the owner said otherwise.
3. **Funding (positions and programmes).** Under the fully-funded rule, the source must state who pays and what is covered (salary or stipend; tuition where charged, including the international rate if the owner would pay it). Self-funded or "competition-funded only" is a drop, or a maybe when a named studentship competition exists. Set `fundingVerified: true` only when a page confirms it.
4. **Hiring signal (groups).** Record the evidence in `signalText` and bucket it in `signal` (definitions in `references/save-file.md`). Signals refer to the owner's start window: a grant ending before the window is `endsbefore`.
5. **Timing.** The earliest start must fit the owner's start window and come after the current degree ends. A position that must start before the degree is complete is a drop (record it in `ads` as `offfit` or `excluded`).
6. **Eligibility.** Check each line of the owner's Eligibility checklist against this target (mobility rule, fee status, language, visa, nationality restrictions, degree timing). Record `eligibility: {status, notes}`: `ok` when every line passes; `check` when any line depends on something unconfirmed (name it); `fail` when a line fails. A `fail` is a drop unless the owner wants it watched.

## Priority
| Pri | Positions and programmes | Groups (no open post) |
|---|---|---|
| **A** | Area rank 1–2, work type matches, funding verified, eligibility `ok` | Area rank 1–2, work type matches, signal `young` or `network` (or a standing call), eligibility `ok` |
| **B** | Good fit with exactly one open question (funding unverified, start date, one eligibility check), or area rank 3+ with everything else in order | Good fit with a weaker signal (`project`, `endsnear`, `none`) or one open question |
| **C** | Weaker fit worth remembering: `kind: "watch"` | Weaker fit, or work type `no`: `kind: "watch"` |

Unverified funding keeps a position or programme below A.

## Fit judgement (for target research)
Score 1–5 as a selection committee at that institution would see the owner:
- 5: the owner's strongest evidence matches the group's core methods and questions, and nothing is missing.
- 4: strong match with one gap a committee would forgive (for example a method they would train).
- 3: plausible, with a visible gap (no hands-on work in the core method, a neighbouring field).
- 2: a stretch: the case rests on motivation rather than evidence.
- 1: not competitive.
Name the single strongest match and the biggest weakness in one line each.
