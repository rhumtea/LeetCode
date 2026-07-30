class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        even = 0
        for i in range(len(nums1)):
            if nums1[i]%2:
                return True
            else:
                even += 1
        return False if even != len(nums1) else True