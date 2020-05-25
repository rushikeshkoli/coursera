#Uses python3

import sys


def negative_cycle(adj, cost):
    #write your code here
    dist = [10**4] * len(adj)
    dist[0] = 0
    flag = True
    for k in range(len(adj) - 1):
        for i in range(len(adj)):
            for j in range(len(adj[i])):
                if dist[adj[i][j]] > dist[i] + cost[i][j]:
                    dist[adj[i][j]] = dist[i] + cost[i][j]
                    flag = False
        if flag == True:
            return 0
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            if dist[adj[i][j]] > dist[i] + cost[i][j]:
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
