from typing import List, TextIO


class BashScriptGenerator:
    def __init__(self, path):
        self._path = path

        self._lines = []

    def add_lines(self, lines: List[str]):
        self._lines += lines

    def add_line(self, line: str = ""):
        self._lines.append(line)

    @staticmethod
    def _write_lines(file: TextIO, lines):
        file.writelines((str(i) + "\n" for i in lines))

    def _write_header(self, file: TextIO):
        self._write_lines(file, [
            "#! /bin/bash",
            "",
            "# make sure to quit on errors in subcommands",
            "set -e",
            "",
        ])

    def build_file(self):
        with open(self._path, "w") as f:
            self._write_header(f)
            self._write_lines(f, self._lines)
