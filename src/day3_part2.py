from __future__ import annotations

from typing import NoReturn


def smarter_max(bank: str) -> str:
    return _rec_smarter_max(bank[0:-11], bank[-11:])


def _rec_smarter_max(bank: str, tail: str) -> str:
    max_val = max(int(v) for v in bank)

    if len(tail) == 0:
        return str(max_val)

    new_bank = bank[bank.find(str(max_val)) + 1 :] + tail[0]

    return str(max_val) + _rec_smarter_max(new_bank, tail[1:])


def main() -> NoReturn:
    with open("inputs/day3.txt") as fin:
        banks = [line.strip() for line in fin.readlines()]

    print(sum(map(lambda bank: int(smarter_max(bank)), banks)))

    exit(0)


if __name__ == "__main__":
    main()
