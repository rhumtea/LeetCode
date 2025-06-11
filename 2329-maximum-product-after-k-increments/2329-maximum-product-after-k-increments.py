class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heappush(pq, num)
        for i in range(k):
            heappush(pq, heappop(pq) + 1)
        res = 1
        mod = 10**9 + 7
        for num in pq:
            res = (res * num) % mod
        return res