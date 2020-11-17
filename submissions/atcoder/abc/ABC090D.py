# problem: https://atcoder.jp/contests/abc090/tasks/arc091_b
# code: https://atcoder.jp/contests/abc090/submissions/15695982

N,K=map(int,input().split())
if K==0:
  print(N**2)
  exit()
ans=0
for i in range(1,N+1):
  q,r=divmod(N,i)
  ans += q*max(0,i-K)+max(0,r-K+1)
print(ans)