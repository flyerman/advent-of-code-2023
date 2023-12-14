#!/usr/bin/env python

import re

# Open and read the file
with open('day3/input.txt', 'r') as file:
    lines = file.readlines()

score = 0

def symbol_found(line, start, end):
    if start > 0:
        start -= 1
    if end + 1 < len(line):
        end += 1
    return re.search(r'[^.\d]', line[start:end]) is not None

# Display each line
for i in range(len(lines)):
    
    prev_line = lines[i - 1].strip() if i > 0 else None
    next_line = lines[i + 1].strip() if i + 1 < len(lines) else None

    line = lines[i].strip()
    print(line)
    
    it = re.finditer(r'\d+', line)
    for match in it:
        
        number = int(match.group())
        pos_start = match.start()
        pos_end   = match.end()
        
        print(number, "is at pos", pos_start)
        
        if pos_start > 0 and line[pos_start - 1] != '.':
            score += number
            continue
        
        if pos_end < len(line) and line[pos_end] != '.':
            score += number
            continue

        if prev_line and symbol_found(prev_line, pos_start, pos_end):
            score += number
            continue

        if next_line and symbol_found(next_line, pos_start, pos_end):
            score += number
            continue

print("Final score", score)
