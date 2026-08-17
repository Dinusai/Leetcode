class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pos=[]
        neg=[]
        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)
        for j in range(n//2):
            nums[j*2]=pos[j]
            nums[j*2+1]=neg[j]
        return nums
        