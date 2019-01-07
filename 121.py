class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        leng = len(prices)
        if leng <= 1:
            return 0
        nums = [None] * leng
        nums[0] = prices[0]
        nums[1] = prices[1] - prices[0]
        i = 2
        min_tmp = min(prices[0], prices[1])
        while i < leng:
            if prices[i] < min_tmp:
                min_tmp = prices[i]
            nums[i] = max(nums[i - 1], prices[i] - min_tmp)
            i += 1
        if nums[-1] < 0:
            return 0
        else:
            return nums[-1]


s = Solution()
print(s.maxProfit([2, 1, 4]))

