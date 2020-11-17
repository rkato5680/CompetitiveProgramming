# problem: https://atcoder.jp/contests/abc162/tasks/abc162_d
# code: https://atcoder.jp/contests/abc162/submissions/16019012

from collections import Counter

N=int(input())
S=input()

c=Counter(S+'RGB')
ans = (c['R']-1)*(c['G']-1)*(c['B']-1)

max_d = (N-3)//2+1

for d in range(1,max_d+1):
  for i in range(N-2):
    j = i+d
    k = j+d
    if k > N-1:break
    if len(set([S[i],S[j],S[k]]))==3:
      ans -= 1
      
print(ans)