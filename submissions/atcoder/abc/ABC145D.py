# problem: https://atcoder.jp/contests/abc145/tasks/abc145_d
# code: https://atcoder.jp/contests/abc145/submissions/15324543

X,Y=map(int,input().split())
mod = 10**9+7

if 2*X < Y or 2*Y < X:print(0)
elif (X+Y) % 3 != 0:print(0)
else:
  n = (X+Y) // 3
  X,Y=X-n,Y-n
  
  factorial=[1 for i in range(X+Y+1)]
  for i in range(1,X+Y+1):
    if i==1:factorial[i]=1
    else:factorial[i] = factorial[i-1]*i % mod
  print(factorial[X+Y]*pow(factorial[X]*factorial[Y],-1,mod)%mod)