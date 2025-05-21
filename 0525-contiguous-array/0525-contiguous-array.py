class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        def prefix_diff(nums):
            prefix_diff = [0] * len(nums)
            num0 = num1 = 0
            prefix_diff[0] = -1 if nums[0] == 0 else 1
            for i in range(1, len(nums)):
                temp = -1 if nums[i] == 0 else 1
                prefix_diff[i] = prefix_diff[i-1] + temp
            return prefix_diff
        res = 0
        prefix_diff = prefix_diff(nums)
        mp = defaultdict(int)
        mp[0] = -1
        for r in range(len(prefix_diff)):
            if prefix_diff[r] in mp:
                res = max(res, r - mp[prefix_diff[r]])
            else:
                mp[prefix_diff[r]] = r
        return res