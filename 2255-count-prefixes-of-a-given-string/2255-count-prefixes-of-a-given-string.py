class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        prefix = [s[:i+1] for i in range(len(s))]
        count = 0
        for i in words:
            if i in prefix:
                count += 1
        return count