class Solution:
    def minimumPushes(self, word: str) -> int:
        jump = len(word) // 8
        res = 0
        for i in range(1, jump + 1):
            res += 8*i
        return res + len(word) % 8 * (jump + 1) 