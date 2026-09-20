class Solution:
    def reverseDegree(self, s: str) -> int:
        s1=0
        for i,j in enumerate(s,1):
            value=26-(ord(j)-ord('a'))
            s1+=(value*i)
        return s1