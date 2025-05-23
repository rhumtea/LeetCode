class Solution:
    def findValidPair(self, s: str) -> str:
        res = ""
        mp = defaultdict(int)
        for c in s:
            mp[c] += 1
        temp = s[0]
        count = mp[temp]
        for i in range(1, len(s)):
            if temp == s[i] or int(temp) != count or int(s[i]) != mp[s[i]]:
                temp = s[i]
                count = mp[s[i]]
            else:
                return temp + s[i]
        return ""