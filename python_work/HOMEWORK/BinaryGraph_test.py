from graphviz import Digraph
from HOMEWORK.BinaryGraph import BinaryGraph

tree = BinaryGraph()

tree.add_node_left("71", 71)
tree.add_node_right("41", 41)

tree.add_node_left("31_71_left", 31, parent_id="71")
tree.add_node_right("10_71_right", 10, parent_id="71")

tree.add_node_left("11_41_left", 11, parent_id="41")
tree.add_node_right("16_41_right", 16, parent_id="41")

tree.add_node_left("46_31_left", 46, parent_id="31_71_left")
tree.add_node_right("51_31_right", 51, parent_id="31_71_left")

tree.add_node_left("31_10_left", 31, parent_id="10_71_right")
tree.add_node_right("21_10_right", 21, parent_id="10_71_right")

tree.add_node_left("13_11_left", 13, parent_id="11_41_left")

dot = Digraph(comment='Binary Tree')

for node_id, node_value in tree.nodes.items():
    dot.node(node_id, str(node_value))

for parent_id in tree.edge_names:
    if 'left' in tree.edge_names[parent_id]:
        left_child_id = tree.edge_names[parent_id]['left']
        dot.edge(parent_id, left_child_id)
    if 'right' in tree.edge_names[parent_id]:
        right_child_id = tree.edge_names[parent_id]['right']
        dot.edge(parent_id, right_child_id)

dot.render('binary_tree', view=True)
