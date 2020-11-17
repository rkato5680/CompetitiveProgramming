# problem: https://atcoder.jp/contests/abc101/tasks/arc099_a
# code: https://atcoder.jp/contests/abc101/submissions/16216627

N,K=map(int,input().split())
*A,=map(int,input().split())

argmin = A.index(1)

back = (argmin+(K-1)-1)//(K-1)
forward = (N-argmin-1+(K-1)-1)//(K-1)
ans1 = back+forward

ans2 = ((N-1)+(K-1)-1)//(K-1)

print(min(ans1,ans2))