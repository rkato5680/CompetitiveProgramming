# problem: https://atcoder.jp/contests/abc158/tasks/abc158_d
# code: https://atcoder.jp/contests/abc158/submissions/15129769

S=input()
Q=int(input())
rev = 0
front, back=[],[]
for i in range(Q):
  q = input()
  if len(q)==1:rev = 1- rev
  else:
    n,f,c=q.split()
    if f=='1' and rev==0:
      front.append(c)
    elif f=='2' and rev==1:
      front.append(c)
    elif f=='1' and rev==1:
      back.append(c)
    elif f=='2' and rev == 0:
      back.append(c)

if rev==0:
  S = ''.join(front[::-1]) + S + ''.join(back)
else:
  S = ''.join(back[::-1]) + S[::-1] + ''.join(front)
print(S)