# https://adventofcode.com/2021/day/5

from collections import defaultdict
from typing import NamedTuple

class Point(NamedTuple):
    x: int
    y: int

class Input(NamedTuple):
    lines: list[list[Point]]

    @classmethod
    def from_file(cls, filename):
        with open(filename) as f:
            data = f.read()
        
        lines = []
        for line in data.split("\n"):
            points = line.split("->")
            row = []
            for p in points:
                p = p.split(",")
                row.append(Point(x=int(p[0]), y=int(p[1])))
            lines.append(row)
        return cls(lines=lines)

test_input = Input.from_file("test-input")
input = Input.from_file("input")

def part1(input):
    points = defaultdict(int)

    for line in input.lines:
        p1, p2 = line[0], line[1]
        
        if p1.x == p2.x:
            for i in range(min(p1.y, p2.y), max(p1.y, p2.y)+1):
                points[(p1.x, i)] += 1
        elif p1.y == p2.y:
            for i in range(min(p1.x, p2.x), max(p1.x, p2.x)+1):
                points[(i, p2.y)] += 1
    return sum(p > 1 for p in points.values())

print("[part 1] test input", part1(test_input))
print("[part 1] actual input", part1(input))

def part2(input):
    points = defaultdict(int)

    for line in input.lines:
        p1, p2 = line[0], line[1]
        
        if p1.x == p2.x:
            for i in range(min(p1.y, p2.y), max(p1.y, p2.y)+1):
                points[(p1.x, i)] += 1
        elif p1.y == p2.y:
            for i in range(min(p1.x, p2.x), max(p1.x, p2.x)+1):
                points[(i, p2.y)] += 1
        else:
           for i in range(0, abs(p1.x-p2.x)+1):
               points[(p1.x + (i if p2.x > p1.x else -i), p1.y + (i if p2.y > p1.y else -i))] += 1

    return sum(p > 1 for p in points.values())

print("[part 2] test input", part2(test_input))
print("[part 2] actual input", part2(input))