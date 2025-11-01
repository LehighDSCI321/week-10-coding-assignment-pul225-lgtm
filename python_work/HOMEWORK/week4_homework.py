class VersatileDigraph:
    def __init__(self):
        self.edges = {} #format[{source: {edge_name: target, ...}, ...}]
    
    def predecessors(self, node):
        return[source for source, edges in self.edges.items()
               for target in edges.values() if target == node]
    
    def successors(self, node):
        return[target for target in self.edges.get(node, {}).values()]
    
    def successor_on_edge(self, node, edge_name):
        return[self.edges.get(node, {}).get(edge_name)]
    
    def indegree(self, node):
        return(len(source for source, edges in self.edges.items()
                   for target in edges.values() if target == node))
    
    def outdegree(self, node):
        return(len(self.edges.get(node, {})))
