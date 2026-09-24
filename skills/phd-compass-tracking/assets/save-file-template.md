# PhD Compass save file

- Owner: TODO
- Created: __TODAY__
- Last updated: __TODAY__
- Format: phd-compass save file, schema 1

**Keep this file.** It is your whole PhD search: profile, priorities, targets and progress. In Claude Code it lives in your working folder. In a claude.ai chat, upload it at the start of every conversation and download the updated copy at the end. Sections marked "generated" are rewritten from the data block at the bottom, so edit the data block through Claude and leave those sections as they are.

## Profile
<!-- Facts from the CV, confirmed by the owner. TODO marks a gap. Every document is built from these facts only. -->

### Basics
- Name: TODO
- Email: TODO
- Citizenships: TODO
- Current residence (country, since): TODO
- Countries lived or worked in during the last 36 months, with dates: TODO
- Languages and levels: TODO
- Language certificates (test, score, date): TODO

### Education
<!-- One block per degree: title, institution, country, dates (expected end if ongoing), grade with scale, thesis topic and supervisor. -->
TODO

### Research experience
TODO

### Publications, talks, posters
TODO

### Work experience
TODO

### Skills
TODO

### Awards and service
TODO

### Known gaps (for fit judgements)
TODO

## Interests and priorities

### Ranked areas
<!-- Rank 1 is the core area. Keys match meta.areas in the data block and become the report's columns. -->
| Rank | Key | Area | In the owner's words |
|---|---|---|---|

### Specific questions or directions
TODO

### Search keywords
TODO

### Pitch
TODO: one paragraph, the base for "why me, why this" in letters and emails.

## Constraints and preferences
- Current degree ends (expected): TODO
- Start window: TODO
- Funding rule: fully funded only
- Regions, in order: TODO
- Countries to prioritise: TODO
- Countries to avoid: TODO
- Preferred type of work (e.g. experimental, computational, theoretical, fieldwork): TODO
- Industry-linked PhDs acceptable: TODO
- Other constraints (visa, family, accessibility, partner): TODO
- Document spelling: TODO (British or American)
- Document format: TODO (Word or LaTeX; set by phd-compass-documents)

## Eligibility checklist
<!-- Derived from the constraints and the region notes. Every target is checked against each line. -->
TODO

## Next actions (generated)
<!-- next:start -->
<!-- next:end -->

## Tracker (generated)
<!-- tracker:start -->
<!-- tracker:end -->

Legend. **Pri**: A = strong fit, eligible, funding verified (for groups: evidence of an active grant) · B = good fit with one open question · C = weaker fit, watch list only. **Status**: idea → researching → contacted → preparing → submitted → interview → offer → accepted, or rejected / withdrawn / closed.

## Watch list (generated)
<!-- watch:start -->
<!-- watch:end -->

## External scholarships (generated)
<!-- scholarships:start -->
<!-- scholarships:end -->

## Scan log
<!-- Newest first. One entry per scan: date, focus, sources searched, sources unreachable (with the reason), keywords, counts, and the dropped list so later scans skip those quickly. -->

## Target notes
<!-- Short research notes per target (chat), or links to full reports in targets/ (Claude Code). -->

## Outreach
| Date | PI | Institution | Tracker ID | Subject | Status | Follow-up by | Draft |
|---|---|---|---|---|---|---|---|

Status: drafted → sent → replied (positive / negative / redirected) · no reply → followed up → closed

## Documents
| Date | Document | Target | Format | File | Status |
|---|---|---|---|---|---|

## Interviews
<!-- One entry per interview: date, target, format, prep file, notes, outcome. -->

## Submissions
| Date sent | Tracker ID | Position | Documents sent | Portal or confirmation | Status |
|---|---|---|---|---|---|

## Referees
| Referee | Relationship | Contact | Asked on | Agreed | Letters due for | Brag sheet sent |
|---|---|---|---|---|---|---|

## Materials checklist
| Item | Needed for | Status | Notes |
|---|---|---|---|
| Academic CV | All | TODO | |
| Motivation or cover letter | All | TODO | Tailored per target |
| Research proposal | Some (e.g. UK, some graduate schools) | TODO | |
| Transcripts | All | TODO | Certified translation needed? |
| Degree certificates | All | TODO | |
| Expected-completion letter | While the current degree is unfinished | TODO | |
| Referee letters or contacts | All | TODO | |
| Language certificate | Where required | TODO | |
| Writing sample or thesis | Some | TODO | |
| Passport or ID copy | Some | TODO | |

Status values: TODO · in progress · ready · needs update

## Data
<!-- Managed by Claude with scripts/compass.py. Format: references/save-file.md. -->
<!-- data:start -->
```json
{
  "schema": 1,
  "meta": {
    "title": "PhD search",
    "updated": "__TODAY__",
    "areas": [
      {"key": "core", "label": "TODO core area", "priority": 1}
    ],
    "start": {"from": "__TODAY__", "to": "__TODAY__", "label": "Target start", "detail": "TODO"},
    "lastScan": null,
    "previousScan": null
  },
  "targets": [],
  "ads": [],
  "grants": [],
  "calls": [],
  "scholarships": [],
  "actions": [],
  "log": []
}
```
<!-- data:end -->
