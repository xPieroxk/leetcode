from collections import deque


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        ans = 0
        visited = set()

        for i in range(n):
            if i in visited:
                continue
            d = deque([i])
            ans += 1

            while d:
                edge = d.popleft()
                for nei in graph[edge]:
                    if nei not in visited:
                        d.append(nei)
                        visited.add(nei)

        return ans