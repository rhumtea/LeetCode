class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        nums = nums * 2
        m = len(nums)
        st = []
        for i in range(m):
            while st and nums[st[-1]] < nums[i]:
                j = st.pop()
                L = 0
                if st:
                    L = st[-1] + 1
                R = i - 1
                if j < n:
                    res[j] = nums[R+1]
            st.append(i)
        return res

            