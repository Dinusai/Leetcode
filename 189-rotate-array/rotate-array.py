class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        numslast=nums[-k:]
        numsfirst=nums[:-k]
        nums[:]=numslast+numsfirst