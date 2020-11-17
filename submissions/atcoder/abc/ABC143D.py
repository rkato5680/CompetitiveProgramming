# problem: https://atcoder.jp/contests/abc143/tasks/abc143_d
# code: https://atcoder.jp/contests/abc143/submissions/15330749

N=int(input())
L=list(map(int,input().split()))
L = sorted(L)

def binary_search(func, array, left=0):
    right=len(array)-1
    y_left, y_right = func(array[left]), func(array[right])
    if y_left==False:return 0
    while True:
        middle = (left+right)//2
        y_middle = func(array[middle])
        if y_left==y_middle: left=middle
        else: right=middle
        if right-left==1:break

    return left

SUM = 0
for i in range(N-2):
  for j in range(i+1,N-1):
    l = L[i]+L[j]
    if L[-1]<l:
      k = N-1
    else:
      k = binary_search(lambda x: x<l, L, j+1)
    SUM += max(0,k-j)

print(SUM)