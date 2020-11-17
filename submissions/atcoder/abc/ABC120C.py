# problem: https://atcoder.jp/contests/abc120/tasks/abc120_c
# code: https://atcoder.jp/contests/abc120/submissions/15492212

S=list(map(int, list(input())))

num1 = sum(S)
num0 = len(S) - num1

print(min(num1,num0)*2)