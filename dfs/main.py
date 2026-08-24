graph = {
    'S': ['B', 'D', 'A'],
    'A': ['C'],
    'B': ['D'],
    'C': ['G', 'D'],
    'D': ['G'],
    'G': []
}
def dfs(graph, start, goal):
    visited = []
    stack = [[start]]
    while stack:
       path = stack.pop()
       node = path[-1]
       if node in visited:
           continue
       visited.append(node)
       if node == goal:
           return path 
       for current_node in graph.get(node,[]):
           new_path = path + [current_node]
           stack.append(new_path)
    return None






result = dfs(graph, 'S', 'G')
print('DFS path:', result)