# problem: https://atcoder.jp/contests/abc156/tasks/abc156_d
# code: https://atcoder.jp/contests/abc156/submissions/15192721

n,a,b=map(int,input().split())
p=10**9+7
q,res=divmod(n,10000)
n1=(2**10000)%p

total = 1
for i in range(q):
  total *= n1
  total %= p
total *= 2**res
total %= p

def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n&1:res=res*a%mod
        a = a * a % mod
        n>>=1
    return res

def modinv(a, mod): return modpow(a,mod-2,mod)

A = 1
for i in range(a//3):
  A = A*modinv((a-3*i)*(a-3*i-1)*(a-3*i-2), p)
  A = A*(n-3*i)*(n-3*i-1)*(n-3*i-2) % p
for j in range(a%3):
  A = A*modinv(a-3*(a//3)-j,p)
  A = A*(n-3*(a//3)-j)%p

B = 1
for i in range(b//3):
  B = B*modinv((b-3*i)*(b-3*i-1)*(b-3*i-2), p)
  B = B*(n-3*i)*(n-3*i-1)*(n-3*i-2) % p
for j in range(b%3):
  B = B*modinv(b-3*(b//3)-j,p)
  B = B*(n-3*(b//3)-j)%p

print((total-A-B-1)%p)