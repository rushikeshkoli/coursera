#Uses python3

import sys

def dfs(adj, i, vis):
    vis[i] = True
    for vertex in adj[i]:
        if vis[vertex] == False:
            dfs(adj, vertex, vis)


def number_of_components(adj, n):
    result = 0
    #write your code here
    vis = [False] * n
    for i in range(n):
        if vis[i] == False:
            dfs(adj, i, vis)
            result += 1
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj, n))
