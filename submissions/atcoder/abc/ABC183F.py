# problem: https://atcoder.jp/contests/abc183/tasks/abc183_f
# code: https://atcoder.jp/contests/abc183/submissions/18156456

class UnionFind():
    def __init__(self, n=0):
        self.d = [-1]*n
        self.g = [{} for _ in range(n)]
    
    def find(self, x):
        if self.d[x] < 0: return x
        self.d[x] = self.find(self.d[x])
        return self.d[x]

    def unite(self, x, y):
        x,y=self.find(x),self.find(y)
        if x==y:return False
        if self.d[x] > self.d[y]: x,y=y,x
        self.d[x] += self.d[y]
        for k in self.g[y].keys():
          if self.g[x].get(k):
            self.g[x][k] += self.g[y][k]
          else:
            self.g[x][k] = self.g[y][k]
        self.d[y] = x
        return True

    def same(self,x,y): return self.find(x)==self.find(y)
    def size(self,x): return -self.d[self.find(x)]
    
N,Q=map(int,input().split())
*C,=map(int,input().split())
uf = UnionFind(N)
for i in range(N):
  uf.g[i][C[i]] = 1

for i in range(Q):
  t,a,b = map(int,input().split())
  if t==1:
    uf.unite(a-1,b-1)
  else:
    a = uf.find(a-1)
    print(uf.g[a][b] if uf.g[a].get(b) else 0)