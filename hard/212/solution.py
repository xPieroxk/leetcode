class Node:
    def __init__(self):
        self.isEnd = False
        self.children = {}
        self.word = None


class Trie:
    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isEnd = True
        curr.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.addWord(w)

        n = len(board)
        m = len(board[0])
        ans = []

        def dfs(i, j, node):
            if node.isEnd:
                ans.append(node.word)
                node.isEnd = False

            if (i < 0 or i >= n or j < 0 or j >= m or
                    board[i][j] == '#' or board[i][j] not in node.children):
                return

            parent = node
            node = parent.children[board[i][j]]
            tmp = board[i][j]
            board[i][j] = '#'

            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(i + di, j + dj, node)

            board[i][j] = tmp
            # pruning, not necessary
            if not node.children:
                del parent.children[tmp]

        for i in range(n):
            for j in range(m):
                dfs(i, j, trie.root)

        return ans


