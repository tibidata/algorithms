from typing import List, Tuple


def load_data(path: str) -> List[Tuple[int, int]]:
    """
    Load test case data from a file and return a list of tuples, each containing
    two integers representing the values from each row in the file.

    Args:
        path (str): The path to the file containing test case data. The file
                    should have disk counts separated by commas (e.g., "3,4,5").

    Returns:
        List[Tuple[int, int]]: A list of tuples where each tuple contains two integers
                                representing the values from a single row in the file.

    Raises:
        FileNotFoundError: If the file at the given path does not exist.
        ValueError: If the file content cannot be converted to integers.
    """

    # Use list comprehension to read and convert each line into a tuple of integers
    with open(path, "r") as file:
        test_cases = [
            (
                int(parts[0]),
                int(parts[1]),
            )  # Convert the two parts of the line to integers
            for line in file
            if (
                parts := line.strip().split(",")
            )  # Split line by comma and strip whitespace
        ]

    return test_cases
