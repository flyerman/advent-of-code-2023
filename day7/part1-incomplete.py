#!/usr/bin/env python

import re

# Open and read the file
with open('day7/input.txt', 'r') as file:
    lines = file.readlines()

#print(lines)

all_hands = [ [s[0], int(s[1])] for s in map(lambda l: l.strip().split(' '), lines)]

#print(all_hands)

def parse_hand(hand):
    cards_count = {}
    for c in hand:
        cards_count[c] = cards_count.get(c, 0) + 1
    print(cards_count)

for hand in all_hands:
    parse_hand(hand[0])