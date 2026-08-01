class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ""
        for word in words:
            total = 0
            for c in word:
                index = ord(c) - ord('a')
                t = weights[index]
                total += t
            a = total%26
            b = 25 - a + 97
            res += chr(b)
        return res