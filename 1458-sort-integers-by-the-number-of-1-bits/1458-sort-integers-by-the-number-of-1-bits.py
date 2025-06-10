class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def helper(num):
            count = 0
            while num > 0:
                count += (num & 1)
                num >>= 1
            return count
        arr.sort(key = lambda num : (helper(num), num))
        return arr