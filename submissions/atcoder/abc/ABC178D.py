# problem: https://atcoder.jp/contests/abc178/tasks/abc178_d
# code: https://atcoder.jp/contests/abc178/submissions/16691412

S=int(input())
mod = 10**9 + 7
N = 2*S

factorial=[1 for i in range(N+1)]
for i in range(1,N+1):
    if i==1:factorial[i]=1
    else:factorial[i] = factorial[i-1]*i % mod
      
def comb(n,k):
    return (factorial[n]*pow(factorial[n-k]*factorial[k], -1, mod))%mod

ans = 0
for i in range(S//3):
  s = S - (i+1)*3
  ans += comb(s+i,i)
  ans %= mod
  
print(ans)