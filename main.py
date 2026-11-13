# Entry: decodes the base64 image shipped in this repo to /output/entry.png.
import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

with open(os.path.join(HERE, "entry.b64"), "r") as f:
    data = base64.b64decode(f.read())

# Validate the decoded bytes are a real image before writing anything.
PNG_MAGIC = b"\x89PNG"
JPEG_MAGIC = b"\xff\xd8\xff"
if not (data.startswith(PNG_MAGIC) or data.startswith(JPEG_MAGIC)):
    raise ValueError(
        "decoded entry.b64 is not a PNG or JPEG image "
        "(missing PNG/JPEG magic bytes)"
    )

os.makedirs(OUT_DIR, exist_ok=True)
with open(os.path.join(OUT_DIR, "entry.png"), "wb") as f:
    f.write(data)
