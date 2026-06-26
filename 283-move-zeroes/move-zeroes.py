class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:]=[x for x in nums if x != 0]+nums.count(0)*[0]