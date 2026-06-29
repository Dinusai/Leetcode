class Solution:
    def judgeCircle(self, moves: str) -> bool:
        u=list(moves)
        count=0
        count1=0
        for i in u:
            if i=="U" :
                count+=1
            elif i=="D":
                count-=1
            elif i=="R":
                count1+=1
            else:
                count1-=1
        return count==0 and count1==0
