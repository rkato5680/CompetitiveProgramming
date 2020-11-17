# problem: https://atcoder.jp/contests/abc138/tasks/abc138_d
# code: https://atcoder.jp/contests/abc138/submissions/15356660

from collections import deque

N,Q=map(int,input().split())
G=[[] for i in range(N+1)]
for i in range(N-1):
  a,b=map(int,input().split())
  G[a].append(b)
  G[b].append(a)

P=[0 for i in range(N+1)]
for i in range(Q):
  p,x=map(int,input().split())
  P[p] += x

def bfs(s):
    seen = [0 for i in range(N+1)]
    prev = [0 for i in range(N+1)]
    todo = deque([])
    now = s
    seen[now]=1
    todo.append(now)
    while 1:
      if len(todo)==0:break
      a = todo.popleft()
      for b in G[a]:
        if seen[b] == 0:
          seen[b] = 1
          todo.append(b)
          prev[b] = a
          P[b] += P[a]

bfs(1)
print(*P[1:])