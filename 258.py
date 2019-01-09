class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        sum = ""
        for i in str(num):
            sum += i
        return (int(sum) - 1) % 9 + 1
