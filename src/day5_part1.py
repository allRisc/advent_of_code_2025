from __future__ import annotations

from collections.abc import Iterable
from functools import partial
from itertools import dropwhile, takewhile
from typing import NoReturn


def is_fresh(ingredient: str, fresh_ranges: Iterable[str]) -> bool:
    ingredient_int = int(ingredient)

    for frange in fresh_ranges:
        lbound, rbound = frange.split(sep="-")
        if ingredient_int >= int(lbound) and ingredient_int <= int(rbound):
            return True
    return False


def main() -> NoReturn:
    with open("inputs/day5.txt") as fin:
        data = [line.strip() for line in fin.readlines()]

    fresh_ranges = list(takewhile(lambda val: val != "", data))
    ingredients = dropwhile(lambda val: not val.isdigit(), data)

    print(sum(map(
        partial(is_fresh, fresh_ranges=fresh_ranges),
        ingredients
    )))

    exit(0)

if __name__ == "__main__":
    main()
