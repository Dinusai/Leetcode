class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        d=1
        while num>0:
            num-=d
            d+=2
        if num==0:
            return True
        else:
            return False
        
