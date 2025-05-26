class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        mp = defaultdict(int)
        res = 0
        for i in range(len(nums)-1):
            if nums[i] == key:
                mp[nums[i+1]] += 1
                if mp[nums[i+1]] > mp[res]:
                    res = nums[i+1]
        return res