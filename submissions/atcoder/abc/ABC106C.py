# problem: https://atcoder.jp/contests/abc106/tasks/abc106_c
# code: https://atcoder.jp/contests/abc106/submissions/15559113

S=input()
K=int(input())

for i in range(K):
  if S[i]!='1':
    print(S[i])
    exit()
print(S[K-1])