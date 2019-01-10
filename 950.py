class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck1 = sorted(deck)[::-1]
        res = []
        print("keyi")
        for i in deck1:
            j = 0
            while j < len(res) - 1:
                tmp = res.pop(0)
                res.append(tmp)
                j += 1
            res.insert(0, i)
        return res


s = Solution()
print(s.deckRevealedIncreasing([17, 13, 11]))

