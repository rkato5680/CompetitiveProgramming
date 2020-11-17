# problem: https://atcoder.jp/contests/abc142/tasks/abc142_d
# code: https://atcoder.jp/contests/abc142/submissions/15332791

from math import gcd

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
  
A,B=map(int,input().split())
GCD = gcd(A,B)
GCDs = make_divisors(GCD)
ans = [1 for i in range(len(GCDs)//2+1)]
for i in range(1,len(GCDs)//2):
  for j in range(i+1,len(GCDs)//2+1):
    if GCDs[j]%GCDs[i]==0:ans[j]=0
print(sum(ans))