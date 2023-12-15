#!/usr/bin/env python

import re

# Open and read the file
with open('day3/input.txt', 'r') as file:
    lines = file.readlines()

score = 0

def find_adjacent_numbers(line, pos):
    results = []
    it = re.finditer(r'\d+', line)
    for match in it:
        
        number = int(match.group())
        pos_start = match.start()
        pos_end   = match.end()
        
        #print(number, "is at pos ", pos_start, ":", pos_end)

        if pos - 1 <= pos_start <= pos + 1:
            results.append(number)
        elif pos_start < pos - 1 and pos_end >= pos:
            results.append(number)

    return results        

# Display each line
for i in range(len(lines)):
    
    prev_line = lines[i - 1].strip() if i > 0 else None
    next_line = lines[i + 1].strip() if i + 1 < len(lines) else None

    line = lines[i].strip()
    print(line)
    
    it = re.finditer(r'\*', line)
    for match in it:
        
        pos_start = match.start()
        
        #print("found star at", pos_start)

        part_numbers = []
        part_numbers += find_adjacent_numbers(line, pos_start)
        if prev_line:
            part_numbers += find_adjacent_numbers(prev_line, pos_start)
        if next_line:
            part_numbers += find_adjacent_numbers(next_line, pos_start)            
        
        if len(part_numbers) == 2:
            score += part_numbers[0] * part_numbers[1]

print("Final score", score)
