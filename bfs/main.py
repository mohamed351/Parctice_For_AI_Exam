graph = {
    'S': ['B', 'D', 'A'],
    'A': ['C'],
    'B': ['D'],
    'C': ['G', 'D'],
    'D': ['G'],
    'G': []
}
def bfs(graph, start, goal):
    visited = []
    qeueue = [[start]]
    while qeueue:
       path = qeueue.pop(0)
       node = path[-1]
       if node in visited:
           continue
       visited.append(node)
       if node == goal:
           return path
       for current_node in graph.get(node,[]):
           new_path = path + [current_node]
           qeueue.append(new_path)
    return None



result = bfs(graph, 'S', 'G')
print('BFS path:', result)