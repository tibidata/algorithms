"""
Edge Class for Graph Representation in Eulerian Path Solver.

This module defines an `Edge` class that represents a directed edge 
(teleporter) between two levels in the game. Each 
edge has a starting and ending node, and a `used` flag to track whether 
the edge has been traversed in an Eulerian path.

Class:
- `Edge`: Represents a directed edge (teleporter) between two nodes (levels) in the game.

Methods:
- `__init__`: Initializes an edge with a starting node, ending node, 
and a flag to track if the edge has been used.
"""


class Edge:
    """
    Represents a directed edge (teleporter) from one level to another.

    Attributes:
    - from_node (int): The starting level of the edge (teleporter).
    - to_node (int): The ending level of the edge (teleporter).
    - used (bool): A flag that tracks if the edge has been used in the Eulerian path.
    """

    def __init__(self, from_node: int, to_node: int):
        """
        Initializes an Edge object representing a teleporter between two levels.

        Parameters:
        - from_node (int): The starting level of the edge.
        - to_node (int): The ending level of the edge.
        """
        self.from_node = from_node  # Set the starting level of the edge
        self.to_node = to_node  # Set the ending level of the edge
        self.used = False  # Initially, the edge has not been used in the path
