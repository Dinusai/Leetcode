class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lst=[]
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for key,value in freq.items():
            if value>=2:
                lst.append(key)
        return lst
