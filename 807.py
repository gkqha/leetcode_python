class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        vertical = [] * 4
        horizontal = [] * 4
        res = 0
        for i in range(len(grid)):
            horizontal.append(max(grid[i]))
            tmp = []
            for j in range(len(grid[i])):
                tmp.append(grid[j][i])
            vertical.append(max(tmp))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                tmp = min(horizontal[i], vertical[j]) - grid[i][j]
                if tmp > 0:
                    res += tmp
        return res


s = Solution()
print(
    s.maxIncreaseKeepingSkyline(
        [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    )
)

