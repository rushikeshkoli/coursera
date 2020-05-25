#Uses python3
import sys
import math
import queue

def minimum_distance(x, y):
    # print(x[0])
    # print(y[0])
    result = 0.
    cost = [10**4] * len(x)
    cost[0] = 0
    vis = [False] * len(x)
    que = queue.PriorityQueue()
    que.put((cost[0], 0))
    while que.empty() == False:
        u = que.get()
        dis = u[0]
        vertex = u[1]
        if vis[vertex] == True:
            pass
        vis[vertex] = True
        for i in range(len(x)):
            val = math.sqrt((x[vertex] - x[i])**2 + (y[vertex] - y[i])**2)
            if vis[i] == False and cost[i] > val:
                cost[i] = val
                que.put((cost[i], i))

    #write your code here
    for i in range(len(x)):
        result += cost[i]
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
