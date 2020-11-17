# problem: https://atcoder.jp/contests/abc121/tasks/abc121_c
# code: https://atcoder.jp/contests/abc121/submissions/15489295

N,M=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(N)]
ab = sorted(ab)

SUM=0
for i in range(N):
  a,b=ab[i]
  x = min(M,b)
  SUM += a*x
  M -= x
  if M==0:break
    
print(SUM)