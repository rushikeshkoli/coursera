#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**32)  # new thread will get stack of such size

def IsBinarySearchTree(tree, root = 0, upperB = 2 ** 32, lowerB = -(2 ** 32)):
  # Implement correct algorithm here
  if root == -1:
    return True
  if tree[root][0] > lowerB and tree[root][0] < upperB:
    return IsBinarySearchTree(tree, tree[root][1], tree[root][0], lowerB) and IsBinarySearchTree(tree, tree[root][2], upperB, tree[root][0])
  return False


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  # print(tree[0][0])
  # print(tree[0][1])
  # print(tree[0][2])
  if nodes == 0 or IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
