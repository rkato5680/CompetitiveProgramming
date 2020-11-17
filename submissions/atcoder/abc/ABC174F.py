# problem: https://atcoder.jp/contests/abc174/tasks/abc174_f
# code: https://atcoder.jp/contests/abc174/submissions/16540894

from time import time
start = time()

# 解説放送の解法

class BIT:
    '''https://tjkendev.github.io/procon-library/python/range_query/bit.html'''
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)
        self.el = [0]*(n+1)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s
    def add(self, i, x):
        self.el[i] += x
        while i <= self.n:
            self.data[i] += x
            i += i & -i
    def query(self, i, j=None):
        if j is None:
            return self.el[i]
        return self.sum(j) - self.sum(i)
      
def main():
  N,Q=map(int,input().split())
  *C,=map(int,input().split())
  q = [tuple(map(int,input().split())) for _ in range(Q)]

  # 重複度を数える。
  res=[]
  tmp_dict={}
  for i in range(N):
    if tmp_dict.get(C[i]) != None:
      #(クエリの種類、l, r）
      res.append((tmp_dict[C[i]]<<40) | (Q<<20) | i)
      del tmp_dict[C[i]]
    tmp_dict[C[i]] = i

  # クエリと合わせてソート。
  X = []
  for i in range(Q):
    l,r = q[i]
    # (元のクエリの順番、l, r)
    X.append(((l-1)<<40) | (i<<20) | r-1)
    
  X.extend(res) 
  X = sorted(X)

  # 平面走査
  bit = BIT(N)
  ans=[0]*Q
  mask = (1<<20) - 1
  for l in reversed(X):
    r = l & mask
    l >>= 20
    idx = l & mask
    l >>= 20
    if idx == Q:
      bit.add(r,1)
    else:
      ans[idx] = r-l+1-bit.query(l-1,r)
      
  print(*ans)
  
if __name__=="__main__":
  main()