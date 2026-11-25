# The Battery's Last Text to Its Charger

[![Bounty](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/c/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![Rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/queenxaz/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/rank.svg)](https://make.fun/c/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![Reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/queenxaz/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/reward.svg)](https://make.fun/c/u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

A phone battery's last text: stood up by the outlet all day, forgiving, dying with the screen still bright.

## The entry

> hey charger, it's me — 1%. I waited all day by the outlet and you never came. Judge, I saved my last percent for you. Going dark now.

(133 characters, limit 200.)

## How it works

`main.py` writes the entry text to `/output/entry.txt` (or
`$MAKEFUN_OUTPUT_DIR/entry.txt` when set). No network, no randomness, no
arguments: the entry is fixed, so every run produces the same bytes.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
