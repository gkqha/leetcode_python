class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right + 1):
            tmp = True
            if "0" in str(i):
                continue
            else:
                for j in str(i):
                    if i % int(j) != 0:
                        tmp = False
                        break
            if tmp == True:
                res.append(i)
        return res
