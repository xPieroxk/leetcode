from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        ans = []
        visited = set()
        visiting = set()

        def hasCycle(edge):
            if edge in visited: return False
            if edge in visiting: return True

            visiting.add(edge)
            for e in graph[edge]:
                if hasCycle(e):
                    return True
            ans.append(edge)
            visiting.remove(edge)
            visited.add(edge)
            return False

        for i in range(numCourses):
            if hasCycle(i):
                return []

        return ans