"""
Module for testing graph-based game solutions.

This module loads graph-based test data from a JSON file and checks for solution paths
within each test case. Each test case is represented as a graph, where the goal is to 
find a specific path or determine if one exists.

The main function coordinates loading data, creating the graph, and outputting potential
solution paths for each test case. The user is prompted to proceed through each test case
one at a time.

Functions:
    - main: Loads test data, creates a graph from each test case, and prints solution paths.
"""

from argparse import ArgumentParser
from src.graph import Graph
from src.tools import load_data


def main(**kwargs):
    """
    Executes the graph solution finder for each test case.

    This function loads test data from the specified JSON file, initializes a graph
    for each test case, and attempts to find a solution path. The results are printed
    to the console. The function pauses after each test case, prompting the user
    to press Enter before proceeding to the next one.

    Args:
        **kwargs: Arbitrary keyword arguments, expected to include:
            - path (str): The file path to the JSON file containing the test case data.

    Raises:
        FileNotFoundError: If the specified path does not lead to a valid JSON file.

    """
    # Load test case data from the specified file path
    for data in load_data(path=kwargs.get("path")):
        # Initialize a graph with levels and edges defined in the test case
        graph = Graph(num_levels=data[0][0], edges_init=data[1])

        # Execute the graph's main function to get a solution path
        print(f"Solution path: {graph()}")

        # Pause to allow the user to review each solution before continuing
        input("Press enter to continue...")


if __name__ == "__main__":
    # Argument parser setup to handle command-line input for the test path
    parser = ArgumentParser(
        description="Run solution finder on graph-based test cases."
    )

    # Add the argument for specifying the path to the JSON test data file
    parser.add_argument(
        "--test_path",
        type=str,
        required=True,
        help="The path to the JSON file containing the input data.",
    )

    # Parse the arguments from the command line
    args = parser.parse_args()

    # Call the main function with the provided test path
    main(path=args.test_path)
