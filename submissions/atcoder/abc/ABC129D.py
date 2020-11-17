# problem: https://atcoder.jp/contests/abc129/tasks/abc129_d
# code: https://atcoder.jp/contests/abc129/submissions/15410409

H,W=map(int,input().split())
S=[input() for _ in range(H)]

res=[[] for i in range(H)]
for i in range(H):
  count=0
  for j in range(W):
    if S[i][j]=='#':
      if j != 0 and S[i][j-1]=='.':
        res[i].append(count)
      res[i].append(0)
      count=0
      continue
    else:
      count += 1
      if j == W-1:
        res[i].append(count)

cum = [[] for i in range(len(res))]
for i in range(len(res)):
  for j in range(len(res[i])):
    if res[i][j]==0:cum[i].append(0)
    else:cum[i].extend([res[i][j]]*res[i][j])

res=[[] for i in range(W)]
for i in range(W):
  count=0
  for j in range(H):
    if S[j][i]=='#':
      if j != 0 and S[j-1][i]=='.':
        res[i].append(count)
      res[i].append(0)
      count=0
      continue
    else:
      count += 1
      if j == H-1:
        res[i].append(count)

cum2 = [[] for i in range(len(res))]
for i in range(len(res)):
  for j in range(len(res[i])):
    if res[i][j]==0:cum2[i].append(0)
    else:cum2[i].extend([res[i][j]]*res[i][j])

ans=0
for i in range(H):
  for j in range(W):
    tmp = cum[i][j]+cum2[j][i]-1
    if tmp > ans:ans=tmp

print(ans)