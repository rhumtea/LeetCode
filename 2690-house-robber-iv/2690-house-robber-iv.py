class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(capability):
            i = k1 = 0
            while i < len(nums):
                if nums[i] <= capability: 
                    k1 += 1
                    i += 2
                else: 
                    i += 1
            return k1 >= k
        
        L, R = 0, max(nums)
        while L <= R:
            mid = L + (R-L)//2
            if check(mid): 
                R = mid - 1
            else:
                L = mid + 1
        return L
                    
        
        


        