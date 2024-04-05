class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        maxSub = 0
        right = 0
        freq = Counter()
        for left, char in enumerate(s): 
            freq[char] += 1
            while freq[char] == 3: 
                freq[s[right]] -= 1
                right += 1
            maxSub = max(maxSub, left - right + 1)
        return maxSub
        
            
                