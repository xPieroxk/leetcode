class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = {}
        for e1, e2 in prerequisites:
            edges.setdefault(e1, []).append(e2)

        visiting = set()
        visited = set()

        def dfs(e):
            if e in visiting: return True
            if e in visited: return False

            visiting.add(e)
            if e in edges:
                for nei in edges[e]:
                    if dfs(nei):
                        return True
            visiting.remove(e)
            visited.add(e)
            return False

        for edge in edges.keys():
            if dfs(edge):
                return False

        return True