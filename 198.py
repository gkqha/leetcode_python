class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 2
        leng = len(nums)
        if leng == 1:
            return nums[0]
        if leng == 0:
            return 0
        memo = [None] * leng
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])
        while i < leng:
            memo[i] = max(memo[i - 1], nums[i] + memo[i - 2])
            i += 1
        return memo[leng - 1]


s = Solution()
print(s.rob([]))

