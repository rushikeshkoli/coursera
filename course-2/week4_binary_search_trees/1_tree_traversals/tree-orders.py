# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.inO(0)        
    return self.result


  def inO(self, root):
    if root == -1:
      return
    self.inO(self.left[root])
    self.result.append(self.key[root])
    self.inO(self.right[root])


  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.preO(0)     
    return self.result

  def preO(self, root):
    if root == -1:
      return
    self.result.append(self.key[root])
    self.preO(self.left[root])
    self.preO(self.right[root])

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.posO(0)   
    return self.result

  def posO(self, root):
    if root == -1:
      return
    self.posO(self.left[root])
    self.posO(self.right[root])
    self.result.append(self.key[root])

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
