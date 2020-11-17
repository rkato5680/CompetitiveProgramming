# problem: https://atcoder.jp/contests/abc172/tasks/abc172_d
# code: https://atcoder.jp/contests/abc172/submissions/14759830

N = int(input())

if N == 1:
  print(1)

else:
  sum_ = N*(N+1)//2
  for i in range(2, N//2+1):
    n = N // i
    sum_ += i*(n*(n+1)//2)

  sum_ += (N//2+1 + N) * (N - (N//2+1) + 1) // 2

  print(sum_)