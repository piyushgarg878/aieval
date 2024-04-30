def uniform_cost_search(goal, start):
  global graph
  queue = []
  answer=1000000 #optimal path cost
  queue.append([0, start])
  visited = {}
  while (len(queue) > 0):
    queue = sorted(queue)
    print(queue)
    p = queue[0]
    del queue[0]
    if(p[1]==goal):
      if (answer > p[0]):
        answer = p[0]
        del queue[0]
        return answer
    if (p[1] not in visited):
      for i in range(len(graph[p[1]])):
        if(graph[p[1]][i]!=0):
          queue.append( [(p[0] + graph[p[1]][i]), i])
          visited[p[1]] = 1
  return answer

graph=[[0,2,0,5,0,0,0],[2,0,4,5,0,0,1],[0,4,0,0,4,6,0],[5,5,0,2,0,0,6],[0,0,4,2,0,3,7],[0,0,6,0,3,0,3],[0,1,0,6,7,3,0]]
goal = 6
answer = uniform_cost_search(goal, 0)
print("Minimum cost from 0 to 6 is = ",answer)
