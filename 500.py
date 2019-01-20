class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        map = {0: 'qwertyuiop', 1: 'asdfghjkl', 2: 'zxcvbnm'}
        res = []
        for w in words:
            lower_w = w.lower()
            char = lower_w[0]
            if char in map[0]:
                where = 0
            elif char in map[1]:
                where = 1
            else:
                where = 2
            append = True
            for s in lower_w:
                if s not in map[where]:
                    append = False
                    break
            if append:
                res.append(w)
        return res
