# problem: https://atcoder.jp/contests/abc122/tasks/abc122_c
# code: https://atcoder.jp/contests/abc122/submissions/15483905

N,Q=map(int,input().split())
S=input()
lr = [list(map(int,input().split())) for _ in range(Q)]

indices=[0]*(N+1)
for i in range(1,N+1):
  if S[i-1:i+1]=='AC':
    indices[i] += indices[i-1] + 1
  else:
    indices[i] += indices[i-1]

for i in range(Q):
  l,r=lr[i]
  print(indices[r-1]-indices[l-1])