import operator


class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        list_pattern = []
        res = []
        list_pattern_res = []
        i = 0
        for s in pattern:
            if s not in list_pattern:
                list_pattern.append(s)
            list_pattern_res.append(list_pattern.index(s))
        for l in words:
            list_words = []
            list_words_res = []
            for s in l:
                if s not in list_words:
                    list_words.append(s)
                list_words_res.append(list_words.index(s))
            if operator.eq(list_pattern_res, list_words_res):
                res.append(l)
        return res


s = Solution()
print(s.findAndReplacePattern(["badc", "abab", "dddd", "dede", "yyxx"], "baba"))
