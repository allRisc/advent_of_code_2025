from __future__ import annotations

from collections.abc import Generator, Iterable
from functools import reduce
from itertools import takewhile
from typing import NoReturn


def cephalopod_math_cols(data: list[str]) -> Generator[str]:
    for i in range(0, len(data[0])):
        yield "".join(data[j][i] for j in range(0, len(data))).strip()


def cephalopod_math_inputs(data: list[str]) -> Generator[list[str]]:
    cols = cephalopod_math_cols(data)
    while True:
        yield [val for val in takewhile(lambda val: val != "", cols)]


def parse_cephalopod_math(data: list[str]) -> Generator[tuple[str, list[str]]]:
    yield from zip(
        data[-1].split(),
        cephalopod_math_inputs(data[0:-1]),
        strict=False
    )


def product(vals: Iterable[int]) -> int:
    return reduce(lambda x, y: x * y, vals, 1)


def main() -> NoReturn:
    with open("inputs/day6.txt") as fin:
        data = fin.readlines()

    ans_sum = sum(map(
        lambda val: product(map(int, val[1])) if val[0] == "*" else sum(map(int, val[1])),
        parse_cephalopod_math(data)
    ))

    print(ans_sum)

    exit(0)


if __name__ == "__main__":
    main()
