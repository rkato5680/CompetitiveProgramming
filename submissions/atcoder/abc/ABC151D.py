# problem: https://atcoder.jp/contests/abc151/tasks/abc151_d
# code: https://atcoder.jp/contests/abc151/submissions/15236868

from collections import deque

H,W=map(int,input().split())
S=[]
for i in range(H):
  S.append(input())
  
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
  return max(map(max, total))

MAX=0
for i in range(H):
  for j in range(W):
    s = (i,j)
    max_ = bfs(s)
    if MAX < max_:MAX=max_

print(MAX)