# problem: https://atcoder.jp/contests/abc167/tasks/abc167_d
# code: https://atcoder.jp/contests/abc167/submissions/15996891

N,K=map(int,input().split())
*A,=map(int,input().split())

vis=[0]*(N+1)
now=1
vis[now] = 1
his=[now]
while 1:
  new = A[now-1]
  if vis[new]==0:
    vis[new]=1
    his.append(new)
    now = new
  else:
    idx = his.index(new)
    cycle = his[idx:]
    margin = his[:idx]
    break
    
if K <= len(margin):
  print(his[K])
  exit()
  
K -= len(margin)
K %= len(cycle)

print(cycle[K])