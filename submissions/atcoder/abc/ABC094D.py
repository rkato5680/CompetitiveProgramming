# problem: https://atcoder.jp/contests/abc094/tasks/arc095_b
# code: https://atcoder.jp/contests/abc094/submissions/15655793

N=int(input())
A=list(map(int,input().split()))

if N == 2:
  print(*(max(A),min(A)))
  exit()
  
m = max(A)/2
nearest=-1
for i in range(N):
  if abs(A[i]-m)<abs(nearest-m):
    nearest = A[i]

print(*(max(A),nearest))