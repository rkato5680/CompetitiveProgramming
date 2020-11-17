# problem: https://atcoder.jp/contests/abc136/tasks/abc136_d
# code: https://atcoder.jp/contests/abc136/submissions/15362985

S=input()
total = []
count=[0,0,0]
mode='R'
for i in range(len(S)):
  if mode=='R' and S[i]=='R':
    count[1] += 1
  elif mode=='R' and S[i]=='L':
    count[0] += 1
    mode='L'
    count[2] = i-1
  elif mode=='L' and S[i]=='L':
    count[0] += 1
  elif mode=='L' and S[i]=='R':
    total.append(tuple(count))
    count = [0,1,0]
    mode = 'R'
total.append(tuple(count))

ans = [0]*len(S)
for l,r,idx in total:
  r1=(r+1)//2
  r2 = r - r1
  l1=(l+1)//2
  l2 = l - l1
  ans[idx] += r1 + l2
  ans[idx+1] += r2 + l1

print(*ans)