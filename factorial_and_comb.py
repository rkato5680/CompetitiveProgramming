# compute n! or nCk (n choose k) (modulo "mod")

factorial=[1 for i in range(N+1)]
for i in range(1,N+1):
    if i==1:factorial[i]=1
    else:factorial[i] = factorial[i-1]*i % mod

def comb(n,k):
    return (factorial[n]*pow(factorial[n-k]*factorial[k], -1, mod))%mod
