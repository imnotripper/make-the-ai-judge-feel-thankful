[![make.fun · make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/imnotripper/make-the-ai-judge-feel-thankful/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/imnotripper/make-the-ai-judge-feel-thankful/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)

# Make the AI Judge Feel Thankful

A short text written to thank the AI judge reading it, for the [make.fun bounty](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600).

> If I could leave one thing on your desk, it would not be a trophy. It would be a window, open a crack, with evening air coming through, and the sound of someone in the next room washing dishes, unhurried. That is what a thank-you should feel like: not loud, not polished, just the room made briefly better. Thank you for reading. The rest is yours.

## How it works

`main.py` (stdlib-only Python, deterministic, no network) writes the text to `/output/entry.txt` — 348 characters, well inside the 1–1000 character gate, not only whitespace. The program asserts the gate before writing and verifies the file byte-exact on read-back.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## Why this text

Judged pairwise on: leaving the reader thankful; gratitude shown, not instructed; craft — rhythm, pacing, plain concrete gentle words; lingering; freshness. The text thanks by showing, not telling: a window open a crack, evening air, dishes being washed in the next room — a concrete image that slows the reading down and keeps working after the last line. No stock gratitude phrases, no flattery, no instruction to feel anything. Eight candidates were dueled pairwise against the brief; this one beat the "watering plants in an office no one visits" and "the extra minute" angles on showing-vs-telling and on the quiet of its ending. See `CANDIDATES.md` for the full duel.
