# PhD Compass

Claude skills for finding and applying to funded PhD positions, in any field and any country.

Give Claude your CV. It asks what it needs to know, ranks your research interests with you, searches for open positions, doctoral programmes, research groups worth emailing and scholarships, checks your eligibility and the funding, and builds an interactive HTML report of everything it found. The add-on skills then tailor your documents, prepare you for interviews and track your applications.

Everything lives in one **save file** (`phd-compass.md`), so a search can continue across conversations: in Claude Code it sits in your working folder; in a claude.ai chat you download it at the end and upload it next time.

## The skills

| Skill | What it does |
|---|---|
| **phd-compass** (core) | Reads your CV and asks the gap questions (citizenship, residence history, degree dates, start window, funding rule, regions). Ranks your research areas. Explains how PhDs are funded in your chosen regions and builds your eligibility checklist. Scans job boards, programme pages, paper and grant databases and scholarship schemes. Ranks every target A/B/C with sourced funding and eligibility. Researches individual groups in depth. Renders the HTML report. |
| **phd-compass-documents** | Rebuilds your CV in **Word or LaTeX**, then tailors copies for a target. Writes research proposals and emails to potential supervisors. You write your own motivation letters and statements of purpose; the skill critiques them (and any other draft) as a selection committee would, checking fit, evidence and consistency with your CV. |
| **phd-compass-interviews** | Prepares a prep sheet for a specific interview (the group's recent work, likely questions with answers built from your real experience, pitch, questions to ask), runs mock interviews with feedback, and records the debrief. |
| **phd-compass-tracking** | Agenda of what is due; records submissions, emails, replies, interviews, offers and rejections; referee requests with brag sheets; external scholarship applications; calendar reminders (via a calendar connector or an `.ics` file). |

The core skill works on its own. The add-ons read the same save file, and documents and interviews also work without one.

## Install

### Claude Code
```
/plugin marketplace add <path-or-git-url-of-this-repository>
/plugin install phd-compass@phd-compass
```
Then start a session in an empty folder for your search and say, for example, "Here's my CV (cv.pdf). Help me find a funded PhD."

### claude.ai (chat)
1. Get the four zip files: download them from this repository's releases, or build them with `python tools/build.py` (they land in `dist/`).
2. In claude.ai, open Settings → Capabilities, make sure code execution and file creation is on, and upload each zip as a skill.
3. Turn on web search in the chat.
4. Start a chat: attach your CV and say "Help me find a funded PhD". At the end, download `phd-compass.md` and `phd-compass-report.html`. Next time, attach `phd-compass.md` and say "Continue my PhD search".

A full scan is long. In chat, the skill works in batches (one region and one or two research areas per batch) and saves after each, so you can continue in a new chat.

## Things to know
- **Check before you act.** Every fact the skills record about a position, grant or rule carries a source link and access date, or says `unknown`. Rules and deadlines change; open the link before you rely on a claim.
- **Your data.** The save file holds personal details (citizenship, residence history, grades). It stays where you keep it; the skills send nothing anywhere except the web searches Claude runs.
- **You stay in control.** Claude drafts your CV, research proposal and emails, and reviews the letters and statements you write yourself; you send and submit everything. Documents use only facts you have confirmed.
- **The region notes are structural.** `skills/phd-compass/references/regions/` explains how PhDs are usually funded and found in Continental Europe, the UK and Ireland, the US and Canada, and elsewhere, with sources accessed 2026-09-17. Stipends, fees and deadlines are always looked up live.

## Example
`examples/sample-save-file.md` and `examples/sample-report.html` show a finished search for an invented marine-biology student. Open the HTML file in a browser.

## Development
- Shared files (`shared/`) are copied into each skill by `tools/build.py`, because each claude.ai zip must be self-contained. Edit `shared/`, never the copies.
- `python tools/build.py` copies shared files, validates the skills (frontmatter, file references, line counts), renders the example and writes the zips. `python tools/build.py --check` checks without writing.
- `shared/compass.py` (standard library only) validates the save file, regenerates its tables, prints the agenda and builds the report.

## License
MIT. See `LICENSE`.
