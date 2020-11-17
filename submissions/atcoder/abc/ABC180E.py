# problem: https://atcoder.jp/contests/abc180/tasks/abc180_e
# code: https://atcoder.jp/contests/abc180/submissions/17466118

N=int(input())
xyz=[tuple(map(int,input().split())) for _ in range(N)]
INF = 10**20

def dist(x,y):
  return abs(y[1]-x[1])+abs(y[0]-x[0])+max(0,y[2]-x[2])

dp = [[INF]*N for _ in range(1<<N)]
dp[0][0] = 0

for S in range(1<<N):
  for i in range(N):
    if (S>>i)&1:
      dp[S][i] = min(dp[S^(1<<i)][j] + dist(xyz[j],xyz[i]) for j in range(N))
      
print(min(dp[-1][i] + dist(xyz[i],xyz[0]) for i in range(N)))