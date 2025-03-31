class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        count = defaultdict(int)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        for R in range(len(nums)):
            count[prefix[R]%k] += 1
            res = res + count[prefix[R+1]%k]
        return res
        
