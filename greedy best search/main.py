H_table = {'S':7,'A':6,'D':5,'B':4,'C':2,'G':0}
graph = {
    'S': ['B', 'D', 'A'],
    'A': ['C'],
    'B': ['D'],
    'C': ['G', 'D'],
    'D': ['G'],
    'G': []
}
def path_h_cost(path):
   last_node =  path[-1]
   return H_table[last_node]

def greedy(graph, start, goal):
    visited =[]
    queue = [[start]]
    while queue:
        queue.sort(key= path_h_cost)
        path =queue.pop(0)
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        for n in graph.get(node,[]):
            new_path = path + [n]
            queue.append(new_path)
    return None

result = greedy(graph,'S','G')
print(f"the path is {result}")