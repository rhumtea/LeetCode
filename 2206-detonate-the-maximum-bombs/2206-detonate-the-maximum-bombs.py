class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(bombs)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                d = sqrt((bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2)
                if d <= bombs[i][2]:
                    adj[i].append(j)
        res = 0
        for i in range(n):
            cnt = 0
            q = deque([i])
            visit = {i}
            while q:
                cur = q.popleft()
                cnt += 1
                for ne in adj[cur]:
                    if ne not in visit:
                        q.append(ne)
                        visit.add(ne)
            res = max(res, cnt)
        return res