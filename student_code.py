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
        """Depth-first search traversal from the start node"""
        if start not in self.nodes:
            raise KeyError(f"Start node '{start}' not found in graph.")
        visited = set()
        stack = [start]
        result = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                # 添加后继节点，逆序以保持遍历顺序一致
                stack.extend(reversed(self.successors(node)))
        return result
    def bfs(self, start):
        """Breadth-first search traversal from the start node using yield"""
        if start not in self.nodes:
            raise KeyError(f"Start node '{start}' not found in graph.")
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                yield node
                queue.extend(self.successors(node))
class DAG(TraversableDigraph):
    def add_edge(self, start, end, start_node_value=None, end_node_value=None,
                 edge_name="default", edge_weight=0):
        """Add edge only if it does not create a cycle"""
        if end in self.nodes:
            for node in self.dfs(end):
                if node == start:
                    raise ValueError(f"Adding edge {start} → {end} would create a cycle.")
        super().add_edge(start, end, start_node_value, end_node_value, edge_name, edge_weight)
