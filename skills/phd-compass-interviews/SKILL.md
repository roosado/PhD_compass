---
name: phd-compass-interviews
description: Prepare a PhD applicant for interviews with supervisors, panels and doctoral programmes - research the group, build answers from the applicant's real experience, draft the research pitch and questions to ask, run a mock interview with feedback, and record notes and follow-ups afterwards. Use when someone has a PhD interview, a call with a potential supervisor or a programme visit day coming up, wants to practise interview questions or their research pitch, or wants to debrief after one.
license: MIT
metadata:
  version: "1.1.0"
  family: phd-compass
---

# PhD Compass: interviews

Gets one person, the **owner**, ready for a PhD interview, and captures what happened afterwards. It reads the phd-compass save file when there is one, and also works on its own.

Read first:
- `references/rules.md`: above all, answers are built only from the owner's real experience.
- `references/save-file.md`: modes, sections and `scripts/compass.py`.

Paths are relative to this skill's folder. Run scripts with `python3` (on Windows `py -3` or `python`).

## 1. Load
1. Work out the mode and find the save file. With it, read Profile, Interests (pitch), the target's entry, its Target notes or report, the Documents sent to it, and any earlier Interviews. Without it, ask for the CV, the position or programme, and what was sent in the application.
2. Pin down the interview: date and time zone, format (online or on site; one-to-one, panel or group), who will be there, length, and whether a presentation is required.

Done when you know the interview's date, format and panel, and hold the owner's facts and the application they sent.

## 2. Pick the branch
| The owner wants to… | Reference |
|---|---|
| prepare for a specific interview | `references/prep.md` |
| practise with a mock interview | `references/mock.md` |
| debrief after an interview, or send a thank-you note | `references/after.md` |

Preparation usually comes first, then one or more mock rounds, then the debrief after the real interview. The question bank in `references/question-bank.md` serves all three.

## 3. Record
- **Folder mode:** the prep and notes go in `interviews/<YYYY-MM-DD>_<institution>_<surname-or-programme>.md`, from `assets/interview.md`.
- **Chat mode:** a compact entry under **Interviews** in the save file (date, target, format, key prep points, then notes and outcome), and the prep sheet as a downloadable file.
- The target's data entry: `status: "interview"` before, then the next action (thank-you note, expected decision) with dates. Run `sync`.

In chat mode, present the prep sheet and the updated save file for download.
