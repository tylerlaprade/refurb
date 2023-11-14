import pathlib
from pathlib import Path

# these will match

a = str(Path("file.txt"))[:4] + ".pdf"

p = Path("file.txt")
b = f"{str(p)[:4]}.pdf"

a = str(pathlib.Path("file.txt"))[:4] + ".pdf"


# these will not

x = "file.txt"[:4] + ".pdf"
