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

    score += max_red * max_green * max_blue

print("Final score", score)