class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words: return -1
        elif words[startIndex] == target: return 0
        n = len(words)
        for i in range(1, n):
            if words[(startIndex + i) % n] == target or words[(startIndex - i + n) % n] == target:
                return i