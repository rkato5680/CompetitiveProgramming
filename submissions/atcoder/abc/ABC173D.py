# problem: https://atcoder.jp/contests/abc173/tasks/abc173_d
# code: https://atcoder.jp/contests/abc173/submissions/15004011

N = int(input())
A = list(map(int, input().split()))

A = sorted(A, reverse=True)

ans = A[0]
count = 2
index = 1
if N == 2:
  print(ans)
else:
  flag = 0
  while flag == 0:
    for i in range(2):
      ans += A[index]
      count += 1
      
      if count == N:
        flag = 1
        break
    index += 1
  print(ans)