# problem: https://atcoder.jp/contests/abc130/tasks/abc130_d
# code: https://atcoder.jp/contests/abc130/submissions/15405819

from bisect import bisect_left

N,K=map(int,input().split())
A=list(map(int,input().split()))
cumA=[0]
for i in range(N):
  cumA.append(cumA[-1]+A[i])

count=0
for i in range(N):
  idx = bisect_left(cumA,K+cumA[i])
  count += N-idx+1
print(count)