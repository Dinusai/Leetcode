class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        o1=float("inf")
        o2=0
        for i in prices:
            o1=min(o1,i)
            o2=max(o2,i-o1)
        return o2