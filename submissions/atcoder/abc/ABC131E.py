# problem: https://atcoder.jp/contests/abc131/tasks/abc131_e
# code: https://atcoder.jp/contests/abc131/submissions/15395461

from itertools import combinations

N,K=map(int,input().split())

MAX=(N-1)*(N-2)//2

if K>MAX:
  print(-1)
  exit()

n_add=MAX-K
M=N-1+n_add
e_comb = list(combinations(range(2,N+1),r=2))

print(M)
for i in range(M):
  if i < N-1:
    print(*(1,2+i))
  else:
    print(*e_comb[i-(N-1)])