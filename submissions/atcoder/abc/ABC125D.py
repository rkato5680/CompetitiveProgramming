# problem: https://atcoder.jp/contests/abc125/tasks/abc125_d
# code: https://atcoder.jp/contests/abc125/submissions/15470100

from bisect import bisect_left

N=int(input())
A=list(map(int,input().split()))
A=sorted(A)

idx = bisect_left(A,0)
if idx != 0 and idx != N:
  if idx % 2 == 1:
    if abs(A[idx-1]) > abs(A[idx]):
      A[idx-1] *= -1
      A[idx] *= -1
  for i in range(0,idx-1,2):
    A[i] *= -1
    A[i+1] *= -1

if idx==N:
  if N % 2 == 0:
    print(-sum(A))
    exit()
  else:
    print(-sum(A[:-1])+A[-1])
    exit()

print(sum(A))