class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        cnt = Counter(nums)
        new_nums = [[k,v] for k,v in sorted(cnt.items())]
        res = []
        while new_nums:
            temp = []
            for num in new_nums:
                res.append(num[0])
                num[1] -= 1
                if num[1] > 0:
                    temp.append(num)
            new_nums = temp
        return res