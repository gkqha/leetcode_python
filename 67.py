class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        car = 0
        res = []
        a_list = [int(x) for x in a]
        b_list = [int(x) for x in b]
        while a_list and b_list:
            val = a_list.pop() + b_list.pop() + car
            res.append(val % 2)
            car = val // 2
        if b_list:
            a_list = b_list
        while a_list:
            val = a_list.pop() + car
            res.append(val % 2)
            car = val // 2
        if car == 1:
            res.append(car)
        return "".join(str(x) for x in res[::-1])
