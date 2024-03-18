class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Use Sliding Window
        myset = set()
        maxLength = 0
        left = 0
        for right in range(len(s)):
        # Use while: keep remove char of set and move left until there is no more repeat char
            while s[right] in myset:
                myset.remove(s[left])
                left += 1
            else:
                myset.add(s[right])
                maxLength = max(maxLength, right - left + 1)
        return maxLength