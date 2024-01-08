class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        L = []
        for i in range(len(candies)):
            sum = candies[i] + extraCandies
            if sum < max(candies):
                L.append(False)
            else:
                L.append(True)
        return L