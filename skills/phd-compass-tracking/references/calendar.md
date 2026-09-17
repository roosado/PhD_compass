# Calendar reminders

Only when the environment has a calendar connector (for example Google Calendar) and the owner wants reminders. Creating events writes to the owner's account, so ask before adding and never change or delete an existing event without asking.

## Which dates
A deadline is **confirmed** when the data block holds a specific date sourced from the ad, programme or scheme page. Add only confirmed deadlines: application deadlines, scholarship deadlines and interview dates. Soft next actions stay in the save file.

## How
1. Authenticate the connector if needed.
2. List existing events whose titles start with `PhD:` so nothing is duplicated.
3. Show the owner the events you would add, then add the ones they approve:
   - Title: `PhD: <Institution> – <position, programme or scheme> deadline` (interviews: `PhD: <Institution> interview`).
   - All-day event on the deadline date; timed event for interviews, in the time zone stated by the institution.
   - Reminders 14 days and 3 days before (1 day for interviews).
   - Description: the tracker ID and the source link.
4. Report the events added and any that already existed.

## No connector
Offer an `.ics` file instead: write one VEVENT per confirmed deadline with the same title, date, description and `VALARM` reminders, save it as `phd-deadlines.ics` (folder mode: beside the save file; chat mode: the outputs folder), and tell the owner to import it into their calendar.
