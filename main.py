"""agency-poem-01 entry (Python 3.13, standard library only).

Writes one fixed poem about agency to /output/entry.txt.

The poem is about the power to choose and to act, and what happens to
that power when you hand the doing to an agent: the work comes back
finished, and what stays with you is the decision itself -- the why,
the saying of "this, not that", and the willingness to answer for it.

Deterministic: the same bytes on every run, no input, no network, no
clock, no randomness. The output directory defaults to /output (the
grader mounts it writable) and honours MAKEFUN_OUTPUT_DIR elsewhere.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM_LINES = [
    "I handed it the plans, and it built.",
    "By lunch the walls stood, square and true,",
    "every nail sunk where my hand would have sunk it \u2014",
    "the house I meant, raised without me.",
    "",
    "That is the wonder, and the wound:",
    "the work comes back finished, finished well,",
    "and I am left holding the one thing",
    "no borrowed hands can lift from me: the why.",
    "",
    "It can carry the hammer. It can swing.",
    "It cannot stand in the yard at dusk",
    "and decide the house is worth the building.",
    "That decision is mine. That is the whole job.",
    "",
    "So I lend it my hands, and keep my reasons \u2014",
    "the part of me that says this, not that,",
    "and means it, and will answer for it.",
]

POEM = "\n".join(POEM_LINES)


def validate_poem(text: str) -> None:
    """Guard the gate before writing: 1-1000 code points, not only whitespace."""
    if not 1 <= len(text) <= 1000:
        raise ValueError(f"poem must be 1-1000 characters, got {len(text)}")
    if not any(not c.isspace() for c in text):
        raise ValueError("poem must contain a non-whitespace character")


def main() -> None:
    validate_poem(POEM)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
