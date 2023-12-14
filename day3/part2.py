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
    
    it = re.finditer(r'\*', line)
    for match in it:
        
        pos_start = match.start()
        
        print("found star at", pos_start)
        

print("Final score", score)
