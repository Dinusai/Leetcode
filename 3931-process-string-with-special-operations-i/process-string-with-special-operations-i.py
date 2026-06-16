class Solution:
    def processStr(self, s: str) -> str:
        s1=list(s)
        s2=[]
        for i in s1:
            if i=="*" and len(s2)!=0:
                s2.pop(-1)
            elif i=="#":
                s2+=s2
            elif i=="%":
                s2.reverse()
            elif i.islower():
                s2.append(i)
        return "".join(s2)