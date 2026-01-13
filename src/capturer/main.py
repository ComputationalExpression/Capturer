""" Captures the Maltese Python when found """

import os
import sys
import zlib

def main(cwd: str = "", python_crc: int = 0):
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
        buffer_size = 65536
        file_crc = zlib.crc32(data, buffer_size)
        if file_crc == python_crc:
            print("You've found the Maltese Python!")
            sys.exit(0)
        print("Looks like that ain't it.")
        sys.exit(1)

if __name__ == "__main__":
    main(cwd = os.getcwd(), python_crc = 71201740)
