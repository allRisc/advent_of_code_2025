from __future__ import annotations

from typing import Iterable, NoReturn
from collections.abc import Reversible
from itertools import accumulate


def turn_lock(starting_val: int, turn_str: str) -> int:
    if turn_str.startswith("R"):
        return starting_val + int(turn_str[1:]) % 100
    else:
        if rval := (starting_val - int(turn_str[1:]) % 100) > 0:
            return rval
        return 100 + rval


def main() -> NoReturn:
    with open("inputs/day1.txt") as fin:
        inputs = fin.readlines()
    positions = accumulate(
        inputs,
        func=lambda acc, nval: (acc + 100 - (int(nval[1:]) * (-1 if nval[0] == "R" else 1))) % 100,
        initial=50
    )
    num_zeros = len(list(filter(lambda x: x == 0, positions)))
    print(num_zeros)
    exit(0)

if __name__ == "__main__":
    main()
