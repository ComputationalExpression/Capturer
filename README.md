# Capturer

A lightweight, Python-only CLI tool that captures the elusive **Maltese Python** and detects hidden directories.

> "It's like the Ghostbusters thing, but also not."

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## About

`Capturer` is a small command-line game built for educational purposes. It ships two CLI commands:

- `capture` — validates a file by checksum and, if it matches the secret `maltese-python.png`, copies the file into a `cage` directory.
- `detect` — scans the current directory for hidden folders (names starting with `.`) and reports whether the room feels "drafty."

## Features

- No external dependencies (uses Python's standard library only).
- Two lightweight entry points: `capture` and `detect`.
- Checksum verification with MD5.
- Automatic upward search for the project root (marked by `.gatorgrade.yml`).

## Installation

Clone the repository and install the package in editable mode:

```bash
git clone https://github.com/ComputationalExpression/Capturer.git
cd Capturer
pip install -e .
```

After installation, the `capture` and `detect` commands are available in your terminal.

## Usage

### `capture`

Provide a file for `capture` to inspect. If the file's MD5 checksum matches the Maltese Python, it will be captured.

```bash
capture maltese-python.png
```

Example outputs:

```text
You've found the Maltese Python!
```

```text
Looks like that ain't it.
```

### `detect`

Run `detect` in any directory to check for hidden folders.

```bash
detect
```

Example outputs:

```text
This room seems a bit drafty...
```

```text
Nothing to see here. Might move on...
```

## Project Structure

```text
.
├── pyproject.toml          # Package metadata and entry points
├── src/
│   ├── capturer/
│   │   └── main.py         # capture command implementation
│   └── detect/
│       └── main.py         # detect command implementation
└── README.md
```

## Contributing

This is a small educational project. Feel free to open an issue or submit a pull request if you have ideas or improvements.

## License

No license has been assigned to this project yet. See the repository root for any future `LICENSE` file.

## Author

- **Douglas Luman** — [dluman@allegheny.edu](mailto:dluman@allegheny.edu)
