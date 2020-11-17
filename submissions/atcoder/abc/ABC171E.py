# problem: https://atcoder.jp/contests/abc171/tasks/abc171_e
# code: https://atcoder.jp/contests/abc171/submissions/16052252

N=int(input())
*A,=map(int,input().split())

total=0
for i in range(N):
  total ^= A[i]
  
print(*[total^A[i] for i in range(N)])