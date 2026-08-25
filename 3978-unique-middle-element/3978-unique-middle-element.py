class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid = len(nums) // 2
        mp = defaultdict(int)
        for i in range(len(nums)):
            if i == mid: continue
            mp[nums[i]] += 1
            if nums[mid] in mp: return False
        return True