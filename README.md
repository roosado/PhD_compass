# PhD Compass

Claude skills for finding and applying to funded PhD positions, in any field and any country.

Give Claude your CV. It asks what it needs to know, ranks your research interests with you, searches for open positions, doctoral programmes, research groups worth emailing and scholarships, checks your eligibility and the funding, and builds an interactive HTML report of everything it found. The add-on skills then tailor your documents, prepare you for interviews and track your applications.

Everything lives in one **save file** (`phd-compass.md`), so a search can continue across conversations: in Claude Code it sits in your working folder; in a claude.ai chat you download it at the end and upload it next time.

## Your report

The report is a web page built from your save file. It has two tabs:
- **Target map:** every group, programme and position found so far, by country and research area, with hiring signals, funding timelines, a sortable lookup table and the ads seen in each scan.
- **Pipeline:** the targets you've starred, with a log of what you did (emailed, followed up, got a reply, applied…) and the next step for each: follow up after 14 days, apply before an ad closes, refresh research that is over 90 days old.

How you open it depends on where you run the skills:

| You use | To open your report | Pipeline tab |
|---|---|---|
| **Claude Code** | Ask Claude "open my PhD report". Or, in your search folder, double-click `open-report.cmd` (Windows) or run `./open-report.sh` (macOS, Linux). Your browser opens at `http://localhost:8765`; close the terminal window to stop it. | **Editable:** star targets, log actions, edit or delete entries. Every change saves to `phd-compass.md` straight away. |
| **Any computer** | Open `phd-compass-report.html` from your search folder in any browser. It is one self-contained file. | Read-only: tell Claude what you did ("I emailed Okafor today") and it updates the save file and the report. |
| **claude.ai chat** | Download `phd-compass-report.html` at the end of the chat and open it in your browser. | Read-only, as above. Keep downloading the updated save file too. |

The launchers (`open-report.cmd`, `open-report.sh`) are written into your search folder each time Claude rebuilds the report. They run a small local server from `compass.py`, which needs Python 3.8 or later and nothing else. It listens only on your own computer (`127.0.0.1`). If you'd rather use a terminal, run `python3 <skill folder>/scripts/compass.py serve phd-compass.md` (on Windows: `py -3 …`). The launchers contain the full path.

**See an example first:** download [`examples/sample-report.html`](examples/sample-report.html) (on that page, use the "Download raw file" button, since GitHub shows HTML as code) and open it in your browser. It shows a fictional marine-biology search with three starred targets.

## The skills

| Skill | What it does |
|---|---|
| **phd-compass** (core) | Reads your CV and asks the gap questions (citizenship, residence history, degree dates, start window, funding rule, regions). Ranks your research areas. Explains how PhDs are funded in your chosen regions and builds your eligibility checklist. Scans job boards, programme pages, paper and grant databases and scholarship schemes. Ranks every target A/B/C with sourced funding and eligibility. Researches individual groups in depth. Renders the HTML report. |
| **phd-compass-documents** | Rebuilds your CV in **Word or LaTeX**, then tailors copies for a target. Writes research proposals and emails to potential supervisors. You write your own motivation letters and statements of purpose; the skill critiques them (and any other draft) as a selection committee would, checking fit, evidence and consistency with your CV. |
| **phd-compass-interviews** | Prepares a prep sheet for a specific interview (the group's recent work, likely questions with answers built from your real experience, pitch, questions to ask), runs mock interviews with feedback, and records the debrief. |
| **phd-compass-tracking** | Agenda of what is due; records submissions, emails, replies, interviews, offers and rejections in the Pipeline log; opens your report for editing; referee requests with brag sheets; external scholarship applications; calendar reminders (via a calendar connector or an `.ics` file). |

The core skill works on its own. The add-ons read the same save file, and documents and interviews also work without one.

## Install

### Claude Code
```
/plugin marketplace add roosado/PhD_compass
/plugin install phd-compass@phd-compass
```
Then start a session in an empty folder for your search and say, for example, "Here's my CV (cv.pdf). Help me find a funded PhD."

### claude.ai (chat)
1. Get the four zip files: download them from this repository's releases, or build them with `python tools/build.py` (they land in `dist/`).
2. In claude.ai, open Settings → Capabilities, make sure code execution and file creation is on, and upload each zip as a skill.
3. Turn on web search in the chat.
4. Start a chat: attach your CV and say "Help me find a funded PhD". At the end, download `phd-compass.md` and `phd-compass-report.html` (open the report in your browser). Next time, attach `phd-compass.md` and say "Continue my PhD search".

A full scan is long. In chat, the skill works in batches (one region and one or two research areas per batch) and saves after each, so you can continue in a new chat.

## Things to know
- **Check before you act.** Every fact the skills record about a position, grant or rule carries a source link and access date, or says `unknown`. Rules and deadlines change; open the link before you rely on a claim.
- **Your data.** The save file holds personal details (citizenship, residence history, grades). It stays where you keep it; the skills send nothing anywhere except the web searches Claude runs.
- **You stay in control.** Claude drafts your CV, research proposal and emails, and reviews the letters and statements you write yourself; you send and submit everything. Documents use only facts you have confirmed.
- **The region notes are structural.** `skills/phd-compass/references/regions/` explains how PhDs are usually funded and found in Continental Europe, the UK and Ireland, the US and Canada, and elsewhere, with sources accessed 2026-09-17. Stipends, fees and deadlines are always looked up live.

## Example
`examples/sample-save-file.md` and `examples/sample-report.html` show a search in progress for an invented marine-biology student. To see the report, download the HTML file and open it in a browser. To try the editable Pipeline tab, copy the save file somewhere, rename it `phd-compass.md`, and run `python3 skills/phd-compass/scripts/compass.py serve <path>/phd-compass.md` from this repository.

## Development
- Shared files (`shared/`) are copied into each skill by `tools/build.py`, because each claude.ai zip must be self-contained. Edit `shared/`, never the copies.
- `python tools/build.py` copies shared files, validates the skills (frontmatter, file references, line counts), renders the example and writes the zips. `python tools/build.py --check` checks without writing.
- `shared/compass.py` (standard library only) validates the save file, regenerates its tables, prints the agenda, builds the report (`report`), serves it with an editable Pipeline tab (`serve`), writes the double-click launchers (`launcher`) and records pipeline events (`log`).

## License
MIT. See `LICENSE`.
