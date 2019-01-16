class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        if len(S) <= 1:
            return len(S)
        i = 1
        res = [S[0]]
        while i < len(S):
            if res == []:
                res.append(S[i])
            elif S[i] == ")" and res[-1] == "(":
                res.pop()
            else:
                res.append(S[i])
            i += 1
        return len(res)


s = Solution()
print(s.minAddToMakeValid("())"))
