"""
Module to calculate the median of each sliding window of size k in an array.

The function `sliding_window_median` computes the median of 
each sliding window of size `k` over a given list of integers. 
A `SortedList` from the `sortedcontainers` library is used 
to maintain the elements in sorted order for efficient median calculation.

Function:
    - sliding_window_median(n, k, arr): Returns a list of medians f
    or each sliding window of size `k` over the input array `arr`.

Constraints:
    - 1 ≤ k ≤ n ≤ 2 * 10^5
    - 1 ≤ x_i ≤ 10^9
"""

from sortedcontainers import SortedList
from typing import List, Tuple


def sliding_window_median(n, k, arr):
    """
    Calculate the median of each sliding window of size `k` in the array `arr`.

    Args:
        n (int): The size of the array.
        k (int): The size of the sliding window.
        arr (list of int): The list of integers representing the array.

    Returns:
        list of int: A list of medians, one for each sliding window.

    Description:
        The function maintains a sorted window of size `k` using `SortedList`
        from the `sortedcontainers` module.
        It slides this window across the array, calculates the median for
        each window, and appends it to the result list.
        The median for an odd-sized window is the middle element, while
        for an even-sized window, it is the smaller of the two middle elements.
    """

    # This will store the elements in the current window in sorted order
    window = SortedList()

    # List to store the medians of each window
    medians = []

    # First, fill the window with the first k elements from the array
    for i in range(k):
        window.add(arr[i])

    # Now, process the remaining windows
    for i in range(k, n):
        # The median for the current window is the middle element of the sorted window
        medians.append(window[k // 2])

        # Remove the element that is sliding out of the window
        window.remove(arr[i - k])

        # Add the new element that is sliding into the window
        window.add(arr[i])

    # After processing the last window, append the median for the final window
    medians.append(window[k // 2])

    # Return the list of medians
    return medians


def load_data(path: str) -> List[Tuple[int, int, List[int]]]:
    """
    Reads data from a file at the given path, where each example consists of:
    - A line containing two integers n and k (size of array and window size).
    - A subsequent line containing n integers representing the array.

    Args:
        path (str): The path to the file containing the input data.

    Returns:
        List[Tuple[int, int, List[int]]]: A list of tuples, where each tuple contains:
            - n (int): The size of the array.
            - k (int): The window size.
            - arr (List[int]): The list of integers representing the array.
    """

    examples = []

    with open(path, "r") as file:
        while True:
            # Read the first line for n and k
            line1 = file.readline()
            if not line1:  # End of file
                break
            n, k = map(int, line1.split(","))

            # Read the second line for the array elements
            line2 = file.readline()
            arr = list(map(int, line2.split(",")))

            # Append the tuple to the examples list
            examples.append((n, k, arr))

    return examples
