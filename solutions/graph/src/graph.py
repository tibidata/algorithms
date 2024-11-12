"""
Graph-based Eulerian Path Solver and Visualizer.
This module defines a `Graph` class that models the levels of a 
game as nodes and teleporters between levels as directed edges.
The goal is to determine if an Eulerian path exists from level 
1 to the last level, traversing each teleporter exactly once.
"""

from typing import Any, Tuple, List

from src.node import Node
from src.edge import Edge


class Graph:
    """
    Represents the entire game graph, managing nodes,
    edges, and finding an Eulerian path if it exists.

    Attributes:
    - nodes (dict): Maps each level to its corresponding `Node` object.
    - edges (list): A list of `Edge` objects representing directed connections between levels.
    - edge_count (int): Total number of edges in the graph.
    - edges_init (list): List of initial edges provided to build the graph.
    - path (list or str): Stores the Eulerian path if found, otherwise "IMPOSSIBLE".
    """

    def __init__(self, num_levels: int, edges_init: List[Tuple[int, int]]):
        """
        Initialize the Graph with nodes and edges.

        Parameters:
        - num_levels (int): Total number of levels in the game.
        - edges_init (List[Tuple[int, int]]):
        List of tuples representing edges (teleporters) between levels.
        """
        self.nodes = {
            i: Node(i) for i in range(1, num_levels + 1)
        }  # Dictionary of nodes by level
        self.edges = []  # List of all edges
        self.edge_count = 0  # Total number of edges added
        self.edges_init = edges_init  # List of the initial edges to build the graph
        self.path = None  # Stores the Eulerian path if found

    def __call__(self) -> Any:
        """
        Executes the graph build, path finding, and
        visualization in sequence when the instance is called.

        Returns:
        - path (list or str): The Eulerian path if it exists, or "IMPOSSIBLE".
        """
        self.build()  # Build the graph from initial edges
        self.find_eulerian_path()  # Find the Eulerian path if possible
        self.visualize()  # Visualize the path and graph structure
        return self.path

    def visualize(self) -> None:
        """
        Visualizes the Eulerian path in the graph as a textual representation.

        Raises:
        - ValueError: If this method is called before finding the Eulerian path.
        """
        if self.path:
            # Display path as a sequence (e.g., "1 -> 2 -> 3")
            visualized_path = (
                "".join(f"{step} -> " for _, step in enumerate(self.path))
                if not self.path == "IMPOSSIBLE"
                else self.path
            ).strip("-> ")
            print(visualized_path)
        else:
            raise ValueError(
                "Visualize method cannot be called before finding the route."
            )

    def build(self) -> None:
        """Constructs the graph by adding edges between nodes as per the initial edge list."""
        for from_node, to_node in self.edges_init:
            self.__add_edge(from_node=from_node, to_node=to_node)

    def __add_edge(self, from_node: int, to_node: int) -> None:
        """
        Adds a directed edge from one node to another in the graph.

        Parameters:
        - from_node (int): Starting level of the edge.
        - to_node (int): Ending level of the edge.
        """
        edge = Edge(from_node, to_node)
        self.edges.append(edge)  # Append edge to edges list
        self.nodes[from_node].add_outgoing(
            edge
        )  # Add edge to the from_node's outgoing list
        self.nodes[to_node].add_incoming(
            edge
        )  # Add edge to the to_node's incoming list
        self.edge_count += 1  # Increment total edge count

    def find_eulerian_path(self) -> None:
        """
        Finds an Eulerian path in the graph if it exists, using Hierholzer's algorithm.

        If a valid Eulerian path is found, it is stored
        in `self.path`. Otherwise, `self.path` is set to "IMPOSSIBLE".
        """
        if not self.__has_eulerian_path():
            self.path = "IMPOSSIBLE"
            return

        path = []
        stack = [1]  # Start from level 1

        # Construct the path by exploring nodes and marking edges as used
        while stack:
            u = stack[-1]
            if self.nodes[u].outgoing:
                edge = self.nodes[u].outgoing.pop()  # Get next outgoing edge
                if not edge.used:
                    edge.used = True  # Mark edge as used
                    stack.append(edge.to_node)  # Move to the next node
            else:
                path.append(stack.pop())  # Backtrack and add node to the path

        path.reverse()  # Reverse the path to get the correct order

        # Set the path if it's valid; otherwise, set as impossible
        self.path = path if len(path) == self.edge_count + 1 else "IMPOSSIBLE"

    def __has_eulerian_path(self) -> bool:
        """
        Checks if an Eulerian path exists in the graph, specifically from level 1 to the last level.

        Returns:
        - bool: True if an Eulerian path exists, otherwise False.
        """
        start, end = 1, len(self.nodes)  # Define the start and end levels
        start_count = end_count = 0  # Track nodes with excess out-degree and in-degree

        # Iterate through nodes to verify Eulerian path conditions
        for node_id, node in self.nodes.items():
            if node.out_degree - node.in_degree == 1:
                if start_count or node_id != start:
                    return False  # Only one node can have out-degree excess
                start_count += 1
            elif node.in_degree - node.out_degree == 1:
                if end_count or node_id != end:
                    return False  # Only one node can have in-degree excess
                end_count += 1
            elif node.in_degree != node.out_degree:
                return False  # Other nodes must have equal in and out degrees

        return True
