from __future__ import annotations

import math
from dataclasses import dataclass
from functools import reduce
from itertools import combinations
from typing import NoReturn, Self


@dataclass(frozen=True)
class Point:
    x: int
    y: int
    z: int

    def distance(self, other: Point) -> float:
        return math.sqrt(
            pow(self.x - other.x, 2) + pow(self.y - other.y, 2) + pow(self.z - other.z, 2)
        )

    @classmethod
    def from_line(cls, line: str) -> Self:
        coords = line.split(",")
        return cls(int(coords[0]), int(coords[1]), int(coords[2]))


def combine(circuits: list[set[Point]], points: set[Point]) -> list[set[Point]]:
    join_circuits = list(filter(lambda s: len(s & points) > 0, circuits))
    no_join_circuits = list(filter(lambda s: len(s & points) == 0, circuits))

    if len(join_circuits) == 0:
        return no_join_circuits + [points]

    if len(join_circuits) == 1:
        return no_join_circuits + [join_circuits[0] | points]

    return no_join_circuits + [join_circuits[0] | join_circuits[1] | points]


def main() -> NoReturn:
    with open("inputs/day8.txt") as fin:
        points = [Point.from_line(line.strip()) for line in fin.readlines()]

    vals = sorted(map(lambda pts: (pts[0].distance(pts[1]), pts), combinations(points, 2)))

    circuits: list[set[Point]] = reduce(
        combine,
        (set(val[1]) for val in vals[0:1000]),
        []
    )

    sorted_circuits = sorted(circuits, key=len)

    print(len(sorted_circuits[-1]) * len(sorted_circuits[-2]) * len(sorted_circuits[-3]))

    exit(0)


if __name__ == "__main__":
    main()
