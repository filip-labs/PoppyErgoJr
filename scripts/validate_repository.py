"""Compile application, tools and tests without importing or moving hardware."""

from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    paths = [root / "ColorSort"]
    for directory in ("poppy_sort", "scripts", "tests"):
        paths.extend(sorted((root / directory).rglob("*.py")))
    for path in paths:
        compile(path.read_text(encoding="utf-8"), str(path), "exec")
        print("Syntax OK:", path.relative_to(root))


if __name__ == "__main__":
    main()
