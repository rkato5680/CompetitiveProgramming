# problem: https://atcoder.jp/contests/abc127/tasks/abc127_d
# code: https://atcoder.jp/contests/abc127/submissions/15460596

from bisect import bisect_left

N,M=map(int,input().split())
A=list(map(int,input().split()))
A=sorted(A)

change=[tuple(map(int,input().split())) for _ in range(M)]
change=sorted(change,key=lambda x: x[1],reverse=True)
change2=[]
count=0
for i in range(M):
  b,c=change[i]
  change2.extend([c]*b)
  count += b
  if count >= N:break

A.extend(change2)
A = sorted(A)
print(sum(A[len(A)-N:]))