# problem: https://atcoder.jp/contests/abc144/tasks/abc144_d
# code: https://atcoder.jp/contests/abc144/submissions/15327386

from math import atan,pi

a,b,x=map(int,input().split())

if b-x/a**2 <= x/a**2:print(atan((b-x/a**2)/(a/2))*(180/pi))
else:
  y = x/a*2/b
  print(atan(b/y)*(180/pi))