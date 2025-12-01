#!/usr/bin/env python3

"""
Advent of Code 2025 - Day 1 Solution in Python
"""

import utils

lines = utils.read_input('day01.txt')

position = 50
counter = 0

for line in lines:
    direction = line[0]
    amount = int(line[1:])
    if direction == 'L':
        position = (position - amount) % 100
    elif direction == 'R':
        position = (position + amount) % 100
    if position == 0:
        counter += 1

print(f"Password: {counter}")