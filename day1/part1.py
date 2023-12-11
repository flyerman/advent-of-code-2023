#!/usr/bin/env python

import re

# Open and read the file
with open('day1/input.txt', 'r') as file:
    lines = file.readlines()

score = 0

# Display each line
for line in lines:
    print(line.strip())
    first_digit  = re.search(r"^[A-Za-z]*\d", line).group()[-1]
    second_digit = re.search(r"\d[A-Za-z]*$", line).group()[0]
    print(first_digit, second_digit)
    score += int(first_digit) * 10 + int(second_digit)

print("Final score", score)
