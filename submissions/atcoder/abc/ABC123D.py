# problem: https://atcoder.jp/contests/abc123/tasks/abc123_d
# code: https://atcoder.jp/contests/abc123/submissions/15482411

from bisect import bisect_left

X,Y,Z,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

if X*Y*Z <= 50000:
  D = sorted([A[i]+B[j]+C[k] for i in range(X) for j in range(Y) for k in range(Z)],reverse=True)
  for i in range(K):
    print(D[i])
  
else:
  A = sorted(A)
  D = sorted([B[i]+C[j] for i in range(Y) for j in range(Z)])

  thr = K
  s = A[-1]+D[max(0,len(D)-thr)]
  prev_idx=0
  selected = [A[-1] + D[i] for i in range(max(0,len(D)-thr),len(D))]
  
  for i in range(1,X):
    r = s - A[-1-i]
    if r<=0:break
    idx = bisect_left(D,r,prev_idx,len(D)-1)
    if idx == len(D):break
    selected.extend([A[-1-i] + D[j] for j in range(idx,len(D))])
    prec_idx = idx

  selected = sorted(selected,reverse=True)

  for i in range(K):
    print(selected[i])