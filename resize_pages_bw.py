"""
Convert JP2 page scans to small black-and-white JPGs in pages_760h_bw/.

Steps per image:
1. Open the JP2
2. Convert to greyscale and apply a threshold to get pure black and white
3. Crop blank space around the content
4. Resize to 760px tall (preserving aspect ratio)
5. Save as JPG
"""

import os
from PIL import Image

SOURCE_DIR = os.path.join(os.path.dirname(__file__), "SINGLE PAGE PROCESSED JP2")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "pages_760h_bw")
TARGET_HEIGHT = 760
THRESHOLD = 180  # pixels brighter than this become white, darker become black

os.makedirs(OUTPUT_DIR, exist_ok=True)

files = sorted(f for f in os.listdir(SOURCE_DIR) if f.endswith(".jp2"))
print(f"Found {len(files)} JP2 files to convert.")

for i, filename in enumerate(files):
    src_path = os.path.join(SOURCE_DIR, filename)
    out_name = os.path.splitext(filename)[0] + ".jpg"
    out_path = os.path.join(OUTPUT_DIR, out_name)

    img = Image.open(src_path).convert("L")

    # Apply threshold to get pure black and white
    img = img.point(lambda p: 255 if p > THRESHOLD else 0, mode="L")

    # Crop blank space (invert for getbbox since it finds non-zero pixels)
    from PIL import ImageOps
    inverted = ImageOps.invert(img)
    bbox = inverted.getbbox()
    if bbox:
        img = img.crop(bbox)

    # Resize to target height
    ratio = TARGET_HEIGHT / img.height
    new_width = int(img.width * ratio)
    img = img.resize((new_width, TARGET_HEIGHT), Image.LANCZOS)

    img.save(out_path, "JPEG", quality=85)

    if (i + 1) % 50 == 0 or i == 0 or i == len(files) - 1:
        print(f"  [{i + 1}/{len(files)}] {out_name} ({new_width}x{TARGET_HEIGHT})")

print("Done.")
