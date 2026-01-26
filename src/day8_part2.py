from __future__ import annotations

import math
from dataclasses import dataclass
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

    idx = 0
    circuits: list[set[Point]] = []

    while len(circuits) != 1 or len(circuits[0]) != len(points):
        circuits = combine(circuits, set(vals[idx][1]))
        idx += 1

    idx -= 1

    print(vals[idx][1][0].x * vals[idx][1][1].x)
    exit(0)


if __name__ == "__main__":
    main()
