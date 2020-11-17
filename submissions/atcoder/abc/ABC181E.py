# problem: https://atcoder.jp/contests/abc181/tasks/abc181_e
# code: https://atcoder.jp/contests/abc181/submissions/17801882

from bisect import bisect_left

N,M=map(int,input().split())
*H,=map(int,input().split())
*W,=map(int,input().split())

H = sorted(H)

cum1 = [0]
for i in range(N//2):
  cum1.append(cum1[-1]+H[2*i+1]-H[2*i])
  
cum2 = [0]
for i in range(N//2):
  cum2.append(cum2[-1]+H[2*i+2]-H[2*i+1])
  
ans = 10**20
for i in range(M):
  res = 0
  idx = bisect_left(H,W[i])
  if idx%2:
    res += abs(W[i]-H[idx-1])
    res += cum1[(idx-1)//2]
    res += cum2[-1]-cum2[(idx-1)//2]
  else:
    res += abs(W[i]-H[idx])
    res += cum1[idx//2]
    res += cum2[-1]-cum2[idx//2]
  ans = min(ans,res)
  
print(ans)