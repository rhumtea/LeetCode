class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        #s.count(letter)
        #math.floor(int(current[:1]))
        count = 0 
        for i in s: 
            if i == letter:
                count += 1
        return int(count/len(s)*100)