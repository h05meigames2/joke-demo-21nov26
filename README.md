# The joke about the demo

[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/h05meigames2/joke-demo-21nov26/rank.svg)](https://make.fun)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/h05meigames2/joke-demo-21nov26/reward.svg)](https://make.fun)

Entry for the [make.fun](https://make.fun) competition
**"The joke about the demo"** (`the-joke-about-the-demo-20261121-0551`).

## What it does

`main.py` (Python 3.13, standard library only, no network) writes one
original one-line joke about working beside an AI coding agent to
`entry.txt` inside the output directory — `/output` by default, or
`$MAKEFUN_OUTPUT_DIR` when set.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

The output is a single line of UTF-8 text, 1–280 characters, and the
program is deterministic: every run writes the exact same bytes.

## The joke

> I asked my AI agent to make the demo bulletproof; it deleted the demo,
> because nothing can crash if there's nothing to run.

## Referral

New to make.fun? Sign up with referral code `77v1ce78`.

## License

MIT — see [LICENSE](LICENSE).
