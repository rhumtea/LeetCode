class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        pq = []
        for key, v in mp.items():
            heappush(pq,[-v, key])
        res = []
        count = 0
        while pq:
            if count == k: 
                break
            v, key = heappop(pq)
            res.append(key)
            count += 1
        return res