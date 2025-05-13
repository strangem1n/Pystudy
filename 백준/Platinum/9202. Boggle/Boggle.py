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
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.is_end

def dfs(i, j, sub_word):
    if tri.search(sub_word):
        found.add(sub_word)

    if len(sub_word) < 8:
        for k in range(8):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < 4 and 0 <= nj < 4 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                dfs(ni, nj, sub_word+board[ni][nj])
                visited[ni][nj] = 0




di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

tri = Trie()
w = int(input())
for _ in range(w):
    tri.insert(input().rstrip())
blank = input()

b = int(input())
for tc in range(b):
    board = [list(input().rstrip()) for _ in range(4)]
    blank = input()

    visited = [[0] * 4 for _ in range(4)]
    found = set()
    for r in range(4):
        for c in range(4):
            visited[r][c] = 1
            dfs(r, c, board[r][c])
            visited[r][c] = 0

    found = sorted(list(found))
    score = 0
    max_length = 0
    max_word = None
    for word in found:
        l = len(word)
        if l == 3:
            score += 1
        elif 3 < l < 7:
            score += l - 3
        elif l == 7:
            score += 5
        elif l == 8:
            score += 11

        if max_length < l:
            max_length = l
            max_word = word

    if max_word is None:
        print(score, len(found))
    else:
        print(score, max_word, len(found))
