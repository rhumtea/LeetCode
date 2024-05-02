class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        thisdict = Counter(nums)
        res = 0
        left = 0
        right = len(nums)
        for i, freq in thisdict.items():
            right -= freq
            res += left * freq * right
            left += freq
        return res
        # thisdict =  defaultdict(lambda:0)
        # invalid_pairs, invalid_triplets = 0, 0 
        # for i, num in enumerate(nums):
        #     invalid_triplets += (i - thisdict[num]) * thisdict[num]
        #     invalid_triplets += invalid_pairs
        #     invalid_pairs += thisdict[num]
        #     thisdict[num] += 1
        # # n*(n-1)*(n-2)/6 is number of triplets which can be chosen from n items
        # return len(nums) * (len(nums) -  1) * (len(nums) - 2) // 6 - invalid_triplets
