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
    counter += amount // 100
    remainder = amount % 100

    if direction == 'L':
        if position - remainder < 0:
            counter += 1
        position = (position - remainder) % 100
    elif direction == 'R':
        if position + remainder >= 100:
            counter += 1
        position = (position + remainder) % 100

print(f"Password: {counter}")