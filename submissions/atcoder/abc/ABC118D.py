# problem: https://atcoder.jp/contests/abc118/tasks/abc118_d
# code: https://atcoder.jp/contests/abc118/submissions/15503458

N,M=map(int,input().split())
A=list(map(int,input().split()))

if N % 2 == 0:
  if 1 in A:
    print(int('1'*(N//2)))
    exit()

need =(2,5,5,4,5,6,3,7,6)

if 2 in A and 3 in A:
  del A[A.index(2)]
if 3 in A and 5 in A:
  del A[A.index(3)]
if 6 in A and 9 in A:
  del A[A.index(6)]
if 1 in A and 4 in A:
  del A[A.index(4)]
if 6 in A and 7 in A:
  del A[A.index(6)] 
if 7 in A and 9 in A:
  del A[A.index(9)] 
if 1 in A and 6 in A:
  del A[A.index(6)] 
if 1 in A and 9 in A:
  del A[A.index(9)] 
  
A = tuple(A)
M = len(A)

dp = [[0]*(N+1) for _ in range(M)]
dpmax = [0]*(N+1)

def take_max():
  return max(A[i]*(10**len(str(tmp2)) + tmp2,tmp2*10+A[i]))

for j in range(2,N+1):
  tmpmax = 0
  for i in range(M):
    tmp = need[A[i]-1]
    if j == tmp:
      dp[i][j] = A[i]
    elif j > tmp:
      if dpmax[j-tmp] != 0:
        tmp2 = dpmax[j-tmp]
        dp[i][j] = take_max()
    if tmpmax < dp[i][j]:
      tmpmax = dp[i][j]
  dpmax[j] = tmpmax
  
print(dpmax[-1])