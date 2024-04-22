class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        res = [s[i] for i in range(len(s)) if s[i] in target]
        resDict = Counter(res)
        targetDict = Counter(target)
        minCount = 100
        for i in resDict:
            minCount = min(minCount, resDict[i]//targetDict[i])
        return minCount if len(resDict) == len(targetDict) else 0