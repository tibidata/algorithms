"""
Module to define additional functions.

This module contains helper functions that assist in the Towers of Hanoi problem. 
Currently, it provides a function to load test case data from a file. 
The `load_data` function reads the number of disks from a file, parses them, 
and returns them as a list of integers.
"""

from typing import List


def load_data(path: str) -> List[int]:
    """
    Load test case data from a file and return a list of integers representing
    the number of disks for each test case.

    Args:
        path (str): The path to the file containing test case data. The file
                    should have disk counts separated by commas (e.g., "3,4,5").

    Returns:
        List[int]: A list of integers where each integer represents the number
                   of disks in a test case.

    Raises:
        FileNotFoundError: If the file at the given path does not exist.
        ValueError: If the file content cannot be converted to integers.
    """

    # Open the file and read the first line
    with open(path, "r") as file:
        # Split the line by commas and convert each value to an integer
        test_cases = [int(disks) for disks in file.readline().split(",")]

        # Print the loaded test cases (this can be removed or controlled with a verbosity flag)
        print(test_cases)

        return test_cases
