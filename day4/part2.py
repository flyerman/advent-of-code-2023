#!/usr/bin/env python

import re

# Open and read the file
with open('day4/input.txt', 'r') as file:
    lines = file.readlines()

cards_copies = [1] * len(lines)

# Display each line
for i in range(len(lines)):

    line = lines[i].strip()

    all_numbers = line.split(":")[1].split("|")
    wining_numbers = [int(x) for x in re.findall(r'\d+', all_numbers[0])]
    draw_numbers   = [int(x) for x in re.findall(r'\d+', all_numbers[1])]

    card_score = 0
    for draw in draw_numbers:
        if draw in wining_numbers:
            card_score += 1
    
    print(line, "score", card_score)
    #cards_scores.append(card_score)

    for j in range(1, card_score + 1):
        cards_copies[i + j] += cards_copies[i]

print("Final score", sum(cards_copies))