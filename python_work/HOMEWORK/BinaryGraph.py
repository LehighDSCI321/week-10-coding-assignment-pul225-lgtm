from VersatileDigraph_class import VersatileDigraph

class BinaryGraph(VersatileDigraph):
    '''BinaryGraph class inherits from VersatileDigraph and implements binary tree behavior'''
    def __init__(self):
        super().__init__()
        # Initialize the root node, which is required by the test cases
        self.add_node("Root", 0)

    def add_node_left(self, child_id, child_value, parent_id="Root"):
        """Adds a left child to the specified parent node"""
        if parent_id not in self.nodes:
            raise KeyError(f'Parent node "{parent_id}" does not exist')
        if "left" in self.edge_names.get(parent_id, {}):
            raise ValueError(f'Left child already exists for node "{parent_id}"')
        self.add_edge(parent_id, child_id, self.nodes[parent_id], child_value, edge_name="left")

    def add_node_right(self, child_id, child_value, parent_id="Root"):
        """Adds a right child to the specified parent node"""
        if parent_id not in self.nodes:
            raise KeyError(f'Parent node "{parent_id}" does not exist')
        if "right" in self.edge_names.get(parent_id, {}):
            raise ValueError(f'Right child already exists for node "{parent_id}"')
        self.add_edge(parent_id, child_id, self.nodes[parent_id], child_value, edge_name="right")

    def get_node_left(self, parent_id):
        """Returns the ID of the left child node for the specified parent"""
        if parent_id not in self.nodes:
            raise KeyError(f'Node "{parent_id}" does not exist')
        if parent_id not in self.edge_names or "left" not in self.edge_names[parent_id]:
            return None
        return self.edge_names[parent_id]["left"]
    
    def get_node_right(self, parent_id):
        """Returns the ID of the right child node for the specified parent"""
        if parent_id not in self.nodes:
            raise KeyError(f'Node "{parent_id}" does not exist')
        if parent_id not in self.edge_names or "right" not in self.edge_names[parent_id]:
            return None
        return self.edge_names[parent_id]["right"]
