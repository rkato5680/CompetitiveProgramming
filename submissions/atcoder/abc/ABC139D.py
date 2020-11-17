# problem: https://atcoder.jp/contests/abc139/tasks/abc139_d
# code: https://atcoder.jp/contests/abc139/submissions/15347539

N=int(input())
if N==1:print(0)
else:print((1+(N-1))*(N-1)//2)