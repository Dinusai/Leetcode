class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        win=set()
        for i in range(n):
            if nums[i] in win:
                return True
            win.add(nums[i])

            if len(win)>k:
                win.remove(nums[i-k])
        return False