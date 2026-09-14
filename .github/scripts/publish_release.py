"""Publish already-signed desktop artifacts; never build or sign in Actions."""

import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
from urllib.parse import quote


BOT = "github-actions[bot]"
REPOSITORY = "xeusxlabs/xeusx-desktop-mac"
ASSETS = {"Xeusx+.dmg", "Xeusx+.dmg.sha256", "updates.json", "updates.json.sig"}
TAG_PATTERN = r"v([0-9]{2})\.([0-9]+)\.([0-9]+)\+([0-9]+)"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def decode64(value, url=False):
    value = value.strip()
    return base64.b64decode(value + "=" * (-len(value) % 4),
                            altchars=b"-_" if url else None, validate=True)


def version(tag):
    match = re.fullmatch(TAG_PATTERN, tag)
    require(match is not None, "Invalid desktop release tag")
    return tuple(map(int, match.groups()))


class GitHub:
    def __init__(self, repository):
        require(repository == REPOSITORY, "Unexpected delivery repository")
        self.repository = repository

    def request(self, endpoint, method="GET", data=None, output=None,
                upload=None, missing_ok=False):
        if not endpoint.startswith("https://uploads.github.com/"):
            endpoint = f"repos/{self.repository}/{endpoint}"
        command = ["gh", "api", endpoint, "--method", method]
        if upload is not None:
            command += ["-H", "Content-Type: application/octet-stream", "--input", str(upload)]
        elif data is not None:
            command += ["--input", "-"]
        if output is not None:
            command += ["-H", "Accept: application/octet-stream"]
        result = subprocess.run(
            command, input=json.dumps(data).encode() if data is not None else None,
            stdout=output if output is not None else subprocess.PIPE,
            stderr=subprocess.PIPE, timeout=300 if upload or output else 60,
        )
        if result.returncode:
            if missing_ok and b"(HTTP 404)" in result.stderr:
                return None
            raise RuntimeError(result.stderr.decode(errors="replace").strip())
        if output is None and result.stdout.strip():
            return json.loads(result.stdout)
        return None

    def release(self, release_id):
        return self.request(f"releases/{release_id}", missing_ok=True)

    def by_tag(self, tag):
        return self.request(f"releases/tags/{quote(tag, safe='')}", missing_ok=True)

    def draft(self, tag):
        page = 1
        matches = []
        while True:
            releases = self.request(f"releases?per_page=100&page={page}")
            matches.extend(r for r in releases if r["tag_name"] == tag)
            if len(releases) < 100:
                break
            page += 1
        require(len(matches) <= 1, "Ambiguous publication draft")
        return matches[0] if matches else None

    def tag_commit(self, tag):
        item = self.request(f"git/ref/tags/{quote(tag, safe='')}")["object"]
        for _ in range(4):
            if item["type"] == "commit":
                return item["sha"]
            require(item["type"] == "tag", "Release tag must reference a commit")
            item = self.request(f"git/tags/{item['sha']}")["object"]
        raise RuntimeError("Excessively nested release tag")

    def download(self, asset, directory):
        path = directory / asset["name"]
        with path.open("wb") as stream:
            self.request(f"releases/assets/{asset['id']}", output=stream)
        require(path.stat().st_size == asset["size"], "Downloaded asset size differs")
        require("sha256:" + sha256(path) == asset["digest"], "Downloaded asset digest differs")


def inventory(release, bot=False):
    assets = release["assets"]
    require(len(assets) == len(ASSETS) and {a["name"] for a in assets} == ASSETS,
            "Release must contain exactly the four approved assets")
    require(not release["prerelease"] and not release.get("immutable", False),
            "Only mutable stable releases are supported")
    if bot:
        require(release["author"]["login"] == BOT, "Release is not owned by the Actions bot")
    for asset in assets:
        require(asset["state"] == "uploaded" and asset["size"] > 0,
                "Release contains an incomplete asset")
        require(re.fullmatch(r"sha256:[0-9a-f]{64}", asset.get("digest") or ""),
                "GitHub has not provided an asset digest")
        if bot:
            require(asset["uploader"]["login"] == BOT, "Asset is not owned by the Actions bot")
    return {a["name"]: (a["size"], a["digest"], a.get("label")) for a in assets}


