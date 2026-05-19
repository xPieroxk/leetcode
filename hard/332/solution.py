from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = defaultdict(list)
        for a, b in tickets:
            graph[a].append(b)

        ans = ['JFK']

        def dfs(src):
            if len(ans) == len(tickets) + 1: return True
            if not graph[src]: return False

            tmp = list(graph[src])
            for i, v in enumerate(tmp):
                ans.append(v)
                graph[src].pop(i)
                if dfs(v): return True
                ans.pop()
                graph[src].insert(i, v)

        dfs('JFK')
        return ans

# Eulerian path
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        graph = defaultdict(list)
        for a, b in tickets[::-1]:
            graph[a].append(b)
        ans = []
        stack = ['JFK']

        while stack:
            curr = stack[-1]

            if graph[curr]:
                stack.append(graph[curr].pop())
            else:
                ans.append(stack.pop())

        return ans[::-1]