class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid = len(nums) // 2
        mp = defaultdict(int)
        for i in range(len(nums)):
            mp[nums[i]] += 1
        return True if mp[nums[mid]] == 1 else False