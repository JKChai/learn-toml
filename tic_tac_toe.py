from pathlib import Path
import tomllib ## Part of Python 3.11 stdlib

print(Path(__file__).parent)

# with open("tic_tac_toe.toml", mode="rb") as fp:
#     config = tomllib.load(fp)
# print(config)

# print(tomllib.loads(Path("tic_tac_toe.toml").read_text(encoding="utf-8")))

