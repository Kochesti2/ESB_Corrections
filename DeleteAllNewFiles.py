import os
import config
from pathlib import Path

cwd = os.getcwd()
for path in Path(cwd).rglob('New*.*'):
    print(path)

inp = input("Remove these files? (y/n)")
if inp == "y":
    for path in Path(cwd).rglob('New*.*'):
        os.remove(path)
    print("Removed.")
else:
    print("Exit")
