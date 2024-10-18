"""
@description: DFS algortithm implementation
@authors: Aracelli Melissa Boza Zabarburú A01662934, Adolfo Hernández Fernández A01664412, Luis Enrique Salazar Pérez A00833460
@date: 2024/17/10 
"""

# Step 1: Read and construct the graph from a text file
def read_graph(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        
        # Split the edges correctly
        edges = content.split('),(')
        edges = [edge.strip("()") for edge in edges]
        
        # Convert each edge into a tuple of integers
        edges = [tuple(map(int, edge.split(','))) for edge in edges if edge]
    
    # Create an adjacency list representation of the graph
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    
    return graph

# DFS Algorithm using a stack
def dfs(graph):
    # Step 2: DFS initialization
    root = 1
    stack = [root]  # Stack for DFS
    visited = set([root])  # Set of visited nodes
    L = []  # Ordered list of visited nodes

    iteration = 0
    while stack:
        # Display current state of the graph traversal
        print(f"Iteration {iteration}")
        print(f"Traversed Graph: {list(L)}")
        print(f"Stack: {list(stack)}")
        print("-" * 30)
        
        iteration += 1
        current = stack.pop()
        if current not in L:
            L.append(current)  # Append to DFS order
        
        # Explore the neighbors in reverse sorted order to simulate stack behavior
        for neighbor in sorted(graph[current], reverse=True):  
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    
    # Final ordered list of visited nodes
    print(f'DFS Traversal Order: {L}')
    return L

# Step 1: Build the graph
graph = read_graph("dfs.txt")

# Perform DFS
dfs(graph)
