"""
This script counts the number of valid numbers between two specified bounds (inclusive), where
no two adjacent digits are the same. The bounds are provided through command-line arguments.

The main function utilizes the `Counter` class from the `src.counter` module to perform the
counting and returns the result. The script handles the parsing of command-line arguments for
the lower and upper bounds of the range.
"""

from typing import Tuple
from argparse import ArgumentParser

from src.counter import Counter
from src.tools import load_data


def main(test_path: str) -> int:
    """
    Main function to initialize the Counter and calculate the number of valid numbers
    between the specified lower and upper bounds, where no two adjacent digits are the same.

    Args:
        num_range (Tuple[int, int]): A tuple where the first element is the lower bound
                                      and the second element is the upper bound of the range.

    Returns:
        int: The total number of valid numbers between the lower and upper bounds.
    """

    # Return the result of the count by calling the Counter instance

    test_data = load_data(path=test_path)

    for idx, num_range in enumerate(test_data):

        # Create an instance of the Counter class with the provided range
        counter = Counter(num_range=num_range, verbose=True)

        # Call instance to count numbers
        counter()
        if idx != len(test_data) - 1:
            input("Press enter to continue...")


if __name__ == "__main__":

    # Initialize the argument parser for command-line arguments
    parser = ArgumentParser(description="Count valid numbers between two bounds.")

    parser.add_argument(
        "--test_path", type=str, required=True, help="Path for the test CSV file."
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Print the result of counting valid numbers between the lower and upper bounds
    main(test_path=args.test_path)
