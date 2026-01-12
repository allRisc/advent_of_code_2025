from __future__ import annotations

from itertools import accumulate
from typing import NoReturn


def main() -> NoReturn:
    with open("inputs/day1.txt") as fin:
        inputs = fin.readlines()
    positions = accumulate(
        inputs,
        func=lambda acc, nval: (acc - (int(nval[1:]) * (-1 if nval[0] == "R" else 1))) % 100,
        initial=50,
    )
    num_zeros = len(list(filter(lambda x: x == 0, positions)))
    print(num_zeros)
    exit(0)


if __name__ == "__main__":
    main()
