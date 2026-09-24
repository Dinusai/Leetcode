class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            s=0
            for j in str(nums[i]):
                s+=int(j)

            if s==i:
                return i
        return -1
