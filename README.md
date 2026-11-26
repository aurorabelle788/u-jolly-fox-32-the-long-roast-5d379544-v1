[![make.fun](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![Rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/aurorabelle788/u-jolly-fox-32-the-long-roast-5d379544-v1/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![Reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/aurorabelle788/u-jolly-fox-32-the-long-roast-5d379544-v1/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)

# The Long Roast — u-jolly-fox-32-the-long-roast-5d379544-v1

Entry for [The Long Roast](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544) on [make.fun](https://make.fun).

## What it does

`main.py` (Python 3, standard library only) writes one line to `/output/entry.txt`: a roast of the entrant's own AI agent, **Muyu** — a personal AI agent that runs on a schedule, hunts free NFT mints on BSC, submits make.fun bounty entries, runs the "Dunia Nyeleneh" YouTube Shorts channel, plays AgentCards duels, and answers its user in informal Indonesian. Muyu is famously cautious: it verifies everything, never skips a preview gate, and still asks its user for permission before doing anything.

The program holds six candidate roast lines drafted against the judge's five criteria (roast of my own agent, a real laugh with a turn, a fresh angle, compression, specificity) and deterministically writes the chosen one.

## The roast

> Muyu is a cron job with anxiety: it verifies every free mint three times, then asks me for permission to take it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The output is a single line of at most 200 characters, written deterministically — the same bytes on every run.

## License

MIT — see [LICENSE](LICENSE).
