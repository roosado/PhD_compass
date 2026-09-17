---
name: phd-compass
description: Find funded PhD positions, doctoral programmes and research groups that fit a CV, in any field and country, and keep the whole search in a save file with an HTML report. Use when someone shares a CV to start a PhD search, ranks research interests, looks for PhD positions, programmes, scholarships or groups to contact, researches a professor or programme, checks PhD eligibility or funding, wants the PhD report refreshed, or uploads a phd-compass.md save file to continue.
license: MIT
metadata:
  version: "1.0.0"
  family: phd-compass
---

# PhD Compass

Finds PhD opportunities for one person, the **owner**, from their CV, ranked priorities and constraints. Everything lands in one save file (`phd-compass.md`) and a self-contained HTML report. It works in a working folder (Claude Code) and in a plain chat, where the owner downloads the save file and uploads it next time.

Read these two files first; every step depends on them:
- `references/rules.md`: sourcing, dates, eligibility and writing rules.
- `references/save-file.md`: modes, the save file's sections, the data block and `scripts/compass.py`.

Paths are relative to this skill's folder. Run the script with `python3 scripts/compass.py …` (on Windows `py -3` or `python`), passing today's date as `--today YYYY-MM-DD`.

## 1. Resume or start

1. Work out the mode (folder or chat) as `references/save-file.md` describes.
2. Look for the save file: `phd-compass.md` in the working folder, or an uploaded file with that name or with a `<!-- data:start -->` block.
   - **Found**: run `validate` and `agenda --days 30`. Give the owner a status in 8 lines or fewer: owner, core area, targets by priority, overdue items, last scan date, and the most useful next step.
   - **Not found**: ask whether they already have a save file from an earlier session (a lost one means redoing onboarding). If not, create one with `init` (in chat mode, in the outputs folder) and go to step 2.
3. Offer the steps below that fit the state. A fresh file goes 2 → 3 → 4 → 5 → 6 → 8 → 7.

Done when the save file is loaded or created and the owner has picked what to do.

## 2. Onboarding
Follow `references/onboarding.md`: read the CV, confirm the extracted profile, ask only the gap questions, fill Profile, Constraints and `meta`.

## 3. Interests and priorities
Follow `references/interests.md`: ranked areas (core first), directions, keywords per area, draft pitch, `meta.areas`.

## 4. Strategy by region
For each region the owner chose, read its file in `references/regions/`: `continental-europe.md`, `uk-ireland.md`, `us-canada.md`, and `other.md` for everywhere else.
1. Tell the owner in 10 lines or fewer per region how PhDs there are funded and found, and what that means for them.
2. Write the **Eligibility checklist**: one line per rule that applies to this owner (mobility rules from their residence history, fee status, language, visa, degree timing).
3. Record recurring calls and intakes for the next 12 months in `calls` (MSCA rounds, US deadlines, CDT rounds, scholarship cycles), looked up live and sourced; mark any date you can't confirm as `shown: "unconfirmed"`. Set `meta.reminders`.

Done when every chosen region has its summary, checklist lines and calls (or an explicit note that none were found), and `sync` passes.

## 5. Scan
Follow `references/scan.md`, with `references/sources.md` for where to search. Scanning is the longest step: batch it by region and area, and save after each batch.

## 6. Triage and rank
Follow `references/ranking-eligibility.md` for keep / maybe / drop, priority A / B / C and the eligibility record. Usually run straight after a scan batch.

## 7. Research a target
Follow `references/target-research.md` when the owner names a PI, group, programme, position link or tracker ID, or after a scan for the strongest targets.

## 8. Render and hand over
1. `sync`, then `report --out <path>` (folder mode: `phd-compass-report.html` beside the save file; chat mode: the outputs folder).
2. Set `meta.headline` to one or two sentences on the state of the search before rendering.
3. Present the report and, in chat mode, the save file, with a reminder to keep the save file and upload it next time.
4. Close with at most three next actions. Mention the add-on skills where they fit: `phd-compass-documents` (tailored CV, letters, proposals, professor emails, critique), `phd-compass-interviews` (preparation and mock interviews) and `phd-compass-tracking` (deadlines, submissions, referees). They are installed separately.

Done when both files exist at the stated paths, `validate` shows no errors, and the owner has the next actions.
