class Solution:
    def similarPairs(self, words: List[str]) -> int:
        thisdict ={}
        for word in words:
            temp = sorted(set(word))
            temp = ''.join(temp)
            if temp not in thisdict:
                thisdict[temp] = 1
            else:
                thisdict[temp] += 1
        res = 0
        for i in thisdict.values():
            res += (i*(i-1)//2)
        return res