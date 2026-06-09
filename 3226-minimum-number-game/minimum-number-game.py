class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n1=[]
        nums.sort()
        for i in range(0,len(nums),2):
            n1.append(nums[i+1])
            n1.append(nums[i])
        return n1