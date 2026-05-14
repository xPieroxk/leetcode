class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        p = [i for i in range(n + 1)]
        rank = [1 for _ in range(n + 1)]

        def find(u):
            if u != p[u]:
                p[u] = find(p[u])
            return p[u]

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv: return False

            if rank[pu] > rank[pv]:
                p[pv] = pu
                rank[pu] += rank[pv]
            else:
                p[pu] = pv
                rank[pv] += rank[pu]

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]