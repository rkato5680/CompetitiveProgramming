# problem: https://atcoder.jp/contests/abc159/tasks/abc159_f
# code: https://atcoder.jp/contests/abc159/submissions/17018811

N,S=map(int,input().split())
*A,=map(int,input().split())
mod = 998244353

dp = [0]*(S+1)

for i in range(N):
  if A[i]>S: continue
  if A[i]==S:
    dp[S] += (i+1)*(N-i)
    continue
  for j in range(S-A[i],-1,-1):
    if j == S-A[i]: dp[S] += dp[j]*(N-i)
    elif j == 0: dp[A[i]] += i+1
    else: dp[j+A[i]] += dp[j]
    dp[j] %= mod
  dp[S] %= mod

print(dp[-1])