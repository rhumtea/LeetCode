class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a,b):
            while b:
                a, b = b, a % b
            return abs(a)
        mp = defaultdict(int)
        gcd_list = 0
        for card in deck:
            mp[card] += 1
            gcd_list = mp[card]
        values = list(mp.values())
        for value in values:
            gcd_list = gcd(gcd_list, value)
            if gcd_list == 1:
                return False
        return True  