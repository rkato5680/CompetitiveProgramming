# check whether the given positive integer is prime or not

def is_prime(n):
    max_factor = int(np.sqrt(n))
    for i in range(2, max_factor+1):
        if n % i == 0:
            return False
    return True



# list all prime numbers in closed interval [L,R]

def sieve(L,R):
    if L<2:L=2
    flag=[0]*(R+1)
    for i in range(2, int(R**.5)+5):
        if flag[i] == 1:continue
        for j in range(i*2,R+1, i):
            if flag[j] == 1:continue
            if j % i == 0:
                flag[j] = 1
    
    return [i for i in range(L,R+1) if flag[i] == 0]
