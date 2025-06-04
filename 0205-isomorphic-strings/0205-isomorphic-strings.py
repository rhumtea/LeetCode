class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mp_s = defaultdict(str)
        mp_t = defaultdict(str)
        for i in range(len(s)):
            if s[i] not in mp_s and t[i] not in mp_t:
                mp_s[s[i]] = t[i]
                mp_t[t[i]] = s[i]
            elif mp_s[s[i]] != t[i] or mp_t[t[i]] != s[i]:
                return False
        return True