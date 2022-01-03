with open('input.txt', 'rt') as f:
    txt = f.read().split('\n')

    lines = []
    for t in txt:
        strt, end = t.split(' -> ')
        strt = [int(i) for i in strt.split(',')]
        end = [int(i) for i in end.split(',')]
        lines.append([strt, end])
    

def part1(lines):
    max_x = max([pt[0] for line in lines for pt in line])
    max_y = max([pt[1] for line in lines for pt in line])
    
    world = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for line in lines:
        strt = line[0]
        end = line[1]
        if strt[0] == end[0]: # vertical line
            x = strt[0]
            min_ = min(strt[1], end[1])
            max_ = max(strt[1], end[1])
            for y in range(min_, max_ + 1):
                world[y][x] += 1
        elif strt[1] == end[1]: # horizontal line
            y = strt[1]
            min_ = min(strt[0], end[0])
            max_ = max(strt[0], end[0])
            for x in range(min_, max_ + 1):
                world[y][x] += 1
        else: # non horizontal or vertical lines
            continue
    
    count = 0
    for r in range(len(world)):
        for c in range(len(world[0])):
            if world[r][c] >= 2:
                count += 1
    return count

def part2(lines):
    max_x = max([pt[0] for line in lines for pt in line])
    max_y = max([pt[1] for line in lines for pt in line])
    
    world = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for line in lines:
        strt = line[0]
        end = line[1]
        if strt[0] == end[0]: # vertical line
            x = strt[0]
            min_ = min(strt[1], end[1])
            max_ = max(strt[1], end[1])
            for y in range(min_, max_ + 1):
                world[y][x] += 1
        elif strt[1] == end[1]: # horizontal line
            y = strt[1]
            min_ = min(strt[0], end[0])
            max_ = max(strt[0], end[0])
            for x in range(min_, max_ + 1):
                world[y][x] += 1
        elif abs(end[1] - strt[1]) == abs(end[0] - strt[0]): # diagonal lines
            sgn_y = 1 if end[1] - strt[1] > 0 else -1
            sgn_x = 1 if end[0] - strt[0] > 0 else -1
            curr = strt
            while curr != end:
                world[curr[1]][curr[0]] += 1
                curr[1] += sgn_y
                curr[0] += sgn_x
            world[curr[1]][curr[0]] += 1
        else:
            continue
    
    count = 0
    for r in range(len(world)):
        for c in range(len(world[0])):
            if world[r][c] >= 2:
                count += 1
    return count

print(f"Part1: {part1(lines)}")
print(f"Part2: {part2(lines)}")