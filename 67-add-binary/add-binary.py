class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum_decimal = int(a, 2) + int(b, 2)
        binary_result = bin(sum_decimal)[2:]   # first 2 characters '0b' remove
        return binary_result