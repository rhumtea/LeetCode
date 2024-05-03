class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        res = sentence.split()
        if res[0][0] != res[-1][-1]: return False
        for i in range(len(res)-1):
            if res[i][-1] != res[i+1][0]: return False
        return True