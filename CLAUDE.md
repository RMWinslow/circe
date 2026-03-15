# CLAUDE.md

## Style and communication

- Use natural, complete English in commit messages and all written text. Do not drop
  articles, prepositions, or other small words. Write like a person, not a telegram.
  Good: "Add the first pass at cleaning up Dialog 2"
  Bad: "Add Dialog 2 cleanup"
- Always update this file with todos, context, what was tried, what worked, and what
  didn't, so that future sessions can pick up where we left off.

## What this project is

This is a transcription of **Giovanni Battista Gelli's *La Circe***, in the 1702 English
translation by **Thomas Brown** (the satirist, 1663–1704), published by John Nutt in
London. The work is a series of philosophical dialogues in which Ulysses converses with
various Greeks who were transformed into animals by Circe and who (mostly) prefer their
animal forms.

The Internet Archive has scans of the 1702 edition, but the automated OCR is mangled
beyond usability — the long-s (ſ) is consistently misread as "f", producing things like
"Ulyffes", "pleafant", "reafon", etc. No clean digital transcription exists on any major
platform (Project Gutenberg, HathiTrust, Google Books) as of 2026. This repo is one of
the only attempts at a manual transcription.

There is a modern Robert Martin Adams edition (with Peter Kahn illustrations) that used
Thomas Brown's translation, but it is not in the public domain.

## Repository structure

```
circe/
├── CLAUDE.md              # This file — project context for Claude
├── README.md              # Brief project description
├── _config.yaml           # Jekyll / GitHub Pages config (just-the-docs-tweaked theme)
├── .gitignore             # Excludes all 318 JP2 page scans
├── fullraw.md             # Raw OCR dump from Internet Archive (~11,700 lines)
├── abbr/                  # Abbreviated / abridged versions of dialogs
│   ├── 1.md               # Dialog 1: Oyster (& Mole) — abridged (~51 lines)
│   └── 2.md               # Dialog 2 — stub (~10 lines)
├── ch/                    # Cleaned-up chapter transcriptions
│   └── 1.md               # Dialog 1: Oyster & Mole — partially cleaned (~421 lines)
└── SINGLE PAGE PROCESSED JP2/   # High-res page scans (untracked, ~200 MB)
    └── b30535827_0000.jp2 ... b30535827_0317.jp2  (318 files)
```

### Key details

- **fullraw.md** is the raw OCR text, hidden from site navigation (`nav_exclude: True`
  in `_config.yaml`). It is the reference for what still needs to be transcribed.
- **ch/** contains the "real" transcriptions — manually cleaned and corrected.
- **abbr/** contains condensed/abridged versions, not full transcriptions.
- Only **Dialog 1** has any significant transcription work done. The project is very
  early stage — roughly 3–4% of the raw text has been manually processed.
- The JP2 scans are kept locally for reference but are gitignored.

## Source material

- Internet Archive scan: https://archive.org/details/bim_eighteenth-century_la-circe-english-the-_gelli-giovanni-battista_1702
- Raw OCR text (unusable without correction): https://archive.org/stream/circesigniorgio00gellgoog/circesigniorgio00gellgoog_djvu.txt
- HathiTrust (access-restricted): https://babel.hathitrust.org/cgi/pt?id=mdp.39015023171559

## Current status and todos

- [ ] Dialog 1 (Oyster & Mole): partially transcribed in `ch/1.md` — needs review and completion
- [ ] Dialogs 2–11: not yet transcribed
- [ ] Determine the full list of dialogs and their animal/character pairings
- [ ] Decide on a consistent approach to modernizing spelling vs. preserving period forms

## What has been tried

- Raw OCR dump from Internet Archive was pulled into `fullraw.md` — confirmed to be
  heavily mangled, especially around long-s characters.
- Some manual transcription and correction was done for Dialog 1 in `ch/1.md`.
- Abbreviated versions were started in `abbr/` but seem to have been abandoned.
- No automated OCR correction scripts or tools have been tried yet.
