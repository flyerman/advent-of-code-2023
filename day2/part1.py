#!/usr/bin/env python

import re

# Open and read the file
with open('day2/input.txt', 'r') as file:
    lines = file.readlines()

score = 0

def max_color(line, color):
    pattern = fr"\b(\d+) {color}\b"
    return max([int(x) for x in re.findall(pattern, line)])

for line in lines:
    print(line.strip())
    max_red   = max_color(line, "red")
    max_green = max_color(line, "green")
    max_blue  = max_color(line, "blue")

    if max_red <= 12 and max_green <= 13 and max_blue <= 14:
        score += int(re.search(r"Game (\d+):", line).group(1))

print("Final score", score)
