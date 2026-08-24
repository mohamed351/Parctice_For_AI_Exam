graph = {
    "S": [("A", 2), ("B", 3), ("D", 5)],
    "A": [("C", 4)],     
    "B": [("D", 4)],    
    "C": [("D", 1), ("G", 2)], 
    "D": [("G", 5)],    
    "G": [],
}

def path_cost(path):
    total =0
    for (node, cost) in path:
        total+=cost
    return total

def ucs(graph, start, goal):
    visited =[]
    queue =[[(start,0)]]
    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]
        if node in visited:
            continue
        if node == goal:
            return path
        for (n, c) in graph.get(node,[]):
            new_path = path + [(n,c)]
            queue.append(new_path)
    return None
        

result = ucs(graph,'S','G')
print(f"the path is {result}")