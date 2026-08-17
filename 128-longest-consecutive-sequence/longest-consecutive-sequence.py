class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        larg=0
        count=0
        pre=float("-inf")
        for i in range(len(nums)):
            if nums[i]-1==pre:
                count+=1
                pre=nums[i]
            elif nums[i]!=pre:
                count=1
                pre=nums[i]
            larg=max(larg,count)
        return larg