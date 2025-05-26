class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        mp = defaultdict(int)
        res = 0
        max_freq = 0
        for i in range(len(nums)-1):
            if nums[i] == key:
                mp[nums[i+1]] += 1
        for k, v in mp.items():
            if v > max_freq:
                max_freq = v
                res = k
        return res