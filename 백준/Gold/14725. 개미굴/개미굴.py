import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, array):
        node = self.root
        for a in array:
            if a not in node.children:
                node.children[a] = Node()
            node = node.children[a]
        node.is_end = True

    def find(self, array, depth):
        if depth == 0:
            node = self.root
            array = node.children

        line = '-' * depth * 2
        for next_node in sorted(array):
            print(f'{line}{next_node}')
            self.find(array[next_node].children, depth+1)

tri = Trie()
n = int(input())
for _ in range(n):
    dep, *info = input().split()
    tri.insert(info)
tri.find(None, 0)
