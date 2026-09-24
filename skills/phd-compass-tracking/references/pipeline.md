# The pipeline

The report's Pipeline tab follows the targets the owner has **starred**: what they did for each one (the `log` in the data block, described in `references/save-file.md`), and the next step `sync` derives from it: follow up 14 days after an email, apply before an ad closes, refresh research older than 90 days.

## Open the report site
- **Folder mode:** start `scripts/compass.py serve <save>` in the background (it keeps running) and give the owner the address it prints, `http://localhost:8765`. There they star targets and log actions themselves, and every change saves straight into the save file. Run `launcher <save>` too, so next time they can double-click `open-report.cmd` (Windows) or run `./open-report.sh` in their search folder without asking.
- **Chat mode:** no server can run for the owner. Present `phd-compass-report.html`; its Pipeline tab is read-only, and the owner tells you what to record.

## Record what the owner tells you
Log every event with `compass.py log <save> <ID> <type> [--date] [--note] [--follow-up] [--link] --by owner`, then do the Markdown side in `references/updates.md`. The command stars the target and runs `sync`, which sets the status and next action from the log. Starring alone ("add T004 to my pipeline") is `log <save> T004 note --note "Starred" --by owner`, or set `"starred": true` on the target and run `sync`.

## Fold in what the owner logged on the site
Entries with `by: "owner"` come from the report site (or from you, on the owner's word). At the start of any tracking session in folder mode, and whenever the owner says they updated the site:
1. Run `validate`; read the `log` entries newer than the latest Outreach, Submissions and Interviews rows.
2. Mirror each one in its Markdown section, as `references/updates.md` describes for that event: `emailed` sets the Outreach row `sent` with the entry's follow-up date (add a row when there was no draft), `followup` → `followed up`, `reply-yes` / `reply-no` / `reply-other` → `replied (positive / negative / redirected)`, `applied` → a Submissions row, `interview` → an Interviews entry, `closed` → the Outreach row `closed`.
3. When the save file knows something newer than the log (an event recorded before the pipeline existed), add it to the log with `compass.py log` rather than letting an older entry set the status.

Done when every log entry has its matching Markdown row and `sync` passes.
