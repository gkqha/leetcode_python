class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        i = 0
        while i < len(s):
            if i != len(s) - 1 and h[s[i]] < h[s[i + 1]]:
                result += h[s[i + 1]] - h[s[i]]
                i += 1
            else:
                result += h[s[i]]
            i += 1
        return result
