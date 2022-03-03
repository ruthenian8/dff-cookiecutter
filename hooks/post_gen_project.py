#!/bin/python3

from pathlib import Path

path: Path
for path in Path(".").glob(""):
    data = path.read_bytes()
    linuxized_data = data.replace(b"\r\n", b"\n")
    path.write_bytes(linuxized_data)
