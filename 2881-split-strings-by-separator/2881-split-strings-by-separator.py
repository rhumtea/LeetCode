class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for word in words:
            word = word.split(separator)
            for i in word:
                if i:
                    ans.append(i)
        return ans