class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def isAnagrams(s1, s2):
            s1, s2 = sorted(s1), sorted(s2)
            return s1 == s2
        i = 1
        while i != len(words):
            if isAnagrams(words[i-1], words[i]):
                words.remove(words[i])
            else:
                i += 1
        return words
        