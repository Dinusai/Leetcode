class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=max(nums)
        s=min(nums)
        d=1
        for i in range(1,l+1):
            if s%i==0 and l%i==0:
                d=i
        return d