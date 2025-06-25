class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        for i in range(1, len(heights)):
            temp = heights[i] - heights[i-1]
            if temp > 0:
                heappush(pq, temp)
                if ladders > 0:
                    ladders -= 1
                else:
                    t = heappop(pq)
                    bricks -= t
                    if bricks < 0:
                        return i - 1
        return len(heights) - 1