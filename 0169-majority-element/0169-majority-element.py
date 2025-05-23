class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        for k, v in mp.items():
            if v > n:
                return k