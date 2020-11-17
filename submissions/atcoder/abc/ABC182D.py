# problem: https://atcoder.jp/contests/abc182/tasks/abc182_d
# code: https://atcoder.jp/contests/abc182/submissions/17965298

N=int(input())
*A,=map(int,input().split())

cum = [0]
for i in range(N):
  cum.append(cum[-1]+A[i])
  
cummax = [0]*N
MAX=0
for i in range(N):
  MAX = max(MAX,cum[i+1])
  cummax[i] = MAX
  
ans = 0
pos = 0
for i in range(N):
  ans = max(ans,pos+cummax[i])
  pos += cum[i+1]
  ans = max(ans,pos)
  
print(ans)