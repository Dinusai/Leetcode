class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lst=[x for row in matrix for x in row]
        lst.sort()
        return lst[k-1]
        