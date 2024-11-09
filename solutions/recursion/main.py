"""
Main module for solving the Towers of Hanoi puzzle.

This module allows the user to either solve the Towers of Hanoi puzzle for a specific 
number of disks or run multiple test cases using data loaded from a specified file. 
The puzzle solution process is logged, and verbosity can be controlled through 
command-line arguments.

Usage:
    - Either specify the number of disks (`--n_disks`) or provide a test file (`--test_path`), 
      but not both.
    - The `--verbose` flag controls whether the steps are printed to the console.
"""

from argparse import ArgumentParser
from src.hanoi import Hanoi
from src.tools import load_data


def main(**kwargs):
    """
    Main function that either solves the Towers of Hanoi puzzle for a given number of disks
    or runs multiple test cases loaded from a file.

    Depending on the provided arguments, the function either:
        1. Solves the puzzle for a single number of disks (if `n_disks` is provided).
        2. Loads test cases from the specified file and solves the puzzle for each test case
           (if `test_path` is provided).

    Args:
        kwargs (dict): Dictionary of arguments that may include:
            - n_disks (int): The number of disks for the puzzle (if `test_path` is not provided).
            - test_path (str): Path to the file containing test cases (if `n_disks` is not provided).
            - verbose (bool): Flag to determine if the steps of the puzzle are printed to standard output.
                Defaults to `True`.
    """
    if kwargs.get("test_path"):
        # Load test cases from the provided path
        test_cases = load_data(path=kwargs.get("test_path"))

        # Solve the puzzle for each test case
        for idx, n_disks in enumerate(test_cases):
            hanoi = Hanoi(
                n_disks=n_disks,
                verbose=kwargs.get("verbose"),
            )
            hanoi()  # Solve the puzzle and log the steps

            # If there are more test cases, ask the user to press Enter to continue
            if idx < len(test_cases) - 1:
                input("Press enter to continue for next test")
    else:
        # Solve the puzzle for a single specified number of disks
        hanoi = Hanoi(
            n_disks=kwargs.get("n_disks"),
            verbose=kwargs.get("verbose"),
        )
        hanoi()  # Solve the puzzle and log the steps


if __name__ == "__main__":
    #
    # Parse command-line arguments and call the main function.

    # The script requires either `--n_disks` or `--test_path` to be provided, but not both.
    # It also optionally accepts a `--verbose` flag to control the verbosity of the output.

    # Command-line arguments:
    #     - --n_disks (int): The number of disks in the Towers of Hanoi puzzle.
    #     - --test_path (str): Path to a file containing test cases.
    #     - --verbose (bool): Boolean flag to control verbosity (default is `True`).
    #

    # Create an ArgumentParser object for handling command-line arguments
    parser = ArgumentParser(description="Solve the Towers of Hanoi puzzle.")

    # Create a mutually exclusive group to ensure only one of these arguments is provided
    group = parser.add_mutually_exclusive_group(required=True)

    # Argument for the number of disks (required if no test_path)
    group.add_argument(
        "--n_disks",
        type=int,
        help="The number of disks in the puzzle (required if no test_path).",
    )

    # Argument for the path to a file containing test cases (required if no n_disks)
    group.add_argument(
        "--test_path",
        type=str,
        help="Path to the file with test cases (required if no n_disks).",
    )

    # Verbosity flag to determine if the solution steps are printed to the output
    parser.add_argument(
        "--verbose",
        type=bool,
        required=False,
        default=True,
        help="If True, prints the steps to standard output. If False, only logs them.",
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Print parsed arguments for debugging (optional)
    print(args)

    # Call the main function with the parsed arguments
    main(
        n_disks=args.n_disks,
        verbose=args.verbose,
        test_path=args.test_path,
    )
