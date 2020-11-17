# problem: https://atcoder.jp/contests/abc152/tasks/abc152_d
# code: https://atcoder.jp/contests/abc152/submissions/15216962

from collections import defaultdict
strN=input()
lenN=len(strN)
N=int(strN)

if N<=9:print(N)
else:
  count = defaultdict(int)
  for i in range(10,N+1):
    a,b=int(str(i)[0]),int(str(i)[-1])
    if b==0:continue
    count[(a,b)] += 1

  ans=0
  for i in range(1,10):
    count[(i,i)] += 1
  count = dict(count)
  for key in count.keys():
    if key[0]<key[1] and count.get((key[1],key[0])):
      ans += count[key] * count[(key[1],key[0])] * 2
    if key[0]==key[1]:
      ans += count[key]**2
  print(ans)