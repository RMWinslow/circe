"""
Resize all JP2 page scans to 760px wide and save as JPGs in pages_760w/.
"""

import os
from PIL import Image

SOURCE_DIR = os.path.join(os.path.dirname(__file__), "SINGLE PAGE PROCESSED JP2")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "pages_760w")
TARGET_WIDTH = 760

os.makedirs(OUTPUT_DIR, exist_ok=True)

files = sorted(f for f in os.listdir(SOURCE_DIR) if f.endswith(".jp2"))
print(f"Found {len(files)} JP2 files to convert.")

for i, filename in enumerate(files):
    src_path = os.path.join(SOURCE_DIR, filename)
    out_name = os.path.splitext(filename)[0] + ".jpg"
    out_path = os.path.join(OUTPUT_DIR, out_name)

    img = Image.open(src_path)
    ratio = TARGET_WIDTH / img.width
    new_height = int(img.height * ratio)
    img = img.resize((TARGET_WIDTH, new_height), Image.LANCZOS)
    img.save(out_path, "JPEG", quality=85)

    if (i + 1) % 50 == 0 or i == 0 or i == len(files) - 1:
        print(f"  [{i + 1}/{len(files)}] {out_name} ({TARGET_WIDTH}x{new_height})")

print("Done.")
