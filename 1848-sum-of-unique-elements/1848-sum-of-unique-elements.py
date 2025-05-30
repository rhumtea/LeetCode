class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        summ = 0
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
            if mp[num] == 1:
                summ += num
            elif mp[num] == 2:
                summ -= num
        return summ