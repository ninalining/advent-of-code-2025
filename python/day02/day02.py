#!/usr/bin/env python3

"""
Advent of Code 2025 - Day 2 Solution in Python
"""

from pathlib import Path

input_path = Path(__file__).with_name('inputs02.txt')
with input_path.open(encoding='utf-8') as file:
    line = file.read().strip()
    values = line.split(',')

ranges = []
for value in values:
    start_str, stop_str = value.split('-')
    start = int(start_str)
    stop = int(stop_str)
    ranges.append((start, stop))

def is_half_match(number: int) -> bool:
    """return True if number meets half-match criteria."""
    digits = str(abs(number))
    lens = len(digits)
    if lens % 2 != 0:
        return False
    half = lens // 2
    return digits[:half] == digits[half:]

match_numbers = []

for start, stop in ranges:
    for number in range(start, stop + 1):
        if is_half_match(number):
            match_numbers.append(number)

print(f"Sum of all matching numbers: {sum(match_numbers)}")
