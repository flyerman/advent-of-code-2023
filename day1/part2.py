#!/usr/bin/env python

import re
from word2number import w2n

def find_all_digits(line):
    all_digits = []
    search_idx = 0
    while True:
        match = re.search(r"\d|one|two|three|four|five|six|seven|eight|nine", line[search_idx:])
        if not match:
            break;
        if match.group().isdigit():
            all_digits.append(int(match.group()))
        else:
            all_digits.append(w2n.word_to_num(match.group()))
        search_idx += match.start() + 1
    return all_digits

# Open and read the file
with open('day1/input.txt', 'r') as file:
    lines = file.readlines()

score = 0

# Display each line
for line in lines:
    print("Line:", line.strip())

    all_digits = find_all_digits(line)
    
    first_digit_int  = all_digits[0]
    second_digit_int = all_digits[-1]
 
    # Update score
    print(first_digit_int, second_digit_int)
    score += first_digit_int * 10 + second_digit_int

print("Final score", score)
