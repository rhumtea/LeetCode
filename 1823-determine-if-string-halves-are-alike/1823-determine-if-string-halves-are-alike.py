class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')
        n = len(s)//2
        count = 0
        for c in s[:n]:
            if c in vowel:
                count += 1
        for c in s[n:]:
            if c in vowel:
                count -= 1
        return count == 0