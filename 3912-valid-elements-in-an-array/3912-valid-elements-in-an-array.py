class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [0] * n
        res = []
        high = 0
        for i in range(n):
            if nums[i] > high:
                ans[i] = nums[i]
                high = nums[i]
        high = nums[n-1] - 1
        for i in range(n-1,0,-1):
            if nums[i] != 0 and nums[i] > high:
                ans[i] = nums[i]
                high = nums[i]
        for i in range(n):
            print(res)
            if ans[i] != 0:
                res.append(nums[i])
        return res