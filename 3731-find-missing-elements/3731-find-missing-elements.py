class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a = min(nums)
        b = max(nums)
        c = {}
        res = []
        for num in nums:
            c[num] = 1
        for i in range(a, b+1):
            if i not in c:
                res.append(i)
        return res