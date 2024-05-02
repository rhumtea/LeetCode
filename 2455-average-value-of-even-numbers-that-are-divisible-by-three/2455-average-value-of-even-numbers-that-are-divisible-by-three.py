class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res, count = 0, 0
        for i in nums:
            if i%6 == 0: 
                res += i
                count += 1
        return res//count if count != 0 else 0