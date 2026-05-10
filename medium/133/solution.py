"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(n):
            if n.val in visited:
                return visited[n.val]

            copy = Node(n.val)
            visited[copy.val] = copy
            for neig in n.neighbors:
                copy.neighbors.append(dfs(neig))

            return copy

        return dfs(node) if node else node
