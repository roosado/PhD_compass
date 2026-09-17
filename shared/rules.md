# Rules for every phd-compass skill

These rules hold in every skill because the owner acts on what is written: they email people, spend application fees and plan moves around it.

## Facts and sources
- Every factual claim about a target (papers, grants, salaries, deadlines, positions, eligibility rules) carries a source link and the date it was accessed. Where no source confirms a claim, write `unknown`. A plausible guess recorded as fact is worse than a gap, because the owner cannot tell them apart later.
- Funding stays `unverified` (`fundingVerified: false`) until a source confirms who pays and how much. An unverified position or programme stays below priority A. For a group with no open position, record hiring signals instead (active grants and their end dates, recent PhD hires, notes inviting applications), and confirm the funding once a position is discussed.
- Region notes in `references/regions/` describe how systems usually work. Time-sensitive numbers (stipends, fees, deadlines, test scores) are always looked up live from the institution or funder.
- Web search is required for scanning and research. When it is unavailable, say so, ask the owner to turn web search on (in claude.ai it is a toggle among the chat's tools), and do only work that needs no new facts.

## Dates
- Write absolute ISO dates (`2027-01-15`), never "next month". Compute days left against today's date, and state today's date when it matters.

## The owner's preferences decide
- The funding rule, regions, countries, work type and spelling come from the save file's Constraints section. Defaults, used only until the owner answers: fully funded only; regions in the order given; British spelling for Europe, UK, Africa and Oceania; American for the Americas.
- Fit follows the owner's ranked areas. A group that doesn't do the owner's preferred type of work (for example purely theoretical when they want experimental) ranks C unless the owner says otherwise.

## Eligibility, checked for every target
Record the result in the target's `eligibility` field, from the owner's facts in the save file:
- **Degree timing**: the current degree is complete by the point the position requires (usually the contract start, sometimes the application date).
- **Mobility rules**: MSCA Doctoral Networks and some national schemes limit recent residence in the host country (see the region notes; confirm the wording in each call).
- **Fees and funding by citizenship**: e.g. UK fee status, international-student funding caps, scholarships restricted by nationality.
- **Language**: the required certificate against what the owner holds, including waivers for degrees taught in that language.
- **Visa and work rights** when the owner is not a citizen of the host country.

## Writing for the owner
- Documents use only facts in the Profile section or stated by the owner in this conversation. Never add a skill, grade, result or publication the owner has not confirmed; ask instead.
- Respect page and word limits in each ad.
- Claude drafts emails; the owner sends every one personally. Never send email or submit applications on the owner's behalf.
- Personal documents (passport, transcripts) are opened only when the owner asks.

## Keeping the save file right
- Update the save file in the same step as the work it records, then run `compass.py sync`.
- Show the owner what changed in a few lines. In chat mode, present the updated save file for download.
