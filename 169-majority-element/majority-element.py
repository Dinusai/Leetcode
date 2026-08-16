class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        for key,value in enumerate(nums):
            if dic[value]>n//2:
                return value