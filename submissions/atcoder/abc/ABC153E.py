# problem: https://atcoder.jp/contests/abc153/tasks/abc153_e
# code: https://atcoder.jp/contests/abc153/submissions/16541831

H,N=map(int,input().split())
AB = [tuple(map(int,input().split())) for _ in range(N)]
dp = [[0]*(N+1) for _ in range(2*10**4+5)]

for j in range(1,H+1):
  for i in range(1,N+1):
    if AB[i-1][0] < j:
      dp[j][i] = dp[j - AB[i-1][0]][i] + AB[i-1][1]
    else:
      dp[j][i] = AB[i-1][1]
  MIN = min(dp[j][1:])
  dp[j][1:] = [MIN]*(len(dp[j])-1)

print(min(dp[H][1:]))