from __future__ import annotations

import dataclasses
from itertools import product
from typing import NoReturn


@dataclasses.dataclass
class Position:
    col: int
    row: int

    def __add__(self, other: Position) -> Position:
        return Position(col=self.col + other.col, row=self.row + other.row)


def is_populated(pos: Position, floor_map: list[str]) -> bool:
    if pos.row < 0 or pos.col < 0:
        return False
    if pos.col >= len(floor_map[0]):
        return False
    if pos.row >= len(floor_map):
        return False
    return floor_map[pos.row][pos.col] == '@'


def is_accessible(pos: Position, floor_map: list[str]) -> bool:
    if floor_map[pos.row][pos.col] == ".":
        return False

    return sum(map(
        lambda offset: is_populated(pos + offset, floor_map),
        (Position(col=offset[0], row=offset[1]) for offset in product([-1, 0, 1], [-1, 0, 1]))
    )) <= 4


def main() -> NoReturn:
    with open("inputs/day4.txt") as fin:
        lines = fin.readlines()

    total_rolls = 0

    lines = [line.strip() for line in lines]

    while True:
        rolls_pulled = sum(map(
            lambda pos: is_accessible(pos, lines),
            (
                Position(col=p[0], row=p[1])
                for p in product(range(0, len(lines[0])), range(0, len(lines)))
            )
        ))
        if rolls_pulled == 0:
            break

        total_rolls += rolls_pulled

        nlines: map[map[str]] = map(
            lambda eline: map(
                lambda echar: echar[1] if not is_accessible(
                                Position(col=echar[0], row=eline[0]), lines
                              ) else '.',
                enumerate(eline[1]),
            ),
            enumerate(lines)
        )
        lines = ["".join(line) for line in nlines]



    print(total_rolls)
    exit(0)


if __name__ == "__main__":
    main()
