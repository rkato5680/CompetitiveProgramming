# problem: https://atcoder.jp/contests/abc181/tasks/abc181_d
# code: https://atcoder.jp/contests/abc181/submissions/17793164

from collections import Counter

S=input()
c = Counter(S)

if len(S)==1:
  if int(S)%8==0:
    print("Yes")
  else:
    print("No")
  exit()

if len(S)==2:
  if int(S)%8==0 or int(S[1]+S[0])%8==0:
    print("Yes")
  else:
    print("No")
  exit()
  
for i in range(0,1000,8):
  c_ = Counter(str(i)+'0'*(3-len(str(i))))
  flag=1
  for k in c_.keys():
    if c_[k]>c[k]:
      flag=0
      break
  if flag:
    print("Yes")
    exit()
    
print("No")