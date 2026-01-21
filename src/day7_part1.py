from __future__ import annotations

from collections.abc import Generator, Iterable
from itertools import accumulate, starmap
from typing import NoReturn


def tripwise[T](iterable: Iterable[T]) -> Generator[tuple[T, T, T]]:
    iterator = iter(iterable)
    a = next(iterator)
    b = next(iterator)

    for c in iterator:
        yield (a, b, c)
        a = b
        b = c


def split_manifold(beams: list[bool], splitter: str) -> list[bool]:
    left_most = beams[0] or (beams[1] and splitter[1] == "^")
    right_most = beams[-1] or (beams[-2] and splitter[-2] == "^")
    return [left_most] + list(starmap(
        lambda b, s: (b[0] and s[0] == "^") or (b[1] and s[1] != "^") or (b[2] and s[2] == "^"),
        zip(tripwise(beams), tripwise(splitter), strict=False)
    )) + [right_most]


def main() -> NoReturn:
    with open("inputs/day7.txt") as fin:
        data = [line.lower().strip() for line in fin.readlines()]

    beam_list = accumulate(
        data[1:],
        split_manifold,
        initial=list(map(lambda val: val == "s", data[0]))
    )

    manifold_mapping = zip(beam_list, data[1:], strict=False)
    splits_per_row = map(
        lambda row: sum(map(
            lambda loc: loc[0] and loc[1] == "^",
            zip(row[0], row[1], strict=False)
        )),
        manifold_mapping
    )

    print(sum(splits_per_row))

    exit(0)


if __name__ == "__main__":
    main()
