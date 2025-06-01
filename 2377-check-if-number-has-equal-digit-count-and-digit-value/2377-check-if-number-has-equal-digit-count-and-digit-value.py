class Solution:
    def digitCount(self, num: str) -> bool:
        mp = defaultdict(int)
        for c in num:
            mp[int(c)] += 1
        for i in range(len(num)):
            if int(num[i]) != mp[i]:
                return False
        return True