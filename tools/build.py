#!/usr/bin/env python3
"""Build the phd-compass skills. Python 3.8+, standard library only.

  py -3 tools/build.py            copy shared files into the skills, check everything, render the example, zip to dist/
  py -3 tools/build.py --check    check only; fail if a shared copy has drifted (use before committing)

Checks: shared copies identical; SKILL.md frontmatter (allowed keys, name, description); SKILL.md under 500 lines;
exactly one SKILL.md per skill; every references/, assets/ and scripts/ path a skill mentions exists inside that
skill (each claude.ai zip must be self-contained); plugin manifests agree; no private terms (tools/private-terms.txt,
git-ignored, one term per line) anywhere in the published files; the example save file validates and renders.
"""

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
SHARED = ROOT / "shared"
DIST = ROOT / "dist"

ALL = ["phd-compass", "phd-compass-documents", "phd-compass-interviews", "phd-compass-tracking"]
# shared file -> (destination inside each skill, skills that ship it)
COPIES = {
    "rules.md": ("references/rules.md", ALL),
    "save-file.md": ("references/save-file.md", ALL),
    "save-file-template.md": ("assets/save-file-template.md", ALL),
    "compass.py": ("scripts/compass.py", ALL),
    "report-template.html": ("assets/report-template.html", ["phd-compass", "phd-compass-tracking"]),
}
ALLOWED_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
PATH_RE = re.compile(r"`((?:references|assets|scripts)/[A-Za-z0-9_./<>-]+)`")
SKIP_PARTS = {"__pycache__", ".DS_Store"}
PUBLISHED = ["skills", "shared", "examples", "tools/build.py", "README.md", "CLAUDE.md", ".claude-plugin", "LICENSE"]

problems = []


def problem(msg):
    problems.append(msg)
    print(f"  FAIL {msg}")


def sync_shared(check_only):
    print("Shared copies")
    for src_name, (dest, skills) in COPIES.items():
        src = SHARED / src_name
        data = src.read_bytes()
        for skill in skills:
            target = SKILLS / skill / dest
            if target.exists() and target.read_bytes() == data:
                continue
            if check_only:
                problem(f"{skill}/{dest} differs from shared/{src_name}; run tools/build.py")
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
                print(f"  copied shared/{src_name} -> {skill}/{dest}")


