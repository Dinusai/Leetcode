class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        n=[]
        for key,value in dic.items():
            if value>(len(nums)/3):
                n.append(key)
        return n
