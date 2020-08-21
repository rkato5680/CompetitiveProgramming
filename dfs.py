# generate sequences in which each entry is not greater than the given array a i.e. generate sequence b s.t. b_i <= a_i for all i

def dfs(h=[]):
    if len(h)==len(a):
        print(h) #あるいは特定の処理
        return
    for i in range(a[len(h)]+1):
        h.append(i)
        dfs(h)
        h.pop()
    return
    
    
    
# DFS on grid
# compute distance from starting point ('s') to arbitrary movable point ('.')
# e.g. S=['##....#', '....###']. '.': movable, '#':wall

def dfs(s):
  if seen[s[0]][s[1]] == 0:
    seen[s[0]][s[1]] = 1
  for d in [(1,0),(-1,0),(0,1),(0,-1)]:
    new = (s[0]+d[0], s[1]+d[1])
    if new[0]<0 or new[0]>=H:continue
    if new[1]<0 or new[1]>=W:continue
    if seen[new[0]][new[1]]==1:continue
    if S[new[0]][new[1]]=='#':continue
    dfs(new)



# DFS on tree or Graph
# seen = [0]*(N+1)
# G = [[] for _ in range(N)]

def dfs(v):
    seen[v] = 1
    #print(v) #code here (preorder)
    for next_v in G[v]:
        if seen[next_v]:continue
        dfs(next_v)
    
    #print(v) #code here (postorder)
