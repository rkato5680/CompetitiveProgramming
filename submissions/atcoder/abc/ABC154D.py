# problem: https://atcoder.jp/contests/abc154/tasks/abc154_d
# code: https://atcoder.jp/contests/abc154/submissions/15213331

N,K=map(int,input().split())
p=list(map(int,input().split()))
exp0 = (sum(p[:K])+K)/2
MAX=exp0
old = exp0
for i in range(1,N-K+1):
  new = old + (p[K+i-1]+1)/2 - (p[i-1]+1)/2
  if new > MAX: MAX = new
  old = new
print(MAX)