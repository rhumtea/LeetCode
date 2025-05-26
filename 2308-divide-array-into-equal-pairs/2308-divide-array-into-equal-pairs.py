class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        for v in mp.values():
            if v % 2:
                return False
        return True