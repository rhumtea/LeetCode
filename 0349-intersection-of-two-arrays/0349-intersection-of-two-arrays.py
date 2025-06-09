class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        mp = defaultdict(int)
        for num in nums1:
            mp[num] += 1
        for num in nums2:
            if num in mp:
                res.add(num)
        return list(res)