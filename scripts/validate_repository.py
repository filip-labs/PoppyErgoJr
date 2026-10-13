"""Compile Python sources without importing dependencies or moving hardware."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
paths = [root / "ColorSort"] + sorted((root / "scripts").glob("*.py"))
for path in paths:
    compile(path.read_text(encoding="utf-8"), str(path), "exec")
    print("Syntax OK:", path.relative_to(root))
