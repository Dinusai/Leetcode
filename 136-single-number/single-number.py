class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic={}
        for ch in nums:
            dic[ch]=dic.get(ch,0)+1
        for i,ch in enumerate(nums):
            if dic[ch]==1:
                return nums[i]