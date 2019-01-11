class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        tmp = num
        res = 0
        #获取类似二进制1000在+1
        while tmp > 0:
            res = res * 2 + 1
            tmp = tmp >> 1
        return res ^ num

