# problem: https://atcoder.jp/contests/abc176/tasks/abc176_e
# code: https://atcoder.jp/contests/abc176/submissions/16156908

from collections import defaultdict

H,W,M=map(int,input().split())
hw = defaultdict(int)
sum1=[0]*H
sum2=[0]*W
for i in range(M):
  h,w=map(int,input().split())
  hw[(h-1,w-1)] += 1
  sum1[h-1] += 1
  sum2[w-1] += 1

sum1 = sorted(enumerate(sum1),key=lambda x:x[1],reverse=True)
sum2 = sorted(enumerate(sum2),key=lambda x:x[1],reverse=True)

max1,max2=set([sum1[0][0]]),set([sum2[0][0]])
for i in range(1,H):
  if sum1[i][1]<sum1[0][1]:
    break
  else:
    max1.add(sum1[i][0])
    
for i in range(1,W):
  if sum2[i][1]<sum2[0][1]:
    break
  else:
    max2.add(sum2[i][0])

ans = sum1[0][1]+sum2[0][1]
count=0
for k in hw.keys():
  h,w=k
  if h in max1 and w in max2:
    count += 1
    
if count < len(max1)*len(max2):
  print(ans)
else:
  print(ans-1)