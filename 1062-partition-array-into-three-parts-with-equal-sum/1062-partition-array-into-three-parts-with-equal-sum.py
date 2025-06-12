class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        summ = sum(arr)
        if summ%3 != 0:
            return False
        num = summ//3
        prefix_sum = 0
        parts = 0
        for i in range(len(arr)):
            prefix_sum += arr[i]
            if prefix_sum == num:
                parts += 1
                prefix_sum = 0
                if parts == 2 and i < len(arr) - 1:
                    return True
        return False