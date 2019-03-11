class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        s = list("#" + "#".join(s) + "#")
        rl = [0] * len(s)
        for i in range(len(s)):
            j = 1
            while True:
                r = i - j
                l = i + j
                if r < 0 or l >= len(s):
                    break
                if s[r] == s[l]:
                    rl[i] += 1
                else:
                    break
                j += 1
        pos = rl.index(max(rl))
        print(rl)
        print(pos - max(rl) + 1, pos + max(rl) - 1)
        return "".join([i for i in s[pos - max(rl) + 1: pos + max(rl)] if i != "#"])
