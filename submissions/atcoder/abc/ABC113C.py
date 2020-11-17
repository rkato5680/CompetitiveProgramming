# problem: https://atcoder.jp/contests/abc113/tasks/abc113_c
# code: https://atcoder.jp/contests/abc113/submissions/15528884

def pad(n):
  n = str(n)
  n = '0'*(6-len(n))+n
  return n

N,M=map(int,input().split())
py = [tuple(map(int,input().split())) for _ in range(M)]

py = sorted(enumerate(py),key=lambda x: x[1])

pref=0
count=0
new_py = []
for i in range(M):
  j,(p,y)=py[i]
  if p==pref:
    count += 1
  else:
    count = 1
  new_py.append((j,pad(p)+pad(count)))
  pref = p
  
new_py = sorted(new_py)
for i in range(M):
  print(new_py[i][1])