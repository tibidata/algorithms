"""
Module for loading game configuration data from a JSON file.

This module defines the `load_data` function, which reads a JSON file containing game
test cases and formats it into a usable structure for further processing. Each test case
describes a game with a number of levels, teleporters, and specifies the levels connected
by each teleporter.

Functions:
    - load_data: Loads and parses game test case data from a JSON file.
"""

from typing import List, Tuple, Union
import json


def load_data(path: str) -> Union[Tuple[int, int], List[Tuple[int, int]]]:
    """
    Loads game test case data from a JSON file and converts it to a structured format.

    This function reads a JSON file from the specified path and parses the test case data.
    Each test case is represented as a tuple containing:
        1. A tuple with two integers: (number of levels, number of teleporters).
        2. A list of tuples, each containing two integers (from_level, to_level),
           representing the teleporter connections between levels.

    Args:
        path (str): The file path to the JSON file containing the test case data.

    Returns:
        List[Tuple[int, int]]: A list of tuples, where each tuple represents a test case.
                               Each test case tuple contains:
                               - A tuple with (num_levels, num_teleporters).
                               - A list of (from_level, to_level) tuples for each teleporter.

    Raises:
        TypeError: If the data in the JSON file is not in the expected format.
    """

    with open(path, "r") as file:
        # Load JSON data from the provided file path
        json_data = json.load(file)

    try:
        # Parse each test case into a structured format
        data = [
            [
                # Extract number of levels and teleporters
                (test_case["num_levels"], test_case["num_teleporters"]),
                # Extract teleporter connections as (from_level, to_level) tuples
                [
                    (teleporter["from_level"], teleporter["to_level"])
                    for teleporter in test_case["teleporters"]
                ],
            ]
            for test_case in json_data["test_cases"]
        ]

    except TypeError as e:
        # Handle any TypeError exceptions that indicate invalid JSON structure
        print("Invalid input data. Ensure JSON structure matches expected format.")
        print(e)

    return data
