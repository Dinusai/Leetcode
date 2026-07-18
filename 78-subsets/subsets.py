from itertools import combinations
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a=[[]]
        for i in range(1,len(nums)+1):
            for j in combinations(nums,i):
                a.append(list(j))
        return a