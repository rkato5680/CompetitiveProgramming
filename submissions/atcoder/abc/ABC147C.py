# problem: https://atcoder.jp/contests/abc147/tasks/abc147_c
# code: https://atcoder.jp/contests/abc147/submissions/15299571

from itertools import product

N=int(input())
statement = [[] for i in range(N)]
for i in range(N):
  A=int(input())
  for j in range(A):
    x,y=map(int,input().split())
    x -= 1
    statement[i].append((x,y))

MAX=0
for p in product(range(2),repeat=N):
  flag=0
  for i in range(N):
    if p[i] == 1:
      for j in range(len(statement[i])):
        if statement[i][j][1]==1:
          x = statement[i][j][0]
          if p[x] != 1:
            flag=1
            break
        if statement[i][j][1]==0:
          x = statement[i][j][0]
          if p[x] == 1:
            flag=1
            break
    if flag==1:break
  if flag==1:continue
  if sum(p) > MAX:
    MAX=sum(p)

print(MAX)