class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        thisdict = {}
        for i in range(len(heights)):
            thisdict[heights[i]] = names[i]
        res = dict(sorted(thisdict.items(), reverse = True))
        return res.values()