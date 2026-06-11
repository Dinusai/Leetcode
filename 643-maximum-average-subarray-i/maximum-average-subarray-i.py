class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        win=sum(nums[:k])
        max_sum=win
 
        for i in range(k,n):
            win+=nums[i]-nums[i-k]
            max_sum=max(max_sum,win)
            
        return max_sum/k