from collections import defaultdict, deque

with open('input.txt', 'rt') as f:
    fish = [int(i) for i in f.read().split(',')]

def run_sim(fish, num_days):
    born_on_day = defaultdict(int)
    for f in fish:
        for day in range(f + 1, num_days + 1, 7):
            born_on_day[day] += 1

    processed = {}
    while born_on_day.keys():
        day = min(born_on_day.keys())
        mul = born_on_day[day]
        for d in range(day + 9, num_days + 1, 7):
            born_on_day[d] += mul
        processed[day] = born_on_day[day]
        del born_on_day[day]
    
    return len(fish) + sum(processed.values())

print(f"Part1: {run_sim(fish, 80)}")
print(f"Part2: {run_sim(fish, 256)}")