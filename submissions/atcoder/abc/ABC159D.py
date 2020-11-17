# problem: https://atcoder.jp/contests/abc159/tasks/abc159_d
# code: https://atcoder.jp/contests/abc159/submissions/15116282

from collections import Counter
N=int(input())
A=list(map(int, input().split()))

count = Counter(A)
vals = count.values()
sum_ = 0
for v in vals:
  if v >= 2: sum_ += v*(v-1)
sum_ //= 2

for k in range(N):
  if count[A[k]] < 2: print(sum_)
  else:print(sum_ + 1 - count[A[k]])