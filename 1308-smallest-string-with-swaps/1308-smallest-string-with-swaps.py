class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        p = list(range(n))
        R = [0] * n
        def find(u):
            while u != p[u]:
                u = p[u]
            return u
        def union(u, v):
            u, v = find(u), find(v)
            if u == v:
                return False
            if R[u] < R[v]:
                u, v = v, u
            p[v] = u
            if R[u] == R[v]:
                R[u] += 1
            return True
        char_mp = defaultdict(list)
        pos_mp = defaultdict(list)
        for i in range(len(pairs)):
            u, v = pairs[i]
            union(u, v)
        for i in range(n):
            char_mp[find(i)].append(s[i])
            pos_mp[find(i)].append(i)
        for key in char_mp:
            char_mp[key].sort()
        res = [''] * n
        for key in pos_mp:
            for i, ch in zip(pos_mp[key], char_mp[key]):
                res[i] = ch
        return ''.join(res)