# Union Find (disjoint set)

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
