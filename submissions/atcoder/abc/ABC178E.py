# problem: https://atcoder.jp/contests/abc178/tasks/abc178_e
# code: https://atcoder.jp/contests/abc178/submissions/16696262

N=int(input())
xy=[]
xmax,xmin,ymax,ymin = -10**10,10**10,-10**10,10**10
for i in range(N):
  x,y=map(int,input().split())
  xmax = max(xmax,x+y)
  ymax = max(ymax,x-y)
  xmin = min(xmin,x+y)
  ymin = min(ymin,x-y)
print(max(xmax-xmin,ymax-ymin))