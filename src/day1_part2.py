from __future__ import annotations

from itertools import accumulate
from typing import NamedTuple, NoReturn


class DialTracker(NamedTuple):
    dial_location: int
    password_acc: int


def turn_lock(acc: DialTracker, turn_str: str) -> DialTracker:
    clicks = int(turn_str[1:])
    if turn_str[0] == "R":
        new_relative_location = acc.dial_location + clicks
    else:
        new_relative_location = acc.dial_location - clicks

    if new_relative_location > 0:
        times_past_zero = int(new_relative_location / 100)
    elif new_relative_location == 0:
        times_past_zero = 1 + int(clicks / 100)
    else:
        times_past_zero = abs(int(new_relative_location / 100)) + (acc.dial_location != 0)

    return DialTracker(
        dial_location=new_relative_location % 100, password_acc=acc.password_acc + times_past_zero
    )


def main() -> NoReturn:
    with open("inputs/day1.txt") as fin:
        inputs = fin.readlines()
    positions = list(
        accumulate(
            inputs,
            func=turn_lock,
            initial=DialTracker(50, 0),
        )
    )
    print(positions[-1].password_acc)
    exit(0)


if __name__ == "__main__":
    main()
