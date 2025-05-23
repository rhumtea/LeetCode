class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        mp = defaultdict(int)
        for i in range(len(word1)):
            mp[word1[i]] += 1
            mp[word2[i]] -= 1
        for v in mp.values():
            if v > 3 or v < -3:
                return False
        return True