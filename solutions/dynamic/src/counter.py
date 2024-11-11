"""
This module provides a class `Counter` that allows counting the number of valid numbers
within a specified range where no two adjacent digits are the same. The valid numbers are 
counted using dynamic programming (digit DP) techniques.

The class allows counting numbers in a given range [a, b] (both inclusive), where the numbers
do not have consecutive digits that are the same.

The class works by using a recursive function with memoization to efficiently calculate the valid
numbers without iterating through each possible number in the range.
"""

from typing import Tuple, List
import os
import time


class Counter:
    """
    A class to count the number of valid numbers in a specified range where no two adjacent
    digits are the same.

    Attributes:
        num_range (Tuple[int, int]): A tuple representing the lower and upper bounds of the range.
    """

    def __init__(self, num_range: Tuple[int, int], verbose: bool) -> None:
        """
        Initializes the Counter object with the specified range of numbers.

        Args:
            num_range (Tuple[int, int]): A tuple where the first element is the lower bound
                                         and the second element is the upper bound of the range.
        """

        self.num_range = num_range
        self.verbose = verbose

        # Log file name based on the current time and number of disks
        start_time = time.strftime("%Y%m%d_%H%M%S")
        self.log_file_name = f"counter_{start_time}_range_{self.num_range}.log"

        log_folder_path = "./logs/counter"

        # Open log file for writing
        self.log_file = open(os.path.join(log_folder_path, self.log_file_name), "w")

    def __call__(self) -> int:
        """
        Calculates the total number of valid numbers in the range [a, b] where no two adjacent
        digits are the same. This method is invoked when an instance of Counter is called.

        Returns:
            Any: The count of valid numbers between the lower and upper bounds,
                 modulo 10^9+7.
        """
        # Count valid numbers in the upper bound and subtract those in the lower bound

        result = self.count_valid_numbers(bound="upper") - self.count_valid_numbers(
            bound="lower"
        )

        self.__log(message=f"Range: {self.num_range}, valid numbers between: {result}")

        return

    def __get_digits(self, bound: str) -> Tuple[List[str], int]:
        """
        Converts the number at the bound (upper or lower) to a list of digits and returns the
        digits along with their length.

        Args:
            bound (str): The bound, either "lower" or "upper", used to determine which number
                         to process.

        Returns:
            Tuple[List[str], int]: A tuple where the first element is a list of digits of the
                                    bound number, and the second element is the length of the
                                    list of digits.
        """
        # Select the correct bound (lower bound is exclusive, so we subtract 1)
        n = max(0, self.num_range[0] - 1) if bound == "lower" else self.num_range[1]

        # Return the digits and their length
        return list(map(int, str(n))), len(list(map(int, str(n))))

    def count_valid_numbers(self, bound: str) -> int:
        """
        Counts the number of valid numbers up to the specified bound, where no two adjacent
        digits are the same.

        Args:
            bound (str): The bound for which to count valid numbers. It can be "lower" or
                         "upper".

        Returns:
            int: The count of valid numbers up to the specified bound.
        """
        digits, length = self.__get_digits(
            bound=bound
        )  # Get digits of the bound number
        memo = {}  # Dictionary to store memoized results for dynamic programming

        def recursion(pos: int, last_digit: int, tight: bool) -> int:
            """
            A recursive function to calculate the number of valid numbers with the current state
            of the digit positions.

            Args:
                pos (int): The current position in the number (starting from 0).
                last_digit (int): The last digit chosen in the previous position.
                tight (bool): A flag indicating whether the current number is tight to the bound.

            Returns:
                int: The number of valid numbers that can be formed from the current position onward.
            """
            # Base case: If we've processed all positions, return 1 (valid number)
            if pos == length:
                return 1

            # Check if the result is already computed for this state
            if (pos, last_digit, tight) in memo:
                return memo[(pos, last_digit, tight)]

            # Determine the limit for the current digit based on whether we're tight to the bound
            limit = digits[pos] if tight else 9

            result = 0
            # Try all digits from 0 to limit
            for d in range(0, limit + 1):
                # Skip if the digit is the same as the last digit (to avoid adjacent duplicates)
                if d == last_digit:
                    continue

                # If we are placing digit d, check if we are still tight (if d == limit)
                result += recursion(pos + 1, d, tight and (d == limit))

            # Memoize the result for the current state
            memo[(pos, last_digit, tight)] = result
            return result

        # Start the recursion from the first position with no last digit and tight bound
        return recursion(0, -1, True)

    def __log(self, message: str) -> None:
        """
        Log a message to the log file and optionally print it to the console.

        Args:
            message (str): The message to log.
        """
        # Write the message to the log file
        self.log_file.write(message + "\n")

        # Optionally print the message to the console based on verbosity
        if self.verbose:
            print(message + "\n")
