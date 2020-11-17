# problem: https://atcoder.jp/contests/abc124/tasks/abc124_c
# code: https://atcoder.jp/contests/abc124/submissions/15480609

S=input()

cost1 = 0
cost2 = 0
for i in range(len(S)):
  if i % 2 == int(S[i]):
    cost1 += 1
  else:
    cost2 += 1

print(min(cost1,cost2))