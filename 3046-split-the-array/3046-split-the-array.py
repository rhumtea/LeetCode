class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        thisdict = Counter(nums)
        for i in thisdict.values():
            if i > 2:
                return False
        return True
         
            
                