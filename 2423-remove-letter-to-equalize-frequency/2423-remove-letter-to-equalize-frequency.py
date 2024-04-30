class Solution:
    def equalFrequency(self, word: str) -> bool:
        thisdict = Counter(word)
        for i in word:
            thisdict[i] -= 1
            if thisdict[i] == 0:
                thisdict.pop(i)
            if len(set(thisdict.values())) == 1: 
                return True
            thisdict[i] += 1
        return False
