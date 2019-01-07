class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            if result <= tmp:
                result = tmp
            if tmp < 0:
                tmp = 0
        return result
