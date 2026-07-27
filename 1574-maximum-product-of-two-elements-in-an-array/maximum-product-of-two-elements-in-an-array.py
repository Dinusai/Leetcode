class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums1=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                nums1.append((nums[i]-1)*(nums[j]-1))
        return max(nums1)