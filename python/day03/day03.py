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
    results = []
    needed = 12
    start_index = 0
    while needed > 0:
        remaining = needed - 1
        end_index = len(digits) - remaining
        search_range = digits[start_index:end_index]
        max_digit = max(search_range)
        found_index = start_index + search_range.index(max_digit)
        results.append(max_digit)
        start_index = found_index + 1
        needed -= 1
    
    line_value = ''.join(str(digit) for digit in results)
    total_sum = total_sum + int(line_value)

    # max_joltage_in_the_line = 0
    # for i in range(len(digits)):
    #     for j in range(i + 1, len(digits)):
    #         tens = digits[i]
    #         ones = digits[j]
    #         current_joltage = tens * 10 + ones
    #         if current_joltage > max_joltage_in_the_line:
    #             max_joltage_in_the_line = current_joltage
    # total_sum += max_joltage_in_the_line

print(f"Total sum of max joltages: {total_sum}")