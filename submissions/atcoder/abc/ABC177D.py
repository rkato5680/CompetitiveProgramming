# problem: https://atcoder.jp/contests/abc177/tasks/abc177_d
# code: https://atcoder.jp/contests/abc177/submissions/16332793

class UnionFind():
    def __init__(self, n=0):
        self.d = [-1]*n
    
    def find(self, x):
        if self.d[x] < 0: return x
        self.d[x] = self.find(self.d[x])
        return self.d[x]

    def unite(self, x, y):
        x,y=self.find(x),self.find(y)
        if x==y:return False
        if self.d[x] > self.d[y]: x,y=y,x
        self.d[x] += self.d[y]
        self.d[y] = x
        return True

    def same(self, x,y): return self.find(x)==self.find(y)
    def size(self,x): return -self.d[self.find(x)]
    
N,M=map(int,input().split())
uf = UnionFind(N+1)
for i in range(M):
  a,b=map(int,input().split())
  uf.unite(a,b)
  
print(-min(uf.d))