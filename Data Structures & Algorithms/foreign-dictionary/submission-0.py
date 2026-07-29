class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        

        graph = {c: [] for word in words for c in word}

        for i in range(len(words) - 1):

            w1 = words[i]
            w2 = words[i + 1]

            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""

            for j in range(min(len(w1), len(w2))):

                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    break

        visit = {}
        res = []

        def dfs(c):

            if c in visit:
                return visit[c]

            visit[c] = True

            for nei in graph[c]:

                if dfs(nei):
                    return True

            visit[c] = False
            res.append(c)

            return False

        for c in graph:

            if dfs(c):
                return ""

        res.reverse()

        return "".join(res)
        