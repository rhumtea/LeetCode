class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        temp = ""
        for c in paragraph:
            temp += c.lower() if c.isalpha() else ' '
        temp = ''.join(temp).split()

        mp_banned = defaultdict(int)
        for s in banned:
            mp_banned[s] += 1
        res = ""
        max_freq = 0
        mp = defaultdict(int)
        for t in temp:
            mp[t] += 1
            if t not in mp_banned and mp[t] > max_freq:
                res = t
                max_freq = mp[t]
        return res