class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix=[0]+[0]*len(gain)
        prefix[0]=gain[0]
        for i in range(1,len(gain)):
            prefix[i]=gain[i]+prefix[i-1]
        return max(prefix)