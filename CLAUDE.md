# phd-compass (development)

Shareable Claude skills for PhD searches: `skills/phd-compass` (core) and three add-ons. Each skill must work as a standalone claude.ai zip and inside the Claude Code plugin.

- Edit `shared/` (rules, save-file spec and template, `compass.py`, report template), never the copies inside `skills/`. `tools/build.py` copies them.
- Run `py -3 tools/build.py` after any change and fix every FAIL before committing. It validates frontmatter, checks that every `references/`, `assets/` and `scripts/` path a skill mentions ships in that skill, renders `examples/`, checks private terms and writes `dist/` zips.
- No personal data in this repository. Examples use invented people, institutions and `example.org` links. `tools/private-terms.txt` (git-ignored) lists terms the build rejects.
- Frontmatter keys allowed on claude.ai: `name`, `description`, `license`, `allowed-tools`, `metadata`, `compatibility`. Description on one line, 1024 characters or fewer, no angle brackets. Skills must not rely on Claude Code-only features (`$ARGUMENTS`, `argument-hint`).
- Bump `version` in `.claude-plugin/plugin.json` and every skill's `metadata.version` together.
- Region notes hold structural facts with a source and access date; never add stipends, fees or deadlines there.
- Commit after each finished change, with a message that says what changed.
