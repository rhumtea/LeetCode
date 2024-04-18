class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while start or goal:
            if start%2 != goal%2:
                count += 1
            start //= 2
            goal //= 2
        # xor_num = start ^ goal
        # while xor_num:
        #     xor_num &= xor_num - 1
        #     count += 1
        return count