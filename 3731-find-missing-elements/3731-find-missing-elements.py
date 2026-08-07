class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a, b = min(nums), max(nums)
        c = set(nums)
        res = []
        for i in range(a, b+1):
            if i not in c:
                res.append(i)
        return res