# problem: https://atcoder.jp/contests/abc112/tasks/abc112_d
# code: https://atcoder.jp/contests/abc112/submissions/15530100

N,M=map(int,input().split())

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
  
d = make_divisors(M)
d = list(filter(lambda x:x<=M/N,d))

print(d[-1])