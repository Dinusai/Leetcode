class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum={}
        prefix=0
        count=0
        prefixsum[0]=1
        for i in range(len(nums)):
            prefix+=nums[i]

            rem=prefix-k
            if rem in prefixsum:
                count+=prefixsum[rem]
            prefixsum[prefix]=prefixsum.get(prefix,0)+1
        return count
