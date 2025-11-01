from HOMEWORK.VersatileDigraph_class import VersatileDigraph
# build a digraph class
graph = VersatileDigraph()

# add the node
graph.add_node("Allentown", 66)
graph.add_node("Easton", 74)
graph.add_node("Freemansburg", 12)
graph.add_node("Bethlehem", 70)

# add the edge
graph.add_edge("Allentown", "Easton", edge_name="US22E", edge_weight=17)
graph.add_edge("Allentown", "Bethlehem", edge_name="Hanover", edge_weight=6)
graph.add_edge("Easton", "Allentown", edge_name="US22W", edge_weight=17)
graph.add_edge("Easton", "Bethlehem", edge_name="Freemansburg", edge_weight=12)
graph.add_edge("Bethlehem", "Allentown", edge_name="Hanover", edge_weight=6)
graph.add_edge("Bethlehem", "Easton", edge_name="US22E", edge_weight=12)

# print the information of the graph
graph.print_graph()

# use the graphviz to plot the directed graph
graph.plot_graph(filename="graph_output")

# use the bokeh to plot the weighting bar chart
graph.plot_edge_weights(filename="edge_weights.html")
