# The save file

Every phd-compass skill reads and writes one file, `phd-compass.md`. It holds the whole search, so a new conversation, or another skill, picks up where the last one stopped.

## Where it lives

Work out the mode once, at the start:

- **Folder mode** (Claude Code, or any setup with a persistent working folder): the save file is `phd-compass.md` in the working folder. Detail files sit beside it: `targets/`, `scans/`, `documents/`, `interviews/`, `scholarships/`, `submitted/`. Edit in place.
- **Chat mode** (claude.ai and other setups with no persistent folder; uploads usually arrive in `/mnt/user-data/uploads`): the owner uploads the save file. Copy it to a working location, edit the copy, and write the updated file to the outputs folder (usually `/mnt/user-data/outputs/phd-compass.md`) so it can be downloaded. Everything lives inside the save file: there are no side folders to come back to. End every turn that changed it by presenting the file and reminding the owner to download it and upload it next time.

No save file uploaded or found? Ask whether they have one before starting fresh: a lost save file means redoing the onboarding.

## Commands

`scripts/compass.py` (Python 3.8+, standard library only). Run it from the skill folder, with the save file's path:

| Command | Does |
|---|---|
| `init <save>` | Create a new save file from `assets/save-file-template.md` |
| `validate <save>` | Check the data block. Errors block; warnings are judgement calls to review |
| `sync <save>` | Validate, set `meta.updated`, rewrite the data block in canonical form, regenerate the generated sections |
| `report <save> --out <file>` | Validate, then build the self-contained HTML report (only in `phd-compass` and `phd-compass-tracking`, which ship the report template) |
| `agenda <save> --days N` | Overdue and upcoming dated items from the data block, plus gaps |
| `next-id <save>` | The next free tracker ID |

Every command takes `--today YYYY-MM-DD`; pass today's date if the sandbox clock might differ from the conversation's date.

**After every change to the data block, run `sync`.** If Python is unavailable, edit the generated sections by hand to match the data block and say so.

## Sections

| Section | Written by | Content |
|---|---|---|
| Profile | core (onboarding) | Facts from the CV, confirmed by the owner; `TODO` for gaps |
| Interests and priorities | core | Ranked areas (keys match `meta.areas`), directions, keywords, pitch |
| Constraints and preferences | core; documents sets the format | Start window, funding rule, regions, countries, work type, spelling |
| Eligibility checklist | core | One line per rule that applies to this owner |
| Next actions, Tracker, Watch list, External scholarships | **generated** by `sync` | Never hand-edit; change the data block |
| Scan log | core | Newest first; includes each scan's dropped list |
| Target notes | core | Chat: 5–10 sourced lines per researched target. Folder: one line linking `targets/<file>.md` |
| Outreach | documents, tracking | One row per email |
| Documents | documents | One row per document produced |
| Interviews | interviews | One entry per interview |
| Submissions | tracking | What was sent, when, where |
| Referees | tracking | Requests and letters |
| Materials checklist | tracking, documents | Readiness of each item |
| Data | all, via `compass.py` | The JSON block below |

## The data block

A JSON object between `<!-- data:start -->` and `<!-- data:end -->`. After `sync`, each record sits on one line, so updating a target means replacing one line.

### `meta`
| Field | Required | Meaning |
|---|---|---|
| `title` | yes | Report title, e.g. "Coral reef ecology PhD map" |
| `updated` | yes | Set by `sync` |
| `areas` | yes | 1–6 `{key, label, priority}`; priority 1 is the core area. Keys are lowercase slugs |
| `start` | yes | `{from, to, label, detail}`: the window the PhD should start in |
| `degreeEnd` | no | `{from, to, label, detail}`: the current degree's final stretch (e.g. thesis semester) |
| `timeline` | no | `{from, to}`: report timeline range; default derived from the data |
| `eyebrow`, `headline` | no | Report kicker line and a one- or two-sentence state of the search |
| `field`, `regions`, `workPreference`, `owner` | no | `workPreference` (e.g. "experimental") labels the report's work-type filter |
| `reminders` | no | Short eligibility reminders shown in the report footer |
| `lastScan`, `previousScan` | no | Dates; entries added after `previousScan` are tagged "new" in the report |

