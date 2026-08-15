class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        mp = defaultdict(list)
        b = {"electronics", "grocery", "pharmacy", "restaurant"}
        ALLOWED = set(string.ascii_letters + string.digits + '_')
        for i in range(len(code)):
            is_valid = bool(code[i]) and set(code[i]) <= ALLOWED
            if businessLine[i] in b and isActive[i] and is_valid:
                mp[businessLine[i]].append(code[i])
        res = []
        for k,v in sorted(mp.items()):
            for code in sorted(v):
                res.append(code)
        return res