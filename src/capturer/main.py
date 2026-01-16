""" Captures the Maltese Python when found """

import os
import sys
import zlib
import shutil

from pathlib import Path

def copy_python(cwd: str = "", loc: str = "", obj: str = ""):
    """ Moves python to the correct location """
    path = Path(cwd).resolve()
    while True:
        if Path(f"{path}/.gatorgrade.yml").is_file():
            shutil.copy(f"{cwd}/{obj}", f"{path}/{loc}/{obj}")
            break
        path = Path(path).resolve().parent

def verify_checksum(data: bytes):
    """
        Verifies that the checksums between
        file found and correct file match
    """
    buffer_size = 65536
    python_crc = 3955143656
    print(zlib.crc32(data, buffer_size), python_crc)
    return python_crc == zlib.crc32(data, buffer_size)

def main(cwd: str = os.getcwd()):
    """ Functionality that makes the capture """
    try:
        file = sys.argv[-1]
        with open(file, "rb") as fh:
            data = fh.read()
        if not data:
            raise ValueError
    except ValueError:
        print("""
            The Capturer needs an object to capture!

            usage: capturer {file_name}
        """)
        sys.exit(1)
    except FileNotFoundError:
        print(f"Looks like there's nothing {file} that around here!")
        sys.exit(1)
    except IsADirectoryError:
        print(f"{file} is a folder!")
        sys.exit(1)
    finally:
        if verify_checksum(data):
            copy_python(cwd, "cage", "maltese-python.png")
            print("You've found the Maltese Python!")
            sys.exit(0)
        print("Looks like that ain't it.")
        sys.exit(1)
