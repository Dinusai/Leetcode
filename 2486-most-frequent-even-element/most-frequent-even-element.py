class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        c=-1
        d = {}
        for i in nums:
            if i%2==0:
                try:
                    d[nums.count(i)]=min(d[nums.count(i)],i)
                except:
                    d[nums.count(i)]=i
        
        if d:
            return list(d.values())[list(d.keys()).index(max(list(d.keys())))]
        else:
            return c