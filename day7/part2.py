#!/usr/bin/env python

import re

# Open and read the file
with open('day7/input.txt', 'r') as file:
    lines = file.readlines()

#print(lines)

all_hands = [ [s[0], int(s[1])] for s in map(lambda l: l.strip().split(' '), lines)]

#print(all_hands)

card_power_map = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 1,
    'Q': 12,
    'K': 13,
    'A': 14
}


def key_hand(hand):
    cards_count = {}
    card_power = []
    for c in hand:
        cards_count[c] = cards_count.get(c, 0) + 1
        card_power.append(card_power_map[c])

    j_count = cards_count.pop('J', None)
    
    hand_power = list(cards_count.values())
    hand_power.sort(reverse=True)
    
    if j_count:
        if hand_power:
            hand_power[0] += j_count
        else:
            hand_power += [j_count]

    return [hand_power, card_power]


all_hands.sort(key=lambda x: key_hand(x[0]))

score = 0
for i in range(len(all_hands)):
    hand = all_hands[i]
    key = key_hand(hand[0])
    print(hand, key)
    score += hand[1] * (i + 1)

print("Final score", score)