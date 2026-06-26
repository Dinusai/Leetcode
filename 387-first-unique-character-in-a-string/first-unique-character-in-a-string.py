class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic={}
        for i in s:
            dic[i]=dic.get(i,0)+1
        for i,ch in enumerate(s):
            if dic[ch]==1:
                return i
        return -1