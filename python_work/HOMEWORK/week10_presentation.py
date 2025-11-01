import networkx as nx
import matplotlib.pyplot as plt

tree = nx.Graph()
tree.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)])

nx.draw(tree,
        pos = nx.spring_layout(tree, seed = 42),
        with_labels = True,
        node_color = 'lightblue',
        node_size = 600)

plt.show()
