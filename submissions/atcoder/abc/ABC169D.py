# problem: https://atcoder.jp/contests/abc169/tasks/abc169_d
# code: https://atcoder.jp/contests/abc169/submissions/16034234

from collections import Counter

N=int(input())

if N==1:
  print(0)
  exit()
  
def factorize(n):
    out=[]
    i = 2
    while 1:
        if n%i==0:
            out.append(i)
            n //= i
        else:
            i += 1
        if n == 1:break
        if i > int(n**.5+3):
            out.append(n)
            break
    
    return out
  
c = Counter(factorize(N))

def n_unique(n):
  out = 0
  while 1:
    if out*(out+1)//2 > n:
      return out-1
    out += 1

ans = 0
for k in c.keys():
  ans += n_unique(c[k])
  
print(ans)