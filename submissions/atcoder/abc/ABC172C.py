# problem: https://atcoder.jp/contests/abc172/tasks/abc172_c
# code: https://atcoder.jp/contests/abc172/submissions/16174436

N,M,K=map(int,input().split())
*A,=map(int,input().split())
*B,=map(int,input().split())

def binary_search(func, array, left=0, right=-1):
    if right==-1:right=len(array)-1
    y_left, y_right = func(array[left]), func(array[right])
    while True:
        middle = (left+right)//2
        y_middle = func(array[middle])
        if y_left==y_middle: left=middle
        else: right=middle
        if right-left==1:break

    return left

cumA = [0]
for i in range(N):
  cumA.append(cumA[-1]+A[i])
  
cumB = [0]
for i in range(M):
  cumB.append(cumB[-1]+B[i])
cumB.append(10**20)
  
if cumA[-1]+cumB[-1]<=K:
  print(N+M)
  exit()
  
if A[0] > K and B[0] > K:
  print(0)
  exit()
  
ans = 0
for i in range(N+1):
  if K-cumA[i]<0:break
  idx = binary_search(lambda x:x<=K-cumA[i],cumB)
  res = max(0,i+idx)
  ans = max(ans, res)
  
print(ans)