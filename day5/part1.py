#!/usr/bin/env python

import re
from collections import namedtuple

# Open and read the file
with open('day5/input.txt', 'r') as file:
    lines = file.readlines()

all_seeds = [int(x) for x in re.findall(r'\d+', lines[0])]

print(all_seeds)

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

all_locations = []
for seed in all_seeds:
    print('Looking for seed:', seed)
    translation = seed
    for map in all_maps:
        for range in map:
            print(range)
            if range.src <= translation < range.src + range.len:
                print('Found range:', range)
                translation = range.dst + translation - range.src
                print('Translated to:', translation)
                break
    all_locations.append(translation)
    #break

print(all_locations)
print("Nearest location:", min(all_locations))