class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0 
        for i in s: 
            if i == letter:
                count += 1
        return math.floor(count/len(s)*100)