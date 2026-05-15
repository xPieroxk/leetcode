# single bfs
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        n = len(beginWord)
        ans = 1
        d = deque([beginWord])
        wordSet = set(wordList)
        while d:
            for _ in range(len(d)):
                word = d.popleft()
                if word == endWord:
                    return ans

                for i in range(n):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nei = word[:i] + c + word[i + 1:]
                        if nei in wordSet:
                            d.append(nei)
                            wordSet.remove(nei)
            ans += 1

        return 0

# double bfs
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        beginSet, endSet, wordSet = {beginWord}, {endWord}, set(wordList)
        n, ans = len(beginWord), 1
        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
            nextSet = set()

            for word in beginSet:
                for i in range(n):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        nei = word[:i] + c + word[i + 1 :]
                        if nei in endSet:
                            return ans + 1
                        if nei in wordSet:
                            nextSet.add(nei)
                            wordSet.remove(nei)
            beginSet = nextSet
            ans += 1

        return 0
