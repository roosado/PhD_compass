# Recording updates

Each event changes the data block (the target's status and next action) and one Markdown section. Ask for any detail below that the owner did not give; dates are always absolute.

Record the data-block side with `scripts/compass.py log <save> <ID> <type> --by owner` (types in `references/save-file.md`: `emailed`, `followup`, `reply-yes`, `reply-no`, `reply-other`, `meeting`, `applied`, `interview`, `offer`, `accepted`, `rejected`, `withdrawn`, `closed`, `note`). It stars the target, puts the event in the report's Pipeline tab, and lets `sync` set the status and next action below; adjust `next` by hand only where the owner agreed a different step.

| Event | Data block (the target) | Markdown |
|---|---|---|
| Email sent | `status: "contacted"` if earlier; `next` = follow up, `nextDate` = sent date + 10–14 days | Outreach row: `sent`, follow-up date |
| Reply received | `next`/`nextDate` for the agreed step; a redirect to another PI becomes a new target | Outreach row: `replied (positive / negative / redirected)` and a one-line summary |
| Follow-up sent / no reply after follow-up | `nextDate` moved, or the outreach closed with the target kept | Outreach row: `followed up` or `closed` |
| Application submitted | `status: "submitted"`; `next` = expected decision or a check-in date | Submissions row (below); Documents rows: `sent` |
| Interview invitation | `status: "interview"`; `next` = the interview, `nextDate` = its date | Interviews: date, format, who; suggest `phd-compass-interviews` |
| Offer | `status: "offer"`; `next` = reply deadline | Submissions row: outcome and reply deadline; note funding terms and conditions |
| Accepted | `status: "accepted"` | Note start date and conditions; suggest updating other targets to `withdrawn` |
| Rejected | `status: "rejected"`; clear `nextDate` | Submissions row: outcome, date, any feedback given |
| Withdrawn / closed | `status: "withdrawn"` or `"closed"`; clear `nextDate` | One-line reason |

## Submissions
For each application record: date sent, tracker ID, position or programme, the documents sent (with versions), the portal or address used, the confirmation or reference number, and the expected decision date if stated.

**Frozen copies.** In folder mode, copy exactly what was sent into `submitted/<YYYY-MM-DD>_<institution>_<position>/` with a `note.md` listing each file and which personal documents (transcripts, certificates, passport) were attached, without copying those personal documents unless the owner asks. In chat mode, list the files in the Submissions row and remind the owner to keep their own copies.

## Offers
Before the owner accepts, check that the offer matches the funding recorded (who pays, amount, duration, fees, start date) and list any difference. For US programmes, check whether the university has signed the [April 15 Resolution](https://cgsnet.org/resources/for-current-prospective-graduate-students/april-15-resolution) (accessed 2026-09-17), under which admitted students need not accept or decline a funded offer before 15 April.

Done when every event the owner reported is in both the data block and the right section, and `sync` passes.
