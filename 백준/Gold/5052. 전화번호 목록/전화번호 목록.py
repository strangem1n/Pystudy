import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
            if node.is_end:
                return True
        node.is_end = True
        return False

t = int(input())
for tc in range(t):
    tri = Trie()
    n = int(input())
    phone = list(input().rstrip() for _ in range(n))
    phone.sort(key=lambda x: (len(x), x))
    for p in phone:
        if tri.insert(p):
            print('NO')
            break
    else:
        print('YES')
