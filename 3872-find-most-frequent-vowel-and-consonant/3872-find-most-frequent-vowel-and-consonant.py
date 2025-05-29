class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = ('a', 'e', 'i', 'o', 'u')
        mp = defaultdict(int)
        max_vowel = max_consonant = 0
        for c in s:
            mp[c] += 1
            if c in vowel:
                max_vowel = max(max_vowel, mp[c])
            else:
                max_consonant = max(max_consonant, mp[c])
        return max_vowel + max_consonant