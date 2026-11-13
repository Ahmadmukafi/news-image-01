import base64, os
from pathlib import Path
here = Path(__file__).resolve().parent
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_bytes(base64.b64decode((here / "entry.b64").read_text()))
