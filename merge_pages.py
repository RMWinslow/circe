"""
Merge per-page transcriptions from pages_txt/ into ch/.

Two-phase approach:
1. Concatenate all pages into ch/all.md, stripping headers and catch-words
   and joining text that flows across page boundaries.
2. Split ch/all.md into individual chapter files (ch/1.md–ch/10.md) by
   finding lines that say "Dialogue I.", "Dialogue II.", etc.
"""

import os
import re

BASE = os.path.dirname(__file__)
PAGES_DIR = os.path.join(BASE, "pages_txt")
CH_DIR = os.path.join(BASE, "ch")

# All content pages in order (front matter through FINIS)
FIRST_PAGE = 15
LAST_PAGE = 309

# Chapter metadata for YAML front matter
CHAPTERS = {
    "I": (1, "Dialogue I. Oister and Mole"),
    "II": (2, "Dialogue II. The Snake"),
    "III": (3, "Dialogue III. The Hare"),
    "IV": (4, "Dialogue IV. The Goat"),
    "V": (5, "Dialogue V. The Hind"),
    "VI": (6, "Dialogue VI. The Lyon"),
    "VII": (7, "Dialogue VII. The Horse"),
    "VIII": (8, "Dialogue VIII. The Dog"),
    "IX": (9, "Dialogue IX. The Bullock"),
    "X": (10, "Dialogue X. The Elephant"),
}


def read_page(scan_num):
    fname = f"b30535827_{scan_num:04d}.txt"
    path = os.path.join(PAGES_DIR, fname)
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def strip_header(text):
    """Remove the bracketed running header (first line if it starts with [)."""
    lines = text.split("\n")
    if lines and lines[0].startswith("["):
        lines = lines[1:]
        if lines and lines[0].strip() == "":
            lines = lines[1:]
    return "\n".join(lines)


def strip_catchword(text):
    """Remove the catch-word: the last non-empty line preceded by a blank line."""
    lines = text.rstrip("\n").split("\n")
    if len(lines) < 2:
        return text

    i = len(lines) - 1
    while i >= 0 and lines[i].strip() == "":
        i -= 1

    if i < 1:
        return text

    if lines[i - 1].strip() == "":
        lines = lines[:i - 1]

    return "\n".join(lines)


def join_pages(pages):
    """Join page texts, merging flowing text across page boundaries."""
    if not pages:
        return ""

    result = pages[0]
    for page in pages[1:]:
        if not page:
            continue

        prev_lines = result.rstrip("\n").split("\n")
        next_lines = page.lstrip("\n").split("\n")

        prev_last = prev_lines[-1] if prev_lines else ""
        next_first = next_lines[0] if next_lines else ""

        prev_is_text = prev_last.strip() != "" and prev_last.strip() != "---"
        next_is_continuation = (next_first.strip() != ""
                                and not next_first.startswith("---")
                                and not next_first.startswith("Dialogue ")
                                and not next_first.startswith("CIRCE")
                                and not next_first.startswith("*")
                                and not next_first.startswith("["))

        if prev_is_text and next_is_continuation:
            if prev_last.rstrip().endswith("-"):
                result = result.rstrip("\n").rstrip()
                result = result[:-1]
                result += page.lstrip("\n")
            else:
                result = result.rstrip("\n") + " " + page.lstrip("\n")
        else:
            result = result.rstrip("\n") + "\n\n" + page.lstrip("\n")

    return result


# --- Phase 1: Build ch/all.md ---

print("Phase 1: Building ch/all.md from all content pages...")

pages = []
for scan in range(FIRST_PAGE, LAST_PAGE + 1):
    raw = read_page(scan)
    if raw is None:
        continue
    text = strip_header(raw)
    text = strip_catchword(text)
    pages.append(text.strip())

all_text = join_pages([p for p in pages if p])

os.makedirs(CH_DIR, exist_ok=True)

all_path = os.path.join(CH_DIR, "all.md")
with open(all_path, "w", encoding="utf-8") as f:
    f.write("---\ntitle: \"La Circe — Complete Text\"\nnav_exclude: true\n---\n\n")
    f.write(all_text.strip() + "\n")

print(f"  -> ch/all.md ({len(all_text)} chars)")

# --- Phase 2: Split into individual chapters ---

print("Phase 2: Splitting into individual chapter files...")

# Split on lines that match "Dialogue <roman>." exactly
# The pattern to split on is the --- before each "Dialogue N." line
# We look for the sequence: \n---\n\nDialogue <roman>.\n
dialog_pattern = re.compile(
    r'\n---\n\n(Dialogue ([IVXL]+)\.)\n',
)

# Find all dialog boundaries in the full text
boundaries = list(dialog_pattern.finditer(all_text))

for idx, match in enumerate(boundaries):
    roman = match.group(2)
    if roman not in CHAPTERS:
        print(f"  WARNING: Unknown dialog numeral: {roman}")
        continue

    dialog_num, title = CHAPTERS[roman]

    # Chapter starts at the --- before "Dialogue N."
    start = match.start() + 1  # skip the leading \n

    # Chapter ends at the next boundary, or end of text
    if idx + 1 < len(boundaries):
        # Find the --- that starts the next dialog
        end = boundaries[idx + 1].start()
    else:
        end = len(all_text)

    chapter_text = all_text[start:end].strip()

    outpath = os.path.join(CH_DIR, f"{dialog_num}.md")
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(f"---\ntitle: \"{title}\"\nnav_order: {dialog_num}\n---\n\n")
        f.write(chapter_text + "\n")

    print(f"  Dialog {dialog_num:2d}: ch/{dialog_num}.md")

print("Done.")
