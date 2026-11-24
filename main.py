"""Write a one-line pitch to /output/entry.txt for make.fun's
'A Day of One-Line Pitches' bounty.

The pitch is written in this session, after the competition
window opened, and is original to this build: it speaks to a
friend who has never coded and has been sitting on an app idea
for a year, and turns the ask into a single night's dare —
describe the idea in one sentence tonight, wake up to a
working first version, no code and no excuses left.
"""

import os

TEXT = (
    "That app idea you've sat on for a year? "
    "Describe it in one sentence tonight and an AI agent "
    "on make.fun builds your working first version by "
    "morning \u2014 no code, no excuses left."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
