with open('input.txt', 'rt') as f:
    lines = f.read().split('\n')

def part1(lines):
    h, d = 0, 0
    for line in lines:
        cmd, num = line.split(' ')
        if cmd == 'forward':
            h += int(num)
        elif cmd == 'down':
            d += int(num)
        elif cmd == 'up':
            d -= int(num)
        else:
            raise ValueError(f'Invalid cmd {cmd}')
    return h * d

def part2(lines):
    h, d, aim = 0, 0, 0
    for line in lines:
        cmd, num = line.split(' ')
        if cmd == 'forward':
            h += int(num)
            d += aim * int(num)
        elif cmd == 'down':
            aim += int(num)
        elif cmd == 'up':
            aim -= int(num)
        else:
            raise ValueError(f'Invalid cmd {cmd}')
    return h * d

print(f'Part1: {part1(lines)}')
print(f'Part2: {part2(lines)}')