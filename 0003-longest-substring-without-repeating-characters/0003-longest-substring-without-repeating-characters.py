class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        thisset = set()
        maxLen = left = 0
        for right in range(len(s)):
            while s[right] in thisset:
                thisset.remove(s[left])
                left += 1
            else:
                thisset.add(s[right])
                maxLen = max(maxLen, right - left + 1)
        return maxLen
                