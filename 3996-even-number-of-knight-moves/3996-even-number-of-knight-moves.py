class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        a = sum(start)%2
        b = sum(target)%2
        return a == b