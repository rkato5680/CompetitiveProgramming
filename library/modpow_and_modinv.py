# compute power and inverse (mod "mod")
# author (C++): https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a#3-%E5%89%B2%E3%82%8A%E7%AE%97-a--b

def modpow(a, n, mod):
    res = 1
    while n > 0:
        if n&1:res=res*a%mod
        a = a * a % mod
        n>>=1
    return res

def modinv(a, mod): return modpow(a,mod-2,mod)
