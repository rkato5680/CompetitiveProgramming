# problem: https://atcoder.jp/contests/abc182/tasks/abc182_e
# code: https://atcoder.jp/contests/abc182/submissions/17976237

H,W,N,M=map(int,input().split())
#lamps = [tuple(map(int,input().split())) for _ in range(N)]

S = [["."]*W for _ in range(H)]
#res = [[0]*W for _ in range(H)]

ans = 0
for i in range(N):
  x,y = map(int,input().split())
  S[x-1][y-1] = '@'
  #res[x-1][y-1] = 1
  ans += 1

for i in range(M):
  x,y = map(int,input().split())
  S[x-1][y-1] = '#'

for i in range(H):
  flag = 0
  for j in range(W):
    if S[i][j] == '#':
      flag = 0
      continue
    if S[i][j] == '@':
      flag = 1
    if flag and S[i][j] == '.':
      ans += 1
      S[i][j] = 'x'
      #print(i,j)
  flag = 0
  for j in range(W-1,-1,-1):
    if S[i][j] == '#':
      flag = 0
      continue
    if S[i][j] == '@':
      flag = 1
    if flag and S[i][j] == '.':
      ans += 1
      S[i][j] = 'x'
      #print(i,j)
    
for j in range(W):
  flag = 0
  for i in range(H):
    if S[i][j] == '#':
      flag = 0
      continue
    if S[i][j] == '@':
      flag = 1
    if flag and S[i][j] == '.':
      ans += 1
      S[i][j] = 'x'
      #print(i,j)
  flag = 0
  for i in range(H-1,-1,-1):
    if S[i][j] == '#':
      flag = 0
      continue
    if S[i][j] == '@':
      flag = 1
    if flag and S[i][j] == '.':
      ans += 1
      S[i][j] = 'x'
      #print(i,j)
      
print(ans)