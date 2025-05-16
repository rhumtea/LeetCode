class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {'M' : 1000,
                'D' : 500,
                'C' : 100,
                'L' : 50,
                'X' : 10,
                'V' : 5,
                'I' : 1
                }
        
        res = 0
        i = 0
        while i < len(s)-1:
            if mp[s[i]] < mp[s[i+1]]:
                res = res - mp[s[i]]
            else:
                res += mp[s[i]]
            i += 1
        return res + mp[s[len(s)-1]]
