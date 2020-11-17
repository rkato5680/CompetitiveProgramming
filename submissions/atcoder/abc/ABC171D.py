# problem: https://atcoder.jp/contests/abc171/tasks/abc171_d
# code: https://atcoder.jp/contests/abc171/submissions/15072637

N=int(input())
A=list(map(int,input().split()))
count = [0 for i in range(110000)]
sum_ = sum(A)
for i in range(N):
  count[A[i]] += 1

Q=int(input())
for i in range(Q):
  b,c = map(int,input().split())
  count[c] += count[b]
  sum_ += (c-b)*count[b]
  count[b] = 0
  print(sum_)