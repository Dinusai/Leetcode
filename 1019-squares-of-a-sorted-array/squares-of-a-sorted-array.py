class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squ=[]
        for i in nums:
            squ.append(i*i)
        s=sorted(squ)
        return s