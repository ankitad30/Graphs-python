#DFS using Stack

def dfs(graph,start):
    path = []
    stack = [start]
    while stack != []:
        v = stack.pop()
        if v not in path:
            path.append(v)
        for w in reversed(graph[v]):
            if w not in path:
                stack.append(w)
    return path



def bfs(graph,root,target):
    #q = Queue()
    checked = []
    q.enqueue(root)
    path = 0
    while not q.isEmpty():
        v = q.dequeue()
        if v == target:
           return True
        elif v not in checked:
            for edge in graph[v]:
                if v not in checked:
                    q.enqueue(edge)
            checked.append(v)
    return False
    
"""

def dfs_rec(graph,start,path = []):
    path = path + [start]
    for edge in graph[start]:
        if edge not in path:
            path = dfs_rec(graph, edge,path)
    return path """

graph = {1: [2, 3],
         2: [1, 4, 5, 6],
         3: [1, 4],
         4: [2, 3, 5],
         5: [2, 4, 6],
         6: [2, 5]}
print dfs(graph,1)
print bfs(graph,1,6)
#print dfs_rec(graph,1)
