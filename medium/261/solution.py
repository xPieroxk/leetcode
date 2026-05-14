from collections import defaultdict


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set()

        def hasCycle(parent, node):
            visited.add(node)

            for nei in graph[node]:
                if nei == parent: continue
                if nei in visited: return True
                if hasCycle(node, nei): return True
            return False

        return not hasCycle(-1, 0) and len(visited) == n

