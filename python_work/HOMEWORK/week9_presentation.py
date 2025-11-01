def topological_sort(graph):
    # record the node already visit
    visited = set()
    # store the node that has been dealt with
    stack = []

    # recursively visit all unvisited adjacent nodes
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        # after all adjacent nodes are processed
        # they are pushed into the stack
        stack.append(node)
    
    # traverse all nodes
    for node in graph:
        if node not in visited:
            dfs(node)
    
    # reverse the stack to get the sequence
    return stack[::-1]

graph = {
    "A": ["D", "E"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

print("result:", topological_sort(graph))
