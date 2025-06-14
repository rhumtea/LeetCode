class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(mid):
            i = count = 0
            while i < len(nums):
                if nums[i] <= mid:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= k
        l, r = 0, 10**9
        while l <= r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid - 1
            else:    
                l = mid + 1
        return l