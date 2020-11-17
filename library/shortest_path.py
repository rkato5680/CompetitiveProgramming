def BellmanFord(G, start = 0, INF=10000):
    d = [INF for i in range(len(G))]
    d[start] = 0
    for i in range(len(G)):
        while True:
            update = False
            for j in range(len(G)):
                for k in G[j].keys():
                    if (d[j] != INF) & (d[k] > d[j] + G[j][k]):
                        d[k] = d[j] + G[j][k]
                        update = True
            
            if not update:
                break
    
    return d



from heapq import heappop, heappush

def dijkstra(start = 0):
    d = [INF for i in range(len(G))]
    d[start] = 0
    que = []
    heappush(que, (0, start))

    while len(que):
        p = heappop(que)
        v = p[1]
        if d[v] < p[0]:
            continue
        for u in G[v].keys():
            if d[u] > d[v] + G[v][u]:
                d[u] = d[v] + G[v][u]
                heappush(que, (d[u], u))
    return d
    
    
def FloydWarshall(G, INF=10**20):
    d = [[INF for i in range(len(G))] for j in range(len(G))]
    for i in range(len(G)):
        d[i][i] = 0
        for j in G[i].keys():
            d[i][j] = G[i][j]

    for k in range(len(G)):
        for i in range(len(G)):
            for j in range(len(G)):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    
    return d
