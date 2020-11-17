# problem: https://atcoder.jp/contests/abc183/tasks/abc183_d
# code: https://atcoder.jp/contests/abc183/submissions/18131704

N,W=map(int,input().split())
T = [0]*(2*10**5+5)

for i in range(N):
  s,t,p = map(int,input().split())
  T[s] += p
  T[t] += -p
  
cum = [0]
for i in range(len(T)):
  cum.append(cum[-1]+T[i])
  
for i in range(len(cum)):
  if cum[i] > W:
    print("No")
    exit()
    
print("Yes")