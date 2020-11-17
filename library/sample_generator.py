from random import randint,random, shuffle

def int_generator(L=0, R=10):
    return randint(L,R)

def perm_generator(amin=1,amax=10):
    A = list(range(amin,amax+1))
    shuffle(A)
    return A

def string_generator(N, mode='l', S=None):
    if mode=='l':
        return ''.join([chr(randint(97,122)) for _ in range(N)])
    elif mode=='u':
        return ''.join([chr(randint(65,90)) for _ in range(N)])
    elif mode=='lu':
        return ''.join([chr(randint(*([(65,90),(97,122)][randint(0,1)]))) for _ in range(N)])
    else:
        return ''.join([S[randint(0,len(S)-1)] for _ in range(N)])
    
def grid_generator(H,W,S='#.'):
    return [''.join([S[randint(0,len(S)-1)] for _ in range(W)]) for _ in range(H)]

def tree_generator(N, weight=False, wspan=[]):
    used = {1}
    not_used=set(range(2,N+1))
    E = []
    for i in range(N-1):
        tmp1, tmp2 = list(used),list(not_used)
        if i == 0:
            a,b = tmp1[0],tmp2[randint(0,len(tmp2)-1)]
        elif i == N-2:
            a,b = tmp1[randint(0,len(tmp1)-1)], tmp2[0]
        else:
            a, b = tmp1[randint(0,len(tmp1)-1)], tmp2[randint(0,len(tmp2)-1)]
        if weight:
            c = randint(*wspan)
            E.append((a,b,c))
        else:
            E.append((a,b))
        used.add(b)
        not_used.remove(b)
        
    return E

def graph_generator(N,M,weight=False,wspan=[]):
    E = set()
    while len(E)<M:
        a,b=0,0
        while a == b:
            a, b = randint(1,N),randint(1,N)
        E.add((a,b))
    E = list(E)
    if weight:
        E = [(*E[i], randint(*wspan)) for i in range(M)]
    return E

def sample_generator(which=[], args=[], n_samples=1):
    out=[]
    for i in range(n_samples):
        tmp=[]
        for j in range(len(which)):
            if which[j]=='int':
                g = int_generator
            elif which[j]=='perm':
                g = perm_generator
            elif which[j]=='string':
                g = string_generator
            elif which[j]=='grid':
                g = grid_generator
            elif which[j]=='tree':
                g = tree_generator
            elif which[j]=='graph':
                g = graph_generator
            if isinstance(args[j], list) or isinstance(args[j], tuple):
                tmp.append(g(*args[j]))
            else:
                tmp.append(g(**args[j]))
        out.append(tmp)
    return out
