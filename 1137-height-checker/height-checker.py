class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        h=sorted(heights)
        for i in range(len(heights)):
            if heights[i]!=h[i]:
                count+=1
            
        return count
            
            