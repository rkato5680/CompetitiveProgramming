# problem: https://atcoder.jp/contests/abc096/tasks/abc096_c
# code: https://atcoder.jp/contests/abc096/submissions/15653788

H,W=map(int,input().split())
s=[list(map(int, list(input().replace('#','1').replace('.','0')))) for _ in range(H)]

padded = [[0 for i in range(W+2)] for j in range(H+2)]

for i in range(H):
  for j in range(W):
    padded[i+1][j+1] = s[i][j] 

for i in range(1,H+1):
  for j in range(1,W+1):
    if padded[i][j]==1:
      if padded[i+1][j]==0 and padded[i-1][j]==0 and padded[i][j+1]==0 and padded[i][j-1]==0:
        print('No')
        exit()
print('Yes')