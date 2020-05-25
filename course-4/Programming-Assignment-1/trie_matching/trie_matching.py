# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4

def build_trie(patterns):
	tree = []
	temp = {'A': 1, 'C': 2, 'G':3, 'T': 0}
	j = 1
	tree.append(Node())
	for pattern in patterns:
		currNode = 0
		for i in range(len(pattern)):
			currSymbol = pattern[i]
			# print(currSymbol)
			if tree[currNode].next[temp[currSymbol]] != NA:
				currNode = tree[currNode].next[temp[currSymbol]]
			else:
				tree[currNode].next[temp[currSymbol]] = j
				currNode = j
				tree.append(Node())
				j += 1
	return tree

def is_leaf(v):
	for i in range(4):
		if v.next[i] != NA:
			return False
	return True


def pref_trie_match(text, tree):
	symbol = text[0]
	temp = {'A': 1, 'C': 2, 'G':3, 'T': 0}
	v = tree[0]
	i = 0
	while True:
		if is_leaf(v):
			return True
		elif v.next[temp[symbol]] != NA:
			i += 1
			v = tree[v.next[temp[symbol]]]
			if i == len(text):
				return is_leaf(v)
			symbol = text[i]
		else:
			return False


def solve (text, n, patterns):
	tree = build_trie(patterns)
	#  write your code here
	result = []
	i = 0
	j = len(text)
	while i < j:
		if pref_trie_match(text[i:], tree) == True:
			result.append(i)
		# print(text)
		i += 1

	return result


text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
