class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        ans=[]
        for key,value in dic.items():
            if value==2:
                ans.append(key)
                break
        for i in range(1,len(nums)+1):
            if i not in nums:
                ans.append(i)
        return ans
                