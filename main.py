#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head — make.fun entry (account B).

Writes one joke about office life to /output/entry.txt.

Premise: the daily standup as a ghost story. The meeting that could have
been an email was killed — and now it haunts the team every morning at nine.
Setup, turn, punchline last, one line, under 200 characters.
"""

import os

JOKE = (
    "Our standup could have been an email, so we killed it — "
    "but it haunts us every morning at nine, because even ghosts "
    "can't decline a recurring calendar invite."
)


def write_entry(path="/output/entry.txt"):
    """Validate the entry against the competition gate, then write it."""
    text = JOKE
    encoded = text.encode("utf-8")
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    return text


if __name__ == "__main__":
    entry = write_entry()
    print(f"{len(entry)} characters, {len(entry.split())} words")
    print(entry)
