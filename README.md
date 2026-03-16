# La Circe

This is a transcription of Giovanni Battista Gelli's La Circe, as translated by Thomas Brown.
It can be read online at [RMWinslow.com/circe](https://rmwinslow.com/circe).

This translation, published 1702, is in the public domain, but I had difficulty finding a clean transcription of it online, with the automated OCR texts on the [Internet Archive](https://archive.org/details/b30535827/page/n7/mode/2up) plagued by the menace of the 'long s'.

So here is a new transcription, using Claude Opus 4.6. I've instructed the robot to modernize the s's, while otherwise leaving the old timey spelling intact.



## Process

1. Go to the [Internet Archive scan](https://archive.org/details/b30535827/page/n7/mode/2up), and download the `SINGLE PAGE PROCESSED JP2 ZIP`. Extract it into the `pages/` folder.
2. Run `resize_pages.py` to scale the images down to about 1 megapixel each.
3. Ask the LLM to batch transcribe the images using the transcribe skill. Each page is converted to a single text file in `pages/txt/`
4. After the text is extracted, run `merge_pages.py` to generate the final markdown pages, which are served using Github Pages.


## Repository structure

```
circe/
├── index.md               # Jekyll site homepage (table of contents,etc)
├── README.md              # GitHub repo description (This file.)
├── CLAUDE.md              # Project context for Claude (nav_exclude)
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

