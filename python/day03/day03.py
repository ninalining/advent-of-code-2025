#!/usr/bin/env python3
"""
Advent of Code 2025 - Day 3 Solution in Python
"""

from pathlib import Path
input_path = Path(__file__).with_name('inputs03.txt')
with input_path.open(encoding='utf-8') as file:
    lines = file.read().splitlines()

total_sum = 0
for line in lines:
    digits = [int(char) for char in line]

    max_joltage_in_the_line = 0

    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            tens = digits[i]
            ones = digits[j]
            current_joltage = tens * 10 + ones
            if current_joltage > max_joltage_in_the_line:
                max_joltage_in_the_line = current_joltage
    total_sum += max_joltage_in_the_line

print(f"Total sum of max joltages: {total_sum}")