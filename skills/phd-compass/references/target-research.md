# Research a target

A deep look at one PI, group, programme or position, ending in a fit judgement and a recommended move.

## 1. Identify
Resolve the request to a PI or programme lead, a group or programme, an institution and, if there is one, a specific position. For a tracker ID, start from that entry. Check the save file (and `targets/` in folder mode) for an existing entry, and update it rather than duplicating.

Done when you know the full name, institution, group or programme URL, and whether an entry exists.

## 2. Research
Use `references/sources.md`:
- The group or programme website: members, research lines, facilities, open positions, how to apply. Note the PI's email if the page lists it: a later email draft uses it instead of a fresh lookup.
- The last ~3 years of papers (Google Scholar, OpenAlex, the preprint server). Pick the 3–5 most relevant to the owner's areas.
- Grants: the region's grant database and CORDIS. Record the funder, title, start and end dates.
- The position ad or programme's admissions and funding pages, if any: funding, duration, start, requirements, documents, deadline.
- The institution's doctoral pages: contract or stipend, degree requirement and timing, language requirement, fees for international students.
- Hiring signals for a group with no open post: active grants with end dates, recent PhD hires, notes inviting applications.
- Group signals worth noting: size, where recent graduates went, collaborations, supervision style where the group states it.

Done when every section of `assets/target-report.md` holds sourced content or `unknown`.

## 3. Judge fit
Apply the fit judgement in `references/ranking-eligibility.md` (score 1–5, strongest match, biggest weakness). If the profile still has important TODOs, say which missing facts limit the judgement.

## 4. Record
- **Folder mode:** write `targets/<cc>_<institution>_<surname-or-programme>.md` from `assets/target-report.md`, and set the target's `report` field to that path.
- **Chat mode:** add 5–10 lines under **Target notes** in the save file: tracker ID and name, the PI's email if found, fit score with the strongest match and the biggest weakness, funding and its source, eligibility result, 2–3 key papers (linked), the open question, the recommended move.
- Update the target's data entry: priority, signal, position, funding and `fundingVerified`, eligibility, `why`, `question`, `status: "researching"`, next action and date, links with access dates.
- Run `sync`.

## 5. Report
Fit score, funding status, deadline, eligibility flags, and the recommended move: **apply**, **email the PI** (the documents add-on drafts it), **watch** (with a date to check again), or **drop** (with the reason). Offer to refresh the report.
