# bfs on grid like '##...#'

from collections import deque

def bfs(s):
  seen = [[0 for i in range(W)] for j in range(H)]
  total = [[0 for i in range(W)] for j in range(H)]
  todo = deque([])
  now = s
  if S[now[0]][now[1]]=='#':return 0
  seen[now[0]][now[1]],total[now[0]][now[1]] = 1,0
  todo.append(now)
  while 1:
    if len(todo)==0:break
    now = todo.popleft()
    for d in [(1,0),(-1,0),(0,1),(0,-1)]:
      new = (now[0]+d[0], now[1]+d[1])
      if new[0]<0 or new[0]>=H:continue
      if new[1]<0 or new[1]>=W:continue
      if seen[new[0]][new[1]]==1:continue
      if S[new[0]][new[1]]=='#':continue
      seen[new[0]][new[1]] = 1
      todo.append(new)
      total[new[0]][new[1]] = total[now[0]][now[1]] + 1
  return total
  
  
  
# bfs on graph or tree

from collections import deque

def bfs(s):
    seen = [0]*(N+1)
    d = [0]*(N+1)
    prev = [0]*(N+1)
    todo = deque()
    seen[s]=1
    todo.append(s)
    while len(todo):
      a = todo.popleft()
      for b in G[a]:
        if seen[b] == 0:
          seen[b] = 1
          todo.append(b)
          d[b] += d[a] + 1
          prev[b] = a
    return d, prev
