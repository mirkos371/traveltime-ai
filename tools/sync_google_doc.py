#!/usr/bin/env python3
"""Publish explicit allowlisted AI context and workspace files to one Google Doc."""
import hashlib
import json
import os
import re
from pathlib import Path

import google.auth
from googleapiclient.discovery import build

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "ai-export-manifest.json").read_text(encoding="utf-8"))
if manifest.get("schema_version") != 2 or manifest.get("context", {}).get("target") != "GOOGLE_DOC_ID":
    raise SystemExit("Unsupported manifest schema")
source = (ROOT / "SOURCE_PRIVATE_COMMIT.md").read_text(encoding="utf-8")
match = re.search(r"### PRIVATE_SOURCE_COMMIT\s+.*?`([0-9a-f]{40})`", source, re.S)
if not match:
    raise SystemExit("Cannot determine declared private source commit")
private_sha = match.group(1)
entries = [{"path": name, "kind": "context", "provenance": "private-mirror", "source_commit": private_sha}
           for name in manifest["context"]["files"]]
if manifest.get("workspace", {}).get("enabled", False):
    entries.extend({"path": item["path"], "kind": "workspace",
                    "provenance": item["provenance"],
                    "source_commit": item.get("source_commit")}
                   for item in manifest["workspace"]["files"])
if not entries or len({x["path"] for x in entries}) != len(entries):
    raise SystemExit("Empty or duplicate export file list")
if "SOURCE_PRIVATE_COMMIT.md" not in {x["path"] for x in entries}:
    raise SystemExit("Missing source commit declaration")
if len(entries) > 40:
    raise SystemExit("Too many export files")
sections = []
inventory = []
for entry in entries:
    name = entry["path"]
    path = Path(name)
    resolved = (ROOT / path).resolve()
    if (path.is_absolute() or ".." in path.parts or not resolved.is_relative_to(ROOT.resolve())
            or not resolved.is_file() or resolved.is_symlink()
            or path.suffix.lower() not in {".md", ".txt", ".py", ".json", ".yaml", ".yml"}):
        raise SystemExit("Unsafe or missing export file: " + name)
    provenance = entry["provenance"]
    if provenance not in {"private-mirror", "synthetic-test"}:
        raise SystemExit("Unsupported provenance: " + name)
    if provenance == "private-mirror" and entry["source_commit"] != private_sha:
        raise SystemExit("Mixed private source commits: " + name)
    if provenance == "synthetic-test" and entry["kind"] != "workspace":
        raise SystemExit("Synthetic tests allowed only in workspace")
    data = resolved.read_bytes()
    if len(data) > 150_000:
        raise SystemExit("File too large: " + name)
    body = data.decode("utf-8")
    digest = hashlib.sha256(data).hexdigest()
    inventory.append({"path": name, "kind": entry["kind"], "provenance": provenance,
                      "source_commit": entry["source_commit"] if provenance == "private-mirror" else "NONE - SYNTHETIC",
                      "sha256": digest, "bytes": len(data)})
    sections.append(f"========== ZAČIATOK SÚBORU: {name} ==========\n"
                    f"PROVENANCE: {provenance}\n"
                    f"PRIVATE_SOURCE_COMMIT: {private_sha if provenance == 'private-mirror' else 'NONE - SYNTHETIC'}\n"
                    f"SHA256: {digest}\n"
                    f"========== OBSAH SÚBORU: {name} ==========\n{body}\n"
                    f"========== KONIEC SÚBORU: {name} ==========")
public_commit = os.getenv("GITHUB_SHA", "UNAVAILABLE")
header = ("TravelTime – AI CONTEXT SNAPSHOT + AI WORKSPACE\n"
          "ODVODENÁ KÓPIA, nie autoritatívny zdroj.\n"
          f"DECLARED PRIVATE_SOURCE_COMMIT: {private_sha}\n"
          f"PUBLIC_MIRROR_COMMIT: {public_commit}\n"
          "SYNTHETIC-TEST files are NOT derived from the private commit.\n"
          "INVENTÁR SÚBOROV (JSON):\n" + json.dumps(inventory, ensure_ascii=False, indent=2) + "\n"
          "KONIEC INVENTÁRA\n\n")
text = header + "\n\n".join(sections) + "\n"
if len(text) > 850_000:
    raise SystemExit("Snapshot too large for configured safety limit")
credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/documents"])
service = build("docs", "v1", credentials=credentials, cache_discovery=False)
doc_id = os.environ["GOOGLE_DOC_ID"]
doc = service.documents().get(documentId=doc_id).execute()
content = doc.get("body", {}).get("content", [])
end = content[-1]["endIndex"] if content else 2
requests = []
if end > 2:
    requests.append({"deleteContentRange": {"range": {"startIndex": 1, "endIndex": end - 1}}})
requests.append({"insertText": {"location": {"index": 1}, "text": text}})
service.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()
check = service.documents().get(documentId=doc_id).execute()
flat = "".join(el.get("textRun", {}).get("content", "")
               for item in check.get("body", {}).get("content", [])
               for el in item.get("paragraph", {}).get("elements", []))
if not all(f"ZAČIATOK SÚBORU: {x['path']}" in flat and
           f"KONIEC SÚBORU: {x['path']}" in flat and x["sha256"] in flat
           for x in inventory) or private_sha not in flat or public_commit not in flat:
    raise SystemExit("Google Doc readback verification failed")
print(f"Verified {len(inventory)} files, private commit {private_sha}, public commit {public_commit}")
