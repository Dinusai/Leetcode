class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        subarray=[]
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                subarray+=[arr[i:j+1]]
        totalsum=0
        for i in range(len(subarray)):
            if len(subarray[i])%2!=0:
                totalsum+=sum(subarray[i])
        return totalsum