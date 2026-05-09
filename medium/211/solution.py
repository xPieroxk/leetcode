class Node:
    def __init__(self):
        self.isEnd = False
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def search(i, curr):
            for i in range(i, len(word)):
                c = word[i]
                # wildcard
                if c == '.':
                    for child in curr.children.values():
                        if search(i + 1, child):
                            return True
                    return False
                # normal search
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.isEnd

        return search(0, self.root)