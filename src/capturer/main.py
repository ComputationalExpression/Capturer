""" Captures the Maltese Python when found """

import os
import sys
import hashlib
import shutil

from pathlib import Path

def copy_python(cwd: str = "", loc: str = "", obj: str = ""):
    """ Moves python to the correct location """
    path = Path(cwd).resolve()
    while True:
        if Path(f"{path}/.gatorgrade.yml").is_file():
            shutil.copy(f"{cwd}/{obj}", f"{path}/{loc}/{obj}")
            break
        if str(path) == "/":
            print("Nothing to capture here!")
            exit(1)
        path = Path(path).resolve().parent

def verify_checksum(data: bytes):
    """
        Verifies that the checksums between
        file found and correct file match
    """
    python_hash = "615bef0c2069416a6c88d28e77faf476"
    return python_hash == hashlib.md5(data).hexdigest()

def main(cwd: str = os.getcwd()):
    """ Functionality that makes the capture """
    try:
        file = sys.argv[-1]
        if len(sys.argv) == 1:
            raise ValueError
        if Path(file).is_dir():
            raise IsADirectoryError
        if not Path(file).is_file():
            raise FileNotFoundError
        with open(file, "rb") as fh:
            data = fh.read()
        if not data:
            raise ValueError
    except (IndexError, ValueError):
        print("""
            The Capturer needs an object to capture!

            usage: capture {file_name}
        """)
        sys.exit(1)
    except IsADirectoryError:
        print(f"{file} is a folder! Unfortunately, we can't capture folders!")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Looks like there's nothing like {file} around here!")
        sys.exit(1)
    if verify_checksum(data):
        copy_python(cwd, "cage", "maltese-python.png")
        print("You've found the Maltese Python!")
        sys.exit(0)
    print("Looks like that ain't it.")
    sys.exit(1)
