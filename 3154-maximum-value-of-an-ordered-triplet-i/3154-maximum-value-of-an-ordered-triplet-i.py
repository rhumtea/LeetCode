class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = diff = maxNum = 0 
        for i in nums: 
            res = max(res, i * diff)
            diff = max(diff, maxNum - i) # keep track max diff
            maxNum = max(maxNum, i) # store max number from start to current
        return res
                
