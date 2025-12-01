# advent-of-code-2025

My solutions for Advent of Code 2025 challenges.

## Running solutions

Each language has a generic runner so you do **not** need per-day npm scripts. Pass the day number (two digits) after `--` so npm forwards it to the script:

```bash
# JavaScript
npm run day:js -- 01

# Python
npm run day:py -- 01
```

> **Note:** Without the `--` separator npm treats `--01` as its own flag, which triggers the warning you saw. Always include the space-delimited argument after `--`.
