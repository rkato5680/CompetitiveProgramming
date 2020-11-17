# problem: https://atcoder.jp/contests/abc180/tasks/abc180_d
# code: https://atcoder.jp/contests/abc180/submissions/17462660

X,Y,A,B=map(int,input().split())

ans = 0
while X < Y:
  if X+B > X*A and X*A<Y:
    ans += 1
    X *= A
  else:
    ans += (Y-X-1)//B
    break
    
print(ans)