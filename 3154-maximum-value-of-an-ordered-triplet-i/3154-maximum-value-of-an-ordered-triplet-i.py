class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = diff = prefix = 0 
        for i in nums: 
            res = max(res, i * diff)
            diff = max(diff, prefix - i)
            prefix = max(prefix, i)
        return res
                
