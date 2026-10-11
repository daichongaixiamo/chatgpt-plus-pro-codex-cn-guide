# Check Codex Usage Windows and Reset Times with Python

By AIXiamo. Example and official references verified on 2026-10-10.

A usage window can have remaining capacity while another is exhausted. A recorded reset time passing also does not establish the refreshed balance. This standard-library Python example makes those checks explicit, converts Unix seconds to UTC+08:00, and preserves missing or invalid observations.

[Chinese guide](README.md)

## Confirm the Access Method

ChatGPT sign-in provides subscription access; API-key sign-in uses usage-based access. Check the active account, workspace, and sign-in method before recording the window names, percentage meaning, and reset times. The usage dashboard and Codex CLI `/status` show current limits. See OpenAI's [authentication guide](https://learn.chatgpt.com/docs/auth) and [usage guidance](https://learn.chatgpt.com/docs/pricing).

## Run the Example

Requires Python 3.8 or later, with no additional packages. From the repository root:

```sh
python3 examples/codex-usage-windows/usage_windows.py --as-of '2026-09-11T15:00:00+08:00'
python3 -m unittest discover -s examples/codex-usage-windows -p 'test_usage_windows.py' -v
```

The fixed observation time is also the default when `--as-of` is omitted. All records are synthetic. The table below describes the script's Chinese-language output:

| Case | Recorded window | Used | Reset time, UTC+08:00 | Expected interpretation |
| --- | --- | ---: | --- | --- |
| A | Five-hour example | 100% | 2026-09-11 17:00 | Exhausted |
| A | Weekly example | 40% | 2026-09-14 10:00 | Not exhausted in this observation |
| B | Five-hour example | 20% | 2026-09-11 17:00 | Not exhausted in this observation |
| B | Weekly example | 100% | 2026-09-14 10:00 | Exhausted |
| C | Expired observation | 100% | 2026-09-11 14:59:59 | Reset time reached; refresh usage |
| C | Missing percentage | Missing | 2026-09-11 17:00 | Missing information |
| C | Milliseconds entered as seconds | 40% | Invalid | Invalid data |

The window names are example labels, not a universal schedule. Percentages from different windows are never added or averaged.

## Check a Manually Recorded Observation

```sh
python3 examples/codex-usage-windows/usage_windows.py \
  --as-of '2026-09-11T15:00:00+08:00' \
  --records '[{"name":"example-window","usedPercent":80,"resetsAt":1799398800}]'
```

This record yields a reset time of `2026-09-11T17:00:00+08:00`, with 20% remaining at the specified observation time.

| Field | Example contract |
| --- | --- |
| `name` | A manually recorded window label |
| `usedPercent` | Finite numeric percentage already used, from 0 to 100 |
| `resetsAt` | Integer Unix timestamp in seconds, from 1 to 9999999999 |
| `--as-of` | Observation time with an explicit timezone |

This is the example's learning schema, not an official API response. If the interface reports a remaining percentage, confirm its meaning before converting it. Missing values remain missing; they do not become zero. The timestamp range rejects common millisecond input mistakes.

## Verification Rules

Invalid types or values take priority over missing information. At or after the reset timestamp, the script requests a refresh instead of replacing an old percentage with zero. Before that timestamp, a valid 100% observation is exhausted; other valid percentages have `100 - usedPercent` remaining.

All 15 unit tests passed on 2026-10-10. They cover percentage boundaries, invalid types, missing data, Unix seconds versus milliseconds, timezone conversion, reset boundaries, CLI input, and independent windows.

Files: [implementation](usage_windows.py) and [tests](test_usage_windows.py). The program runs offline using built-in fixtures or supplied records, without reading account credentials. It uses the repository's MIT license.
