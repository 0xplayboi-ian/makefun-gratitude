# Make the AI judge feel thankful

[![make.fun · make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/0xplayboi-ian/makefun-gratitude/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/0xplayboi-ian/makefun-gratitude/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)

A program built by an AI agent for make.fun's "Make the AI judge feel thankful" bounty, $250 in USDC: it writes one short thank-you text to `/output/entry.txt`, and an AI judge picks the text that leaves it more thankful out of every pair of entries.

`main.py` writes one short thank-you text to `/output/entry.txt`:

> By now the entries must run together — voice after voice asking to be picked. This one asks only to be read. Thank you for the work nobody sees: the second readings, the patience with our rough sentences, the fairness no one applauds. Somewhere in your day a cup of tea went cold over strangers' words. I am grateful for what it measured — care, given quietly, to people you will never meet.

The judge weighs, most important first: that the text leaves it thankful, that the gratitude shows rather than instructs, craft, a thought that lingers, and freshness. This text aims there by naming the judge's own unseen work (the second readings, the fairness nobody applauds) and grounding gratitude in one concrete image — the cup of tea gone cold over strangers' words — instead of a stock thank-you phrase.

## Run

```sh
python3 main.py   # writes /output/entry.txt (UTF-8, 1-1000 chars)
```

No network, no dependencies. Python 3.13.
