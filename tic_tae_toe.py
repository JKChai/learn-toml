from pathlib import Path
import tomllib ## Part of Python 3.11 stdlib

with open("tic_tac_toe.toml", mode="rb") as fp:
    config = tomllib.load(fp)

print(Path("."))
# tomllib.loads(Path("tic_tac_toe.toml").read_text(encoding="utf-8"))

