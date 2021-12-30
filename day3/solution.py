with open('input.txt', 'rt') as f:
    lines = f.read().split('\n')

def freq_at_idx(lines, idx):
    freq = {'0': 0, '1': 0}
    for line in lines:
        freq[line[idx]] += 1
    return freq

def part1(lines):
    freq = {idx: {'0': 0, '1': 0} for idx in range(len(lines[0]))}
    for line in lines:
        for idx, chr in enumerate(line):
            freq[idx][chr] += 1
    gamma, epsilon = '', ''
    for idx in range(len(lines[0])):
        if freq[idx]['0'] > freq[idx]['1']:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    return gamma * epsilon

def part2(lines):
    oxy_cands = list(lines)
    co2_cands = list(lines)
    for idx in range(len(lines[0])):
        if len(oxy_cands) > 1:
            freqs = freq_at_idx(oxy_cands, idx)
            freq_0 = freqs['0']
            freq_1 = freqs['1']
            if freq_0 > freq_1:
                new_cands = [cand for cand in oxy_cands if cand[idx] == '0']
            elif freq_0 <= freq_1:
                new_cands = [cand for cand in oxy_cands if cand[idx] == '1']
            oxy_cands = new_cands
        
        if len(co2_cands) > 1:
            freqs = freq_at_idx(co2_cands, idx)
            freq_0 = freqs['0']
            freq_1 = freqs['1']
            if freq_0 <= freq_1:
                new_cands = [cand for cand in co2_cands if cand[idx] == '0']
            elif freq_0 > freq_1:
                new_cands = [cand for cand in co2_cands if cand[idx] == '1']
            co2_cands = new_cands

        if len(oxy_cands) == 1 and len(co2_cands) == 1:
            break

    return int(oxy_cands[0], 2) * int(co2_cands[0], 2)
            

print(f'Part1: {part1(lines)}')
print(f'Part2: {part2(lines)}')