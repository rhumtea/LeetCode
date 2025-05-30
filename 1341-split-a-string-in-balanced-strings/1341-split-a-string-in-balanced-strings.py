class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        mp = defaultdict(int)
        for c in s:
            mp[c] += 1
            if mp['R'] == mp['L']:
                count += 1
        return count