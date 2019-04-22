class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if 0 <= x < 10:
            return True
        if x < 0:
            return False
        length = len(str(x))
        leng = length // 2
        for i in range(leng):
            if str(x)[i] != str(x)[length - i-1]:
                return False
        return True
