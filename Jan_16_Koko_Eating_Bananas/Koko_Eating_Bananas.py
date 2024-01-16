class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            act_h=0
            for p in piles:
                act_h += (p+k-1)//k
            return act_h <= h
        lo, hi = 0, max(piles)
        while(hi-lo > 1):
            m = (lo+hi)//2
            if check(m):
                hi = m
            else:
                lo = m
        return hi