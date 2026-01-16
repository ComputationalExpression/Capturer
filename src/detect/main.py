from pathlib import Path

def main():
    cwd = Path.cwd()
    hidden = [
        entry for entry in cwd.iterdir()
        if entry.is_dir() and entry.name.startswith(".")
    ]
    if hidden:
        print("This room seems a bit drafty...")
        return
    print("Nothing to see here. Might move on...")
