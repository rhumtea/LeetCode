class Solution:
    def pivotInteger(self, n: int) -> int:
        left, right = 0, n+1
        sum_left, sum_right = 0, 0
        while left != right:
            if sum_left <= sum_right:
                left += 1
                sum_left += left
            elif sum_right >= sum_right:
                right -= 1
                sum_right += right
        return left if sum_left == sum_right else -1
        # s = (n*(n+1)) // 2
        # m = floor(sqrt(s))
        # if (m*m == s):
        #     return int(m)
        # else:
        #     return -1
