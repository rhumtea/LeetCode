class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        A = [0] + nums
        max_left = [0] * len(A)
        min_right = [0] * len(A)
        max_left[1] = A[1]
        min_right[n] = A[n]
        for i in range(2, n+1):
            max_left[i] = max(A[i], max_left[i-1])
        for i in range(n-1, 0, -1):
            min_right[i] = min(A[i], min_right[i+1])
        for i in range(1, n+1):
            score = max_left[i] - min_right[i]
            if score <= k:
                return i-1
        return -1