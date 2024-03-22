class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(a, b):
            return (a == b[0:len(a)] and a == b[-(len(a)):])
        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        return count
        
            