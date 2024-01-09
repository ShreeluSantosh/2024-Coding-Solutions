class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        col = []
        for i in range(len(grid)):
            pair = []
            for j in range(len(grid)):
                pair.append(grid[j][i])
            col.append(pair)
        c = 0
        for i in range(len(grid)):
            for j in range(0, len(grid[i])):
                if(grid[i]==col[j]):
                    c += 1
        return c