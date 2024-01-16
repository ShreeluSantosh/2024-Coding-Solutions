class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        potions.sort()
        p = len(potions)
        s = len(spells)
        for i in range(s):
            lo, hi = 0, p-1
            while(lo <= hi):
                m = lo + (hi-lo)//2
                if potions[m]*spells[i] < success:
                    lo = m+1
                else:
                    hi = m-1
            pairs.append(p-lo)
        return pairs