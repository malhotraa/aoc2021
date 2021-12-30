with open('input.txt', 'rt') as f:
    nums = [int(i) for i in f.read().split('\n')]

def part1(nums):
    counter = 0
    for idx in range(1, len(nums)):
        if nums[idx] > nums[idx-1]:
            counter += 1
    return counter

def part2(nums):
    counter = 0
    for idx in range(0, len(nums) - 3):
        if nums[idx] < nums[idx + 3]:
            counter += 1
    return counter

print('Part1: ', part1(nums))
print('Part2: ', part2(nums))