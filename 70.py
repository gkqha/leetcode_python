class Solution:
    memo = []

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.memo = [-1] * (n + 1)
        return self.getClimStairs(n)

    def getClimStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif self.memo[n] == -1:
            self.memo[n] = self.getClimStairs(n - 1) + self.getClimStairs(n - 2)
        return self.memo[n]
