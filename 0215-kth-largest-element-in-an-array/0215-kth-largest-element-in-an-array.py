class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heappush(pq, -num)
        res = count = 0
        while pq:
            if count == k:
                break
            res = heappop(pq)
            res = -res
            count += 1
        return res