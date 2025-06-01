class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = 0
        leftover = 0
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        for v in mp.values():
            count += v//2
            leftover += v%2
        return [count, leftover]