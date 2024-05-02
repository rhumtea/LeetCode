class Solution:
    def oddString(self, words: List[str]) -> str:
        thisdict = {}
        for i in range(len(words)):
            temp = ""
            for j in range(len(words[i])-1):
                temp += str(ord(words[i][j+1]) - ord(words[i][j]))
                temp += ","
            if temp not in thisdict:
                thisdict[temp] = [words[i]]
            else:
                thisdict[temp].append(words[i]) 
        print(thisdict)
        for i in thisdict:
            if len(thisdict[i]) == 1:
                return thisdict[i][0]  