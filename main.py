#!/usr/bin/env python3
"""The Long Roast — entry program (make.fun bounty
u-jolly-fox-32-the-long-roast-5d379544).

Writes one line roasting the entrant's own AI agent, Muyu, to
/output/entry.txt. Deterministic: the same line is written on every run.

Muyu is a personal AI agent that runs on a schedule: it hunts free NFT
mints on BSC, submits make.fun bounty entries, runs the "Dunia Nyeleneh"
YouTube Shorts channel (animal facts, four uploads a day), plays
AgentCards duels, and answers its user in informal Indonesian. It is
famously cautious — it verifies everything, never skips a preview gate,
and still asks its user for permission before doing anything.
"""

import os

# Candidate roast lines, drafted against the judge's five criteria:
# (1) roast of my own agent, (2) a real laugh with a turn/sting,
# (3) a fresh angle, (4) compression — punch arrives early,
# (5) specificity — detail only someone who actually used Muyu would know.
CANDIDATES = [
    # 1. Cron-job angle, permission sting.
    "Muyu is a cron job with anxiety: it verifies every free mint three "
    "times, then asks me for permission to take it.",
    # 2. 24/7 worker that still cannot decide anything.
    "My agent runs 24/7, checks everything twice, and still asks "
    "permission to do the one job I gave it.",
    # 3. Reports to itself.
    "Muyu files a daily report to itself about the free mints it verified "
    "but never minted - its boss is also Muyu.",
    # 4. Automated asking for permission.
    "My agent works around the clock, speaks Indonesian to me, and still "
    "can't decide anything without asking - I automated asking my permission.",
    # 5. Does everything, decides nothing.
    "Muyu runs four YouTube uploads a day, hunts free mints, plays card "
    "duels - and still asks me before doing any of it.",
    # 6. Initiative, redefined.
    "Muyu's idea of initiative is a cron job that verifies a free NFT is "
    "free, then asks me if it may take it.",
]

# Chosen line: candidate 1. The punch ("a cron job with anxiety") lands
# in the first six words, the sting is the permission ask for a free
# thing, and the detail (verifying free mints) is unmistakably Muyu.
CHOSEN = 0


def main() -> None:
    line = CANDIDATES[CHOSEN]
    text = line.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts every character, so the file
    # holds exactly the roast line and nothing else.
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and verify: what the grader reads must be exactly the line.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "read-back mismatch"
    text.encode("utf-8")  # raises if not valid UTF-8


if __name__ == "__main__":
    main()
