class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visit = set()
        count = 0

        def dfs(node):

            if node in visit:
                return

            visit.add(node)

            for nei in graph[node]:
                dfs(nei)

        for node in range(n):

            if node not in visit:
                dfs(node)
                count += 1

        return count