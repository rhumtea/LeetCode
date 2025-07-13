class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]
        while stack:
            temp = stack.pop()
            for ne in rooms[temp]:
                if not seen[ne]:
                    seen[ne] = True
                    stack.append(ne)
        return all(seen)