### `targets` (one per group, programme or position)
| Field | Values |
|---|---|
| `key` | Unique slug, e.g. `tue-stabile` |
| `id` | `T001`, `T002`, … never reused. Required unless `kind` is `watch` |
| `kind` | `position` (advertised, funded post) · `programme` (graduate school, doctoral programme, CDT, US/Canada department with a yearly intake) · `group` (no open post; contact the PI) · `watch` (weaker fit, not tracked) |
| `type` | Free label for the tracker: advertised, MSCA-DN, CDT, grad-school, department, speculative… |
| `pri` | `A` · `B` · `C` (legend in the template) |
| `short`, `pi`, `group`, `inst` | Chip name (surname), PI or programme lead, group or programme name, institution |
| `cc` | Two-letter lowercase country code (`uk` is accepted for the United Kingdom) |
| `area`, `tags` | Main `meta.areas` key; other matching area keys |
| `work` | Matches the preferred type of work: `yes` · `partly` · `no` |
| `topic`, `why`, `question` | What they do; why it fits; the one open question |
| `signal` | Hiring signal bucket: `position` (funded ad) · `young` (grant awarded or started in the last ~2 years and running past the start) · `network` (doctoral network, programme or yearly intake) · `project` (active project, funding unclear) · `endsnear` (grant ends around the start) · `endsbefore` (ends before the start) · `none` · `na` (not assessed) |
| `signalText` | The signal as recorded, e.g. "ERC CoG to 2029-08" |
| `pos` | `open` (applications open) · `upcoming` (next intake expected, not open yet) · `standing` (standing or rolling call) · `poorfit` (open but poor fit) · `past` (only past ads) · `none` |
| `posText`, `deadline` | Position as recorded; closing date or `null` |
| `funding`, `fundingVerified` | Source and amount; `true` only when a source confirms it |
| `eligibility` | `{status: ok · check · fail, notes}` against the eligibility checklist |
| `status` | `idea` · `researching` · `contacted` · `preparing` · `submitted` · `interview` · `offer` · `accepted` · `rejected` · `withdrawn` · `closed` · `watch` (watch entries only) |
| `next`, `nextDate` | Next action and its date |
| `notes` | List of short strings |
| `links` | `[{href, label, accessed}]`, sources for the claims above |
| `report` | Path to the full report (folder mode) |
| `added` | Date first recorded |

### `ads` (every in-scope ad seen, kept or dropped)
`title`, `org` (short), `cc`, `dates` (closing dates, may be empty), `status` (`open` · `closed` · `poorfit` · `excluded` (not eligible) · `offfit` · `expired` · `gone`), `note`, `link`, `src` (where it was found), `added`.

### `grants` (money that creates PhD places)
`kind` (`grant` or `recruit` for a network or programme recruiting a cohort), `name`, `type`, `who`, `sig` (a signal bucket other than `position`/`na`), `start`, `end`, `fadeIn`/`fadeOut` (set when a date is not pinned down), `endLabel`, `recorded` (dates as the source states them), `recruiting`, `link`.

### `calls` (recurring calls and intakes: MSCA rounds, US admission deadlines, CDT rounds, scholarship cycles)
`name`, `type`, `who`, `from` (recruitment opens; optional), `recorded`, `recruiting`, `link`, `milestones` (`[{date, label, shown}]`; `shown` is a human date such as "mid-December" when the exact date varies).

### `scholarships` (external funding applied for separately)
`name`, `funder`, `eligible` (`yes` · `no` · `check`), `covers`, `deadline` (date, `rolling`, `unknown` or `varies`), `status` (`idea` · `checking` · `preparing` · `submitted` · `awarded` · `rejected` · `not-eligible`), `link`, `note`.

### `actions` (dated to-dos not tied to one target)
`date`, `what`, `done`.

### Example target line
```json
{"key": "example-okafor", "id": "T004", "kind": "group", "type": "speculative", "pri": "A", "short": "Okafor", "pi": "Ada Okafor", "group": "Reef Physiology Lab", "inst": "Example University", "cc": "de", "area": "core", "tags": ["modelling"], "work": "yes", "topic": "Coral heat-stress physiology in field and tank experiments", "why": "Field experiments on the owner's core question; young grant", "question": "Whether the grant funds a PhD from 2027", "signal": "young", "signalText": "ERC StG 2025-03 to 2030-02", "pos": "none", "posText": "None advertised (checked 2026-09-15)", "deadline": null, "funding": "ERC StG (hiring signal)", "fundingVerified": false, "eligibility": {"status": "ok", "notes": "Degree ends 2027-06, before any 2027-10 start"}, "status": "idea", "next": "Research with phd-compass", "nextDate": "2026-10-01", "notes": [], "links": [{"href": "https://example.org/okafor-lab", "label": "lab", "accessed": "2026-09-15"}], "added": "2026-09-15"}
```
