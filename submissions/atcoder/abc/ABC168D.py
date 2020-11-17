# problem: https://atcoder.jp/contests/abc168/tasks/abc168_d
# code: https://atcoder.jp/contests/abc168/submissions/16037083

from collections import deque

N,M=map(int,input().split())
G=[[] for _ in range(N+1)]
for i in range(M):
  a,b=map(int,input().split())
  G[a].append(b)
  G[b].append(a)

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
    return prev
  
prev = bfs(1)

print('Yes')
print(*prev[2:])