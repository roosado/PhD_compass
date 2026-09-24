---
name: phd-compass-tracking
description: Track PhD applications end to end - what is due, submissions, outreach follow-ups, referee letters, scholarship applications, materials readiness and calendar reminders - in a phd-compass.md save file. Use when someone asks what is due or what to do next in their PhD applications, records that they submitted an application or sent an email, got a reply, an interview invitation, an offer or a rejection, needs to ask referees for letters, or wants PhD deadlines in their calendar, or wants to open their report to star targets and log what they did.
license: MIT
metadata:
  version: "1.0.1"
  family: phd-compass
---

# PhD Compass: tracking

Keeps one person's PhD applications moving: an agenda of what is due, a record of what was sent, follow-ups, referees, scholarships and materials. It reads and writes the phd-compass save file.

Read first:
- `references/rules.md`
- `references/save-file.md`: modes, sections, the data block and `scripts/compass.py`.

Paths are relative to this skill's folder. Run scripts with `python3` (on Windows `py -3` or `python`), passing `--today YYYY-MM-DD`.

## 1. Load
Work out the mode and find the save file. Without one, this skill has nothing to track: offer to start one with `compass.py init` (the `phd-compass` skill fills it from a CV), or to track a single application the owner describes, recorded in a new save file.

Run `validate`. Fix any errors before going on (they are usually a malformed date or enum).

## 2. Pick the branch
| The owner wants to… | Reference |
|---|---|
| know what is due, what to do next, or a status overview | `references/agenda.md` |
| record a submission, an email sent, a reply, an interview invitation, an offer, a rejection or a withdrawal | `references/updates.md` |
| ask referees for letters, or check on them | `references/referees.md` |
| track an external scholarship application | `references/scholarships.md` |
| put deadlines in a calendar | `references/calendar.md` |
| open the report to star targets and log actions, star or unstar a target, or says they updated the report site | `references/pipeline.md` |

Several can run in one session; do the agenda last so it reflects the updates.

## 3. Finish
1. Run `sync`, then `report --out <path>` (folder mode: `phd-compass-report.html` beside the save file, plus `launcher <save>` so `open-report.cmd` / `open-report.sh` stay current; chat mode: the outputs folder).
2. Tell the owner what changed, in a few lines, and the next three actions with dates.
3. In chat mode, present the updated save file and report for download.

Done when `validate` passes, every change the owner reported is in the save file, and the report is rebuilt.
