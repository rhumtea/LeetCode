class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mp = defaultdict(int)
        for bill in bills:
            mp[bill] += 1
            if bill == 20:
                if mp[10] and mp[5]:
                    mp[10] -= 1
                    mp[5] -= 1
                elif mp[5] >= 3:
                    mp[5] -= 3
                else:
                    return False
            elif bill == 10:
                if mp[5]:
                    mp[5] -= 1
                else:
                    return False
        return True 