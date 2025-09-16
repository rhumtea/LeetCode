class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visit = set()
        def dfs(cur):
            visit.add(cur)
            for ne in rooms[cur]:
                if ne not in visit:
                    dfs(ne)
        dfs(0)
        return len(visit) == n