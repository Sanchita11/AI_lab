graph = {
  '9' : ['8','7'],
  '8' : ['6','3'],
  '7' : ['4','2'],
  '6' : ['5'],
  '5' : [],
  '4' : ['9'],
  '3' :[],
  '2' :[]
}
visited = [] 
queue = []   
 
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0) 
        print (s, end = " ") 
        for neighbour in graph[s]:
              if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
 
bfs(visited, graph, '9')