class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        mp = defaultdict(int)
        nums1 = nums2 = 0
        for num in nums:
            mp[num] += 1
        for k,v in mp.items():
            if v > 2:
                return False
            elif v == 1:
                if nums1 < nums2:
                    nums1 += 1
                else:
                    nums2 += 1
        return nums1 == nums2