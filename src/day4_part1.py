from __future__ import annotations

from itertools import product
from typing import NoReturn


def is_populated(pos: tuple[int, int], floor_map: list[str]) -> bool:
    if pos[0] < 0 or pos[1] < 0:
        return False
    if pos[0] >= len(floor_map[0]):
        return False
    if pos[1] >= len(floor_map):
        return False
    return floor_map[pos[1]][pos[0]] == '@'


def is_accessible(pos: tuple[int, int], floor_map: list[str]) -> bool:
    if floor_map[pos[1]][pos[0]] == ".":
        return False

    return sum(map(
        lambda p: is_populated((pos[0] + p[0], pos[1] + p[1]), floor_map),
        product([-1, 0, 1], [-1, 0, 1])
    )) <= 4


def main() -> NoReturn:
    with open("inputs/day4.txt") as fin:
        lines = fin.readlines()

    print(sum(map(
        lambda pos: is_accessible(pos, lines),
        product(range(0, len(lines[0]) - 1), range(0, len(lines)))
    )))
    exit(0)


if __name__ == "__main__":
    main()
