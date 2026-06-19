class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,num in enumerate(nums):
            d=target-num

            if d in dic:
                return [dic[d],i]
            dic[num]=i
            
            