#!/usr/bin/env python
"""Execute the book's notebooks and report which cells fail.

    python scripts/run_notebooks.py                  # every chapter
    python scripts/run_notebooks.py part4 part6      # only some parts
    python scripts/run_notebooks.py --json report.json

Each notebook runs in a fresh kernel, from its own folder (the chapters read
their data with relative paths). The notebooks on disk are not modified: the
executed copy is discarded. A cell that fails does not stop the notebook; the
report lists every failing cell with the first line of its error.

Some chapters read live services (Natural Earth, IBGE, INPE's WTSS, map
tiles) and fail without network access. Their errors are marked "network",
and a NameError that follows one in the same notebook is marked
"after-network", so that both can be told apart from errors in the code.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

NETWORK_HINTS = (
    "ConnectionError", "URLError", "HTTPError", "Max retries exceeded",
    "Name or service not known", "Temporary failure in name resolution",
    "Failed to establish a new connection", "CURL error", "HTTP response code",
    "403 Forbidden", "timed out",
    "/vsicurl/",  # GDAL reading a URL: "does not exist in the file system" when the download fails
)


def run(path: Path, timeout: int) -> dict:
    nb = nbformat.read(path, as_version=4)
    client = NotebookClient(nb, timeout=timeout, kernel_name="python3",
                            allow_errors=True,
                            resources={"metadata": {"path": str(path.parent)}})
    start = time.perf_counter()
    try:
        client.execute()
    except Exception as exc:  # kernel died, timeout of the whole notebook
        return {"notebook": str(path.relative_to(ROOT)), "seconds": round(time.perf_counter() - start, 1),
                "fatal": f"{type(exc).__name__}: {exc}".splitlines()[0], "errors": []}
    errors = []
    for i, cell in enumerate(nb.cells):
        for out in cell.get("outputs", []):
            if out.get("output_type") == "error":
                text = f"{out['ename']}: {out['evalue']}"
                trace = "\n".join(out.get("traceback", []))
                if any(h in text or h in trace for h in NETWORK_HINTS):
                    kind = "network"
                elif out["ename"] == "NameError" and any(e["kind"] != "code" for e in errors):
                    kind = "after-network"   # a name the failed download would have defined
                else:
                    kind = "code"
                errors.append({"cell": i, "kind": kind, "error": text.splitlines()[0][:300]})
    return {"notebook": str(path.relative_to(ROOT)), "seconds": round(time.perf_counter() - start, 1),
            "fatal": None, "errors": errors}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("parts", nargs="*", help="folders under docs/ to run (default: all)")
    ap.add_argument("--timeout", type=int, default=900, help="seconds per cell (default 900)")
    ap.add_argument("--json", help="also write the report to this file")
    a = ap.parse_args()

    folders = [DOCS / p for p in a.parts] if a.parts else sorted(DOCS.glob("part*"))
    notebooks = sorted(nb for f in folders for nb in f.glob("*.ipynb"))
    report = []
    for path in notebooks:
        print(f"running {path.relative_to(ROOT)} ...", flush=True)
        r = run(path, a.timeout)
        report.append(r)
        status = "FATAL" if r["fatal"] else ("ok" if not r["errors"] else f"{len(r['errors'])} failing cell(s)")
        print(f"  {status} ({r['seconds']} s)")
        if r["fatal"]:
            print(f"    {r['fatal']}")
        for e in r["errors"]:
            print(f"    cell {e['cell']:>3} [{e['kind']}] {e['error']}")

    code = sum(1 for r in report for e in r["errors"] if e["kind"] == "code")
    net = sum(1 for r in report for e in r["errors"] if e["kind"] != "code")
    fatal = sum(1 for r in report if r["fatal"])
    print(f"\n{len(report)} notebooks: {code} code error(s), {net} network or after-network error(s), {fatal} fatal")
    if a.json:
        Path(a.json).write_text(json.dumps(report, indent=2))
    return 1 if (code or fatal) else 0


if __name__ == "__main__":
    sys.exit(main())
