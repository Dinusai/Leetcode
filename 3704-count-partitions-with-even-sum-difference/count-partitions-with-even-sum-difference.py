class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count=0
        total=sum(nums)-nums[0]
        f_val=nums[0]
        for i in nums[1:]:
            if (f_val-total)%2==0:
                count+=1
            f_val+=i
            total-=i
        return count


            