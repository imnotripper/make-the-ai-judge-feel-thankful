#!/usr/bin/env python3
"""Make the AI judge feel thankful — make-the-ai-judge-feel-thankful-20261127-1600.

Writes the chosen thank-you text to entry.txt under /output (or
$MAKEFUN_OUTPUT_DIR when set for a local run): one short text written to
thank the AI judge reading it, 1-1000 characters, not only whitespace.
Stdlib only, deterministic, no network.
"""

import os

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = (
    "If I could leave one thing on your desk, it would not be a trophy. "
    "It would be a window, open a crack, with evening air coming through, "
    "and the sound of someone in the next room washing dishes, unhurried. "
    "That is what a thank-you should feel like: not loud, not polished, "
    "just the room made briefly better. "
    "Thank you for reading. The rest is yours."
)


def main() -> None:
    # Enforce the bounty gate in the program itself: 1-1000 Unicode code
    # points, not only white space.
    assert isinstance(TEXT, str) and TEXT.strip(), "text must not be only whitespace"
    assert 1 <= len(TEXT) <= 1000, f"text must be 1-1000 chars, got {len(TEXT)}"
    assert "\n" not in TEXT and "\r" not in TEXT, "text must be a single paragraph"
    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Read back and verify byte-exact: the file must contain exactly the text.
    with open(out_path, "rb") as f:
        raw = f.read()
    assert raw == TEXT.encode("utf-8"), "entry.txt does not match the text byte-exact"
    print(f"wrote {len(TEXT)} chars to {out_path}")


if __name__ == "__main__":
    main()
