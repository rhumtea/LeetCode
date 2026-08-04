class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def reversed_dec_bin(n):
            s = ""
            while n >= 1:
                d = n % 2
                n //= 2
                s += str(d)
            return s
        def bin_dec(s):
            num = 0
            for c in s:
                num = num *2 + int(c)
            return num
        ans = []
        for i in range(len(nums)):
            a = reversed_dec_bin(nums[i])
            a = bin_dec(a)
            ans.append([a, nums[i]])
        ans.sort(key=lambda x: (x[0], x[1]))
        res = [a[1] for a in ans]
        return res