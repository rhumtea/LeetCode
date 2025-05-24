class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        count_1 = count_0 = 0
        for num in nums:
            if num%2:
                count_1 += 1
            else:
                count_0 += 1
        return [0] * count_0 + [1] * count_1