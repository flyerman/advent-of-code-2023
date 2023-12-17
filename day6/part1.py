#!/usr/bin/env python

import re

# Open and read the file
with open('day6/input.txt', 'r') as file:
    lines = file.readlines()

print(lines)

all_times     = re.findall(r'\d+', lines[0])
all_distances = re.findall(r'\d+', lines[1])

time     = int(''.join(all_times))
distance = int(''.join(all_distances))

print(all_times, all_distances)
print(time, distance)

final_score = 1

match = 0;
for t in range(1, time):
    if (time - t) * t > distance:
        match += 1
    if t % 1024*1024 == 0:
        print(t)

if match > 0:
    final_score *= match

print("Final score:", final_score)

