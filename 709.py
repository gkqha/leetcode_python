class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        s = ""
        index_u = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        index_l = "abcdefghijklmnopqrstuvwxyz"
        for i in str:
            tmp = index_u.find(i)
            if tmp != -1:
                s = s + index_l[tmp]
            else:
                s = s + i
        return s


t = Solution()
print(t.toLowerCase("Hello"))
