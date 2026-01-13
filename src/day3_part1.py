from __future__ import annotations

from itertools import combinations
from typing import NoReturn


def main() -> NoReturn:
    with open("inputs/day3.txt") as fin:
        banks = [line.strip() for line in fin.readlines()]

    output = sum(max(int(val[0] + val[1]) for val in combinations(bank, 2)) for bank in banks)
    print(output)

    exit(0)


if __name__ == "__main__":
    main()
