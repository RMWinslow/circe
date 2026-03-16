# La Circe

This is a transcription of Giovanni Battista Gelli's La Circe, as translated by Thomas Brown.

[Read it online](https://rmwinslow.com/circe) | [Internet Archive scan](https://archive.org/details/b30535827/page/n7/mode/2up)

[This translation](https://archive.org/details/b30535827/page/n7/mode/2up), published 1702, is in the public domain, but I had difficulty finding a clean transcription of it online, with the automated OCR texts plagued by the menace of the 'long s'.

So here is a new transcription, using Claude Opus 4.6. I've instructed the robot to modernize the s's, while otherwise leaving the old timey spelling in tact.

## Repository structure

- **`index.md`** — Jekyll site homepage with the table of dialogues
- **`_config.yaml`** — Jekyll config (uses the `just-the-docs-tweaked` remote theme)
- **`ch/`** — Merged dialog chapters (`1.md`–`10.md`), one per dialogue, with YAML
  front matter for the Jekyll site. Built from the per-page files by `merge_pages.py`.
  Also contains `all.md`, the complete text in a single file.
- **`pages_txt/`** — Per-page transcriptions with original 1702 spelling (303 `.txt`
  files, one per page scan). These are the authoritative ground truth, transcribed
  directly from the downscaled page images. Includes running headers, catch-words,
  marginal notes, and horizontal rules as they appear in the original printing.
- **`pages_txt_modernized/`** — The same per-page transcriptions with archaic spellings
  updated to modern equivalents (wou'd → would, Oister → Oyster, Lyon → Lion, etc.).
  Original meaning and sentence structure are preserved.
- **`pages_760w/`** — Downscaled page scans (760px wide JPGs, gitignored). Generated
  from the high-res JP2 files by `resize_pages.py`.
- **`merge_pages.py`** — Build script that concatenates per-page transcriptions into
  `ch/all.md`, then splits into individual chapter files by finding `Dialogue N.` lines.
  Strips running headers and catch-words, joins text flowing across page boundaries,
  and rejoins words split by hyphens at page breaks.
- **`resize_pages.py`** — Converts the high-res JP2 scans to 760px-wide JPGs.
- **`resize_pages_bw.py`** — Experimental BW conversion script (results too noisy, unused).
- **`fullraw.md`** — Raw OCR dump from the Internet Archive, kept for reference. Unusable
  without correction due to pervasive long-s misreadings.
- **`abbr/`** — Legacy abbreviated/abridged dialog versions, predating the full transcription.
- **`.claude/skills/transcribe/`** — Reusable `/transcribe` skill for Claude Code,
  encoding the per-page transcription format conventions.
- **`CLAUDE.md`** — Project context and instructions for Claude Code sessions.
- **`SINGLE PAGE PROCESSED JP2/`** — High-res page scans from the Internet Archive
  (318 JP2 files, ~200 MB, gitignored).
