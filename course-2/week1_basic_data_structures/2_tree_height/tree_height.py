# python3

import sys
import threading
from collections import deque

class Node:
    def __init__(self, value):
        self.val = value
        self.childs = []

    def addChild(self, child):
        self.childs.append(child)

def cal(arr, i):
    if len(arr[i].childs) == 0:
        return 1
    val = -1
    for j in range(len(arr[i].childs)):
        val = max(val, cal(arr, arr[i].childs[j]))
    return 1 + val

def compute_height(n, parents):
    # Replace this code with a faster implementation
    arr = [Node(i) for i in range(n)]
    # for i in range(n):
    #     arr[i] = Node(i)
    root = -1
    for vertex in range(n):
        current = parents[vertex]
        if current == -1:
            root = vertex
            pass
        else:
            arr[current].addChild(vertex)
    # print(root)
    # for i in range(n):
    #     print(i, end=' ')
    #     print(arr[i].childs)
    return cal(arr, root)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
