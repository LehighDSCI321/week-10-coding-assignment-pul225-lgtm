import graphviz
from graphviz import Digraph
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool
import pandas as pd

"""
Module for defining the VersatileDigraph class and its node/edge operations
"""

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
            raise ValueError(f"the '{edge_name}' edge name exists for start node '{start}'")
        if edge_name in self.edge_names[start]:
            del self.edges[start][self.edge_names[start][edge_name]]
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
    
    def out_degree(self, node):
        """Count how many edges originate from the given node"""
        return len(self.edges.get(node, {}))
    
    def plot_graph(self, filename = 'graph_output'):
        """visualize the graph using graphviz with node labels and edge weights"""
        if not self.nodes:
            raise ValueError('Graph has no nodes to display')
        try:
            import graphviz
            from graphviz import Digraph
            import pandas as pd
        except ImportError:
            raise ImportError('The plot_graph function needs graphviz library')
        dot = Digraph()
        for node, value in self.nodes.items():
            dot.node(node, f'{node}\nLivability: {value}')
        for start, targets in self.edges.items():
            for end, (weight, name) in targets.items():
                dot.edge(start, end, f"{name}\n{weight} mi")
        dot.render(filename, format = 'png', cleanup = True)

    def plot_edge_weights(self, filename = "edge_weights.html"):
        """visualize the graph using bokeh with node labels and edge weights"""
        if not self.edges:
            raise ValueError('Graph has no edges to visualize')
        try:
            from bokeh.plotting import figure, output_file, show
            from bokeh.models import ColumnDataSource, HoverTool
            import pandas as pd
        except ImportError:
            raise ImportError('The plot_edge_weights function needs bokeh libraries')
        edge_labels = []
        weights = []
        for start in self.edges:
            for end, (weight, name) in self.edges[start].items():
                edge_labels.append(f'{start}→{end} ({name})')
                weights.append(weight)
        output_file(filename)
        p = figure(x_range = edge_labels, title = "Driving distance between cities",
                   toolbar_location = None, tools = "")
        p.vbar(x = edge_labels, top = weights, width = 0.9)
        p.xaxis.major_label_orientation = 1.2
        p.yaxis.axis_label = "Distance(miles)"
        show(p)
