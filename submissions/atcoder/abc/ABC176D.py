# problem: https://atcoder.jp/contests/abc176/tasks/abc176_d
# code: https://atcoder.jp/contests/abc176/submissions/16975342

from itertools import product
import heapq

def main():
  H,W=map(int,input().split())
  sx,sy = map(lambda x: int(x)-1,input().split())
  gx,gy = map(lambda x: int(x)-1,input().split())
  S = [input() for _ in range(H)]
  INF = 10**20

  P = [(p1,p2) for p1 in range(3) for p2 in range(-2,3)]
  G = [{} for _ in range(H*W)]
  for i in range(H):
    for j in range(W):
      if S[i][j] == '#': continue
      for p1,p2 in P:
        i2,j2 = i+p1,j+p2
        if not (0<=i2<H and 0<=j2<W): continue
        if S[i2][j2] == '#': continue
        if sum(map(abs,(p1,p2)))<=1:G[i*W+j][i2*W+j2] = G[i2*W+j2][i*W+j] = 0
        else: G[i*W+j][i2*W+j2] = G[i2*W+j2][i*W+j] = 1

  def dijkstra(start = 0):
      from heapq import heappop, heappush
      d = [INF for i in range(len(G))]
      d[start] = 0
      que = []
      heappush(que, start)
      while que:
          d_,v = divmod(heappop(que),10**7)
          if d[v] < d_: continue
          for u in G[v].keys():
              if d[u] > d[v] + G[v][u]:
                  d[u] = d[v] + G[v][u]
                  heappush(que, d[u]*10**7+u)
      return d

  d = dijkstra(sx*W+sy)
  ans = d[gx*W+gy]
  print(ans if ans < INF else -1)
  
if __name__=="__main__":
  main()