"""Build the entry line for u-clever-harbor-75-the-excuse-that-almost-works-69fde8f5.

Writes a single one-line excuse a gamer texts the boss to skip work on
GTA 6 launch week to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The gate requires UTF-8 text of 1 to 140 characters, not only whitespace,
and the task caps the line at 20 words. The judge is a tired manager who
has heard every excuse twice, so the line skips the stock dead-grandmother /
flat-tyre / sudden-fever angles and lands a boring, specific, unfalsifiable
detail instead: the broadband engineer cannot come till next week, which
leaves the sender stuck offline today. The laugh comes from the excuse's
own logic -- a gamer with no internet -- and the twist sits in the last
three words, like the one-liners that won the micro rounds before it.
"""

import os

ENTRY = (
    "Sorry, my internet's been dropping since last night and the engineer "
    "can't come till next week, I'm stuck offline today."
)


def build_line() -> str:
    """Return the single entry line, trimmed to one tight line."""
    line = " ".join(ENTRY.split())
    min_chars, max_chars = 1, 140  # gate: UTF-8 text, 1-140 chars
    if not (min_chars <= len(line) <= max_chars):
        raise ValueError(
            f"entry line is {len(line)} chars, must be {min_chars}-{max_chars}"
        )
    words = line.split()
    if len(words) > 20:  # task: at most 20 words
        raise ValueError(f"entry line is {len(words)} words, must be at most 20")
    if "\n" in line:
        raise ValueError("entry line must be a single line")
    return line


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    expected = build_line() + "\n"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(expected)
    # Verify what actually landed on disk: read it back and compare
    # byte-for-byte, so a truncated write, BOM or stray carriage return
    # is caught here instead of failing the gate at grading time.
    with open(path, "rb") as handle:
        raw = handle.read()
    if raw != expected.encode("utf-8"):
        raise ValueError("entry.txt on disk does not match the entry line")
    if raw.startswith(b"\xef\xbb\xbf") or b"\r" in raw:
        raise ValueError("entry.txt must not contain a BOM or carriage return")


if __name__ == "__main__":
    main()