def frontmatter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not m:
        return None
    keys, fields = [], {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$", line)
        if km:
            keys.append(km.group(1))
            fields[km.group(1)] = km.group(2).strip()
    return keys, fields


def check_skill(skill):
    base = SKILLS / skill
    md = base / "SKILL.md"
    if not md.exists():
        problem(f"{skill}: SKILL.md missing")
        return
    found = [p for p in base.rglob("SKILL.md") if not SKIP_PARTS.intersection(p.parts)]
    if len(found) != 1:
        problem(f"{skill}: {len(found)} SKILL.md files; claude.ai accepts exactly one")
    text = md.read_text(encoding="utf-8")
    fm = frontmatter(text)
    if not fm:
        problem(f"{skill}: no YAML frontmatter")
        return
    keys, fields = fm
    extra = set(keys) - ALLOWED_KEYS
    if extra:
        problem(f"{skill}: frontmatter keys not allowed on claude.ai: {', '.join(sorted(extra))}")
    name = fields.get("name", "")
    if name != skill:
        problem(f"{skill}: frontmatter name {name!r} must equal the folder name")
    if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", name) or len(name) > 64:
        problem(f"{skill}: name must be kebab-case, 64 characters or fewer")
    desc = fields.get("description", "")
    if not desc:
        problem(f"{skill}: description missing (write it on one line)")
    if len(desc) > 1024:
        problem(f"{skill}: description is {len(desc)} characters; the limit is 1024")
    if "<" in desc or ">" in desc:
        problem(f"{skill}: description cannot contain angle brackets")
    lines = text.count("\n") + 1
    if lines > 500:
        problem(f"{skill}: SKILL.md has {lines} lines; keep it under 500")
    for f in base.rglob("*.md"):
        for ref in PATH_RE.findall(f.read_text(encoding="utf-8")):
            if "<" in ref or ref.endswith("/"):
                continue
            if not (base / ref).exists():
                problem(f"{skill}: {f.relative_to(base)} mentions `{ref}`, which this skill does not ship")
    print(f"  ok {skill}: {len(desc)}-character description, {lines}-line SKILL.md")


def check_manifests():
    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    names = [p.get("name") for p in market.get("plugins", [])]
    if plugin.get("name") not in names:
        problem(f"marketplace.json does not list plugin {plugin.get('name')!r}")
    for skill in ALL:
        md = (SKILLS / skill / "SKILL.md").read_text(encoding="utf-8")
        m = re.search(r'version:\s*"([^"]+)"', md)
        if not m or m.group(1) != plugin.get("version"):
            problem(f"{skill}: metadata.version should match plugin.json version {plugin.get('version')}")
    print(f"  ok manifests: plugin {plugin.get('name')} {plugin.get('version')}")


def check_private():
    terms_file = ROOT / "tools" / "private-terms.txt"
    if not terms_file.exists():
        print("  skipped private-term check (tools/private-terms.txt not present)")
        return
    terms = [t.strip() for t in terms_file.read_text(encoding="utf-8").splitlines() if t.strip() and not t.startswith("#")]
    hits = 0
    for entry in PUBLISHED:
        path = ROOT / entry
        files = [path] if path.is_file() else [p for p in path.rglob("*") if p.is_file()] if path.exists() else []
        for f in files:
            try:
                text = f.read_text(encoding="utf-8")
            except (UnicodeDecodeError, OSError):
                continue
            for term in terms:
                if term.lower() in text.lower():
                    problem(f"private term {term!r} in {f.relative_to(ROOT)}")
                    hits += 1
    if not hits:
        print(f"  ok no private terms ({len(terms)} checked)")


def render_example():
    example = ROOT / "examples" / "sample-save-file.md"
    text = example.read_text(encoding="utf-8")
    m = re.search(r'"updated":\s*"(\d{4}-\d{2}-\d{2})"', text)
    today = m.group(1) if m else "2026-09-17"
    script = SHARED / "compass.py"
    with tempfile.TemporaryDirectory() as tmp:
        work = Path(tmp) / "sample.md"
        shutil.copy(example, work)
        for args in (["sync", str(work)], ["report", str(work), "--template", str(SHARED / "report-template.html"),
                                          "--out", str(ROOT / "examples" / "sample-report.html")]):
            r = subprocess.run([sys.executable, str(script), *args, "--today", today], capture_output=True, text=True, encoding="utf-8")
            if r.returncode != 0:
                problem(f"example {args[0]} failed:\n{r.stdout}{r.stderr}")
                return
        synced = work.read_text(encoding="utf-8")
    if synced != text:
        with open(example, "w", encoding="utf-8", newline="\n") as f:
            f.write(synced)
        print("  updated examples/sample-save-file.md (generated sections)")
    print(f"  ok example renders (today = {today})")


def zip_skills():
    DIST.mkdir(exist_ok=True)
    for skill in ALL:
        base = SKILLS / skill
        out = DIST / f"{skill}.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(base.rglob("*")):
                if f.is_file() and not SKIP_PARTS.intersection(f.parts) and f.suffix != ".pyc":
                    z.write(f, f"{skill}/{f.relative_to(base).as_posix()}")
        print(f"  wrote dist/{out.name} ({out.stat().st_size // 1024} KB)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="check only; write nothing")
    args = ap.parse_args()
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    sync_shared(args.check)
    print("Skills")
    for skill in ALL:
        check_skill(skill)
    print("Manifests and privacy")
    check_manifests()
    check_private()
    if not args.check:
        print("Example")
        render_example()
    if problems:
        print(f"\n{len(problems)} problem(s). Nothing zipped.")
        sys.exit(1)
    if not args.check:
        print("Zips")
        zip_skills()
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
