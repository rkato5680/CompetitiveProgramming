# problem: https://atcoder.jp/contests/abc118/tasks/abc118_c
# code: https://atcoder.jp/contests/abc118/submissions/15501928

N=int(input())
A=list(map(int,input().split()))

MIN= min(A)
while 1:
  newA = []
  MIN0 = MIN
  for i in range(len(A)):
    a = A[i] % MIN
    if a == 0:
      newA.append(a)
    else:
      if a < MIN:
        MIN = a
      newA.append(a)
  if MIN==1:break
  if MIN0 == MIN:break

print(MIN)