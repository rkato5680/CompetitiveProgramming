# problem: https://atcoder.jp/contests/abc109/tasks/abc109_c
# code: https://atcoder.jp/contests/abc109/submissions/15552827

from math import gcd

N,X=map(int,input().split())
x = list(map(int,input().split()))

if N == 1:
  print(abs(X-x[0]))
  exit()

diff = [abs(X-x[i]) for i in range(N)]

for i in range(1,N):
  if i == 1:
    total_gcd = gcd(diff[i],diff[i-1])
  else:
    total_gcd = gcd(diff[i],total_gcd)
    
print(total_gcd)