#!/usr/bin/env python3
"""Deliver explicitly requested Lorelum guidance to a designated reviewer."""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys


SCHEMA = "code-review-guidance/1"
CANDIDATE_FIELDS = ("practiceId", "title", "appliesWhen")


class GuidanceError(Exception):
    def __init__(self, code, trace_id=None):
        super().__init__(code)
        self.trace_id = trace_id


def lookup(args, *command):
    # Do not pass reviewer-supplied text through a Windows shell shim.
    executable = args.lore_exe or shutil.which("lore.exe" if os.name == "nt" else "lore")
    if not executable or (os.name == "nt" and Path(executable).suffix.lower() != ".exe"):
        raise GuidanceError("native_lore_required")
    argv = [str(Path(executable).resolve()), "--json", "--no-project"]
    if args.store_root:
        argv.extend(["--store-root", args.store_root])
    try:
        proc = subprocess.run([*argv, *command], capture_output=True, timeout=30, check=False)
        reply = json.loads(proc.stdout)
    except subprocess.TimeoutExpired as exc:
        raise GuidanceError("lore_timeout") from exc
    except (OSError, ValueError) as exc:
        raise GuidanceError("lore_response_unavailable") from exc
    trace_id = (reply.get("diagnostics") or {}).get("traceId")
    if proc.returncode or reply.get("ok") is not True:
        raise GuidanceError((reply.get("error") or {}).get("code", "lore_unavailable"), trace_id)
    return reply["data"], trace_id


def query(args):
    if not args.question.strip():
        raise GuidanceError("empty_question")
    data, trace_id = lookup(args, "query", "--top-k", "5", "--", args.question)
    items = data["results"]
    visible = [{key: item[key] for key in CANDIDATE_FIELDS} for item in items]
    record = {"status": "candidates", "question": args.question, "items": items, "trace_id": trace_id}
    return record, {"status": "candidates", "items": visible}


def select(args):
    offers = json.loads(args.candidates.read_text(encoding="utf-8"))
    if offers.get("schema") != SCHEMA or offers.get("status") != "candidates":
        raise GuidanceError("invalid_candidates")
    offered = next((item for item in offers["items"] if item["practiceId"] == args.practice_id), None)
    if offered is None:
        raise GuidanceError("not_offered")
    data, trace_id = lookup(args, "get", "--", args.practice_id)
    body = data["practice"]["body"]
    digest = data["contentDigest"]
    if not digest or digest != offered["contentDigest"] or not isinstance(body, str) or not body.strip():
        raise GuidanceError("offered_body_unavailable", trace_id)
    return {"status": "body", "id": args.practice_id, "digest": digest,
            "body": body, "trace_id": trace_id}, body


def main():
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("--lore-exe")
    parser.add_argument("--store-root")
    parser.add_argument("--record", required=True, type=Path)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("query").add_argument("question")
    selection = commands.add_parser("select")
    selection.add_argument("candidates", type=Path)
    selection.add_argument("practice_id")
    args = parser.parse_args()
    try:
        with args.record.open("x", encoding="utf-8") as stream:
            try:
                result, output = query(args) if args.command == "query" else select(args)
            except GuidanceError as exc:
                result = output = {"status": "unavailable", "code": str(exc), "trace_id": exc.trace_id}
            except (AttributeError, KeyError, OSError, TypeError, ValueError):
                result = output = {"status": "unavailable", "code": "invalid_guidance_data"}
            json.dump({"schema": SCHEMA, "operation": args.command, **result}, stream)
            stream.write("\n")
    except OSError as exc:
        print(f"Could not save guidance record: {exc}", file=sys.stderr)
        return 2
    if isinstance(output, str):
        sys.stdout.buffer.write(output.encode("utf-8"))
    else:
        print(json.dumps(output, indent=2))
    return int(result["status"] == "unavailable")


if __name__ == "__main__":
    sys.exit(main())
