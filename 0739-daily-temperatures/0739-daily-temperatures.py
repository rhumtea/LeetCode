class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        temperatures.append(float('inf'))
        st = []
        max_arr = [[0]*2 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            while st and temperatures[st[-1]] < temperatures[i]:
                j = st.pop()
                L = 0
                if st:
                    L = st[-1]+1
                R = i - 1
                max_arr[j] = [L, R]
            st.append(i)
        for i in range(len(max_arr)-1):
            if max_arr[i][1] == len(temperatures)-2:
                res.append(0)
            else:
                res.append(max_arr[i][1]+1-i)
        return res

