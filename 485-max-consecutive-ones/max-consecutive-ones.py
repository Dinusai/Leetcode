class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        c1=[0]
        for i in nums:
            if i==1:
                count+=1
                c1.append(count)
            else:
                count=0
        return max(c1)