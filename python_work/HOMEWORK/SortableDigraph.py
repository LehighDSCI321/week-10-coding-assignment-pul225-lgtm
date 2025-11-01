from VersatileDigraph_class import VersatileDigraph
from collections import deque

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
