class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        mp = defaultdict(int)
        nums1 = nums2 = 0
        for num in nums:
            mp[num] += 1
        for v in mp.values():
            if v > 2:
                return False
        return True