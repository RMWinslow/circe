---
nav_exclude: true
---

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
├── index.md               # Jekyll site homepage (table of dialogues)
├── README.md              # GitHub repo description
├── CLAUDE.md              # This file — project context for Claude (nav_exclude)
├── _config.yaml           # Jekyll / GitHub Pages config (just-the-docs-tweaked theme)
├── .gitignore             # Excludes JP2 scans and downscaled images
├── resize_pages.py        # Script: JP2 → 760px-wide JPGs in pages/jpg_760w/
├── merge_pages.py         # Script: pages/txt/ → ch/ (builds all.md, splits chapters)
├── pages/                 # All page-level assets (scans and transcriptions)
│   ├── SINGLE PAGE PROCESSED JP2/  # High-res scans (gitignored, ~200 MB, 318 files)
│   ├── jpg_760w/          # Downscaled page scans (760px wide JPGs, gitignored)
│   ├── txt/               # Per-page transcriptions, original spelling (303 files)
│   └── txt_modernized/    # Per-page transcriptions, modernized spelling (303 files)
├── ch/                    # Merged dialog chapters, built by merge_pages.py
│   ├── all.md             # Complete text in one file (nav_exclude)
│   └── 1.md – 10.md       # Individual chapters (layout: post, with subtitle)
└── .claude/
    └── skills/
        └── transcribe/    # /transcribe skill for page-by-page transcription
```

### Key details

- **index.md** is the Jekyll site homepage (served at rmwinslow.com/circe).
  **README.md** is the GitHub repo page (separate file, not processed by Jekyll).
- **pages/txt/** contains the authoritative per-page transcriptions with original 1702
  spelling. These are the ground truth, transcribed from the 760px-wide page scans.
- **pages/txt_modernized/** contains the same transcriptions with spelling updated to
  modern English (wou'd → would, Oister → Oyster, Lyon → Lion, etc.).
- **ch/** contains merged dialog chapters built from pages/txt/ by merge_pages.py.
  The script first builds `all.md` (complete text), then splits into individual chapters
  by finding `Dialogue N.` lines. Chapter files have `layout: post` and a `subtitle`
  field with the interlocutor list. Headers, catch-words, and page-break artifacts are
  stripped; flowing text is joined; hyphenated words are rejoined.

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
- [x] Modernized spelling pass (pages/txt_modernized/) — DONE
- [x] Merged dialog chapters in ch/ — DONE
- [ ] Review and proofread the per-page transcriptions against the scans
- [ ] Check for missed marginal notes / footnotes — only two found so far:
  p. 8 (0022, the Portico) and p. 202 (0216, "He means Sicily"). The original
  has marginal notes in small type that are easy to overlook.
- [ ] Add next/previous YAML fields to chapter files for navigation links
  (requires changes to the JTD-RMW theme to support them)
- [ ] Rebuild ch/ from pages/txt_modernized/ for a modernized-spelling edition
- [ ] Decide whether the Jekyll site should serve original or modernized text (or both)
- [ ] Reconsider how to handle the front-matter sections (title page, "To the Reader",
  "The Argument") — currently output as separate ch/ files by merge_pages.py, but it
  might be better to manually transpose the Argument into the start of ch/1.md, fold
  the preface into index.md, etc.

## What has been tried

- Raw OCR dump from Internet Archive was pulled into `fullraw.md` (since removed) —
  confirmed to be heavily mangled, especially around long-s characters.
- Some manual transcription and correction was done for Dialog 1 in `ch/1.md` before
  the systematic per-page approach was adopted.
- **Page-by-page transcription from scans** (2026-03-15/16): All 303 content pages
  transcribed from 760px-wide JPGs using Claude's vision. The `/transcribe` skill
  automates the process. Results are in `pages/txt/`.
- **Modernized spelling** (2026-03-16): All pages modernized in parallel into
  `pages/txt_modernized/`. Archaic forms (wou'd, tho', Oister, Lyon, Rhetorick, etc.)
  updated to modern equivalents. Original spelling preserved in `pages/txt/`.
- **BW image experiment** (2026-03-15): Tried threshold + crop + resize to 760h for
  smaller images. Results were too noisy — sticking with 760w colour images.

## Page-by-page transcription workflow

Each page in `pages/jpg_760w/` gets a matching `.txt` file in `pages/txt/`. Format:

- First line: running header in brackets with em-dash separators for the three zones:
  `[6 — Ulysses, Circe, — Dial. I.]` or `[— Oister, and Mole. — 7]`
- Speaker names inline at the start of the paragraph, italicized: `*Ulysses.* To hear...`
- Italics marked with `*asterisks*`
- Original spelling preserved exactly (only long-s → s corrected)
- Marginal notes in brackets: `[* footnote text]`
- Horizontal rules: `---` on its own line
- Catch-words (the lone word at the bottom-right of each page) on their own line at the
  end of the file, separated by a blank line, not joined to the preceding sentence
