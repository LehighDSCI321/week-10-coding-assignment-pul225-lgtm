#part_1_graph returns a graph using a list of sets
def part1_graph():
    graph_dict = {
        "a" : {"b", "e"},
        "b" : {"c"},
        "c" : {"d", "e"},
        "d" : {"b"},
        "e" : {}
    }
    return[graph_dict["a"], graph_dict["b"], graph_dict["c"], graph_dict["d"], graph_dict["e"]]
graph = part1_graph()
print(graph)

#part_2_graph graph  using a list of lists
def part2_graph():
    graph = [
        ["a", "b", "e"],
        ["c"],
        ["e", "d"],
        [],
        ["d"]
    ]
    return graph
graph = part2_graph()
print(graph)

# part_3_graph returns digraph using a list of dicts
def part3_graph():
    graph = [
        {"a": 8, "b": 1, "e": 4},
        {"c": 3},
        {"a": 2, "e": 4},
        {}
    ]
    return graph
graph = part3_graph()
print(graph)

#part_4_graph returns following digraphas a dict of sets
def prat4_graph():
    graph = {
        "a": {"a", "b", "e"},
        "b": {"c"},
        "c": {"a"},
        "e": {}
    }
    return graph
graph = prat4_graph()
print(graph)

#part_5_graph  returns the following digraph as a dict of dicts
def part5_graph():
    graph = {
        "a": {"b": 5},
        "b": {"e": 3},
        "e": {"a": 6, "b": 2}
    }
    return graph
graph = part5_graph()
print(graph)
