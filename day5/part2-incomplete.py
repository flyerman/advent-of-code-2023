#!/usr/bin/env python

import re
from collections import namedtuple

# Open and read the file
with open('day5/input.txt', 'r') as file:
    lines = file.readlines()

# Parse the seed ranges
all_seeds = [list(map(int, x.split(' '))) for x in re.findall(r'\d+ \d+', lines[0])]

print('All seed ranges:', all_seeds)

# Parse all the maps
all_maps = []
RangeMap = namedtuple('RangeMap', ['dst', 'src', 'len'])
for i in range(2, len(lines)):

    line = lines[i].strip()
    if line == '':
        print('=========================')
        continue

    if re.search(r' map:', line):
        print(line)
        all_maps.append([])
        continue
    
    match = re.search(r'(\d+) (\d+) (\d+)', line)
    assert match
    dst = int(match.group(1))
    src = int(match.group(2))
    len = int(match.group(3))
    range_map = RangeMap(dst, src, len)
    print(range_map)
    all_maps[-1].append(range_map)

print(all_maps)

# Find the lowest locations
lowest_loc = float('inf')

for seed_range in all_seeds:
    start = seed_range[0]
    end   = start + seed_range[1]
    print(f'Looking for seeds[{start}:{end}]')
    
    for map in all_maps:
        for r in map:
            r_end = r.src + r.len
            overlap_start = max(start, r.src)
            overlap_end   = min(end - 1, r_end - 1)

            if overlap_start <= overlap_end:
                lowest_


print("Nearest location:", lowest_loc)