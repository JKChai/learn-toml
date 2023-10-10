
from pathlib import Path
import tomli

with open("tic_tac_toe.toml", mode="rb") as fp:
    config = tomli.load(fp)

tomli.loads(Path("tic_tac_toe.toml").read_text(encoding="utf-8"))

