# problem: https://atcoder.jp/contests/abc104/tasks/abc104_c
# code: https://atcoder.jp/contests/abc104/submissions/15570790

from math import ceil
from itertools import product

D,G=map(int,input().split())
pc=[list(map(int,input().split())) for _ in range(D)]

def calc(P):
  count = 0
  g = G
  for i in range(D):
    p,c = pc[-1-i]
    if P[-1-i]==1:
      count += p
      g -= (D-i)*100*p+c
    if g<=0:
      return count
  for i in range(D):
    p,c = pc[-1-i]
    if P[-1-i]==0:
      tmp = min(p-1,ceil(g/((D-i)*100)))
      count += tmp
      g -= (D-i)*100*tmp
    if g<=0:
      return count
  return -1

MIN=10**9
for P in product(range(2),repeat=D):
  tmp = calc(P)
  if tmp != -1 and tmp < MIN: MIN=tmp
    
print(MIN)