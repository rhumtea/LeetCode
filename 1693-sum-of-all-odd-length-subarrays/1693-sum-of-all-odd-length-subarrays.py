class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for l in range(n):
            cur_sum = 0
            for r in range(l, n):
                cur_sum += arr[r]
                if (r - l + 1) % 2 == 1:
                    res += cur_sum
        return res