class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m1=float("inf")
        m2=0
        for i in prices:
             if i<m1:
                m1=i
             else:
                p=i-m1
                m2=max(p,m2)
        return m2
