class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,n*t+1):
            pro=1
            for j in str(i):
                pro*=int(j)
            if pro%t==0 and i>=n:
                return i