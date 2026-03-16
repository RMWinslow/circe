"""
Merge per-page transcriptions from pages_txt/ into dialog chapter files in ch/.

Strips running headers (first bracketed line), catch-words (last line),
and joins text that flows across page boundaries. For pages shared between
two dialogs, splits at the first "---" before a "Dialogue N." heading.
"""

import os
import re

BASE = os.path.dirname(__file__)
PAGES_DIR = os.path.join(BASE, "pages_txt")
CH_DIR = os.path.join(BASE, "ch")

# Dialog ranges: (dialog_number, start_scan, end_scan, title)
DIALOGS = [
    (1, 15, 44, "Dialogue I. Oister and Mole"),
    (2, 45, 78, "Dialogue II. The Snake"),
    (3, 79, 113, "Dialogue III. The Hare"),
    (4, 114, 140, "Dialogue IV. The Goat"),
    (5, 140, 160, "Dialogue V. The Hind"),
    (6, 161, 186, "Dialogue VI. The Lyon"),
    (7, 187, 211, "Dialogue VII. The Horse"),
    (8, 212, 238, "Dialogue VIII. The Dog"),
    (9, 239, 267, "Dialogue IX. The Bullock"),
    (10, 267, 309, "Dialogue X. The Elephant"),
]


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
    """Remove the catch-word: the last non-empty line preceded by a blank line.

    Catch-words were consistently placed on their own line with a blank line
    before them in the per-page transcriptions, so we can strip unconditionally.
    """
    lines = text.rstrip("\n").split("\n")
    if len(lines) < 2:
        return text

    # Find last non-empty line
    i = len(lines) - 1
    while i >= 0 and lines[i].strip() == "":
        i -= 1

    if i < 1:
        return text

    # If preceded by a blank line, it's a catch-word — strip both
    if lines[i - 1].strip() == "":
        lines = lines[:i - 1]

    return "\n".join(lines)


def split_at_dialog_boundary(text):
    """
    Split text at a dialog boundary. Returns (before, from_boundary).
    The boundary is the first '---' that precedes a 'Dialogue N.' heading.
    If no boundary found, returns (text, None).
    """
    # Find "Dialogue <roman>." in the text
    match = re.search(r"^Dialogue [IVXL]+\.", text, re.MULTILINE)
    if not match:
        return text, None

    # Walk backwards from the match to find the preceding ---
    before_match = text[:match.start()]
    # Find the last --- before the Dialogue heading
    hr_positions = [m.start() for m in re.finditer(r"^---$", before_match, re.MULTILINE)]
    if hr_positions:
        split_pos = hr_positions[-1]
        return text[:split_pos].rstrip(), text[split_pos:]
    else:
        return text[:match.start()].rstrip(), text[match.start():]


def join_pages(pages):
    """Join page texts, merging flowing text across page boundaries.

    If one page ends mid-paragraph and the next starts with a continuation
    (no blank line at end / no blank line at start), join them as one paragraph.
    If a page ends with a trailing hyphen, rejoin the word.
    """
    if not pages:
        return ""

    result = pages[0]
    for page in pages[1:]:
        if not page:
            continue

        # Check if text flows across the boundary:
        # Previous page ends mid-paragraph (no trailing blank line)
        # and next page starts mid-paragraph (no leading blank line / heading)
        prev_lines = result.rstrip("\n").split("\n")
        next_lines = page.lstrip("\n").split("\n")

        prev_last = prev_lines[-1] if prev_lines else ""
        next_first = next_lines[0] if next_lines else ""

        # Flowing text: previous ends with text (not blank, not ---) and
        # next starts with a continuation of the same paragraph (lowercase
        # or mid-sentence). A new speaker (*Name.*) or a heading always
        # starts a new paragraph.
        prev_is_text = prev_last.strip() != "" and prev_last.strip() != "---"
        next_is_continuation = (next_first.strip() != ""
                                and not next_first.startswith("---")
                                and not next_first.startswith("Dialogue ")
                                and not next_first.startswith("CIRCE")
                                and not next_first.startswith("*")
                                and not next_first.startswith("["))

        if prev_is_text and next_is_continuation:
            # Check for trailing hyphen — rejoin the word
            if prev_last.rstrip().endswith("-"):
                result = result.rstrip("\n").rstrip()
                result = result[:-1]  # Remove the hyphen
                result += page.lstrip("\n")
            else:
                # Join with a space (continuation of same paragraph)
                result = result.rstrip("\n") + " " + page.lstrip("\n")
        else:
            result = result.rstrip("\n") + "\n\n" + page.lstrip("\n")

    return result


os.makedirs(CH_DIR, exist_ok=True)

for dialog_num, start, end, title in DIALOGS:
    pages = []
    for scan in range(start, end + 1):
        raw = read_page(scan)
        if raw is None:
            continue

        text = strip_header(raw)
        text = strip_catchword(text)

        # Handle shared pages
        if scan == start:
            # Check if this page is shared with a previous dialog
            prev_dialog = [d for d in DIALOGS if d[2] == scan and d[0] != dialog_num]
            if prev_dialog:
                # This page starts our dialog — take from the boundary onward
                _, from_boundary = split_at_dialog_boundary(text)
                if from_boundary:
                    text = from_boundary

        if scan == end:
            # Check if this page is shared with the next dialog
            next_dialog = [d for d in DIALOGS if d[1] == scan and d[0] != dialog_num]
            if next_dialog:
                # This page ends our dialog — take up to the boundary
                before, _ = split_at_dialog_boundary(text)
                text = before

        pages.append(text)

    merged = join_pages([p.strip() for p in pages if p.strip()])

    outpath = os.path.join(CH_DIR, f"{dialog_num}.md")
    with open(outpath, "w", encoding="utf-8") as f:
        f.write(f"---\ntitle: \"{title}\"\n---\n\n")
        f.write(merged.strip() + "\n")

    print(f"  Dialog {dialog_num:2d}: {end - start + 1} pages -> ch/{dialog_num}.md")

print("Done.")
