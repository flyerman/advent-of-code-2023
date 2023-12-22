#!/usr/bin/env python

import re
import math
from functools import reduce

def lcm(a, b):
    """Compute the Least Common Multiple of two numbers."""
    return abs(a * b) // math.gcd(a, b)

def lcm_of_array(arr):
    """Compute the LCM of an array of numbers."""
    return reduce(lcm, arr)

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

#print(nodes)

down_map = {
    'L': 0,
    'R': 1
}

currents = []
# find all starting nodes
for node in nodes:
    if node[-1] == 'A':
        currents += [node]

cycle_lens = []
# find each cycle length
for c in range(len(currents)):
    i = 0
    while True:
        if currents[c][-1] == 'Z':
            cycle_lens += [i]
            print(i, currents[c])
            break
        currents[c] = nodes[currents[c]][down_map[steps[i % len(steps)]]]
        i += 1

print("Steps count:", i)
print("Lines:", len(lines) - 2)
print("Steps:", len(steps))
print("Cycle length:", cycle_lens)
print("Answer:", lcm_of_array(cycle_lens))
