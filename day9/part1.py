#!/usr/bin/env python

import re

# Open and read the file
with open('day9/input.txt', 'r') as file:
    lines = file.readlines()

#print(lines)
    
measures = [[list(map(int, re.findall(r'-?\d+', l)))] for l in lines]

for i in range(len(measures)):
    while True:
        seq = measures[i][-1]
        print(seq)
        diffs = []
        for j in range(1, len(seq)):
            diffs += [seq[j] - seq[j - 1]]
        measures[i] += [diffs]
        if len(diffs) == 1:
            break
        if sum(1 for x in diffs if x == 0) == len(diffs):
            break
    #break

score = 0
print(len(measures))

#print(measures[0])
for m in measures:
    #print(m)
    next = 0
    while m:
        last = m.pop()
        print(last)
        next += last[-1]
        print("Next:", next)
    print("Score:", next)
    score += next
    #break

print("Final score:", score)