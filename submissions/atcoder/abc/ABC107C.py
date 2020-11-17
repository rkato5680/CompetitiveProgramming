# problem: https://atcoder.jp/contests/abc107/tasks/arc101_a
# code: https://atcoder.jp/contests/abc107/submissions/15558438

N,K=map(int,input().split())
x=list(map(int,input().split()))

res=[]
for i in range(N-K+1):
  tmp = min(abs(x[i]),abs(x[i+K-1]))+x[i+K-1]-x[i]
  res.append(tmp)
  
print(min(res))