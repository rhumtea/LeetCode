class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visit = set()
        def dfs(u):
            if u in visit:
                return
            visit.add(u)
            for v in rooms[u]:
                dfs(v)
        dfs(0)
        return len(visit) == n