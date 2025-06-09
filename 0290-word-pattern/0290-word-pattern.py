class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        mp_p = defaultdict(str)
        mp_s = defaultdict(str)
        for i in range(len(pattern)):
            if pattern[i] in mp_p and mp_p[pattern[i]] != s[i]:
                return False
            mp_p[pattern[i]] = s[i]
            if s[i] in mp_s and mp_s[s[i]] != pattern[i]:
                return False
            mp_s[s[i]] = pattern[i]
        return True
