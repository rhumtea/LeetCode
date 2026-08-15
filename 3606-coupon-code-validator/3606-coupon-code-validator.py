class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ALLOWED = set(string.ascii_letters + string.digits + '_')
        VALID_B = {"electronics", "grocery", "pharmacy", "restaurant"}
        valid = []
        for i in range(len(code)):
            c = code[i]
            b = businessLine[i]
            if isActive[i] and b in VALID_B and c and set(c) <= ALLOWED:
                valid.append((b,c))
        valid.sort()
        return [c for b,c in valid]