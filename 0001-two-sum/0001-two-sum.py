class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(nums)):
            check = target - nums[i]
            if check not in mp:
                mp[nums[i]] = i
            else:
                return [i, mp[check]]
            