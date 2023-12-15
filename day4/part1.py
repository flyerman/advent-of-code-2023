#!/usr/bin/env python

import re

# Open and read the file
with open('day4/input.txt', 'r') as file:
    lines = file.readlines()

score = 0

# Display each line
for i in range(len(lines)):
    line = lines[i].strip()

    all_numbers = line.split(":")[1].split("|")
    wining_numbers = re.findall(r'\d+', all_numbers[0])
    draw_numbers   = re.findall(r'\d+', all_numbers[1])

    card_score = 0
    for i in draw_numbers:
        if i in wining_numbers:
            if card_score == 0:
                card_score = 1
            else:
                card_score *= 2
    
    print(line, "score", card_score)
    score += card_score

print("Final score", score)