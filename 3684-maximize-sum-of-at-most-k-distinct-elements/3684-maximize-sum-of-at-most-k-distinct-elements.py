class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums.sort(reverse=True)
        ans = set()
        for num in nums:
            if k > 0 and num not in ans:
                ans.add(num)
                k -= 1
        res = list(ans)
        res.sort(reverse=True)
        return res