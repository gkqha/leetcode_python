class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        a_min = min(A)
        a_max = max(A)
        res = a_max - a_min
        if res <= 2 * K:
            return 0
        else:
            return res - 2 * K
