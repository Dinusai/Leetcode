from itertools import combinations
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count={}
        for i in range(len(nums)-k+1):
            tail=set(nums[i:i + k])
            for y in tail:
                count[y]=count.get(y,0)+1
        ans=-1

        for y in count:
            if count[y]==1:
                ans=max(ans,y)
        return ans