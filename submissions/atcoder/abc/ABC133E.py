# problem: https://atcoder.jp/contests/abc133/tasks/abc133_e
# code: https://atcoder.jp/contests/abc133/submissions/16762210

from collections import deque

def main():
  N,K=map(int,input().split())
  mod = 10**9+7
  G=[[] for _ in range(N)]
  for i in range(N-1):
    a,b=map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

  def bfs(s):
      seen = [0]*N
      color = [0]*N
      todo = deque()
      seen[s]=1
      todo.append(s)
      color[s]=K
      while todo:
        a = todo.popleft()
        if a == s: count = K-1
        else: count = K-2
        for b in G[a]:
          if seen[b] == 0:
            seen[b] = 1
            todo.append(b)
            color[b] = count %mod
            count -= 1
      return color

  MAX,start = 0,-1
  for i in range(N):
    if len(G[i])>MAX:
      MAX=len(G[i])
      start = i
  
  color = bfs(start)
  ans = 1
  for i in range(N):
    ans *= color[i]
    ans %= mod

  print(ans)
  
if __name__=="__main__":
  main()