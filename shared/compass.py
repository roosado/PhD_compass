#!/usr/bin/env python3
"""phd-compass save-file tool. Python 3.8+, standard library only.

The save file (phd-compass.md) is Markdown for people plus one JSON data block
between <!-- data:start --> and <!-- data:end -->. The data block is the single
source for the generated tables and the HTML report. Format: references/save-file.md.

Commands (every command accepts --today YYYY-MM-DD; default: the system date):
  init <save.md>                          create a new save file from assets/save-file-template.md
  validate <save.md>                      check the data block; exit 1 on errors
  sync <save.md>                          validate, set meta.updated, rewrite the data block in
                                          canonical form and regenerate the generated sections
  report <save.md> [--out F] [--template F]
                                          validate, then build the self-contained HTML report
  agenda <save.md> [--days N]             overdue and upcoming dated items, plus gaps
  next-id <save.md>                       the next free tracker ID
"""

import argparse
import datetime as dt
import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASSETS = HERE.parent / "assets"

DATA_RE = re.compile(r"<!-- data:start -->\s*```json[ \t]*\r?\n(.*?)\r?\n```\s*<!-- data:end -->", re.S)
ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
ID_RE = re.compile(r"^T\d{3,}$")
CC_RE = re.compile(r"^[a-z]{2}$")

KINDS = {"position", "programme", "group", "watch"}
PRIS = {"A", "B", "C"}
WORK = {"yes", "partly", "no"}
SIGNALS = {"position", "young", "network", "project", "endsnear", "endsbefore", "none", "na"}
POSITIONS = {"open", "upcoming", "standing", "poorfit", "past", "none"}
STATUSES = {"idea", "researching", "contacted", "preparing", "submitted", "interview", "offer",
            "accepted", "rejected", "withdrawn", "closed", "watch"}
ACTIVE = {"idea", "researching", "contacted", "preparing", "submitted", "interview", "offer"}
ELIGIBILITY = {"ok", "check", "fail"}
AD_STATUS = {"open", "closed", "poorfit", "excluded", "offfit", "expired", "gone"}
GRANT_KINDS = {"grant", "recruit"}
SCH_ELIGIBLE = {"yes", "no", "check"}
SCH_STATUS = {"idea", "checking", "preparing", "submitted", "awarded", "rejected", "not-eligible"}
SCH_OPEN = {"idea", "checking", "preparing"}
SCH_DEADLINE_WORDS = {"rolling", "unknown", "varies"}
LISTS = ("targets", "ads", "grants", "calls", "scholarships", "actions")
HORIZON_DAYS = 60


# ---------------------------------------------------------------- loading

def load(path):
    text = Path(path).read_text(encoding="utf-8")
    m = DATA_RE.search(text)
    if not m:
        fail(f"{path}: no data block. Expected <!-- data:start -->, a ```json fence, then <!-- data:end -->.")
    try:
        data = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        line = text[:m.start(1)].count("\n") + e.lineno
        fail(f"{path}: invalid JSON in the data block, line {line} column {e.colno}: {e.msg}")
    return text, data, m


