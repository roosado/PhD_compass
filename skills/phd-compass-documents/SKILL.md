---
name: phd-compass-documents
description: Tailor a PhD applicant's CV, motivation or cover letter, research proposal and emails to potential supervisors for a specific position, programme or group, in Word or LaTeX, and critique drafts as a selection committee would. Use when someone wants a CV rebuilt or tailored for a PhD application, a cover letter, statement of purpose or research proposal, an email to a professor, or feedback on any of these. Works with a phd-compass.md save file or on its own.
license: MIT
metadata:
  version: "1.0.0"
  family: phd-compass
---

# PhD Compass: documents

Writes and reviews application documents for one person, the **owner**, aimed at one target. It is part of the phd-compass family and reads the same save file, but it also works on its own.

Read first:
- `references/rules.md`: above all, documents use only confirmed facts, and Claude never sends email.
- `references/save-file.md`: modes, sections and `scripts/compass.py`.

Paths are relative to this skill's folder. Run scripts with `python3` (on Windows `py -3` or `python`).

## 1. Load
1. Work out the mode and look for the save file, as `references/save-file.md` describes.
   - **With a save file:** read Profile, Interests (pitch), Constraints (spelling, document format), the target's data entry and its Target notes or report.
   - **Without one:** ask for the CV and the target (ad link, programme page, or PI and institution). Offer to start a save file with `compass.py init` so the facts carry over to later sessions; if the owner declines, work from what they provide.
2. Read the target's requirements: documents requested, page or word limits, language, format, anything the ad asks the letter to address.
3. Collect 2–3 specific, sourced facts about the target (recent papers, the project, facilities). If the target hasn't been researched, read the group or programme page and its recent papers now, or suggest the `phd-compass` skill for a full report.

Done when you have the owner's facts, the target's requirements with limits, and 2–3 linked target facts.

## 2. Format, once
If Constraints has no document format, ask: **Word** (edit in Word or Google Docs; easy to tweak) or **LaTeX** (precise layout; compile locally or on Overleaf). Record the answer in Constraints.

## 3. Master CV, once per format
Rebuild the owner's existing CV faithfully as the master: same sections, order and wording, fixing only clear typos, which you list for the owner. Every tailored CV starts from this master, which is how tailoring stays honest.
- **LaTeX:** start from `assets/latex/cv.tex` with `assets/latex/phd-compass.sty`; build as in `references/latex.md`.
- **Word:** write the CV in the dialect of `assets/word/cv.md` and build it as in `references/word.md`.
- Folder mode: `documents/master/cv.<tex|md>` plus the built file. Chat mode: the outputs folder.

Done when the owner confirms the master matches their CV, and it builds.

## 4. Write the document
Pick the branch the owner asked for:
| Document | Reference |
|---|---|
| Tailored CV | `references/cv.md` |
| Motivation letter, cover letter, statement of purpose, personal statement | `references/letters.md` |
| Research proposal | `references/proposals.md` |
| Email to a potential supervisor, follow-up, reply | `references/emails.md` |
| Review of any draft | `references/critique.md` |

File names: `<doc>_<cc>_<institution>_<surname-or-programme>.<ext>` (doc = cv, letter, proposal, email), lowercase kebab-case. Folder mode: `documents/<cc>_<institution>_<surname-or-programme>/`. Chat mode: the outputs folder.

## 5. Check before handing over
Run these on every document, then fix what fails:
1. **Facts:** every claim about the owner traces to Profile or to this conversation. List anything you could not trace and ask.
2. **Limits:** pages or words within the target's limit (count them; for PDFs, check the page count).
3. **Build:** LaTeX compiles with no errors or overfull boxes; Word builds and opens (see the build references).
4. **Language:** the owner's spelling variant; names, titles and institution spelled as on the target's own pages.

Done when all four pass, or the owner has been told exactly which one does not and why.

## 6. Record
In the save file, then run `compass.py sync`:
- **Documents** table: date, document, target, format, file, status (`draft` → `final` → `sent`).
- **Outreach** table for emails: status `drafted`; the follow-up date is set when the owner reports it sent.
- **Materials checklist**: update the CV, letter and proposal rows.
- If the target's `status` is `idea` or `researching` and the owner is preparing an application, set it to `preparing`.

In chat mode, present the documents and the updated save file for download.
