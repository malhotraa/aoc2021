with open('input.txt', 'rt') as f:
    crabs = sorted([int(i) for i in f.read().split(',')])

def part1(crabs):
    min_ = None
    for pos in range(crabs[0], crabs[-1] + 1):
        sum_ = sum([abs(c - pos) for c in crabs])
        if min_ is None or sum_ < min_:
            min_ = sum_
    return min_

def part2(crabs):
    min_ = None
    for pos in range(crabs[0], crabs[-1] + 1):
        sum_ = sum([abs(c - pos)*(abs(c - pos) + 1) // 2 for c in crabs])
        if min_ is None or sum_ < min_:
            min_ = sum_
    return min_

print(f"Part1: {part1(crabs)}")
print(f"Part2: {part2(crabs)}")