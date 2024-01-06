class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d  = []
        for i in set(arr):
            d.append(arr.count(i))
        c = set(d)
        if len(d) == len(c):
            return True
        else:
            return False