class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        state = [0] * len(graph)
        def dfs(u):
            if state[u] == 2:
                return True
            if state[u] == 1:
                return False
            state[u] = 1
            for v in graph[u]:
                if dfs(v) == False:
                    return False
            state[u] = 2
            return True
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)
        return res