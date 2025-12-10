from contextlib import contextmanager
from pathlib import Path

@contextmanager
def temp_file():
    path = Path("temp.txt")
    f = path.open("w")
    try:
        yield f
    finally:
        f.close()
        path.unlink()

with temp_file() as f:
    f.write("Autre test\n")