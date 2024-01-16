# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        m = lo + (hi-lo)//2
        while (lo <= hi):
            ans = guess(m)
            if ans == 0:
                return m
            elif ans == -1:
                hi = m-1
            else:
                lo = m+1
            m = lo + (hi-lo)//2
        return m