class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        nums1=[]
        nums2=[]
        nums3=[]
        for i in nums:
            
            if pivot>i:
                nums1.append(i)
            elif pivot==i:
                nums2.append(i)
            else:
                nums3.append(i)
        return nums1+nums2+nums3