def fingerprint(release):
    return {key: release.get(key) for key in
            ("id", "tag_name", "target_commitish", "name", "body", "draft", "prerelease", "immutable")} | {
                "assets": inventory(release),
                "asset_ids": sorted(a["id"] for a in release["assets"]),
                "author": release["author"]["login"],
            }


def verify_signed_assets(directory, tag, public_key):
    require({p.name for p in directory.iterdir()} == ASSETS, "Unexpected local asset inventory")
    raw_key = decode64(public_key.read_text())
    signature = decode64((directory / "updates.json.sig").read_text(), url=True)
    require(len(raw_key) == 32 and len(signature) == 64, "Invalid Ed25519 key or signature length")
    with tempfile.TemporaryDirectory() as scratch:
        key_path = Path(scratch) / "key.der"
        sig_path = Path(scratch) / "signature"
        key_path.write_bytes(bytes.fromhex("302a300506032b6570032100") + raw_key)
        sig_path.write_bytes(signature)
        subprocess.run([
            "openssl", "pkeyutl", "-verify", "-rawin", "-pubin", "-keyform", "DER",
            "-inkey", str(key_path), "-sigfile", str(sig_path),
            "-in", str(directory / "updates.json"),
        ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
    manifest = json.loads((directory / "updates.json").read_text())
    require(set(manifest) == {"plus"}, "Unexpected update channels")
    update = manifest["plus"]
    require(tag == f"v{update['version']}+{update['build']}", "Signed version does not match tag")
    require(update["dmgURL"] == f"https://github.com/{REPOSITORY}/releases/download/{tag}/Xeusx+.dmg",
            "Signed artifact URL must use the original release tag")
    digest = sha256(directory / "Xeusx+.dmg")
    require(update["sha256"] == digest, "DMG differs from signed checksum")
    require((directory / "Xeusx+.dmg.sha256").read_text().split() == [digest, "Xeusx+.dmg"],
            "Checksum sidecar differs from signed checksum")
    return digest


def verify_tag_metadata(github, commit, directory):
    for name in ("updates.json", "updates.json.sig"):
        item = github.request(f"contents/{name}?ref={commit}")
        require(item.get("encoding") == "base64", "Missing signed metadata at release commit")
        require(base64.b64decode(item["content"]) == (directory / name).read_bytes(),
                "Release assets differ from the signed metadata at the tagged commit")


def check_latest(github, tag, source_id, latest):
    current = github.request("releases/latest", missing_ok=True)
    if current is not None:
        require(latest or current["id"] != source_id, "Replacing Latest requires latest=true")
        require(not latest or version(tag) >= version(current["tag_name"]),
                "Refusing to mark an older release as Latest")
    return current


def publish(github, source_id, tag, commit, latest, replace_published, public_key, directory):
    version(tag)
    require(re.fullmatch(r"[0-9a-f]{40}", commit), "A full commit SHA is required")
    require(github.tag_commit(tag) == commit, "Release tag moved or references another commit")
    staging_tag = f"publication-{source_id}"
    source = github.release(source_id)
    staged = github.draft(staging_tag)
    existing = github.by_tag(tag)

    if source is None and existing is not None:
        inventory(existing, bot=True)
        require(not existing["draft"], "Unexpected draft at the final release tag")
        original = existing  # A retry after successful publication is verification-only.
    elif source is None:
        require(staged is not None and staged["draft"], "Source release and resumable draft are missing")
        inventory(staged, bot=True)
        original = staged  # Resume an interrupted swap using the verified bot draft.
    else:
        require(source["tag_name"] == tag, "Source release does not match the requested tag")
        require(existing is None or existing["id"] == source_id, "Another release occupies this tag")
        require(source["draft"] or replace_published, "Replacing a published release was not enabled")
        original = source

    proof = inventory(original)
    snapshot = fingerprint(original)
    for asset in original["assets"]:
        github.download(asset, directory)
    digest = verify_signed_assets(directory, tag, public_key)
    verify_tag_metadata(github, commit, directory)
    check_latest(github, tag, source_id, latest)

    if source is None and existing is not None:
        if latest:
            require(github.request("releases/latest")["id"] == existing["id"],
                    "Already-published release is no longer Latest")
        print(f"Already published and verified: {tag}, release {existing['id']}, SHA-256 {digest}")
        return existing

    if staged is None:
        staged = github.request("releases", "POST", {
            "tag_name": staging_tag, "target_commitish": commit,
            "name": original["name"], "body": original.get("body") or "",
            "draft": True, "prerelease": False,
        })
    require(staged["draft"] and staged["author"]["login"] == BOT,
            "Replacement must be an unpublished Actions bot draft")
    require(staged["target_commitish"] == commit and staged["name"] == original["name"]
            and (staged.get("body") or "") == (original.get("body") or ""),
            "Existing publication draft has different metadata")
    staged_assets = {a["name"]: a for a in staged["assets"]}
    require(len(staged_assets) == len(staged["assets"]) and set(staged_assets) <= ASSETS,
            "Unexpected assets in publication draft")
    for asset in original["assets"]:
        name = asset["name"]
        if name not in staged_assets:
            endpoint = f"https://uploads.github.com/repos/{github.repository}/releases/{staged['id']}/assets?name={quote(name, safe='')}"
            if asset.get("label"):
                endpoint += "&label=" + quote(asset["label"], safe="")
            github.request(endpoint, "POST", upload=directory / name)
    staged = github.release(staged["id"])
    require(inventory(staged, bot=True) == proof, "Replacement assets differ from the source")

    # Re-read all mutation-sensitive state immediately before the short swap.
    require(github.tag_commit(tag) == commit, "Release tag moved during preparation")
    check_latest(github, tag, source_id, latest)
    if source is not None:
        require(fingerprint(github.release(source_id)) == snapshot,
                "Source release changed during preparation")
        current = github.by_tag(tag)
        require((current is None and source["draft"]) or
                (current is not None and current["id"] == source_id), "Release at target tag changed")
        github.request(f"releases/{source_id}", "DELETE")
    else:
        require(github.by_tag(tag) is None, "Release at target tag changed")

    # All asset upload and verification finished before deletion. If this request
    # fails, the complete bot draft remains; rerun the same workflow inputs.
    try:
        github.request(f"releases/{staged['id']}", "PATCH", {
            "tag_name": tag, "target_commitish": commit, "draft": False,
            "make_latest": "true" if latest else "false",
        })
    except Exception as error:
        raise RuntimeError(f"Publication interrupted; verified draft {staged['id']} is retained. "
                           "Rerun with the same source ID, tag, and commit.") from error
    result = github.by_tag(tag)
    require(result is not None and not result["draft"] and result["id"] == staged["id"],
            "Published release is not the verified draft")
    require(inventory(result, bot=True) == proof, "Published assets changed")
    if latest:
        require(github.request("releases/latest")["id"] == result["id"], "Latest pointer did not update")
    print(f"Published and verified: {tag}, release {result['id']}, SHA-256 {digest}")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--source-release-id", type=int, required=True)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--latest", choices=("true", "false"), required=True)
    parser.add_argument("--replace-published", choices=("true", "false"), default="false")
    parser.add_argument("--public-key", type=Path, required=True)
    args = parser.parse_args()
    require(args.source_release_id > 0, "Invalid source release ID")
    require(os.environ.get("GITHUB_ACTIONS") == "true" and
            os.environ.get("GITHUB_REPOSITORY") == args.repository and
            os.environ.get("GITHUB_REF") == "refs/heads/main", "Publish only from the main-branch Actions workflow")
    with tempfile.TemporaryDirectory(prefix="desktop-release-") as scratch:
        publish(GitHub(args.repository), args.source_release_id, args.tag, args.commit,
                args.latest == "true", args.replace_published == "true", args.public_key, Path(scratch))


if __name__ == "__main__":
    main()
