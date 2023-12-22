#!/usr/bin/env python

import re

# Open and read the file
with open('day8/input.txt', 'r') as file:
    lines = file.readlines()

#print(lines)
    
steps = lines[0].strip()

nodes = {}
for i in range(2, len(lines)):
    points = re.findall("[A-Z]{3}", lines[i])
    assert len(points) == 3
    nodes[points[0]] = [points[1], points[2]]

print(nodes)

down_map = {
    'L': 0,
    'R': 1
}

i = 0
current = 'AAA'
while current != 'ZZZ':
    next_step = steps[i % len(steps)]
    assert next_step in ['L', 'R']
    i += 1
    print(next_step, current, nodes[current])
    current = nodes[current][down_map[next_step]]

print("Steps count:", i)