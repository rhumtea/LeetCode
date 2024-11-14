class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            countBit, temp = 0, i
            while(temp):
                countBit += temp & 1
                temp >>= 1
            if countBit == k: res += nums[i]
        return res
