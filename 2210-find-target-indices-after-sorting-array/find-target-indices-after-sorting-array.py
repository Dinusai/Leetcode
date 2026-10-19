class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        n=[]
        for i in range(len(nums)):
            if target == nums[i]:
                n.append(i)
        return n