class Solution:
    def countKeyChanges(self, s: str) -> int:
        a = s.lower()
        count = 0
        for i in range(len(a)-1):
            if a[i] != a[i+1]:
                count += 1
        return count