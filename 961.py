class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        tmp = {}
        n = len(A)
        for a in A:
            if a not in tmp:
                tmp[a] = 0
            tmp[a] += 1
            if tmp[a] == n // 2:
                return a