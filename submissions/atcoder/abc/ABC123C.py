# problem: https://atcoder.jp/contests/abc123/tasks/abc123_c
# code: https://atcoder.jp/contests/abc123/submissions/15481731

N=int(input())
A = [int(input()) for _ in range(5)]

if N==1:
  print(5)
  exit()

if N % min(A)==0:
  print(N//min(A)+4)
  exit()
  
else:
  print(N//min(A)+5)