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
