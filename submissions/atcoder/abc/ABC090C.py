# problem: https://atcoder.jp/contests/abc090/tasks/arc091_a
# code: https://atcoder.jp/contests/abc090/submissions/15695845

N,M=map(int,input().split())
N,M=sorted([N,M])
if N==1:
  if M>=3:print(M-2)
  else:print(2-M)
elif N==2:print(0)
else:print((N-2)*(M-2))