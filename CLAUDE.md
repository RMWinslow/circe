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
├── pages_760w/            # Downscaled page scans (760px wide JPGs, gitignored)
├── pages_txt/             # Per-page transcriptions from scans (tracked in git)
│   └── b30535827_0020.txt ... (one .txt per page image)
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
- The JP2 scans are kept locally for reference but are gitignored.

## Structure of the 1702 edition (318 scans, pages 0000–0317)

```
0000        Colour calibration card (digitizer artifact)
0001        Marbled endpaper (front)
0002        Shelfmark page ("Supp 59987/B" handwritten)
0003        Blank
0004        Internet Archive digitization notice
0005        Blank flyleaf (with faint handwritten marks)
0006        Blank
0007        TITLE PAGE — "The Circe of Signior Giovanni Battista Gelli"
0008        Blank (title page verso, with library stamp bleed-through)
0009        "To the Reader" (preface by Thomas Brown), p. 1
0010        "To the Reader", p. 2 (conclusion)
0011        "The Table of the Dialogues" (table of contents)
0012        Blank (table verso, bleed-through)
0013        "The Argument to the ensuing Dialogues", p. 1
0014        "The Argument", p. 2 (conclusion)
0015–0044   Dialog I: Oister & Mole (pp. 1–30)
0045–0078   Dialog II: the Snake (pp. 31–64)
0079–0113   Dialog III: the Hare (pp. 65–99)
0114–0140   Dialog IV: the Goat (pp. 100–126)
0140–0160   Dialog V: the Hind (pp. 126–146)
0161–0186   Dialog VI: the Lyon (pp. 147–172)
0187–0211   Dialog VII: the Horse (pp. 173–197)
0212–0238   Dialog VIII: the Dog (pp. 198–224)
0239–0267   Dialog IX: the Bullock (pp. 225–253)
0267–0309   Dialog X: the Elephant (pp. 253–295) — FINIS
0310        Publisher's catalogue (John Nutt)
0311        Blank
0312        Handwritten note: "Ulysses quotes Milton, p. 291."
0313–0315   Blank
0316        Marbled endpaper (back)
0317        Colour calibration card (digitizer artifact)
```

### The ten dialogues

| # | Animal | Former occupation | Pages | Outcome |
|---|--------|-------------------|-------|---------|
| I | Oister & Mole | Fisherman / Ploughman | 1–30 | Both refuse |
| II | Snake | Physician | 31–64 | Refuses |
| III | Hare | Country-Gentleman | 65–99 | Refuses |
| IV | Goat | Citizen of Corinth | 100–126 | Refuses |
| V | Hind | Grecian Woman | 127–146 | Refuses |
| VI | Lyon | Sailor | 147–172 | Refuses |
| VII | Horse | (not specified) | 173–197 | Refuses |
| VIII | Dog | Gentleman of Learning | 198–224 | Refuses |
| IX | Calf/Bullock | (not specified) | 225–253 | Refuses |
| X | Elephant | Philosopher (Aglaophemus) | 253–295 | Accepts |

## Source material

- Internet Archive scan: https://archive.org/details/bim_eighteenth-century_la-circe-english-the-_gelli-giovanni-battista_1702
- Raw OCR text (unusable without correction): https://archive.org/stream/circesigniorgio00gellgoog/circesigniorgio00gellgoog_djvu.txt
- HathiTrust (access-restricted): https://babel.hathitrust.org/cgi/pt?id=mdp.39015023171559

## Current status and todos

- [x] Page-by-page transcription of the entire book (pages 0007–0310) — DONE
- [ ] Review and proofread the per-page transcriptions against the scans
- [ ] Second pass on `pages_txt/` to modernize spellings
- [ ] Assemble per-page transcriptions into full dialog chapters in `ch/`
- [ ] Dialog 1 partial transcription in `ch/1.md` predates the per-page work — reconcile

## What has been tried

- Raw OCR dump from Internet Archive was pulled into `fullraw.md` — confirmed to be
  heavily mangled, especially around long-s characters.
- Some manual transcription and correction was done for Dialog 1 in `ch/1.md`.
- Abbreviated versions were started in `abbr/` but seem to have been abandoned.
- No automated OCR correction scripts or tools have been tried yet.
- **Page-by-page transcription from scans** (2026-03-15): Transcribed pages 0020–0029
  (printed pp. 6–15, Dialog I — Oister & Mole) from the 760px-wide JPGs using Claude's
  vision. Results are in `pages_txt/`. This worked well — the downscaled images are
  clearly readable. Marginal notes (e.g., the Portico footnote on p. 8) are rendered as
  bracketed notes after the paragraph they annotate. Original spelling is preserved
  exactly; only the long-s is corrected. Hyphenated line breaks are rejoined. Words split
  across page boundaries end with `—` to mark continuation.

## Page-by-page transcription workflow

Each page in `pages_760w/` gets a matching `.txt` file in `pages_txt/`. Format:

- First line: running header in brackets with em-dash separators for the three zones:
  `[6 — Ulysses, Circe, — Dial. I.]` or `[— Oister, and Mole. — 7]`
- Speaker names inline at the start of the paragraph, italicized: `*Ulysses.* To hear...`
- Italics marked with `*asterisks*`
- Original spelling preserved exactly (only long-s → s corrected)
- Marginal notes in brackets: `[* footnote text]`
- Words split across pages end with `—`
- Catch-words (the lone word at the bottom-right of each page) on their own line at the
  end of the file, separated by a blank line, not joined to the preceding sentence
