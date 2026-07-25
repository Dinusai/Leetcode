class Solution:
    def maxProduct(self, n: int) -> int:
        g=[int(i) for i in str(n)]
        g.sort()
        return g[-1]*g[-2]