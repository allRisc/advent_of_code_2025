from __future__ import annotations

from collections.abc import Generator, Iterable
from itertools import batched
from typing import NoReturn


def ids(ranges: Iterable[str]) -> Generator[int]:
    for rng in ranges:
        low_str, high_str = rng.split("-")
        yield from range(int(low_str), int(high_str) + 1)


def id_checker(val: int) -> bool:
    sval = str(val)

    for i in range(1, len(sval)):
        if len(set(batched(sval, i, strict=False))) == 1:
            return True
    return False


def main() -> NoReturn:
    with open("inputs/day2.txt") as fin:
        ranges = fin.read().strip().split(sep=",")

    print(sum(filter(id_checker, ids(ranges))))
    exit(0)


if __name__ == "__main__":
    main()
