"""
Module for defining the VersatileDigraph class and its node/edge operations
"""
from collections import deque
class VersatileDigraph():
    '''This class add some methods'''
    def __init__(self):
        self.nodes = {}
        self.edges = {}
        self.edge_names = {}
    def add_node(self, node_id, start_node_value = 0):
        """Add a node to the graph if it doesn't already exist"""
        if not isinstance(node_id, str):
            raise TypeError('Node name must be a string')
        if node_id == '':
            raise ValueError('Node id can not be empty')
        if not isinstance(start_node_value, (int, float)):
            raise TypeError("Node value must be numeric")
        if node_id not in self.nodes:
            self.nodes[node_id] = start_node_value
    def add_edge(self, start, end, start_node_value = None, end_node_value = None,
                 edge_name = "default", edge_weight = 0):
        """add an edge to the graph"""
        if not isinstance(start, str) or not isinstance(end, str):
            raise TypeError('Node name must be ')
        if start == '' or end == '':
            raise ValueError('Start and end id can not be empty')
        if edge_weight < 0:
            raise ValueError('edge_weight must be non-negative')
        self.add_node(start, start_node_value if start_node_value is not None else 0)
        self.add_node(end, end_node_value if end_node_value is not None else 0)
        if start not in self.edges:
            self.edges[start] = {}
            self.edge_names[start] = {}
        if edge_name in self.edge_names[start]:
            old_end = self.edge_names[start][edge_name]
            del self.edges[start][old_end]
        self.edges[start][end] = (edge_weight, edge_name)
        self.edge_names[start][edge_name] = end
    def get_nodes(self):
        """Return a list of all node IDs"""
        return list(self.nodes.keys())
    def get_node_value(self, node_id):
        """Return the value associated with a node"""
        if node_id not in self.nodes:
            raise KeyError(f'Node "{node_id}" does not exist')
        return self.nodes.get(node_id)
    def get_edge_weight(self, start, end):
        """Return the weight of the edge from start to end"""
        if start not in self.edges or end not in self.edges[start]:
            raise KeyError(f"Edge from '{start}' to '{end}' not found")
        return self.edges.get(start, {}).get(end, (None, ))[0]
    def print_graph(self):
        "Return the weight of the edge from start to end"
        for node, val in self.nodes.items():
            print(f"Node {node} with value {val}")
        for start, ends in self.edges.items():
            for end, (weight, name) in ends.items():
                print(f"Edge from {start} to {end} with weight {weight} and name {name}")
    def predecessors(self, node):
        """Return a list of nodes that have edges pointing to the given node"""
        if node not in self.nodes:
            raise KeyError(f"Node '{node}' does not exist in the graph.")
        return [source for source, targets in self.edges.items() if node in targets]
    def successors(self, node):
        """Return a list of nodes that are directly reachable from the given node"""
        return list(self.edges.get(node, {}).keys())
    def successor_on_edge(self, node, edge_name):
        """Return the target node connected via a specific edge name from the given node"""
        if node not in self.edge_names:
            raise KeyError(f'Node "{node}" has no out outgoing edges')
        if edge_name not in self.edge_names[node]:
            raise KeyError(f"Edge name '{edge_name}' not found for node '{node}'.")
        return self.edge_names.get(node, {}).get(edge_name)
    def in_degree(self, node):
        """Count how many edges point to the given node"""
        return sum(1 for source, targets in self.edges.items() if node in targets)
class SortableDigraph(VersatileDigraph):
    '''return a topologically sorted list of nodes using Kahn's algorithm'''
    def top_sort(self):
        """return a topologically sorted list list of nodes in the graph"""
        if not self.nodes:
            return []
        in_degree_map = {node: 0 for node in self.nodes}
        for _, ends in self.edges.items():
            for end in ends:
                in_degree_map[end] += 1
        queue = deque([node for node in in_degree_map if in_degree_map[node] == 0])
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
    def dfs(self, start):
        """yield nodes in depth first traversal order (excluding start node)"""
        visited = set([start])
        stack = list(reversed(self.successors(start)))
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                yield node
                stack.extend(reversed(self.successors(node)))
    def bfs(self, start):
        """yield nodes in breadth first traversal order (excluding start node)"""
        visited = set([start])
        queue = deque(self.successors(start))
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                yield node
                queue.extend(self.successors(node))
class DAG(TraversableDigraph):
    def add_edge(self, start, end, edge_weight=1, edge_name=None):
        """Add edge only if it doesn't create a cycle"""
        if start in self.dfs(end):
            raise ValueError(f"adding edge {start}->{end} will create a cycle")
        super().add_edge(
            start, end,
            start_node_value=None,
            end_node_value=None,
            edge_name=edge_name if edge_name else "default",
            edge_weight=edge_weight
        )
        
