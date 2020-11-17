# problem: https://atcoder.jp/contests/abc114/tasks/abc114_c
# code: https://atcoder.jp/contests/abc114/submissions/15526370

from itertools import product

S = input()
nd,N = len(S),int(S)

if N<357:
  print(0)
  exit()

count = 0
for n_digit in range(3,nd+1):
  for p in product(['3','5','7'],repeat=n_digit):
    if set(p) == {'3','5','7'} and int(''.join(p))<=N:
      count += 1
print(count)