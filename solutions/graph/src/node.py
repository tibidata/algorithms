"""
Node Class for Graph Representation in Eulerian Path Solver.

This module defines a `Node` class that represents a level 
in the game. Each `Node` object stores information about 
its connected edges (teleporters) and maintains degree counts
 for the incoming and outgoing edges. The class is used 
within the `Graph` class to construct the game graph, 
find the Eulerian path, and visualize the traversal of levels.

Class:
- `Node`: Represents a single level in the game, with 
outgoing and incoming edges and their corresponding degree counts.

Methods:
- `add_outgoing`: Adds an outgoing edge to the node and increments the out-degree count.
- `add_incoming`: Adds an incoming edge to the node and increments the in-degree count.
"""


class Node:
    """
    Represents a level in the game, storing edges and degree counts.

    Attributes:
    - level_id (int): The unique identifier for the level in the game.
    - outgoing (list): A list of outgoing edges from this node,
    representing teleporters leading from this level.
    - incoming (list): A list of incoming edges to this node,
    representing teleporters arriving at this level.
    - in_degree (int): The count of incoming edges (teleporters arriving at this level).
    - out_degree (int): The count of outgoing edges (teleporters departing from this level).
    """

    def __init__(self, level_id: int):
        """
        Initialize a Node object with a unique level ID and set up its edge lists and degree counts.

        Parameters:
        - level_id (int): The unique identifier for this level in the game.
        """
        self.level_id = level_id  # Store the unique level ID
        self.outgoing = []  # List of outgoing edges from this level (teleporters)
        self.incoming = []  # List of incoming edges to this level (teleporters)
        self.in_degree = 0  # Count of incoming edges
        self.out_degree = 0  # Count of outgoing edges

    def add_outgoing(self, edge) -> None:
        """
        Adds an outgoing edge to this node and updates the out-degree count.

        Parameters:
        - edge (Edge): The outgoing edge to be added,
        representing a teleporter from this level to another.
        """
        self.outgoing.append(edge)  # Add the edge to the list of outgoing edges
        self.out_degree += 1  # Increment the out-degree count

    def add_incoming(self, edge) -> None:
        """
        Adds an incoming edge to this node and updates the in-degree count.

        Parameters:
        - edge (Edge): The incoming edge to be added,
        representing a teleporter leading to this level.
        """
        self.incoming.append(edge)  # Add the edge to the list of incoming edges
        self.in_degree += 1  # Increment the in-degree count
