# problem: https://atcoder.jp/contests/abc148/tasks/abc148_e
# code: https://atcoder.jp/contests/abc148/submissions/16542985

N=int(input())

if N % 2 or N < 10:
  print(0)
  exit()
  
ans = 0
i = 1
while 2*5**i<=N:
  ans += N // (2*5**i)
  i += 1
  
print(ans)