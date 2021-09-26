from pathlib import Path

path = Path("new")
if not path.exists():
    path.mkdir()

print(path.stat())

for f in path.glob("../*"):
    print(f)

if path.exists():
    path.rmdir()
