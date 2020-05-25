#Uses python3

import sys
import queue

# def SiftDown(i, data):
#     maxIndex = i
#     l = 2 * i + 1
#     if l < len(data) and data[l][0] < data[maxIndex][0]:
#         maxIndex = l
#     r = 2 * i + 2
#     if r < len(data) and data[r][0] < data[maxIndex][0]:
#         maxIndex = r
#     if i != maxIndex:
#         # print(i, ' ', maxIndex)
#         data[i], data[maxIndex] = data[maxIndex], data[i]
#         SiftDown(maxIndex, data)


# def SiftUp(i, data):
#     l = i // 2 + i % 2 - 1
#     if l >= 0 and data[l][0] > data[i][0]:
#         data[i], data[l] = data[l], data[i]
#         SiftUp(l, data)


def distance(adj, cost, s, t):
    #write your code here
    dist = [10**4] * (len(adj))
    prev = [-1] * len(adj)
    dist[s] = 0
    vis = [False] * len(adj)
    que = queue.PriorityQueue()
    que.put((dist[s], s))
    while que.empty() == False:
        u = que.get()
        d = u[0]
        vertex = u[1]
        # print(u[1])
        if vis[vertex] == True:
            pass
        vis[vertex] = True
        for i in range(len(adj[vertex])):
            if dist[adj[vertex][i]] > dist[vertex] + cost[vertex][i]:
                dist[adj[vertex][i]] = dist[vertex] + cost[vertex][i]
                prev[adj[vertex][i]] = vertex
                que.put((dist[adj[vertex][i]], adj[vertex][i]))
    if vis[t] == True:
        return dist[t]
    return -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
