# problem: https://atcoder.jp/contests/abc163/tasks/abc163_d
# code: https://atcoder.jp/contests/abc163/submissions/15074564

N,K=map(int, input().split())

sum_ = 0
for k in range(K, N+2):
  sum_ += k*(N-k+1)+1
  sum_ = sum_ % (10**9+7)

print(sum_)