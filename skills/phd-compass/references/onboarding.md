# Onboarding

Builds the Profile and Constraints sections from the owner's CV and a single round of questions. Every later judgement (fit, eligibility, documents) reads these facts, so a wrong date here becomes a wrong eligibility call later.

## 1. Get the CV
Accept whatever the owner has: PDF, DOCX, an image, a LinkedIn export, or pasted text. For a DOCX without a reader, unzip it and read `word/document.xml`. With no CV at all, collect the same facts by asking about education, research, work, skills and awards, one short group at a time.

Tell the owner once that the save file will hold personal data (name, citizenship, residence history) and that they control where it goes.

## 2. Extract the profile
Fill the Profile headings of the save file:
- Record only what the documents state. Dates as `YYYY-MM`; grades with their scale (`8.9/10`, `2:1`, `GPA 3.7/4.0`); degrees under their official names with the country.
- When two documents disagree (an end date, a title), keep both and turn the conflict into a question.
- Draft **Known gaps**: the one to three weaknesses a selection committee would see (for example, no publication, no hands-on work in the core area, a short or unrelated thesis). They are used for fit judgements only; say so.

## 3. Confirm
Show the extracted profile compactly (headings and one line per item) and ask the owner to correct anything wrong or missing. Apply the corrections before moving on.

## 4. Ask the gaps, in one round
Ask only what the CV and the conversation have not answered, as one numbered list of at most ten questions. The first group decides eligibility, so say in one clause why it matters (mobility rules and fee status depend on residence dates).

**Eligibility (always resolve):**
1. Citizenship(s), and any permanent residence.
2. Countries lived, worked or studied in during the last 36 months, with month-level dates.
3. Current degree: expected completion date, and whether the thesis or final exam is included in that date.
4. Language certificates held (test, score, date), and the language each degree was taught in.
5. Start window: the earliest and latest acceptable start.
6. Funding rule: fully funded only (the default), or are partial funding or self-funding acceptable?
7. Regions in order of preference; countries to prioritise and countries to rule out.

**Fit:**
8. Preferred type of work: experimental, computational, theoretical, fieldwork, clinical, archival, mixed.
9. Industry-linked or industrial PhDs: acceptable?
10. Other constraints: visa history, family, accessibility needs, a partner's location, a city they must be near.

**Documents** (only if unknown): British or American spelling. Default from rules.md otherwise.

Accept "don't know" and record it as `unknown (owner unsure)`; flag the affected eligibility checks as `check`.

## 5. Write
- Profile and Constraints sections, with the answers.
- `meta`: `title` (e.g. "Marine ecology PhD map"), `owner`, `field`, `start` (from the start window), `degreeEnd` (the last stretch of the current degree, e.g. the thesis semester), `workPreference` (a short phrase such as "experimental" or "field or experimental"), `regions`.
- Run `sync`.

Done when every eligibility item holds a value or an explicit `unknown (owner unsure)`, the owner has confirmed the profile, and `validate` passes.
