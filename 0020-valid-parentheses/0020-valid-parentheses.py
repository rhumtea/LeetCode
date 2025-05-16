class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mp = {')' : '(', ']' : '[', '}' : '{'}
        for _ in s:
            if _ in "[{(":
                st.append(_)
            else:
                if st and _ in mp and st[-1] == mp[_]:
                    st.pop()
                else:
                    return False
        return st == []

