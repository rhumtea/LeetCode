class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        reverse_s = s[::-1]
        print(reverse_s)
        for i in range(len(s)-1):
            slice_s = s[i:i+2]
            print(slice_s)
            if slice_s in reverse_s:
                return True
        return False