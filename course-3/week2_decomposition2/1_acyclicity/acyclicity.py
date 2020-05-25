#Uses python3

import sys

def dfs(adj, i, vis, preV):
    vis[i] = True
    preV[i] = True
    for vertex in adj[i]:
        if vis[vertex] == False and dfs(adj, vertex, vis, preV):
            return True
        elif preV[vertex] == True:
            return True
    preV[i] = False
    return False


def acyclic(adj):
    vis = [False] * len(adj)
    preV = [False] * len(adj) 
    val = 0
    for i in range(len(adj)):
        if vis[i] == False:
            if dfs(adj, i, vis, preV) == True:
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
