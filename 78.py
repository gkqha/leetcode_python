class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            tmp = res[:]
            for j in tmp:
                res.append([i]+ j)
        return res


s = Solution()
print(s.subsets([1, 2, 3]))

