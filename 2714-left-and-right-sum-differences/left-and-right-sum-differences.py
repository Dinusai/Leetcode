class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum=[0]*len(nums)
        for i in range(1,len(nums)):
            leftsum[i]=nums[i-1]+leftsum[i-1]
        rightsum=[0]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            rightsum[i]=nums[i+1]+rightsum[i+1]
        totalsum=[0]*len(nums)
        for i in range(len(nums)):
            totalsum[i]=abs(leftsum[i]-rightsum[i])
        return totalsum