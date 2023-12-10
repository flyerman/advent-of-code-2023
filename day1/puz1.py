#!/usr/bin/env python

file_path = 'input.txt'  # Replace with your file path

# Open and read the file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Display each line
for line in lines:
    print(line)
