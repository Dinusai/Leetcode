class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic={}
        for index,element in enumerate(nums):
            need=target-element
            if need in dic:
                return [dic[need],index]
            dic[element]=index