def write_text(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def fail(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def is_iso(v):
    if not isinstance(v, str) or not ISO_RE.match(v):
        return False
    try:
        dt.date.fromisoformat(v)
        return True
    except ValueError:
        return False


def days_between(today, iso):
    return (dt.date.fromisoformat(iso) - today).days


def rel(n):
    if n == 0:
        return "today"
    if n == 1:
        return "tomorrow"
    if n == -1:
        return "yesterday"
    return f"in {n} days" if n > 0 else f"{-n} days ago"


# ---------------------------------------------------------------- validation

class Findings:
    def __init__(self):
        self.errors, self.warnings = [], []

    def err(self, where, msg):
        self.errors.append(f"{where}: {msg}")

    def warn(self, where, msg):
        self.warnings.append(f"{where}: {msg}")


def check_str(f, where, obj, key, required=True):
    v = obj.get(key)
    if v is None:
        if required:
            f.err(where, f"missing '{key}'")
        return None
    if not isinstance(v, str) or (required and not v.strip()):
        f.err(where, f"'{key}' must be a {'non-empty ' if required else ''}string")
        return None
    return v


def check_date(f, where, obj, key, required=True, nullable=False):
    v = obj.get(key)
    if v is None:
        if required and not nullable:
            f.err(where, f"missing '{key}' (YYYY-MM-DD)")
        return None
    if not is_iso(v):
        f.err(where, f"'{key}' must be a real date as YYYY-MM-DD, got {v!r}")
        return None
    return v


def check_enum(f, where, obj, key, allowed, required=True):
    v = obj.get(key)
    if v is None:
        if required:
            f.err(where, f"missing '{key}' (one of: {', '.join(sorted(allowed))})")
        return None
    if v not in allowed:
        f.err(where, f"'{key}' is {v!r}; use one of: {', '.join(sorted(allowed))}")
        return None
    return v


def check_window(f, where, obj, key, required):
    w = obj.get(key)
    if w is None:
        if required:
            f.err(where, f"missing '{key}' ({{from, to, label}})")
        return
    if not isinstance(w, dict):
        f.err(where, f"'{key}' must be an object")
        return
    a = check_date(f, f"{where}.{key}", w, "from")
    b = check_date(f, f"{where}.{key}", w, "to")
    check_str(f, f"{where}.{key}", w, "label")
    if a and b and a > b:
        f.err(f"{where}.{key}", "'from' is after 'to'")


def validate(data, today):
    f = Findings()
    if not isinstance(data, dict):
        f.err("data", "the data block must be a JSON object")
        return f
    if data.get("schema") != 1:
        f.err("data", "'schema' must be 1")
    for key in LISTS:
        if key in data and not isinstance(data[key], list):
            f.err("data", f"'{key}' must be a list")
            data[key] = []

    meta = data.get("meta")
    area_keys = set()
    if not isinstance(meta, dict):
        f.err("meta", "missing or not an object")
        meta = {}
    else:
        check_str(f, "meta", meta, "title")
        check_date(f, "meta", meta, "updated")
        check_window(f, "meta", meta, "start", required=True)
        check_window(f, "meta", meta, "degreeEnd", required=False)
        tl = meta.get("timeline")
        if tl is not None:
            if not isinstance(tl, dict):
                f.err("meta", "'timeline' must be an object {from, to}")
            else:
                check_date(f, "meta.timeline", tl, "from")
                check_date(f, "meta.timeline", tl, "to")
        for k in ("lastScan", "previousScan"):
            check_date(f, "meta", meta, k, required=False, nullable=True)
        for k in ("eyebrow", "headline", "field", "workPreference", "owner"):
            check_str(f, "meta", meta, k, required=False)
        for k in ("reminders", "regions"):
            v = meta.get(k)
            if v is not None and not (isinstance(v, list) and all(isinstance(x, str) for x in v)):
                f.err("meta", f"'{k}' must be a list of strings")
        areas = meta.get("areas")
        if not isinstance(areas, list) or not 1 <= len(areas) <= 6:
            f.err("meta", "'areas' must list 1 to 6 research areas")
        else:
            prios = set()
            for i, a in enumerate(areas):
                w = f"meta.areas[{i}]"
                if not isinstance(a, dict):
                    f.err(w, "must be an object {key, label, priority}")
                    continue
                k = check_str(f, w, a, "key")
                if k and not SLUG_RE.match(k):
                    f.err(w, f"'key' {k!r} must be lowercase letters, digits and hyphens")
                elif k in area_keys:
                    f.err(w, f"duplicate key {k!r}")
                elif k:
                    area_keys.add(k)
                check_str(f, w, a, "label")
                p = a.get("priority")
                if not isinstance(p, int) or isinstance(p, bool) or p < 1:
                    f.err(w, "'priority' must be a whole number from 1 (highest)")
                elif p in prios:
                    f.err(w, f"priority {p} is used twice")
                else:
                    prios.add(p)

    keys, ids = set(), set()
    for i, t in enumerate(data.get("targets", [])):
        w = f"targets[{i}]"
        if not isinstance(t, dict):
            f.err(w, "must be an object")
            continue
        key = check_str(f, w, t, "key")
        if key:
            w = f"targets[{i}] ({key})"
            if not SLUG_RE.match(key):
                f.err(w, "'key' must be lowercase letters, digits and hyphens")
            if key in keys:
                f.err(w, "duplicate key")
            keys.add(key)
        kind = check_enum(f, w, t, "kind", KINDS)
        tid = t.get("id")
        if kind != "watch" or tid is not None:
            if not isinstance(tid, str) or not ID_RE.match(tid):
                f.err(w, f"'id' must look like T001 (required unless kind is watch), got {tid!r}")
            elif tid in ids:
                f.err(w, f"duplicate id {tid}")
            else:
                ids.add(tid)
        pri = check_enum(f, w, t, "pri", PRIS)
        for k in ("short", "pi", "inst"):
            check_str(f, w, t, k)
        for k in ("group", "type", "topic", "why", "question", "signalText", "posText", "funding", "next", "report"):
            check_str(f, w, t, k, required=False)
        cc = check_str(f, w, t, "cc")
        if cc and not CC_RE.match(cc):
            f.err(w, f"'cc' must be a two-letter lowercase country code, got {cc!r}")
        area = check_str(f, w, t, "area")
        if area and area_keys and area not in area_keys:
            f.err(w, f"'area' {area!r} is not a key in meta.areas ({', '.join(sorted(area_keys))})")
        tags = t.get("tags", [])
        if not isinstance(tags, list) or any(x not in area_keys for x in tags):
            f.err(w, "'tags' must be a list of meta.areas keys")
        check_enum(f, w, t, "work", WORK)
        signal = check_enum(f, w, t, "signal", SIGNALS)
        pos = check_enum(f, w, t, "pos", POSITIONS)
        deadline = check_date(f, w, t, "deadline", required=False, nullable=True)
        status = check_enum(f, w, t, "status", STATUSES)
        if kind == "watch" and status and status != "watch":
            f.err(w, "a watch entry must have status 'watch'")
        if status == "watch" and kind and kind != "watch":
            f.err(w, "status 'watch' is only for kind 'watch'")
        fv = t.get("fundingVerified", False)
        if not isinstance(fv, bool):
            f.err(w, "'fundingVerified' must be true or false")
        elig = t.get("eligibility")
        if elig is not None:
            if not isinstance(elig, dict):
                f.err(w, "'eligibility' must be an object {status, notes}")
            else:
                check_enum(f, f"{w}.eligibility", elig, "status", ELIGIBILITY)
                check_str(f, f"{w}.eligibility", elig, "notes", required=False)
        next_date = check_date(f, w, t, "nextDate", required=False, nullable=True)
        check_date(f, w, t, "added")
        links = t.get("links", [])
        if not isinstance(links, list):
            f.err(w, "'links' must be a list")
            links = []
        for j, link in enumerate(links):
            lw = f"{w}.links[{j}]"
            if not isinstance(link, dict):
                f.err(lw, "must be an object {href, label, accessed}")
                continue
            check_str(f, lw, link, "href")
            check_str(f, lw, link, "label")
            check_date(f, lw, link, "accessed", required=False)
        notes = t.get("notes", [])
        if not isinstance(notes, list) or not all(isinstance(x, str) for x in notes):
            f.err(w, "'notes' must be a list of strings")

        # Rules that are judgement calls: warn, never block.
        if kind in ("position", "programme") and pri == "A" and fv is not True:
            f.warn(w, "priority A needs verified funding (fundingVerified: true)")
        if kind == "group" and pri == "A" and signal in ("none", "endsbefore", "na"):
            f.warn(w, "priority A group without active grant evidence")
        if kind == "watch" and pri and pri != "C":
            f.warn(w, "watch-list entries are normally priority C")
        if pos == "open" and deadline and deadline < today.isoformat():
            f.warn(w, f"deadline {deadline} has passed; set pos to 'past' or update the deadline")
        if status in ACTIVE and not next_date:
            f.warn(w, "active target with no dated next action")
        if status in ACTIVE and next_date and next_date < today.isoformat():
            f.warn(w, f"next action was due {next_date}")
        if isinstance(elig, dict) and elig.get("status") == "fail" and status in ACTIVE:
            f.warn(w, "eligibility check failed but the target is still active")
        if kind != "watch" and elig is None:
            f.warn(w, "no eligibility check recorded")
        if not links:
            f.warn(w, "no source links")

    for i, a in enumerate(data.get("ads", [])):
        w = f"ads[{i}]"
        if not isinstance(a, dict):
            f.err(w, "must be an object")
            continue
        for k in ("title", "link", "src"):
            check_str(f, w, a, k)
        for k in ("org", "note"):
            check_str(f, w, a, k, required=False)
        cc = check_str(f, w, a, "cc")
        if cc and not CC_RE.match(cc):
            f.err(w, f"'cc' must be a two-letter lowercase country code, got {cc!r}")
        dates = a.get("dates", [])
        if not isinstance(dates, list) or not all(is_iso(d) for d in dates):
            f.err(w, "'dates' must be a list of YYYY-MM-DD dates (empty if none)")
        status = check_enum(f, w, a, "status", AD_STATUS)
        check_date(f, w, a, "added")
        if status == "open" and isinstance(dates, list) and dates and all(is_iso(d) for d in dates) \
                and max(dates) < today.isoformat():
            f.warn(w, "marked open but every closing date has passed")

    for i, g in enumerate(data.get("grants", [])):
        w = f"grants[{i}]"
        if not isinstance(g, dict):
            f.err(w, "must be an object")
            continue
        check_enum(f, w, g, "kind", GRANT_KINDS)
        for k in ("name", "type", "who", "recorded", "recruiting", "link"):
            check_str(f, w, g, k)
        check_str(f, w, g, "endLabel", required=False)
        check_enum(f, w, g, "sig", SIGNALS - {"position", "na"})
        a = check_date(f, w, g, "start")
        b = check_date(f, w, g, "end")
        if a and b and a > b:
            f.err(w, "'start' is after 'end'")
        for k in ("fadeIn", "fadeOut"):
            check_date(f, w, g, k, required=False)

    for i, c in enumerate(data.get("calls", [])):
        w = f"calls[{i}]"
        if not isinstance(c, dict):
            f.err(w, "must be an object")
            continue
        for k in ("name", "type", "who", "recorded", "recruiting", "link"):
            check_str(f, w, c, k)
        check_date(f, w, c, "from", required=False)
        ms = c.get("milestones", [])
        if not isinstance(ms, list):
            f.err(w, "'milestones' must be a list")
            continue
        for j, m in enumerate(ms):
            mw = f"{w}.milestones[{j}]"
            if not isinstance(m, dict):
                f.err(mw, "must be an object {date, label}")
                continue
            check_date(f, mw, m, "date")
            check_str(f, mw, m, "label")
            check_str(f, mw, m, "shown", required=False)

    for i, s in enumerate(data.get("scholarships", [])):
        w = f"scholarships[{i}]"
        if not isinstance(s, dict):
            f.err(w, "must be an object")
            continue
        for k in ("name", "funder", "covers", "link"):
            check_str(f, w, s, k)
        check_str(f, w, s, "note", required=False)
        check_enum(f, w, s, "eligible", SCH_ELIGIBLE)
        check_enum(f, w, s, "status", SCH_STATUS)
        d = s.get("deadline")
        if not (is_iso(d) or d in SCH_DEADLINE_WORDS):
            f.err(w, f"'deadline' must be YYYY-MM-DD or one of {', '.join(sorted(SCH_DEADLINE_WORDS))}, got {d!r}")

    for i, a in enumerate(data.get("actions", [])):
        w = f"actions[{i}]"
        if not isinstance(a, dict):
            f.err(w, "must be an object")
            continue
        check_date(f, w, a, "date")
        check_str(f, w, a, "what")
        if not isinstance(a.get("done", False), bool):
            f.err(w, "'done' must be true or false")
    return f


def print_findings(f, path):
    for e in f.errors:
        print(f"ERROR {e}")
    for w in f.warnings:
        print(f"warning {w}")
    if f.errors:
        print(f"{path}: {len(f.errors)} error(s), {len(f.warnings)} warning(s). Fix the errors and run again.")
    else:
        print(f"{path}: valid ({len(f.warnings)} warning(s)).")


def load_valid(path, today):
    text, data, m = load(path)
    f = validate(data, today)
    print_findings(f, path)
    if f.errors:
        sys.exit(1)
    return text, data, m


# ---------------------------------------------------------------- dated items

def dated_items(data, today):
    """Every dated item the agenda, the Next actions block and the report share."""
    items = []
    for t in data.get("targets", []):
        if t.get("status") not in ACTIVE:
            continue
        who = f"{t.get('id')} {t.get('short')}"
        if t.get("nextDate"):
            items.append({"date": t["nextDate"], "type": "action", "what": f"{who}: {t.get('next') or 'next action'}"})
        if t.get("deadline") and t.get("kind") in ("position", "programme"):
            items.append({"date": t["deadline"], "type": "deadline", "what": f"{who}: application deadline, {t.get('inst')}"})
    for s in data.get("scholarships", []):
        if s.get("status") in SCH_OPEN and is_iso(s.get("deadline")):
            items.append({"date": s["deadline"], "type": "deadline", "what": f"Scholarship deadline: {s.get('name')} ({s.get('funder')})"})
    for c in data.get("calls", []):
        for m in c.get("milestones", []):
            items.append({"date": m["date"], "type": "call", "what": f"{c.get('name')}: {m.get('label')}", "shown": m.get("shown")})
    for a in data.get("actions", []):
        if not a.get("done"):
            items.append({"date": a["date"], "type": "action", "what": a.get("what")})
    items.sort(key=lambda i: i["date"])
    for i in items:
        i["days"] = days_between(today, i["date"])
    return items


def when(i):
    shown = f"about {i['shown']}" if i.get("shown") else i["date"]
    if i["days"] < 0 and i["type"] != "call":
        return f"**{shown}** (overdue, {rel(i['days'])})"
    return f"**{shown}** ({rel(i['days'])})"


# ---------------------------------------------------------------- generated sections

def cell(v):
    s = "" if v is None else str(v)
    return s.replace("|", "\\|").replace("\r", " ").replace("\n", " ").strip() or "—"


def md_table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    out += ["| " + " | ".join(cell(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def link_md(label, href):
    return f"[{label.replace(']', ')')}]({href.replace(' ', '%20')})" if href else ""


def gen_next(data, today):
    items = [i for i in dated_items(data, today)
             if (i["days"] < 0 and i["type"] != "call") or 0 <= i["days"] <= HORIZON_DAYS]
    lines = [f"_Generated {today.isoformat()} by compass.py: overdue items and the next {HORIZON_DAYS} days._"]
    lines += [f"- {when(i)}: {i['what']}" for i in items] or ["- Nothing dated in this window."]
    return "\n".join(lines)


def gen_tracker(data, today):
    rows = []
    targets = [t for t in data.get("targets", []) if t.get("kind") != "watch"]
    for t in sorted(targets, key=lambda t: t.get("id") or ""):
        who = f"{t['group']} / {t['pi']}" if t.get("group") else t.get("pi")
        funding = t.get("funding") or t.get("signalText") or "unknown"
        if t.get("kind") in ("position", "programme") and not t.get("fundingVerified"):
            funding += " (unverified)"
        nxt = t.get("next") or ""
        if t.get("nextDate"):
            nxt = f"{nxt} ({t['nextDate']})"
        if t.get("report"):
            rep = link_md("report", t["report"])
        elif t.get("links"):
            rep = link_md(t["links"][0].get("label", "link"), t["links"][0].get("href"))
        else:
            rep = ""
        rows.append([t.get("id"), t.get("pri"), t.get("inst"), who, t.get("cc"), t.get("type") or t.get("kind"),
                     funding, t.get("deadline") or "—", t.get("status"), nxt, rep])
    if not rows:
        return "_No tracked targets yet._"
    return md_table(["ID", "Pri", "Institution", "Group / PI", "Country", "Type", "Funding", "Deadline",
                     "Status", "Next action (by date)", "Report"], rows)


def gen_watch(data, today):
    areas = {a["key"]: a["label"] for a in data.get("meta", {}).get("areas", [])}
    rows = []
    for t in sorted((t for t in data.get("targets", []) if t.get("kind") == "watch"), key=lambda t: (t.get("cc"), t.get("short"))):
        who = f"{t['group']} / {t['pi']}" if t.get("group") else t.get("pi")
        first = t.get("links") or [{}]
        rows.append([who, t.get("inst"), t.get("cc"), areas.get(t.get("area"), t.get("area")), t.get("why"),
                     link_md(first[0].get("label", "link"), first[0].get("href"))])
    if not rows:
        return "_No watch-list groups yet._"
    return md_table(["Group / PI", "Institution", "Country", "Area", "Why watch only", "Link"], rows)


def gen_scholarships(data, today):
    rows = [[s.get("name"), s.get("funder"), s.get("eligible"), s.get("covers"), s.get("deadline"), s.get("status"),
             link_md("link", s.get("link"))] for s in data.get("scholarships", [])]
    if not rows:
        return "_No external scholarships recorded yet._"
    return md_table(["Scheme", "Funder", "Eligible?", "Covers", "Deadline", "Status", "Link"], rows)


GENERATED = {"next": gen_next, "tracker": gen_tracker, "watch": gen_watch, "scholarships": gen_scholarships}


def dump_data(data):
    """Canonical data block: one JSON object per line inside each list, so one record is one line to edit."""
    parts = []
    keys = list(data.keys())
    for n, k in enumerate(keys):
        v = data[k]
        comma = "," if n < len(keys) - 1 else ""
        if isinstance(v, list) and v:
            inner = ",\n".join("    " + json.dumps(x, ensure_ascii=False) for x in v)
            parts.append(f'  "{k}": [\n{inner}\n  ]{comma}')
        elif isinstance(v, dict) and v:
            inner = ",\n".join(f"    {json.dumps(mk)}: {json.dumps(mv, ensure_ascii=False)}" for mk, mv in v.items())
            parts.append(f'  "{k}": {{\n{inner}\n  }}{comma}')
        else:
            parts.append(f'  "{k}": {json.dumps(v, ensure_ascii=False)}{comma}')
    return "{\n" + "\n".join(parts) + "\n}"


def cmd_sync(args, today):
    path = Path(args.save)
    text, data, m = load_valid(path, today)
    data.setdefault("meta", {})["updated"] = today.isoformat()
    text = text[:m.start(1)] + dump_data(data) + text[m.end(1):]
    for name, gen in GENERATED.items():
        pat = re.compile(rf"(<!-- {name}:start -->)(.*?)(<!-- {name}:end -->)", re.S)
        if not pat.search(text):
            print(f"warning: marker <!-- {name}:start --> not found; that section was not regenerated")
            continue
        body = gen(data, today)
        text = pat.sub(lambda mm: f"{mm.group(1)}\n{body}\n{mm.group(3)}", text, count=1)
    text = re.sub(r"(?m)^- Last updated: .*$", lambda _: f"- Last updated: {today.isoformat()}", text, count=1)
    write_text(path, text)
    n = len([t for t in data.get("targets", []) if t.get("kind") != "watch"])
    print(f"Synced {path}: {n} tracked target(s), {len(data.get('scholarships', []))} scholarship(s).")


# ---------------------------------------------------------------- report

def cmd_report(args, today):
    path = Path(args.save)
    _, data, _ = load_valid(path, today)
    template = Path(args.template) if args.template else ASSETS / "report-template.html"
    if not template.exists():
        fail(f"report template not found at {template}. The phd-compass and phd-compass-tracking skills include it.")
    page = template.read_text(encoding="utf-8")
    for token in ("__COMPASS_TITLE__", "__COMPASS_DATA__"):
        if token not in page:
            fail(f"{template} has no {token} placeholder")
    # "<" is escaped so no string in the data can close the <script> element.
    payload = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")
    page = page.replace("__COMPASS_TITLE__", html.escape(data["meta"]["title"]))
    page = page.replace("__COMPASS_DATA__", payload)
    out = Path(args.out) if args.out else path.with_name("phd-compass-report.html")
    write_text(out, page)
    targets = data.get("targets", [])
    print(f"Report written to {out}: {len(targets)} entries, {len(data.get('ads', []))} ads, "
          f"{len(data.get('grants', [])) + len(data.get('calls', []))} grants and calls.")


# ---------------------------------------------------------------- agenda, ids, init

def cmd_agenda(args, today):
    path = Path(args.save)
    _, data, _ = load(path)
    f = validate(data, today)
    if f.errors:
        print_findings(f, path)
        sys.exit(1)
    items = dated_items(data, today)
    overdue = [i for i in items if i["days"] < 0 and i["type"] != "call"]
    week = [i for i in items if 0 <= i["days"] <= 7]
    later = [i for i in items if 7 < i["days"] <= args.days]
    print(f"# Agenda from {today.isoformat()} ({args.days}-day window)")
    for title, group in (("Overdue", overdue), ("This week", week), (f"Later in the window", later)):
        print(f"\n## {title}")
        print("\n".join(f"- {when(i)}: {i['what']}" for i in group) or "- None.")
    print("\n## Gaps in the data block")
    gaps = [w for w in f.warnings if any(s in w for s in ("no dated next action", "was due", "has passed", "every closing date"))]
    print("\n".join(f"- {g}" for g in gaps) or "- None.")
    print("\nNot covered here: outreach follow-ups, referees, submissions and materials live in the Markdown sections.")


def cmd_next_id(args, today):
    _, data, _ = load(Path(args.save))
    nums = [int(t["id"][1:]) for t in data.get("targets", []) if isinstance(t.get("id"), str) and ID_RE.match(t["id"])]
    print(f"T{(max(nums) + 1 if nums else 1):03d}")


def cmd_init(args, today):
    path = Path(args.save)
    if path.exists():
        fail(f"{path} already exists; nothing written")
    template = ASSETS / "save-file-template.md"
    if not template.exists():
        fail(f"save-file template not found at {template}")
    write_text(path, template.read_text(encoding="utf-8").replace("__TODAY__", today.isoformat()))
    print(f"Created {path}. Fill in the profile, interests and meta, then run: compass.py validate {path}")


def cmd_validate(args, today):
    load_valid(Path(args.save), today)


def main():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    p = argparse.ArgumentParser(description="phd-compass save-file tool")
    p.add_argument("--today", help="YYYY-MM-DD; default: the system date")
    sub = p.add_subparsers(dest="cmd", required=True)
    for name, fn in (("init", cmd_init), ("validate", cmd_validate), ("sync", cmd_sync),
                     ("report", cmd_report), ("agenda", cmd_agenda), ("next-id", cmd_next_id)):
        sp = sub.add_parser(name)
        sp.add_argument("save", help="path to the save file (phd-compass.md)")
        sp.add_argument("--today", dest="today_sub", help="YYYY-MM-DD; default: the system date")
        sp.set_defaults(fn=fn)
        if name == "report":
            sp.add_argument("--out", help="output HTML path; default: phd-compass-report.html beside the save file")
            sp.add_argument("--template", help="report template; default: ../assets/report-template.html")
        if name == "agenda":
            sp.add_argument("--days", type=int, default=30, help="window in days (default 30)")
    args = p.parse_args()
    raw = args.today_sub or args.today
    if raw and not is_iso(raw):
        fail(f"--today must be YYYY-MM-DD, got {raw!r}")
    today = dt.date.fromisoformat(raw) if raw else dt.date.today()
    args.fn(args, today)


if __name__ == "__main__":
    main()
