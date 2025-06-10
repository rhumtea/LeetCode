class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp1 = defaultdict(int)
        mp2 = defaultdict(int)
        res = []
        for num in nums1:
            mp1[num] += 1
        for num in nums2:
            mp2[num] += 1
        for k, v in mp1.items():
            if k in mp2:
                res += [k] * min(v, mp2[k])
        return res