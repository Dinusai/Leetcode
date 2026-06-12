class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        if len(nums)<1:
            return 0
        else:
            p1=[0]*len(nums)
            p1[0]=0
            p2=[0]*len(nums)
            p2[-1]=0
            for i in range(1,len(nums)):
                p1[i]=p1[i-1]+nums[i-1]
            for i in range(len(nums)-2,-1,-1):
                p2[i]=p2[i+1]+nums[i+1]
            return [abs(x-y) for x,y in zip(p1,p2)]