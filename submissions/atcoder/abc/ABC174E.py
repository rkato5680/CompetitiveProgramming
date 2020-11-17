# problem: https://atcoder.jp/contests/abc174/tasks/abc174_e
# code: https://atcoder.jp/contests/abc174/submissions/16213315

N,K=map(int,input().split())
*A,=map(int,input().split())

def C(x):
  return sum([(A[i]+x-1)//x-1 for i in range(N)]) <= K
  
def binary_search2(func, n_min, n_max):
    left,right=n_min,n_max
    while right-left>1:
        middle = (left+right)//2
        y_middle = func(middle)
        if y_middle: right=middle
        else: left=middle

    return right
  
print(binary_search2(C, 0, max(A)+1))