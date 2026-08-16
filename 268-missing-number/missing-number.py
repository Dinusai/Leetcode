class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        s=[]
        for i in range(n+1):
            s.append(i)
        for j in s:
            if j not in nums:
                return j