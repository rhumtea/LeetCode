class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        mp = defaultdict(int)
        track = 0
        for word in arr:
            mp[word] += 1
        for key, v in mp.items():
            if v == 1:
                track += 1
            if track == k:
                return key
        return ""