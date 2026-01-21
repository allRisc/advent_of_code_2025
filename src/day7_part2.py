from __future__ import annotations

from functools import cache
from typing import NoReturn


@cache
def quantum_paths(beam_idx: int, row_idx: int, data: tuple[str, ...]) -> int:
    if row_idx >= len(data):
        return 1

    if data[row_idx][beam_idx] == "^":
        left_path = quantum_paths(beam_idx-1, row_idx+1, data)
        right_path = quantum_paths(beam_idx+1, row_idx+1, data)
        return left_path + right_path

    return quantum_paths(beam_idx, row_idx+1, data)


def main() -> NoReturn:
    with open("inputs/day7.txt") as fin:
        data = [line.lower().strip() for line in fin.readlines()]

    print(quantum_paths(data[0].find("s"), 0, tuple(data[1:])))

    exit(0)


if __name__ == "__main__":
    main()
