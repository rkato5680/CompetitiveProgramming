# problem: https://atcoder.jp/contests/abc174/tasks/abc174_d
# code: https://atcoder.jp/contests/abc174/submissions/15620218

from collections import Counter

N=int(input())
color=input()

c = Counter(color)
r = c['R']

count = 0
for i in range(N):
  if r == 0:break
  if color[i]=='W':
    count += 1
    r -= 1
  else:
    r -= 1

print(count)