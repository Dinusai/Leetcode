import math
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=sum(x for x in range(1,2*n+1) if x%2!=0)
        b=sum(x for x in range(1,2*n+1) if x%2==0)
        while b!=0:
            a,b=b,a%b
        return a

        