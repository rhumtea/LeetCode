class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for i, v in enumerate(arr):
            l, r = i, n - i - 1
            odd_l, odd_r = l // 2 + 1, r // 2 + 1
            even_l, even_r = (l + 1) // 2, (r + 1) // 2
            res += v * odd_l * odd_r
            res += v * even_l * even_r
        return res