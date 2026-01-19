from __future__ import annotations

from functools import reduce
from itertools import takewhile
from typing import NoReturn


def compact_range(nlist: list[tuple[int, int]], nval: tuple[int, int]) -> list[tuple[int, int]]:
    if len(nlist) == 0:
        return [nval]

    if nval[1] < nlist[-1][1]:
        return nlist

    if nval[0] > nlist[-1][1]:
        return nlist + [nval]

    return nlist[:-1] + [(nlist[-1][0], nval[1])]


def main() -> NoReturn:
    with open("inputs/day5.txt") as fin:
        data = [line.strip() for line in fin.readlines()]

    fresh_ranges = sorted(map(
        lambda val: (int((vals := val.split("-"))[0]), int(vals[1])),
        takewhile(lambda val: val != "", data)
    ))

    compact_ranges: list[tuple[int, int]] = reduce(compact_range, fresh_ranges, [])

    fresh_id_count = sum(map(
        lambda r: r[1] - r[0] + 1,
        compact_ranges
    ))

    print(fresh_id_count)

    exit(0)

if __name__ == "__main__":
    main()
