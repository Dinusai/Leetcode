class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        for key,value in enumerate(nums):
            if dic[value]==1:
                return value