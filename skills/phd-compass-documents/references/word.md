# Building Word documents

Two routes produce the same look; use the first that works.

## Route 1: `scripts/md_to_docx.py` (python-docx)
1. Write the document in the Markdown dialect described at the top of the script; templates: `assets/word/cv.md`, `assets/word/letter.md`.
2. Check python-docx: `python3 -c "import docx"`. If it is missing and installing packages is allowed, `pip install python-docx`.
3. Build: `python3 scripts/md_to_docx.py <file>.md <file>.docx`.
4. Check: open the result with python-docx and confirm the paragraphs and headings are present. When a converter is available (LibreOffice `soffice --headless --convert-to pdf`, or Word), export a PDF and check the page count against the limit.

Keep the `.md` source next to the `.docx` in folder mode, so later tailoring edits the source rather than the Word file.

## Route 2: a docx skill
If python-docx cannot be used and the environment offers a skill for creating Word documents (claude.ai has one built in), follow that skill. Use the same structure: centred name and contact lines, section headings with a rule underneath, entries with the title in bold and dates right-aligned, bullets for details, A4 (or Letter for North America), about 2.2 cm margins, a sans-serif body at 10.5–11 pt.

## When the owner edits in Word
If the owner changes the `.docx` directly, treat their file as the new source: read it back before the next tailoring instead of rebuilding from the old `.md`.
