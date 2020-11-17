# problem: https://atcoder.jp/contests/abc110/tasks/abc110_c
# code: https://atcoder.jp/contests/abc110/submissions/15551422

S=input()
T=input()

d = {}
d2 = {}
for i in range(len(S)):
  if not d.get(S[i]):
    d[S[i]] = T[i]
  elif d[S[i]] != T[i]:
    print('No')
    exit()
  if not d2.get(T[i]):
    d2[T[i]] = S[i]
  elif d2[T[i]] != S[i]:
    print('No')
    exit()

print('Yes')