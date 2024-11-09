"""
Module for solving the Towers of Hanoi puzzle using recursion.

This module defines a `Hanoi` class that implements the solution to the Towers of Hanoi 
puzzle using recursion. The class allows solving the puzzle for a given number of disks, 
logging the steps of the process, and measuring the time taken for the solution. The puzzle 
can be solved either by specifying a fixed number of disks or using the default behavior.
"""

import time
from typing import List
import os


class Hanoi:
    """
    Class to represent and solve the Towers of Hanoi puzzle.

    This class implements a recursive solution to the Towers of Hanoi puzzle, where the
    objective is to move a set of disks from a source peg to a destination peg, using an
    auxiliary peg as a temporary storage. The solution process is logged, and the time
    taken to solve the puzzle is measured. The puzzle can be solved for a specific number
    of disks, and verbosity of logging can be controlled.

    Attributes:
        verbose (bool): Controls whether the steps are printed to standard output.
        disks (List[int]): A list representing the disks, ordered from largest (topmost) to smallest.
        source_name (str): Name of the source peg.
        auxiliary_name (str): Name of the auxiliary peg.
        destination_name (str): Name of the destination peg.
        pegs (dict): A dictionary storing the disks on each peg.
        log_file (file object): A file object used for logging the steps.
        log_file_name (str): The name of the log file.
        step_count (int): A counter for the number of steps taken to solve the puzzle.
    """

    def __init__(
        self,
        n_disks: int,
        verbose: bool,
        source: str = "A",
        auxiliary: str = "B",
        destination: str = "C",
    ) -> None:
        """
        Initializes the Hanoi class with the given number of disks and verbosity setting.

        Args:
            n_disks (int): The number of disks in the puzzle.
            verbose (bool): Controls whether the steps are printed to standard output.
            source (str, optional): The name of the source peg. Defaults to 'A'.
            auxiliary (str, optional): The name of the auxiliary peg. Defaults to 'B'.
            destination (str, optional): The name of the destination peg. Defaults to 'C'.
        """
        self.verbose = verbose
        # Initialize disks as a list of integers, from largest to smallest
        self.disks = list(
            range(n_disks, 0, -1)
        )  # List of disk sizes from largest to smallest
        self.source_name = source
        self.auxiliary_name = auxiliary
        self.destination_name = destination

        # Initialize pegs as lists with disks on the source peg
        self.pegs = {
            source: self.disks[:],  # Start with all disks on the source peg
            auxiliary: [],  # Auxiliary peg starts empty
            destination: [],  # Destination peg starts empty
        }

        # Log file name based on the current time and number of disks
        start_time = time.strftime("%Y%m%d_%H%M%S")
        self.log_file_name = f"hanoi_{start_time}_{n_disks}_disks.log"

        log_folder_path = "./logs/hanoi"

        # Open log file for writing
        self.log_file = open(os.path.join(log_folder_path, self.log_file_name), "w")
        self.step_count = 0  # Initialize step count

    def __call__(self) -> None:
        """
        Start solving the Towers of Hanoi puzzle and log the process.

        This method initiates the recursive solution for the Towers of Hanoi puzzle,
        logs the steps, and measures the time taken for the solution.
        """
        self.__log("Starting Towers of Hanoi with disks: " + str(self.disks))

        # Record the start time of the process
        start_time = time.perf_counter()

        # Begin the recursive process of solving the puzzle
        self.__recursive(
            self.disks, self.source_name, self.auxiliary_name, self.destination_name
        )

        # Record the end time and calculate the elapsed time
        end_time = time.perf_counter()
        time_elapsed = end_time - start_time

        # Log the total number of steps taken and the time elapsed
        self.__log(
            f"Total steps taken: {self.step_count}\nTime elapsed: {time_elapsed} seconds\nNumber of disks: {len(self.disks)}"
        )
        self.log_file.close()

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the pegs.

        Returns:
            str: A formatted string showing the state of each peg (source, auxiliary, destination).
        """
        return (
            f"{self.source_name}: {self.pegs[self.source_name]}\n"
            f"{self.auxiliary_name}: {self.pegs[self.auxiliary_name]}\n"
            f"{self.destination_name}: {self.pegs[self.destination_name]}"
        )

    def __recursive(
        self, disks: List[int], source: str, auxiliary: str, destination: str
    ) -> None:
        """
        Recursively solve the Towers of Hanoi puzzle.

        This function uses recursion to move the disks from the source peg to the destination
        peg by using the auxiliary peg as a temporary holding area. It follows the recursive
        steps of the Towers of Hanoi problem:
        1. Move n-1 disks from source to auxiliary peg.
        2. Move the largest disk to the destination peg.
        3. Move the n-1 disks from auxiliary peg to destination peg.

        Args:
            disks (List[int]): List of disks to move.
            source (str): The source peg.
            auxiliary (str): The auxiliary peg.
            destination (str): The destination peg.
        """
        if len(disks) == 1:
            # Base case: only one disk to move
            self.__base(disks[0], source, destination)  # Move the largest disk
        else:
            # Step 1: Move n-1 disks from source to auxiliary
            self.__recursive(disks[1:], source, destination, auxiliary)

            # Step 2: Move the largest disk from source to destination
            self.__base(disks[0], source, destination)

            # Step 3: Move the n-1 disks from auxiliary to destination
            self.__recursive(disks[1:], auxiliary, source, destination)

    def __base(self, disk: int, source: str, destination: str) -> None:
        """
        Handle the base case by moving a single disk and updating peg states.

        This method moves a single disk from the source peg to the destination peg, updates
        the state of the pegs, and logs the move.

        Args:
            disk (int): The disk to move.
            source (str): The source peg from which the disk is moved.
            destination (str): The destination peg to which the disk is moved.
        """
        # Move the disk from the source peg to the destination peg
        self.pegs[source].remove(disk)
        self.pegs[destination].append(disk)
        self.step_count += 1  # Increment the step count

        # Log the move
        self.__log(f"Move disk {disk} from {source} to {destination}")
        self.__log(str(self))  # Log the current state of the pegs after each move

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
