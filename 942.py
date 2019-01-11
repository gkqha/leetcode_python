class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        i = 0
        d = len(S)
        res = []
        for s in S:
            if s == "I":
                res.append(i)
                i += 1
            else:
                res.append(d)
                d -= 1
        if S[-1] == "I":
            res.append(i)
        else:
            res.append(d)
        return res
