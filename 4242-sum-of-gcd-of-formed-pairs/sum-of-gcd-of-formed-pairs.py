class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #gcd helper
        def gcd(a,b):
            while b!=0:
                r = a%b
                a = b
                b = r
            return a
        
        #make the array
        prefixGcd=[]
        n=len(nums)
        current_max=0
        for i in range(n):
            if nums[i] > current_max:
                current_max = nums[i]
            # prefixGcd[i] = gcd(nums[i], mxi)
            prefixGcd.append(gcd(nums[i], current_max))

        prefixGcd.sort() #sort array
        sumgcd = 0
        for i in range(n//2):
            sumgcd += gcd(prefixGcd[i], prefixGcd[n-1-i])
        
        return sumgcd