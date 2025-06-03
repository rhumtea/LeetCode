class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        l1 = l2 = 0
        count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                if count > 2:
                    return False
                elif count == 1:
                    l1 = i
                else:
                    l2 = i
        return s1[l1] == s2[l2] and s1[l2] == s2[l1]