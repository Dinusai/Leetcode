class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num<=9:
            return num
        else:
            while num>=10:
                k=0
                for i in str(num):
                    k+=int(i)
                num=k
            return num
