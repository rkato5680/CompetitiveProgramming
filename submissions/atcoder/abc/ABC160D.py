# problem: https://atcoder.jp/contests/abc160/tasks/abc160_d
# code: https://atcoder.jp/contests/abc160/submissions/15112963

N,X,Y=map(int, input().split())
d = [0]+list(range(N-1, 0, -1))
X,Y=min(X,Y),max(X,Y)

for i in range(1,N):
  for j in range(i+1,N+1):
    if i<= X:
      if j>= Y:
        d[j-i] -=1
        d[j-Y+X-i+1] += 1
      else:
        if j > (X+Y)/2:
          d[j-i] -=1
          d[X-i+1+Y-j] += 1
    else:
      if i-X+abs(j-Y)+1 < j-i:
        d[j-i] -= 1
        d[i-X+abs(j-Y)+1] += 1

for i in range(1,N):
  print(d[i])