from datetime import datetime
from pathlib import Path

date = datetime.fromisoformat('2020-10-11T15:37:57+00:00')
print(date)

for f in sorted(Path('/tmp/all_versions_exported/').glob("*.txt")):
    date = f.stem.split(".")[0]
    lines = f.read_text().split("\n")[1:]
    for line in lines:
        if not line:
            continue
        curr, buyrate, sellrate = line.split()
        with open(f"{curr}.txt", "a") as write_file:
            write_file.write(f"{date} {buyrate} {sellrate}\n")