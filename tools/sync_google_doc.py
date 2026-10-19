#!/usr/bin/env python3
"""Publish approved public AI mirror files into one existing Google Doc."""
import os
import json
import re
from pathlib import Path
import google.auth
from googleapiclient.discovery import build

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "ai-export-manifest.json").read_text(encoding="utf-8"))
if manifest.get("schema_version") != 1 or manifest.get("context", {}).get("target") != "GOOGLE_DOC_ID":
    raise SystemExit("Unsupported export manifest")
FILES = manifest["context"]["files"]
if not FILES or len(FILES) != len(set(FILES)) or "SOURCE_PRIVATE_COMMIT.md" not in FILES:
    raise SystemExit("Invalid context allowlist")
for name in FILES:
    path = Path(name)
    resolved = (root / path).resolve()
    if path.is_absolute() or ".." in path.parts or not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
        raise SystemExit("Unsafe or missing export file: " + name)
if manifest.get("workspace", {}).get("enabled"):
    raise SystemExit("Workspace sync not implemented; refusing partial export")
sections = []
for name in FILES:
    content = (root / name).read_text(encoding="utf-8")
    sections.append(f"========== ZAČIATOK SÚBORU: {name} ==========\n{content}\n========== KONIEC SÚBORU: {name} ==========")
source = (root / "SOURCE_PRIVATE_COMMIT.md").read_text(encoding="utf-8")
sha_matches = re.findall(r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])", source)
if not sha_matches:
    raise SystemExit("Missing private source commit SHA; refusing to publish.")
text = ("TravelTime – AI CONTEXT SNAPSHOT\n"
        "ODVODENÁ KÓPIA z verejného mirroru mirkos371/traveltime-ai; nie zdroj pravdy.\n"
        "Private source commit (pozri SOURCE_PRIVATE_COMMIT.md): " + sha_matches[0] + "\n\n"
        + "\n\n".join(sections) + "\n")
doc_id = os.environ["GOOGLE_DOC_ID"]
credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/documents"])
service = build("docs", "v1", credentials=credentials, cache_discovery=False)
doc = service.documents().get(documentId=doc_id).execute()
body = doc.get("body", {}).get("content", [])
end = body[-1]["endIndex"] if body else 2
requests = []
if end > 2:
    requests.append({"deleteContentRange": {"range": {"startIndex": 1, "endIndex": end - 1}}})
requests.append({"insertText": {"location": {"index": 1}, "text": text}})
service.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()
check = service.documents().get(documentId=doc_id).execute()
flat = "".join(el.get("textRun", {}).get("content", "") for item in check.get("body", {}).get("content", []) for el in item.get("paragraph", {}).get("elements", []))
if not all(f"ZAČIATOK SÚBORU: {name}" in flat and f"KONIEC SÚBORU: {name}" in flat for name in FILES) or sha_matches[0] not in flat:
    raise SystemExit("Readback verification failed")
print("Verified Google Doc update; private source commit:", sha_matches[0])
