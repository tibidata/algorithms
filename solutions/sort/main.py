"""
Module to execute the sliding window median algorithm on multiple test cases.

This script takes a path to a file containing multiple test cases as input and
computes the sliding window medians for each test case. The test data is loaded
from the file, and the results are printed after processing each case. The user
can proceed to the next test case by pressing "Enter" after each result.

Functions:
    - main(**kwargs): Main function that runs the sliding window median algorithm on multiple test cases.
    - Argument parser for command-line execution of the script.
"""

from argparse import ArgumentParser
from typing import List

from src.tools import sliding_window_median, load_data


def main(**kwargs) -> List[int]:
    """
    Main function that handles the processing of multiple test cases.

    Args:
        **kwargs: Arbitrary keyword arguments. Expected to include:
            - "test_path" (str): The path to the file containing test cases.

    Processes each test case from the file:
        - Loads the test cases using `load_data`.
        - For each test case, computes the sliding window median using `sliding_window_median`.
        - Prints the results and waits for user input before moving to the next test case (except for the last one).

    Returns:
        List[int]: A list of sliding window medians computed for each test case. Each result corresponds
        to the medians of one test case.
    """

    # Load test cases from the file specified in kwargs
    test_cases = load_data(path=kwargs.get("test_path"))

    # Iterate over each test case and process it
    for idx, test_case in enumerate(test_cases):
        # Unpack the test case: n, k, arr
        result = sliding_window_median(n=test_case[0], k=test_case[1], arr=test_case[2])

        # Print the result for the current test case
        print(
            f"Sliding window medians with window size: {test_case[1]} for array: {test_case[2]}\n{result}"
        )

        # Wait for user input to continue to the next test case (except for the last case)
        if idx != len(test_cases) - 1:
            input("Press enter to continue")


if __name__ == "__main__":
    # Create an argument parser to handle command-line inputs
    parser = ArgumentParser()

    # Define the argument for specifying the test file path
    parser.add_argument(
        "--test_path",
        type=str,
        required=True,
        help="Path to the CSV containing the test data",
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Execute the main function with the parsed arguments
    main(test_path=args.test_path)
