# problem: https://atcoder.jp/contests/abc175/tasks/abc175_e
# code: https://atcoder.jp/contests/abc175/submissions/16983347

R,C,K=map(int,input().split())
rcv = [tuple(map(int,input().split())) for _ in range(K)]
items = {(r-1)*C+(c-1):v for r,c,v in rcv}

dp = [[0]*4 for _ in range(R)]

for j in range(C):
  for i in range(R):
    if i > 0: dp[i][0] = max(dp[i-1])
    for k in range(2,-1,-1):
      if items.get(i*C+j): dp[i][k+1] = max(dp[i][k+1],dp[i][k]+items[i*C+j])
        
print(max(dp[-1]))