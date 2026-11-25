"""Fix Human Sleep: Funniest Patch Note.

Competition: u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27
Final text (83 characters, one line):
    Fixed: your brain no longer installs updates the moment your head hits the pillow.

Gate (from kit competition.yaml): /output/entry.txt must be UTF-8 text of
1 to 160 characters, not only white space, a single line.

This program is stdlib-only, deterministic, and writes entry.txt to
MAKEFUN_OUTPUT_DIR (default "/output").
"""

import os

TEXT = "Fixed: your brain no longer installs updates the moment your head hits the pillow.\n"


def check_gate() -> None:
    """Assert the kit gate: 1-160 chars, not only whitespace, one line."""
    body = TEXT.rstrip("\n")
    assert 1 <= len(body) <= 160, f"text is {len(body)} chars, must be 1-160"
    assert body.strip(), "text must not be only whitespace"
    assert "\n" not in body, "text must be a single line"


def verify_written_bytes(path: str) -> None:
    """Re-read the written file and compare it byte-for-byte with TEXT."""
    with open(path, "rb") as f:
        written = f.read()
    assert written == TEXT.encode("utf-8"), "written bytes differ from TEXT"


def main() -> None:
    check_gate()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    verify_written_bytes(path)


if __name__ == "__main__":
    main()
