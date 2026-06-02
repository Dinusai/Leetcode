class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        nums = [int(ch) for ch in s]

        for i in range(len(nums) - 1):
            if abs(nums[i] - nums[i + 1]) > 2:
                return False

        return True