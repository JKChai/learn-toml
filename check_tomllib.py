import subprocess

try:
    import tomllib
except ModuleNotFoundError:
    try:
        import tomli
    except ModuleNotFoundError:
        subprocess.run(["python", "-m", "pip", "install", "tomli"], check=True)
        import tomli

