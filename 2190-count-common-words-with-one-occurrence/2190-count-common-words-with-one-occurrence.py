class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        res = 0
        mp1 = defaultdict(int)
        mp2 = defaultdict(int)
        for word in words1:
            mp1[word] += 1
        for word in words2:
            mp2[word] += 1
        for k, v in mp1.items():
            if v == 1 and mp2[k] == 1:
                res += 1
        return res