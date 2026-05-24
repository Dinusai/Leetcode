class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        min=-2**31
        max=2**31-1
        r=int(dividend/divisor)
        if r<min:
            return min
        if r>max:
            return max
        return r
        