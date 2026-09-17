# Scan

Finds open positions and programmes, groups worth contacting, and external scholarships. Then it triages them and records everything in the save file.

## 0. Plan the batches
A full scan covers every chosen region against every ranked area, which is too much for one pass. Split it into **batches** of one region × the top one or two areas, in the owner's order. Tell the owner the batch plan in one line and start with the first batch.
- **Chat mode:** run one or two batches per conversation. After each batch, save (step 6) and hand over the files; ask whether to continue here or in a new chat with the save file uploaded.
- **Folder mode:** run batches back to back, saving after each one.

If the owner asked for a narrower scan ("only Germany", "only groups", "only scholarships"), that is the batch plan.

## 1. Load context
Read the save file: Profile, Interests (keywords), Constraints, Eligibility checklist, the tracker, the watch list, and the **dropped lists** in the Scan log from the last 12 months.

Done when you hold the keywords for this batch, the sources for this region (`references/sources.md`), and the set of names already tracked, watched or dropped.

## 2. Open positions and programmes
- Query every fitting board for the region with several keyword combinations each, including local-language terms. Then run a web-search sweep (`<keyword> PhD position <country> <year>`, `doctoral candidate <keyword>`, local-language equivalents) for ads the boards missed.
- For programme-based systems (US, Canada, graduate schools), list the programmes in the area in the chosen countries, and open each programme's admissions and funding pages.
- Open each candidate ad or programme page and read it in full: funding (source, amount, duration, fees), start date, degree requirement, eligibility conditions, closing date, documents asked for.

Done when every fitting board has been searched or recorded as unreachable with the reason, and every candidate page has been read.

## 3. Groups, advertising or not
Search from several directions, because each misses different groups:
- **Papers:** authors and affiliations of in-scope papers from the last three years (Google Scholar, OpenAlex, the field's preprint server). Last and corresponding authors are usually the PIs.
- **Grants:** holders of recent grants in the area (the region's grant databases, CORDIS for EU projects and doctoral networks). A grant that started in the last two years and runs past the owner's start window is the strongest hiring signal.
- **Networks and schools:** partners in doctoral networks and graduate programmes in the area.
- **Events:** speakers at the area's main conferences and schools.
- **Ads:** groups named in open or recent ads.

For each new group, find the group page and look for hiring signals: active grants with end dates, recent PhD hires, "open positions" or "contact me" notes.

Done when each area in the batch has been searched from at least papers, grants and one more direction, and every new group has an institution and a group URL.

## 4. External scholarships
Search for doctoral scholarships matching the owner's citizenship and the batch's countries: destination-government schemes, home-country schemes for study abroad, university schemes for international doctoral students. Read each scheme's eligibility (nationality, degree timing, age limits, host requirements, return obligations).

Done when the batch's countries and the owner's citizenships have each been searched, with each scheme classed eligible / not eligible / check.

## 5. Triage
Apply `references/ranking-eligibility.md` to every candidate: keep, maybe or drop, a priority, and an eligibility result.

Done when every candidate has a class, and every maybe names its one open question.

## 6. Record
In the save file (then run `sync`):
- `targets`: each keep and maybe as a new entry with the next free ID (`next-id`), `status: "idea"`, `added` = today, sources in `links` with access dates, next action "Research with phd-compass" dated by urgency (open ads: well before the deadline). Weaker-fit groups worth remembering go in as `kind: "watch"`, priority C, without an ID.
- `ads`: every in-scope ad read, kept or not, with its status.
- `grants`: grants and doctoral networks that create places for the owner's start window.
- `calls`: recurring rounds discovered (programme deadlines, scholarship cycles).
- `scholarships`: schemes found, with eligibility.
- `meta.previousScan` = the old `lastScan`, `meta.lastScan` = today (only at the first batch of a new scan).
- **Scan log** entry (newest first): date, batch focus, sources searched, sources unreachable with the reason, keywords used, counts per class, and the **dropped list** (name, link, reason) so later scans skip them quickly. In folder mode, also write `scans/<YYYY-MM-DD>.md` with the full candidate tables and link it from the log.

Done when `validate` passes, and every candidate read in this batch appears as a target, an ad, a watch entry or a dropped line.

## 7. Report the batch
Counts per class; open positions and programme deadlines sorted by date; the three strongest groups for a speculative email and why; what the next batch covers. Then render the report (SKILL.md step 8).
