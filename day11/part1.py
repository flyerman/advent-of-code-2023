#!/usr/bin/env python

import re

# Open and read the file
with open('day11/input.txt', 'r') as file:
    lines = [x.strip() for x in file.readlines()]

#print(lines)
    
# Double empty horizontal lines
offset = 0
line_count = len(lines)
for i in range(len(lines)):
    if lines[i + offset].count('.') < len(lines[i + offset]):
        continue
    lines.insert(i + offset, lines[i + offset])
    offset += 1

# Double empty vertical lines
offset = 0
width = len(lines[0])
for i in range(width):
    dot_count = 0
    i_off = i + offset
    for j in range(len(lines)):
        if lines[j][i_off] == '.':
            dot_count += 1
    if dot_count < len(lines):
        continue
    for j in range(len(lines)):
        lines[j] = lines[j][:i_off] + '.' + lines[j][i_off:]
    offset += 1

assert width + offset == len(lines[0])

# Get all the galaxies coord
coords = []
for i in range(len(lines)):
    find_it = re.finditer(r'#', lines[i])
    for match in find_it:
        coords += [ [i, match.start()] ]

print(coords)

# Compute all distances
score = 0
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        score += abs(coords[i][0] - coords[j][0])
        score += abs(coords[i][1] - coords[j][1])

print("Final score:", score)