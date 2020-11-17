# problem: https://atcoder.jp/contests/abc147/tasks/abc147_d
# code: https://atcoder.jp/contests/abc147/submissions/15300487

N=int(input())
A=list(map(int,input().split()))
mod = 10**9+7
base = [(2**i)%mod for i in range(63,-1,-1)]

count = [0 for i in range(64)]
for i in range(N):
  b = list(map(int, list(bin(A[i])[2:])))
  b = [0]*(64-len(b))+b
  for j in range(64):count[j]+=b[j]

print(sum([base[i]*count[i]*(N-count[i]) for i in range(64)])%mod)