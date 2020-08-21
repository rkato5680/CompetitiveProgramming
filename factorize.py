# prime factorization

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
