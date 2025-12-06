"""
Utility functions for Advent of Code 2025 solutions.
"""

import os


def read_input(file_name, strip_newlines=True):
    """
    Return the puzzle input as a list of lines.
    """

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, file_name)

    with open(file_path, 'r', encoding='utf-8') as file:
        if strip_newlines:
            return [line.rstrip('\n') for line in file]
        return file.readlines()