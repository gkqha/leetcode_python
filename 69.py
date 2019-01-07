class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        r = x
        base = x / r
        while r > base:
            r = (r + x / r) // 2
            base = x / r
        return int(r)
