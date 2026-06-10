class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        l=0
        for i in range(len(nums)):
            right=total-l-nums[i]

            if right==l:
                return i
            l+=nums[i]

        return -1