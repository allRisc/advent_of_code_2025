from __future__ import annotations

from collections.abc import Iterable
from functools import reduce
from typing import NoReturn


def product(vals: Iterable[int]) -> int:
    return reduce(lambda x, y: x * y, vals, 1)


def main() -> NoReturn:
    with open("inputs/day6.txt") as fin:
        data = list(map(str.split, fin.readlines()))

    transposed_data = [[data[i][j] for i in range(0, len(data))] for j in range(0, len(data[0]))]

    ans_sum = sum(map(
        lambda val: product(map(int, val[0:-1])) if val[-1] == "*" else sum(map(int, val[0:-1])),
        transposed_data
    ))

    print(ans_sum)

    exit(0)


if __name__ == "__main__":
    main()
