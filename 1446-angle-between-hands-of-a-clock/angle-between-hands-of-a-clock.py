class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h=abs(30*hour-(11*minutes/2))
        u=360-h
        if u>h:
            return h
        else:
            return u
