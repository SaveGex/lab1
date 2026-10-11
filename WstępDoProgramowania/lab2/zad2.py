lazy import os
from pathlib import Path

TASK_DIR = Path(__file__).resolve().parent

for wiersz in TASK_DIR.rglob("*.wiersz"):
    with wiersz.open() as f:
        print(f.read())