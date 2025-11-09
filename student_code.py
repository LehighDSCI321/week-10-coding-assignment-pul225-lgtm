"""
Module for defining graph classes with various functionalities.
"""
from collections import deque
class VersatileDigraph:
    """Base digraph class with nodes and edges."""
    def __init__(self):
        self.nodes = {}
        self.edges = {}
    def add_node(self, node_id, start_node_value=0):
        """Add a node to the graph if it doesn't already exist."""
        if not isinstance(node_id, str):
            raise TypeError('Node name must be a string')
        if node_id == '':
            raise ValueError('Node id can not be empty')
        if not isinstance(start_node_value, (int, float)):
            raise TypeError("Node value must be numeric")
        if node_id not in self.nodes:
            self.nodes[node_id] = start_node_value
            self.edges[node_id] = {}
    def add_edge(self, start, end, start_node_value=None, end_node_value=None,
                 _="default", edge_weight=0):
        """Add a directed edge to the graph."""
        if not isinstance(start, str) or not isinstance(end, str):
            raise TypeError('Node name must be a string')
        if start == '' or end == '':
            raise ValueError('Start and end id can not be empty')
        if edge_weight < 0:
            raise ValueError('edge_weight must be non-negative')
        self.add_node(start, start_node_value if start_node_value is not None else 0)
        self.add_node(end, end_node_value if end_node_value is not None else 0)
        self.edges[start][end] = edge_weight
    def get_nodes(self):
        """Return a list of all node IDs."""
        return list(self.nodes.keys())
    def get_node_value(self, node_id):
        """Return the value associated with a node."""
        if node_id not in self.nodes:
            raise KeyError(f'Node "{node_id}" does not exist')
        return self.nodes.get(node_id)
    def get_edge_weight(self, start, end):
        """Return the weight of the edge from start to end."""
        if start not in self.edges or end not in self.edges[start]:
            raise KeyError(f"Edge from '{start}' to '{end}' not found")
        return self.edges[start][end]
    def successors(self, node):
        """Return a list of nodes that are directly reachable from the given node."""
        if node not in self.edges:
            return []
        return list(self.edges[node].keys())
    def predecessors(self, node):
        """Return a list of nodes that have edges pointing to the given node."""
        if node not in self.nodes:
            raise KeyError(f"Node '{node}' does not exist in the graph.")
        return [source for source, targets in self.edges.items() if node in targets]
class SortableDigraph(VersatileDigraph):
    '''Return a topologically sorted list of nodes using Kahn's algorithm.'''
    def top_sort(self):
        """Return a topologically sorted list of nodes in the graph."""
        if not self.nodes:
            return []
        in_degree_map = {node: 0 for node in self.nodes}
        for _, ends in self.edges.items():
            for end in ends:
                in_degree_map[end] += 1
        queue = deque([node for node, degree in in_degree_map.items() if degree == 0])
        sorted_list = []
        while queue:
            current = queue.popleft()
            sorted_list.append(current)
            for successor in self.successors(current):
                in_degree_map[successor] -= 1
                if in_degree_map[successor] == 0:
                    queue.append(successor)
        if len(sorted_list) != len(self.nodes):
            raise ValueError("graph contains a cycle")
        return sorted_list
class TraversableDigraph(SortableDigraph):
    '''Apply DFS and BFS.'''
    def dfs(self, start):
        """Depth-first search traversal from the start node"""
        if start not in self.nodes:
            raise KeyError(f"Start node '{start}' not found in graph.")
        visited = set([start])
        stack = list(reversed(self.successors(start)))
        result = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                stack.extend(reversed(self.successors(node)))
        return result
    def bfs(self, start):
        """Breadth-first search traversal from the start node"""
        if start not in self.nodes:
            raise KeyError(f"Start node '{start}' not found in graph.")
        visited = set([start])
        queue = deque(self.successors(start))
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                yield node
                queue.extend(self.successors(node))
class DAG(TraversableDigraph):
    '''A DAG that prevents cycle creation.'''
    def add_edge(self, start, end, start_node_value=None, end_node_value=None,
                 edge_name="default", edge_weight=0):
        """Add edge only if it does not create a cycle"""
        edge_existed = end in self.edges.get(start, {})
        old_weight = self.edges[start][end] if edge_existed else None
        super().add_edge(start, end, 
                         start_node_value=start_node_value,
                         end_node_value=end_node_value,
                         _=edge_name,
                         edge_weight=edge_weight)
        try:
            self.top_sort()
        except ValueError as e:
            if edge_existed and old_weight is not None:
                self.edges[start][end] = old_weight
            else:
                if start in self.edges and end in self.edges[start]:
                    del self.edges[start][end]
            raise ValueError(f"Adding edge {start} → {end} would create a cycle.") from e
