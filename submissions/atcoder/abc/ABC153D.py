# problem: https://atcoder.jp/contests/abc153/tasks/abc153_d
# code: https://atcoder.jp/contests/abc153/submissions/15214315

H=int(input())

def n_attack(h):
  if h==1:return(1)
  else:return 1+2*n_attack(h//2)

print(n_attack(H))