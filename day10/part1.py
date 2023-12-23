#!/usr/bin/env python

import re

# Open and read the file
with open('day10/input.txt', 'r') as file:
    lines = file.readlines()

#print(lines)

for x in range(len(lines)):
    match_s = re.search(r'S', lines[x])
    if match_s:
        y = match_s.start()
        break

print(lines[x])

pipe = ['S']
y += 1
vector_y = 1
vector_x = 0

while True:
    
    next = lines[x][y]
    print(x, y, next)
    if next == 'S':
        break
    
    pipe += next
    current_vector_y = vector_y
    match next:
        case '7':
            vector_y = 0 if current_vector_y else -1
            vector_x = 1 if current_vector_y else 0
        case 'J':
            vector_x = -1 if current_vector_y else 0
            vector_y = 0 if current_vector_y else -1
        case 'L':
            vector_x = -1 if current_vector_y else 0
            vector_y = 0 if current_vector_y else 1
        case 'F':
            vector_x = 1 if current_vector_y else 0
            vector_y = 0 if current_vector_y else 1
        case _:
            assert next in ['-', '|']
    
    x += vector_x
    y += vector_y

    print(vector_x, vector_y)

    #if len(pipe) > 10: break

print(pipe)
print("Final score:", len(pipe) / 2)
