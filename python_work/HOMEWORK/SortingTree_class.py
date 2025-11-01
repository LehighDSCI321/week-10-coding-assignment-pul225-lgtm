from BinaryGraph import BinaryGraph

class SortingTree(BinaryGraph):

    '''SortingTree class inherits from BinaryGraph and implements the sorting tree behavior'''
    def __init__(self, root_value = None):
        super().__init__()
        if root_value is not None:
            self.nodes['Root'] = root_value

    def insert(self, value, current_id = 'Root'):
        """Insert a value into the tree following the sorting rules"""
        current_value = self.nodes[current_id]
        if value < current_value:
            left_id = self.get_node_left(current_id)
            if left_id is None:
                self.add_node_left(f'{current_id}_L', value, current_id)
            else:
                self.insert(value, left_id)
        else:
            right_id = self.get_node_right(current_id)
            if right_id is None:
                self.add_node_right(f'{current_id}_R', value, current_id)
            else:
                self.insert(value, right_id)
                
    def traverse(self, current_id = 'Root'):
        """print and return inorder traversal of the tree as a list"""
        result = []
        def inorder(node_id):
            if node_id is None:
                return
            inorder(self.get_node_left(node_id))
            result.append(self.nodes[node_id])
            inorder(self.get_node_right(node_id))
        inorder(current_id)
        output = ' '.join(str(item) for item in result)
        print(output, end = ' ')
        return result
    