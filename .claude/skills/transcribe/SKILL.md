---
name: transcribe
description: Transcribe page scans from pages_760w/ into pages_txt/. Use when the user wants to transcribe pages from the 1702 La Circe scans.
argument-hint: <start_page> [end_page]
allowed-tools: Read, Write, Edit, Glob, Bash, Grep, Agent
---

# Page-by-page transcription of La Circe (1702)

Transcribe page images from `pages_760w/` into plain text files in `pages_txt/`.

## Arguments

- `$ARGUMENTS[0]` — start page number (e.g., `0030`), required
- `$ARGUMENTS[1]` — end page number (e.g., `0039`), optional (defaults to start + 9, i.e., 10 pages)

Page numbers are the 4-digit suffixes from the filenames, e.g., `b30535827_0030.jpg`.

## Transcription format

Each output file is plain text. No markdown formatting except `*asterisks*` for italics.

- **First line**: page number and running header as a comment:
  `[p. 16 — Ulysses, Circe, Dial. I.]`
- **Speaker names** on their own line, followed by a period: `Ulysses.` / `Oister.`
- **Dialogue text** follows as a regular paragraph
- **Italicized words** in the original (like *Greece*, *Eagle*) marked with `*asterisks*`
- **Preserve all original spelling exactly** (e.g., "mony", "Julips", "Knowledg") — only
  fix the long-s (ſ → s) and actual OCR-type errors
- **Hyphenated line breaks** in the original should be rejoined into whole words
- **Words split across pages**: include the partial word with a trailing `—` to mark
  continuation (the next page's file should start with the remainder)
- **Marginal notes / footnotes**: render as a bracketed note after the paragraph they
  annotate: `[* footnote text here]`

## Workflow

1. Determine the range of pages to transcribe from the arguments
2. Check which files already exist in `pages_txt/` to avoid re-doing work
3. Read the page images from `pages_760w/` (read up to 5 at a time in parallel)
4. Transcribe each page faithfully into the format above
5. Write each transcription to `pages_txt/b30535827_NNNN.txt`
6. After writing all files, spot-check 1–2 pages by re-reading the image alongside the
   transcription and fix any errors
7. Report how many pages were transcribed and any issues encountered

## Tips

- The images are 760px wide JPGs — readable but sometimes marginal notes or small text
  can be tricky. When uncertain about a word, do your best and flag it with `[?]`.
- Watch for the catch-word at the bottom of each page (a single word previewing the next
  page) — do NOT include it in the transcription, as it is a printing artifact.
- Running headers alternate between the two speakers' names on verso/recto pages.
- The printed page number appears in the header area, not the filename number.
